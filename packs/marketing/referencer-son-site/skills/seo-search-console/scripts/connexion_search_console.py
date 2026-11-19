#!/usr/bin/env python3
"""Connexion unique à Google Search Console (lecture seule).

Ce script ouvre le navigateur une fois, la personne se connecte à Google et
accepte l'accès en LECTURE SEULE, puis un jeton de renouvellement est gardé
dans un fichier local. Les autres scripts s'en servent ensuite sans rouvrir le
navigateur.

Garde-fous :
  - portée demandée : webmasters.readonly (aucune écriture possible) ;
  - le jeton va par défaut dans ~/.config/zerogravity/search-console/jeton.json,
    hors de tout dépôt ; le script REFUSE un chemin situé dans un dépôt git ;
  - le fichier ne contient que le jeton de renouvellement (ni identifiant client,
    ni secret) et n'est lisible que par son propriétaire quand le système le permet ;
  - la réponse du navigateur est vérifiée (paramètre state), l'échange utilise PKCE ;
  - rien n'est affiché de secret, rien n'est envoyé ailleurs que chez Google.

Préparation (une fois, gratuite) :
  1. Créer un projet Google Cloud et activer « Google Search Console API ».
  2. Créer un identifiant OAuth de type « Application de bureau ».
  3. Donner l'identifiant et le secret par variables d'environnement
     GOOGLE_CLIENT_ID et GOOGLE_CLIENT_SECRET, ou par GOOGLE_CREDENTIALS_FILE
     (fichier JSON téléchargé chez Google, gardé hors de tout dépôt).

Utilisation :
    python connexion_search_console.py
"""
import base64
import hashlib
import json
import os
import secrets
import sys
import urllib.error
import urllib.request
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlencode, urlparse

PORTEE = "https://www.googleapis.com/auth/webmasters.readonly"
URL_AUTORISATION = "https://accounts.google.com/o/oauth2/v2/auth"
URL_JETON = "https://oauth2.googleapis.com/token"
PORT_DEFAUT = 8765


class ErreurConnexion(Exception):
    pass


# ---------------------------------------------------------------------------
# Chemin du jeton
# ---------------------------------------------------------------------------

def chemin_jeton_defaut():
    env = os.environ.get("GSC_TOKEN_FILE")
    if env:
        return Path(env)
    return Path.home() / ".config" / "zerogravity" / "search-console" / "jeton.json"


def est_dans_un_depot(chemin):
    """Vrai si le chemin est dans un dossier qui contient un .git (dossier ou fichier)."""
    p = Path(chemin).expanduser().resolve()
    for parent in [p] + list(p.parents):
        if (parent / ".git").exists():
            return True
    return False


def verifier_chemin_jeton(chemin):
    if est_dans_un_depot(chemin):
        raise ErreurConnexion(
            f"Le jeton ne doit jamais être gardé dans un dépôt git : {chemin}. "
            "Choisir un dossier hors dépôt (variable GSC_TOKEN_FILE).")
    return Path(chemin)


def ecrire_jeton(chemin, refresh_token):
    chemin = verifier_chemin_jeton(chemin)
    chemin.parent.mkdir(parents=True, exist_ok=True)
    tmp = chemin.with_suffix(".tmp")
    tmp.write_text(json.dumps({"refresh_token": refresh_token, "portee": PORTEE}), encoding="utf-8")
    try:
        os.chmod(tmp, 0o600)
    except OSError:
        pass  # certains systèmes (Windows) ignorent ce réglage
    os.replace(tmp, chemin)


def lire_jeton(chemin):
    chemin = verifier_chemin_jeton(chemin)
    if not chemin.exists():
        raise ErreurConnexion(
            f"Aucun jeton trouvé : {chemin}. Lancer d'abord connexion_search_console.py.")
    data = json.loads(chemin.read_text(encoding="utf-8"))
    if not data.get("refresh_token"):
        raise ErreurConnexion("Jeton incomplet : relancer connexion_search_console.py.")
    return data["refresh_token"]


# ---------------------------------------------------------------------------
# Identifiants OAuth du client (jamais écrits ni affichés)
# ---------------------------------------------------------------------------

def lire_identifiants(env=None):
    env = os.environ if env is None else env
    cid = env.get("GOOGLE_CLIENT_ID", "")
    secret = env.get("GOOGLE_CLIENT_SECRET", "")
    fichier = env.get("GOOGLE_CREDENTIALS_FILE", "")
    if (not cid or not secret) and fichier and Path(fichier).exists():
        data = json.loads(Path(fichier).read_text(encoding="utf-8"))
        if "installed" in data:   # format téléchargé chez Google
            data = data["installed"]
        cid = cid or data.get("client_id", "")
        secret = secret or data.get("client_secret", "")
    if not cid or not secret:
        raise ErreurConnexion(
            "Identifiants Google manquants : définir GOOGLE_CLIENT_ID et GOOGLE_CLIENT_SECRET, "
            "ou GOOGLE_CREDENTIALS_FILE.")
    return cid, secret


# ---------------------------------------------------------------------------
# Étapes OAuth (fonctions pures, testables sans réseau)
# ---------------------------------------------------------------------------

def defi_pkce():
    verifier = secrets.token_urlsafe(64)
    digest = hashlib.sha256(verifier.encode("ascii")).digest()
    challenge = base64.urlsafe_b64encode(digest).rstrip(b"=").decode("ascii")
    return verifier, challenge


def construire_url_autorisation(client_id, redirect_uri, state, challenge):
    params = {
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "response_type": "code",
        "scope": PORTEE,
        "access_type": "offline",
        "prompt": "consent",
        "state": state,
        "code_challenge": challenge,
        "code_challenge_method": "S256",
    }
    return f"{URL_AUTORISATION}?{urlencode(params)}"


def extraire_code(chemin_retour, state_attendu):
    """Lit le chemin de retour du navigateur (« /?code=...&state=... »)."""
    q = parse_qs(urlparse(chemin_retour).query)
    if "error" in q:
        raise ErreurConnexion(f"Accès refusé ou interrompu côté Google : {q['error'][0]}")
    if q.get("state", [None])[0] != state_attendu:
        raise ErreurConnexion("Réponse refusée : le paramètre state ne correspond pas.")
    code = q.get("code", [None])[0]
    if not code:
        raise ErreurConnexion("Aucun code reçu de Google.")
    return code


def echanger_code(code, client_id, client_secret, redirect_uri, verifier, ouvrir=None):
    corps = urlencode({
        "code": code, "client_id": client_id, "client_secret": client_secret,
        "redirect_uri": redirect_uri, "grant_type": "authorization_code",
        "code_verifier": verifier,
    }).encode("ascii")
    ouvrir = ouvrir or urllib.request.urlopen
    req = urllib.request.Request(URL_JETON, data=corps, method="POST",
                                 headers={"Content-Type": "application/x-www-form-urlencoded"})
    try:
        with ouvrir(req, timeout=30) as r:
            return json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        raise ErreurConnexion(f"Échange du code refusé par Google (HTTP {e.code}).") from None
    except urllib.error.URLError as e:
        raise ErreurConnexion(f"Google injoignable : {e.reason}") from None


def attendre_retour(port, state, delai=300):
    """Écoute le retour du navigateur sur 127.0.0.1 et renvoie le code."""
    resultat = {}

    class Gestionnaire(BaseHTTPRequestHandler):
        def do_GET(self):
            if "code=" in self.path or "error=" in self.path:
                resultat["chemin"] = self.path
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write("<h1>Connexion reçue. Vous pouvez fermer cet onglet.</h1>".encode("utf-8"))

        def log_message(self, *args):
            pass

    serveur = HTTPServer(("127.0.0.1", port), Gestionnaire)
    serveur.timeout = delai
    for _ in range(5):          # ignore les requêtes parasites (icône, etc.)
        serveur.handle_request()
        if "chemin" in resultat:
            break
    serveur.server_close()
    if "chemin" not in resultat:
        raise ErreurConnexion("Aucun retour du navigateur : relancer la connexion.")
    return extraire_code(resultat["chemin"], state)


def main():
    try:
        client_id, client_secret = lire_identifiants()
        chemin = verifier_chemin_jeton(chemin_jeton_defaut())
        port = int(os.environ.get("GSC_REDIRECT_PORT", PORT_DEFAUT))
        redirect_uri = f"http://127.0.0.1:{port}"
        state = secrets.token_urlsafe(24)
        verifier, challenge = defi_pkce()
        url = construire_url_autorisation(client_id, redirect_uri, state, challenge)
        print("Ouverture du navigateur pour la connexion Google (lecture seule).")
        print("Si rien ne s'ouvre, copier l'adresse suivante dans le navigateur :")
        print(url)
        webbrowser.open(url)
        code = attendre_retour(port, state)
        jeton = echanger_code(code, client_id, client_secret, redirect_uri, verifier)
        if not jeton.get("refresh_token"):
            raise ErreurConnexion(
                "Google n'a pas fourni de jeton de renouvellement : retirer l'accès de l'application "
                "dans le compte Google puis recommencer.")
        ecrire_jeton(chemin, jeton["refresh_token"])
        print(f"Jeton enregistré hors dépôt : {chemin}")
        print("Étape suivante : python lire_search_console.py sites")
    except ErreurConnexion as e:
        print(f"Erreur : {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
