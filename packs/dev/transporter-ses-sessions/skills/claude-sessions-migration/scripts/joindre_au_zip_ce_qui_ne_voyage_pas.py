# -*- coding: utf-8 -*-
"""Joint au zip d'export les fichiers que la session CITE et que rien d'autre ne transporte.

LE PROBLEME, MESURE
───────────────────
`/export` produit un zip qui contient la CONVERSATION, jamais le TRAVAIL. Mesure du
2026-08-15 sur un export reel : 18 fichiers — transcript, metadonnees, 14 journaux de
l'application — et **zero** fichier de travail.

Le travail voyage normalement par **git**. Mais tout ce qu'une session produit n'est
pas suivi par git : un plan sous `~/.claude/plans/` (dossier `.gitignore`), une note
de scratchpad, un rapport pose hors depot. Ces fichiers ne voyagent alors NI par git
NI par le zip : ils meurent avec le PC. Mesure du meme jour : **97 plans** sur cette
machine, tous dans ce cas — dont celui d'un chantier en cours.

LE CRITERE, ET C'EST LUI QUI REND L'OUTIL SUR
─────────────────────────────────────────────
Un fichier est joint si les TROIS sont vrais :

  1. la session le **cite** (il apparait dans le transcript) ;
  2. il **existe** sur ce disque ;
  3. **git ne le transporte pas** — hors depot, ou ignore, ou jamais suivi.

La condition 3 est ce qui evite de dupliquer le depot dans chaque zip : un fichier
suivi par git arrivera de toute facon par `git pull`, et le joindre fabriquerait une
seconde copie, plus vieille, que quelqu'un finira par croire.

⚠️ CE SCRIPT EST UN FILET, PAS LA SOLUTION. La bonne fin d'un chantier reste de
DISSOUDRE son plan dans le depot (la methode chez sa competence, l'etat chez son
proprietaire). Un fichier joint a un zip reste un fichier que personne ne relira.

Usage :
    py joindre_au_zip_ce_qui_ne_voyage_pas.py <zip> [--dry-run] [--max-ko 512]

Sortie : 0 termine · 3 ABORT (l'instrument ne peut pas conclure — jamais un faux vert)
"""
from __future__ import annotations

import re
import subprocess
import sys
import zipfile
from pathlib import Path

DOSSIER_DANS_ZIP = "fichiers-de-travail"
MAX_KO_DEFAUT = 512

# Seulement ce qui se relit. Un binaire ou un journal n'aide personne a reprendre.
EXTENSIONS = {".md", ".txt", ".json", ".yaml", ".yml", ".toml", ".csv", ".tsv"}

# Un chemin absolu Windows tel qu'il apparait dans du JSON : antislashs doubles.
MOTIF_CHEMIN = re.compile(
    r"[A-Za-z]:(?:\\\\|\\|/)[^\"'\s,;)\]]+?\.(?:md|txt|json|yaml|yml|toml|csv|tsv)"
)

# LISTE BLANCHE de racines, et c'est volontairement une liste blanche.
#
# Une liste noire a ete essayee, puis jetee : sur une trentaine de chemins cites, elle
# retenait la LICENCE de Git, un inventaire de paquets ComfyUI et un `builtins.txt` de
# mingw — des fichiers d'installation qu'un message d'erreur avait cites au passage.
# Le bruit d'un transcript est ILLIMITE et imprevisible ; les endroits ou vit le
# travail sont, eux, en petit nombre et connus. On enumere donc ce qu'on garde.
#
# >>> A ADAPTER CHEZ TOI <<<
# `.claude/plans` est standard, Claude Code les ecrit toujours la. Le second motif nomme
# le dossier ou vivent TES depots : remplace `PROJECTS` ci-dessous par le tien (`code`,
# `dev`, `repos`, `src`...). Sans ca, l'outil ne joindra que les plans.
RACINES_DE_TRAVAIL = re.compile(
    r"(?:\\|/)\.claude(?:\\|/)plans(?:\\|/)"   # les plans — le cas qui a motive l'outil
    r"|(?:\\|/)PROJECTS(?:\\|/)",              # les depots : ce qui y est NON suivi par git
    re.I,
)

# Ce qu'on ne joint jamais, meme sous une racine de travail : derive, volumineux, ou
# reconstruit a l'arrivee. `tool-results` est deja dans le transcript par definition.
EXCLUS = re.compile(
    r"(?:\\|/)(?:\.git|node_modules|__pycache__|logs|\.pytest_logs|site-packages|"
    r"tool-results|\.claude(?:\\|/)worktrees)(?:\\|/)",
    re.I,
)


def _normaliser(brut: str) -> Path:
    return Path(brut.replace("\\\\", "\\").replace("/", "\\"))


def chemins_cites(zip_path: Path) -> set[Path]:
    """Les chemins de fichiers que le transcript mentionne, dedupliques."""
    trouves: set[Path] = set()
    with zipfile.ZipFile(zip_path) as z:
        cibles = [n for n in z.namelist() if n.endswith((".jsonl", ".json"))]
        if not cibles:
            raise ValueError("aucun transcript dans le zip — ce n'est pas un export de session")
        for nom in cibles:
            with z.open(nom) as f:
                for ligne in f:
                    texte = ligne.decode("utf-8", errors="replace")
                    for m in MOTIF_CHEMIN.finditer(texte):
                        trouves.add(_normaliser(m.group(0)))
    return trouves


def git_le_transporte(p: Path) -> bool:
    """Vrai si git suit ce fichier — donc il arrivera par `git pull`, pas par le zip.

    On interroge git DEPUIS le dossier du fichier : un chemin peut appartenir a
    n'importe lequel des depots de la machine, et supposer lequel serait faux.
    """
    try:
        r = subprocess.run(
            ["git", "ls-files", "--error-unmatch", "--", p.name],
            cwd=str(p.parent), capture_output=True, timeout=10,
        )
        return r.returncode == 0
    except (OSError, subprocess.SubprocessError):
        return False  # pas de depot ici : git ne le transporte pas


def main() -> int:
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 3
    zip_path = Path(args[0])
    a_blanc = "--dry-run" in args
    max_ko = MAX_KO_DEFAUT
    if "--max-ko" in args:
        i = args.index("--max-ko")
        if i + 1 < len(args):
            max_ko = int(args[i + 1])
    if not zip_path.exists():
        print(f"[zip] ABORT — introuvable : {zip_path}", file=sys.stderr)
        return 3

    try:
        cites = chemins_cites(zip_path)
    except (ValueError, zipfile.BadZipFile) as e:
        print(f"[zip] ABORT — {e}", file=sys.stderr)
        return 3

    # Temoin positif : une session cite forcement des fichiers. Zero ici mesure
    # l'instrument, pas la session (doctrine : un zero se prouve par un positif).
    print(f"[zip] temoin : {len(cites)} chemin(s) cite(s) dans le transcript")
    if not cites:
        print("[zip] ABORT — aucun chemin lu. Le motif ou le transcript est en cause.", file=sys.stderr)
        return 3

    retenus, ecartes = [], {"absent": 0, "git": 0, "exclu": 0, "gros": 0, "ext": 0, "hors": 0}
    for p in sorted(cites):
        if not RACINES_DE_TRAVAIL.search(str(p)):
            ecartes["hors"] += 1
        elif EXCLUS.search(str(p)):
            ecartes["exclu"] += 1
        elif p.suffix.lower() not in EXTENSIONS:
            ecartes["ext"] += 1
        elif not p.is_file():
            ecartes["absent"] += 1
        elif p.stat().st_size > max_ko * 1024:
            ecartes["gros"] += 1
        elif git_le_transporte(p):
            ecartes["git"] += 1
        else:
            retenus.append(p)

    print(
        f"[zip] ecartes — {ecartes['git']} transportes par git · {ecartes['hors']} hors des "
        f"racines de travail · {ecartes['absent']} absents du disque · {ecartes['exclu']} exclus · "
        f"{ecartes['gros']} > {max_ko} Ko · {ecartes['ext']} hors extensions"
    )
    if not retenus:
        print("[zip] rien a joindre — tout ce que la session cite voyage deja.")
        return 0

    if a_blanc:
        for p in retenus:
            print(f"[zip] joindrait : {p.name} ({p.stat().st_size // 1024} Ko) <- {p.parent}")
        print(f"[zip] {len(retenus)} fichier(s) — relancer sans --dry-run pour ecrire")
        return 0

    with zipfile.ZipFile(zip_path) as z:
        deja = set(z.namelist())
    with zipfile.ZipFile(zip_path, "a", zipfile.ZIP_DEFLATED) as z:
        for p in retenus:
            arc = f"{DOSSIER_DANS_ZIP}/{p.name}"
            if arc in deja:
                print(f"[zip] deja present : {arc}")
                continue
            z.write(p, arc)
            deja.add(arc)
            print(f"[zip] joint : {arc} ({p.stat().st_size // 1024} Ko)")

    # Relecture par un AUTRE chemin que l'ecriture : la reponse d'un outil sur son
    # propre effet n'est pas une preuve.
    with zipfile.ZipFile(zip_path) as z:
        joints = [n for n in z.namelist() if n.startswith(f"{DOSSIER_DANS_ZIP}/")]
    print(f"[zip] OK — {len(joints)} fichier(s) verifie(s) dans le zip apres ecriture")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
