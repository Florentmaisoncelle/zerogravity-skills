#!/usr/bin/env python3
"""Valide, note et classe des idées de shorts (JSON). Python standard seulement.

Chaque idée : id, sujet, accroche, note_potentiel, note_accroche (1 à 10), puces (exactement 3),
reponse_complete, niveau_preuve (1 à 5), statut_affirmation, source (liste de {libelle, url}),
video_reference (https://... ou "a trouver"), emprunt (obligatoire si une référence est donnée),
suite, limite_de_l_affirmation.

Priorité = moyenne de note_potentiel et note_accroche. Le classement met d'abord les idées
prêtes (niveau de preuve 1 ou 2), puis celles à réparer (3), puis à reclasser (4 ou 5).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

CHAMPS_TEXTE = (
    "id", "sujet", "accroche", "reponse_complete", "statut_affirmation", "suite", "limite_de_l_affirmation",
)
CHAMPS_NOTE = ("note_potentiel", "note_accroche")
STATUTS = {"atteint", "estimation", "anecdote", "prevision", "objectif", "plan"}
STATUT_PAR_NIVEAU = {1: "pret", 2: "pret", 3: "a_reparer", 4: "a_reclasser", 5: "a_reclasser"}
ORDRE_STATUT = {"pret": 0, "a_reparer": 1, "a_reclasser": 2}


def charger(chemin: Path) -> list[dict[str, Any]]:
    donnees = json.loads(chemin.read_text(encoding="utf-8"))
    if not isinstance(donnees, list):
        raise ValueError("le fichier doit contenir un tableau JSON")
    if not all(isinstance(ligne, dict) for ligne in donnees):
        raise ValueError("chaque élément du tableau doit être un objet")
    return donnees


def valider(idee: dict[str, Any], numero: int) -> list[str]:
    p = f"ligne {numero}"
    erreurs: list[str] = []

    for champ in CHAMPS_TEXTE:
        if not isinstance(idee.get(champ), str) or not idee[champ].strip():
            erreurs.append(f"{p} : {champ} doit être un texte non vide")

    identifiant = idee.get("id")
    if isinstance(identifiant, str) and not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", identifiant):
        erreurs.append(f"{p} : id doit être en minuscules séparées par des tirets")

    statut = idee.get("statut_affirmation")
    if isinstance(statut, str) and statut not in STATUTS:
        erreurs.append(f"{p} : statut_affirmation doit être l'un de " + ", ".join(sorted(STATUTS)))

    puces = idee.get("puces")
    if not isinstance(puces, list) or len(puces) != 3 or not all(isinstance(x, str) and x.strip() for x in puces):
        erreurs.append(f"{p} : puces doit contenir exactement trois textes")

    niveau = idee.get("niveau_preuve")
    if isinstance(niveau, bool) or niveau not in (1, 2, 3, 4, 5):
        erreurs.append(f"{p} : niveau_preuve doit être un entier de 1 à 5")

    sources = idee.get("source")
    if not isinstance(sources, list):
        erreurs.append(f"{p} : source doit être un tableau")
    else:
        for i, source in enumerate(sources, 1):
            if not isinstance(source, dict):
                erreurs.append(f"{p} : la source {i} doit être un objet")
                continue
            for champ in ("libelle", "url"):
                if not isinstance(source.get(champ), str) or not source[champ].strip():
                    erreurs.append(f"{p} : source {i}, {champ} doit être non vide")
        if niveau in (1, 2) and not sources:
            erreurs.append(f"{p} : un niveau de preuve 1 ou 2 exige au moins une source")

    reference = idee.get("video_reference")
    if not isinstance(reference, str) or not reference.strip():
        erreurs.append(f"{p} : video_reference doit être une adresse https ou 'a trouver'")
    elif reference != "a trouver":
        if not re.match(r"https?://", reference):
            erreurs.append(f"{p} : video_reference doit commencer par http(s):// ou valoir 'a trouver'")
        if not isinstance(idee.get("emprunt"), str) or not idee["emprunt"].strip():
            erreurs.append(f"{p} : emprunt est obligatoire quand une vidéo de référence est donnée")

    for champ in CHAMPS_NOTE:
        valeur = idee.get(champ)
        if isinstance(valeur, bool) or not isinstance(valeur, (int, float)):
            erreurs.append(f"{p} : {champ} doit être un nombre")
        elif not 1 <= valeur <= 10:
            erreurs.append(f"{p} : {champ} doit être compris entre 1 et 10")

    return erreurs


def priorite(idee: dict[str, Any]) -> float:
    return round((float(idee["note_potentiel"]) + float(idee["note_accroche"])) / 2, 1)


def classer(idees: list[dict[str, Any]]) -> list[dict[str, Any]]:
    for idee in idees:
        idee["priorite"] = priorite(idee)
        idee["statut"] = STATUT_PAR_NIVEAU[idee["niveau_preuve"]]
    idees.sort(key=lambda i: (ORDRE_STATUT[i["statut"]], -i["priorite"]))
    for rang, idee in enumerate(idees, 1):
        idee["rang"] = rang
    return idees


def _sortie_utf8() -> None:
    """Sortie en UTF-8 quel que soit l'encodage de la console (Windows : cp1252)."""
    for flux in (sys.stdout, sys.stderr):
        try:
            flux.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass


def main() -> None:
    _sortie_utf8()
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("entree", type=Path)
    parser.add_argument("--sortie", type=Path)
    parser.add_argument("--valider-seulement", action="store_true")
    args = parser.parse_args()

    try:
        idees = charger(args.entree)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"erreur de validation : {exc}", file=sys.stderr)
        raise SystemExit(2)

    erreurs = [e for n, idee in enumerate(idees, 1) for e in valider(idee, n)]
    if erreurs:
        for erreur in erreurs:
            print(erreur, file=sys.stderr)
        raise SystemExit(2)

    if args.valider_seulement:
        print(f"valide : {len(idees)} idées")
        return

    texte = json.dumps(classer(idees), ensure_ascii=False, indent=2) + "\n"
    if args.sortie:
        args.sortie.write_text(texte, encoding="utf-8")
    else:
        print(texte, end="")


if __name__ == "__main__":
    main()
