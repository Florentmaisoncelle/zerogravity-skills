#!/usr/bin/env python3
"""Vérifie que chaque coupe d'un montage commence et finit sur une pensée complète.

Entrées (JSON) :
  --transcript : {"granularity": "sentence" | "word",
                  "segments": [{"start": 0.0, "end": 2.4, "text": "..."}, ...]}
  --clips      : {"retained_clips": [{"id", "source_start", "content_start",
                                      "content_end", "source_end"}, ...]}
                 (ou directement la liste des clips)

Une pensée complète = une phrase. En granularité « word », les mots sont regroupés en
phrases à la ponctuation finale (. ? ! …) ; sans cela, n'importe quel début de mot
passerait pour une coupe propre. Python standard seulement, aucun accès réseau.
"""

import argparse
import json
import sys
from pathlib import Path

FIN_DE_PHRASE = (".", "?", "!", "…")


def phrases(segments, granularity):
    """Renvoie la liste des (début, fin) de phrases."""
    if granularity == "sentence":
        return [(float(s["start"]), float(s["end"])) for s in segments]
    resultat, debut = [], None
    for mot in segments:
        if debut is None:
            debut = float(mot["start"])
        if str(mot.get("text", "")).rstrip().endswith(FIN_DE_PHRASE):
            resultat.append((debut, float(mot["end"])))
            debut = None
    if debut is not None and segments:
        resultat.append((debut, float(segments[-1]["end"])))
    return resultat


def auditer(transcript, clips, tolerance):
    erreurs, audites = [], []
    granularity = transcript.get("granularity")
    segments = transcript.get("segments", [])
    if granularity not in {"word", "sentence"}:
        erreurs.append("la granularité de la transcription doit être 'word' ou 'sentence'")
    if not segments or not clips:
        erreurs.append("la transcription et les clips retenus sont obligatoires")
    if erreurs:
        return {"statut": "ECHEC", "clips": [], "erreurs": erreurs}

    try:
        unites = phrases(segments, granularity)
    except (KeyError, TypeError, ValueError) as exc:
        return {"statut": "ECHEC", "clips": [], "erreurs": [f"transcription mal formée : {exc}"]}
    debuts = [u[0] for u in unites]
    fins = [u[1] for u in unites]

    for index, clip in enumerate(clips, 1):
        clip_id = str(clip.get("id", f"clip-{index}"))
        problemes = []
        proche_debut = proche_fin = 0.0
        try:
            source_start = float(clip["source_start"])
            content_start = float(clip["content_start"])
            content_end = float(clip["content_end"])
            source_end = float(clip["source_end"])
            proche_debut = min(debuts, key=lambda v: abs(v - content_start))
            proche_fin = min(fins, key=lambda v: abs(v - content_end))
            if abs(proche_debut - content_start) > tolerance:
                problemes.append("content_start ne tombe pas sur le début d'une phrase")
            if abs(proche_fin - content_end) > tolerance:
                problemes.append("content_end ne tombe pas sur la fin d'une phrase")
            if not source_start <= content_start < content_end <= source_end:
                problemes.append("les temps source et contenu ne sont pas dans l'ordre")
        except (KeyError, TypeError, ValueError) as exc:
            problemes.append(f"champs de temps mal formés : {exc}")
        audites.append(
            {
                "id": clip_id,
                "debut_proche": proche_debut,
                "fin_proche": proche_fin,
                "statut": "OK" if not problemes else "ECHEC",
                "erreurs": problemes,
            }
        )
        erreurs.extend(f"{clip_id} : {m}" for m in problemes)

    return {
        "statut": "OK" if not erreurs else "ECHEC",
        "granularite": granularity,
        "clips": audites,
        "erreurs": erreurs,
    }


def _sortie_utf8() -> None:
    """Sortie en UTF-8 quel que soit l'encodage de la console (Windows : cp1252)."""
    for flux in (sys.stdout, sys.stderr):
        try:
            flux.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass


def main() -> int:
    _sortie_utf8()
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--transcript", type=Path, required=True)
    parser.add_argument("--clips", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--tolerance", type=float, default=0.12, help="écart toléré en secondes (0,12 par défaut)")
    args = parser.parse_args()

    try:
        transcript = json.loads(args.transcript.read_text(encoding="utf-8"))
        donnees = json.loads(args.clips.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"lecture impossible : {exc}", file=sys.stderr)
        return 2
    clips = donnees.get("retained_clips", []) if isinstance(donnees, dict) else donnees
    rapport = auditer(transcript, clips, args.tolerance)
    rendu = json.dumps(rapport, indent=2, ensure_ascii=False)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendu + "\n", encoding="utf-8")
    print(rendu)
    return 0 if rapport["statut"] == "OK" else 1


if __name__ == "__main__":
    sys.exit(main())
