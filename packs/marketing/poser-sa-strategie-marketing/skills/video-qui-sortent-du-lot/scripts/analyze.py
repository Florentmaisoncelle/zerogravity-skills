#!/usr/bin/env python3
"""Repère les vidéos YouTube qui dépassent nettement la moyenne de leur chaîne.

Utilise l'API officielle YouTube Data v3. La clé se lit dans la variable d'environnement
YOUTUBE_API_KEY (jamais en argument, pour qu'elle ne reste pas dans l'historique du terminal).
Python standard seulement. Les longues et les courtes sont séparées.

Usage :
    python analyze.py --chaines @chaine1,@chaine2 [--jours 30] [--sortie console|json]
"""

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from datetime import datetime, timedelta, timezone
from statistics import median

API = "https://www.googleapis.com/youtube/v3/"

MOTS_VIDES = set(
    "le la les un une des de du d l et ou en à au aux pour par sur dans avec sans ce cet cette ces mon ma mes ton ta "
    "tes son sa ses je tu il elle on nous vous ils elles que qui quoi est sont pas plus the a an i you my your this "
    "that it is are was to in for on of and or how with do not can will just all but be have from at by if so no what "
    "when why who we they them its new now one".split()
)


def appel(cle, endpoint, params):
    """Une requête vers l'API. Ne jamais afficher l'adresse : elle contient la clé."""
    params = dict(params, key=cle)
    adresse = API + endpoint + "?" + urllib.parse.urlencode(params)
    try:
        with urllib.request.urlopen(adresse, timeout=30) as reponse:
            return json.loads(reponse.read())
    except urllib.error.HTTPError as exc:
        raise SystemExit(f"Erreur de l'API YouTube : code {exc.code} ({exc.reason}). Vérifier la clé et le quota.")
    except urllib.error.URLError as exc:
        raise SystemExit(f"Réseau indisponible : {exc.reason}")


def resoudre_chaine(cle, identifiant):
    """Renvoie la fiche de la chaîne désignée par son identifiant @..., ou None."""
    donnees = appel(cle, "channels", {"forHandle": identifiant, "part": "statistics,snippet,contentDetails"})
    items = donnees.get("items") or []
    return items[0] if items else None


def videos_recentes(cle, fiche, limite, maximum=100):
    """Les vidéos publiées après la date limite, avec leurs statistiques."""
    liste = fiche["contentDetails"]["relatedPlaylists"]["uploads"]
    ids, page, fini = [], None, False
    while not fini and len(ids) < maximum:
        params = {"playlistId": liste, "part": "snippet,contentDetails", "maxResults": 50}
        if page:
            params["pageToken"] = page
        donnees = appel(cle, "playlistItems", params)
        for item in donnees.get("items", []):
            publiee = datetime.fromisoformat(item["snippet"]["publishedAt"].replace("Z", "+00:00"))
            if publiee < limite:
                fini = True
                break
            ids.append(item["contentDetails"]["videoId"])
        page = donnees.get("nextPageToken")
        if not page:
            break
    details = []
    for i in range(0, len(ids), 50):
        lot = appel(cle, "videos", {"id": ",".join(ids[i:i + 50]), "part": "snippet,statistics,contentDetails"})
        details.extend(lot.get("items", []))
    return details


def duree_en_secondes(iso):
    m = re.match(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?$", iso or "")
    if not m:
        return 0
    h, mi, s = m.groups()
    return int(h or 0) * 3600 + int(mi or 0) * 60 + int(s or 0)


def analyser_groupe(videos, seuil, minimum):
    """Ajoute moyenne, médiane et multiplicateur ; renvoie (videos, sorties_du_lot).

    Un groupe sous `minimum` vidéos ne produit aucune « vidéo hors du lot » : la moyenne
    d'un petit échantillon est trop instable (et elle inclut la vidéo testée).
    """
    if not videos:
        return videos, []
    vues = [v["vues"] for v in videos]
    moyenne = sum(vues) / len(vues)
    mediane = median(vues)
    for v in videos:
        v["moyenne"] = round(moyenne)
        v["multiplicateur"] = round(v["vues"] / moyenne, 1) if moyenne > 0 else 0
        v["x_mediane"] = round(v["vues"] / mediane, 1) if mediane > 0 else 0
    if len(videos) < minimum:
        return videos, []
    dehors = [v for v in videos if moyenne > 0 and v["vues"] > moyenne * seuil]
    return videos, sorted(dehors, key=lambda v: -v["multiplicateur"])


def mots_recurrents(titres, combien=15):
    mots = []
    for titre in titres:
        mots.extend(re.findall(r"\w+", titre.lower()))
    utiles = [m for m in mots if m not in MOTS_VIDES and len(m) > 2 and not m.isdigit()]
    return Counter(utiles).most_common(combien)


def analyser_chaines(cle, chaines, jours, seuil, minimum, seuil_short):
    limite = datetime.now(timezone.utc) - timedelta(days=jours)
    resultat = {"chaines": {}, "hors_du_lot": {"longues": [], "shorts": []}}
    for identifiant in chaines:
        print(f"  analyse de {identifiant}...", file=sys.stderr)
        fiche = resoudre_chaine(cle, identifiant)
        if not fiche:
            print(f"    chaîne introuvable : {identifiant}", file=sys.stderr)
            continue
        nom = fiche["snippet"]["title"]
        longues, shorts = [], []
        for v in videos_recentes(cle, fiche, limite):
            secondes = duree_en_secondes(v["contentDetails"]["duration"])
            entree = {
                "chaine": nom,
                "titre": v["snippet"]["title"],
                "vues": int(v["statistics"].get("viewCount", 0)),
                "duree_min": round(secondes / 60, 1),
                "publiee": v["snippet"]["publishedAt"][:10],
                "adresse": f"https://www.youtube.com/watch?v={v['id']}",
            }
            (shorts if secondes <= seuil_short else longues).append(entree)
        longues, hl = analyser_groupe(longues, seuil, minimum)
        shorts, hs = analyser_groupe(shorts, seuil, minimum)
        resultat["hors_du_lot"]["longues"].extend(hl)
        resultat["hors_du_lot"]["shorts"].extend(hs)
        resultat["chaines"][nom] = {
            "abonnes": int(fiche["statistics"].get("subscriberCount", 0)),
            "longues": len(longues),
            "shorts": len(shorts),
            "par_semaine": round((len(longues) + len(shorts)) / (jours / 7), 1),
            "echantillon_trop_petit": [
                nom_groupe for nom_groupe, g in (("longues", longues), ("shorts", shorts)) if 0 < len(g) < minimum
            ],
        }
    for cle_groupe in ("longues", "shorts"):
        resultat["hors_du_lot"][cle_groupe].sort(key=lambda v: -v["multiplicateur"])
    return resultat


def afficher(resultat, jours, seuil):
    print(f"\nDerniers {jours} jours, seuil {seuil}x la moyenne de la chaîne\n")
    for nom, d in resultat["chaines"].items():
        petit = f"  [échantillon trop petit : {', '.join(d['echantillon_trop_petit'])}]" if d["echantillon_trop_petit"] else ""
        print(f"  {nom:30s} {d['abonnes']:>10,} abonnés | {d['longues']} longues, {d['shorts']} shorts "
              f"({d['par_semaine']}/semaine){petit}")
    for groupe, etiquette in (("longues", "VIDÉOS LONGUES"), ("shorts", "SHORTS")):
        print(f"\n{etiquette} hors du lot (15 premières)")
        for v in resultat["hors_du_lot"][groupe][:15]:
            print(f"  {v['multiplicateur']:.1f}x moyenne ({v['x_mediane']:.1f}x médiane) | {v['vues']:>10,} vues | "
                  f"[{v['chaine']}] {v['titre'][:70]}")
            print(f"      {v['publiee']} | {v['adresse']}")
    titres = [v["titre"] for g in resultat["hors_du_lot"].values() for v in g]
    print("\nMOTS QUI REVIENNENT dans ces titres (un indice, pas une formule)")
    for mot, n in mots_recurrents(titres):
        print(f"  {n:>3}x  {mot}")


def _sortie_utf8() -> None:
    """Sortie en UTF-8 quel que soit l'encodage de la console (Windows : cp1252)."""
    for flux in (sys.stdout, sys.stderr):
        try:
            flux.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass


def main():
    _sortie_utf8()
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--chaines", required=True, help="identifiants séparés par des virgules, ex. @chaine1,@chaine2")
    parser.add_argument("--jours", type=int, default=30, help="période regardée (30 par défaut)")
    parser.add_argument("--seuil", type=float, default=2.0, help="multiple de la moyenne (2 par défaut)")
    parser.add_argument("--minimum", type=int, default=5, help="vidéos minimum par groupe pour désigner des sorties du lot")
    parser.add_argument("--seuil-short", type=int, default=60, help="durée maximale d'un short, en secondes")
    parser.add_argument("--sortie", choices=["console", "json"], default="console")
    args = parser.parse_args()

    cle = os.environ.get("YOUTUBE_API_KEY")
    if not cle:
        print("Erreur : définir la variable d'environnement YOUTUBE_API_KEY.", file=sys.stderr)
        return 1
    chaines = [c.strip() for c in args.chaines.split(",") if c.strip()]
    if not chaines:
        print("Erreur : indiquer au moins une chaîne avec --chaines.", file=sys.stderr)
        return 1

    resultat = analyser_chaines(cle, chaines, args.jours, args.seuil, args.minimum, args.seuil_short)
    if args.sortie == "json":
        print(json.dumps(resultat, indent=2, ensure_ascii=False))
    else:
        afficher(resultat, args.jours, args.seuil)
    return 0


if __name__ == "__main__":
    sys.exit(main())
