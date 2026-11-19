#!/usr/bin/env python3
"""Lecture de Google Search Console (lecture seule) : trois analyses utiles.

  proches-page-1   requêtes en position 4 à 20, avec la page concernée
  pages-en-baisse  pages dont les clics ont perdu plus de 30 % entre deux périodes
  appareils        répartition mobile / ordinateur / tablette, avec l'évolution
  sites            propriétés Search Console accessibles
  brut             requête libre (corps JSON de l'API)

Aucune écriture : portée webmasters.readonly. Le script n'appelle que Google
(renouvellement du jeton, puis API Search Console). Aucune bibliothèque tierce.

Prérequis : avoir lancé connexion_search_console.py une fois, puis
    GSC_SITE_URL="https://www.exemple.fr/"  (ou "sc-domain:exemple.fr")
    GOOGLE_CLIENT_ID et GOOGLE_CLIENT_SECRET (ou GOOGLE_CREDENTIALS_FILE)

Exemples :
    python lire_search_console.py proches-page-1 --jours 28 --exclure ma-marque
    python lire_search_console.py pages-en-baisse --jours 28 --seuil 30
    python lire_search_console.py appareils --json
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import date, timedelta
from pathlib import Path
from urllib.parse import quote, urlencode

sys.path.insert(0, str(Path(__file__).resolve().parent))
import connexion_search_console as cx  # noqa: E402

URL_API = "https://www.googleapis.com/webmasters/v3"
DECALAGE_DONNEES = 3          # Search Console publie avec quelques jours de retard
LIMITE_LIGNES = 5000


class ErreurApi(Exception):
    def __init__(self, statut, message):
        super().__init__(f"HTTP {statut} : {message}")
        self.statut = statut


def appel_reel(methode, url, json_corps=None, formulaire=None, entetes=None):
    """Seul point d'accès au réseau (remplacé par un faux dans les tests)."""
    entetes = dict(entetes or {})
    corps = None
    if json_corps is not None:
        corps = json.dumps(json_corps).encode("utf-8")
        entetes["Content-Type"] = "application/json"
    elif formulaire is not None:
        corps = urlencode(formulaire).encode("ascii")
        entetes["Content-Type"] = "application/x-www-form-urlencoded"
    req = urllib.request.Request(url, data=corps, method=methode, headers=entetes)
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read().decode("utf-8") or "{}")
    except urllib.error.HTTPError as e:
        try:
            detail = json.loads(e.read().decode("utf-8")).get("error", {})
            msg = detail.get("message", "") if isinstance(detail, dict) else str(detail)
        except Exception:
            msg = ""
        raise ErreurApi(e.code, msg[:200]) from None
    except urllib.error.URLError as e:
        raise ErreurApi(0, f"Google injoignable : {e.reason}") from None


# ---------------------------------------------------------------------------
# Client
# ---------------------------------------------------------------------------

class ClientSearchConsole:
    def __init__(self, site, refresh_token, client_id, client_secret, appeler=appel_reel):
        if not site:
            raise ValueError("Adresse de la propriété manquante : définir GSC_SITE_URL ou --site.")
        self.site = site
        self._refresh = refresh_token
        self._cid = client_id
        self._secret = client_secret
        self._appeler = appeler
        self._acces = None

    def _jeton_acces(self):
        if self._acces:
            return self._acces
        rep = self._appeler("POST", cx.URL_JETON, formulaire={
            "client_id": self._cid, "client_secret": self._secret,
            "refresh_token": self._refresh, "grant_type": "refresh_token"})
        if not rep.get("access_token"):
            raise ErreurApi(0, "Google n'a pas renvoyé de jeton d'accès : relancer la connexion.")
        self._acces = rep["access_token"]
        return self._acces

    def _entetes(self):
        return {"Authorization": f"Bearer {self._jeton_acces()}"}

    def lister_sites(self):
        rep = self._appeler("GET", f"{URL_API}/sites", entetes=self._entetes())
        return rep.get("siteEntry", [])

    def interroger(self, dimensions, debut, fin, limite=LIMITE_LIGNES, filtres=None,
                   type_recherche="web"):
        corps = {"startDate": debut, "endDate": fin, "dimensions": dimensions,
                 "rowLimit": min(limite, 25000), "type": type_recherche, "dataState": "final"}
        if filtres:
            corps["dimensionFilterGroups"] = [{"filters": filtres}]
        url = f"{URL_API}/sites/{quote(self.site, safe='')}/searchAnalytics/query"
        rep = self._appeler("POST", url, json_corps=corps, entetes=self._entetes())
        return rep.get("rows", [])


# ---------------------------------------------------------------------------
# Analyses (fonctions pures)
# ---------------------------------------------------------------------------

def fenetres(jours, aujourdhui=None):
    """Période récente et période précédente de même longueur (dates incluses)."""
    fin = (aujourdhui or date.today()) - timedelta(days=DECALAGE_DONNEES)
    debut = fin - timedelta(days=jours - 1)
    fin_avant = debut - timedelta(days=1)
    debut_avant = fin_avant - timedelta(days=jours - 1)
    return {"apres": (debut.isoformat(), fin.isoformat()),
            "avant": (debut_avant.isoformat(), fin_avant.isoformat())}


def proches_page_1(lignes, position_min=4, position_max=20, impressions_min=50, exclure=()):
    """Lignes [requête, page] en position moyenne 4 à 20, triées par impressions."""
    termes = [t.lower() for t in exclure if t]
    res = []
    for r in lignes:
        requete = r["keys"][0]
        if any(t in requete.lower() for t in termes):
            continue
        if position_min <= r["position"] <= position_max and r["impressions"] >= impressions_min:
            res.append({
                "requete": requete,
                "page": r["keys"][1] if len(r["keys"]) > 1 else "",
                "position": round(r["position"], 1),
                "impressions": int(r["impressions"]),
                "clics": int(r["clicks"]),
                "taux_clic": round(r["ctr"], 4),
            })
    res.sort(key=lambda x: -x["impressions"])
    return res


def pages_en_baisse(avant, apres, seuil_pct=30.0, clics_min=30):
    """Pages dont les clics baissent d'au moins `seuil_pct` %.

    `clics_min` écarte les pages trop petites : une variation de 5 à 3 clics
    n'est pas un signal. Une page absente de la période récente compte 0 clic.
    """
    recent = {r["keys"][0]: r for r in apres}
    res = []
    for r in avant:
        page = r["keys"][0]
        c_avant = r["clicks"]
        if c_avant < clics_min:
            continue
        r2 = recent.get(page)
        c_apres = r2["clicks"] if r2 else 0
        variation = (c_apres - c_avant) / c_avant * 100
        if variation <= -seuil_pct:
            res.append({
                "page": page,
                "clics_avant": int(c_avant),
                "clics_apres": int(c_apres),
                "variation_pct": round(variation, 1),
                "clics_perdus": int(c_avant - c_apres),
                "position_avant": round(r["position"], 1),
                "position_apres": round(r2["position"], 1) if r2 else None,
            })
    res.sort(key=lambda x: -x["clics_perdus"])
    return res


def appareils(avant, apres):
    anc = {r["keys"][0]: r for r in avant}
    res = []
    for r in apres:
        nom = r["keys"][0]
        a = anc.get(nom)
        var = None
        if a and a["clicks"]:
            var = round((r["clicks"] - a["clicks"]) / a["clicks"] * 100, 1)
        res.append({
            "appareil": nom, "clics": int(r["clicks"]), "impressions": int(r["impressions"]),
            "taux_clic": round(r["ctr"], 4), "position": round(r["position"], 1),
            "clics_periode_precedente": int(a["clicks"]) if a else None,
            "variation_clics_pct": var,
        })
    res.sort(key=lambda x: -x["clics"])
    return res


# ---------------------------------------------------------------------------
# Affichage et commandes
# ---------------------------------------------------------------------------

def afficher(titre, lignes, colonnes, en_json, notes=()):
    if en_json:
        print(json.dumps({"titre": titre, "lignes": lignes, "notes": list(notes)},
                         indent=2, ensure_ascii=False))
        return
    print(titre)
    if not lignes:
        print("  Aucune ligne.")
    for l in lignes:
        print("  " + " | ".join(f"{c}: {l[c]}" for c in colonnes))
    for n in notes:
        print(f"Note : {n}")


def construire_client(args):
    site = args.site or os.environ.get("GSC_SITE_URL", "")
    cid, secret = cx.lire_identifiants()
    refresh = cx.lire_jeton(cx.chemin_jeton_defaut())
    return ClientSearchConsole(site, refresh, cid, secret)


def commande_sites(args, client):
    sites = client.lister_sites()
    afficher("Propriétés accessibles", [{"site": s["siteUrl"], "droit": s["permissionLevel"]}
                                         for s in sites], ["site", "droit"], args.json)


def commande_proches(args, client):
    w = fenetres(args.jours)
    lignes = client.interroger(["query", "page"], *w["apres"])
    notes = []
    if len(lignes) >= LIMITE_LIGNES:
        notes.append(f"résultat tronqué à {LIMITE_LIGNES} lignes : réduire la période ou filtrer.")
    res = proches_page_1(lignes, args.position_min, args.position_max, args.impressions_min,
                         args.exclure or ())
    notes.append("La position est une moyenne sur la période. Une requête proche de la page 1 "
                 "n'est pas une promesse de gain : vérifier l'intention de recherche avant de réécrire.")
    afficher(f"Requêtes en position {args.position_min} à {args.position_max} "
             f"({w['apres'][0]} au {w['apres'][1]})", res,
             ["requete", "page", "position", "impressions", "clics"], args.json, notes)


def commande_baisse(args, client):
    w = fenetres(args.jours)
    avant = client.interroger(["page"], *w["avant"])
    apres = client.interroger(["page"], *w["apres"])
    notes = ["Une baisse n'est pas une cause : écarter la saison, une page déplacée ou supprimée, "
             "un retard d'indexation et un changement de suivi avant d'agir (voir /marketing-relire-un-changement)."]
    if len(avant) >= LIMITE_LIGNES or len(apres) >= LIMITE_LIGNES:
        notes.append(f"résultat tronqué à {LIMITE_LIGNES} pages par période.")
    res = pages_en_baisse(avant, apres, args.seuil, args.clics_min)
    afficher(f"Pages en baisse d'au moins {args.seuil:g} % ({w['avant'][0]} au {w['avant'][1]} "
             f"contre {w['apres'][0]} au {w['apres'][1]})", res,
             ["page", "clics_avant", "clics_apres", "variation_pct"], args.json, notes)


def commande_appareils(args, client):
    w = fenetres(args.jours)
    avant = client.interroger(["device"], *w["avant"], limite=10)
    apres = client.interroger(["device"], *w["apres"], limite=10)
    afficher(f"Appareils ({w['apres'][0]} au {w['apres'][1]})", appareils(avant, apres),
             ["appareil", "clics", "impressions", "position", "variation_clics_pct"], args.json)


def commande_brut(args, client):
    corps = json.loads(args.corps)
    url = f"{URL_API}/sites/{quote(client.site, safe='')}/searchAnalytics/query"
    rep = client._appeler("POST", url, json_corps=corps, entetes=client._entetes())
    print(json.dumps(rep, indent=2, ensure_ascii=False))


def construire_parseur():
    p = argparse.ArgumentParser(description="Search Console en lecture seule")
    p.add_argument("--site", help="propriété (défaut : variable GSC_SITE_URL)")
    p.add_argument("--json", action="store_true", help="sortie JSON")
    sub = p.add_subparsers(dest="commande", required=True)

    sub.add_parser("sites").set_defaults(f=commande_sites)

    a = sub.add_parser("proches-page-1")
    a.add_argument("--jours", type=int, default=28)
    a.add_argument("--position-min", type=float, default=4)
    a.add_argument("--position-max", type=float, default=20)
    a.add_argument("--impressions-min", type=int, default=50)
    a.add_argument("--exclure", action="append", help="terme à écarter (nom de marque), répétable")
    a.set_defaults(f=commande_proches)

    b = sub.add_parser("pages-en-baisse")
    b.add_argument("--jours", type=int, default=28)
    b.add_argument("--seuil", type=float, default=30.0, help="baisse minimale en %%")
    b.add_argument("--clics-min", type=int, default=30,
                   help="clics minimaux sur la période précédente pour compter une page")
    b.set_defaults(f=commande_baisse)

    c = sub.add_parser("appareils")
    c.add_argument("--jours", type=int, default=28)
    c.set_defaults(f=commande_appareils)

    d = sub.add_parser("brut")
    d.add_argument("--corps", required=True, help="corps JSON de la requête")
    d.set_defaults(f=commande_brut)
    return p


def main(argv=None):
    for flux in (sys.stdout, sys.stderr):
        if hasattr(flux, "reconfigure"):
            flux.reconfigure(encoding="utf-8")
    args = construire_parseur().parse_args(argv)
    try:
        client = construire_client(args)
        args.f(args, client)
    except (cx.ErreurConnexion, ErreurApi, ValueError) as e:
        print(f"Erreur : {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
