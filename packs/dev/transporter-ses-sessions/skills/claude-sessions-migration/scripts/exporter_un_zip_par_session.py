# -*- coding: utf-8 -*-
"""UN ZIP PAR SESSION, et chaque zip porte son PROMPT-REPRISE.md.

POURQUOI CE SCRIPT EXISTE
─────────────────────────
La regle « un zip par session » est gravee dans SKILL.md depuis le 2026-08-25. Elle
etait DOCTRINE SANS CODE : `export_claude_sessions.py` ne sait produire qu'un bundle
FUSIONNE, sans PROMPT-REPRISE.md ni LISEZ-MOI.md. Mesure du 2026-09-03 — `grep -n
"PROMPT-REPRISE\\|par_session"` sur l'exporteur rendait **zero**. Consequence : chaque
session refabriquait ce pilote a la main, donc chaque session pouvait l'oublier.

Une regle qu'aucun outil n'execute est une regle qu'on applique par memoire.

CE QUE FAIT CE SCRIPT
─────────────────────
Il appelle `export_claude_sessions.py --sidebar --manifest` UNE FOIS PAR SESSION, sur
un manifest a une seule entree, puis ecrit dans chaque dossier son PROMPT-REPRISE.md
(prompt exact, cwd, chemin local du transcript, dernier echange reel de la session),
zippe, et VERIFIE le zip produit.

Le controle est falsifie a chaque execution : un zip vide doit etre REFUSE avant que
le premier OUI ne compte (un controle incapable de dire NON ne vaut
pas son OUI).

⚠️ MAX_PATH — LE PIEGE QUI FAIT ECHOUER L'EXPORTEUR SANS LE NOMMER
`write_session_md` compose le nom du .md depuis le TITRE BRUT (emoji, accents, points).
Sous un dossier de sortie profond, le chemin depasse 260 caracteres et Windows rend un
`FileNotFoundError` — qui se lit comme « fichier absent », jamais comme « chemin trop
long ». D'ou `--travail`, qui force un repertoire de travail COURT. Ne pas le pointer
vers un scratchpad de session : ils font deja ~140 caracteres a eux seuls.

USAGE
─────
    # 1) construire le manifest (PowerShell — %APPDATA% est invisible au harness) :
    #    cf SKILL.md § Pont manifest
    # 2) puis :
    py exporter_un_zip_par_session.py --manifest <json> --dest <dossier> \
       --cli <id> [--cli <id> ...]  [--lot <nom>] [--travail C:\\...\\Temp\\ccx]

    # tout un scope au lieu d'une liste de cli :
    py exporter_un_zip_par_session.py --manifest <json> --dest <dossier> \
       --cwd "C:\\Users\\...\\mon-depot"

APRES : joindre les plans hors-git, zip par zip (ils ne voyagent NI par git NI par le
zip) — `joindre_au_zip_ce_qui_ne_voyage_pas.py <zip> --dry-run` puis sans --dry-run.

Sortie : 0 termine · 1 le controle lui-meme est casse · 2 au moins un zip non conforme
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import unicodedata
import zipfile
from datetime import date
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
EXPORTEUR = SKILL / "scripts" / "export_claude_sessions.py"
PROJECTS = Path(os.path.expanduser("~")) / ".claude" / "projects"
TRAVAIL_DEFAUT = Path(os.environ.get("LOCALAPPDATA", os.path.expanduser("~"))) / "Temp" / "ccx"


def slug(titre: str, cli: str) -> str:
    t = unicodedata.normalize("NFKD", titre or "session")
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = "".join(c if (c.isascii() and (c.isalnum() or c in " -_")) else " " for c in t)
    t = re.sub(r"\s+", "-", t.strip()).strip("-").lower()
    return f"{re.sub(r'-{2,}', '-', t)[:52].strip('-') or 'session'}_{cli[:8]}"


def transcript_de(cli: str, cwd: str) -> Path:
    """Le .jsonl porte le cliSessionId, JAMAIS le sessionId (piege mesure 2026-08-15 :
    chercher par sessionId rend 2 sur 20 — un faux zero parfaitement credible)."""
    encode = Path(cwd).as_posix().replace(":", "-").replace("/", "-").replace("\\", "-")
    direct = PROJECTS / encode / f"{cli}.jsonl"
    if direct.exists():
        return direct
    trouve = list(PROJECTS.glob(f"*/{cli}.jsonl"))
    return trouve[0] if trouve else direct


def dernier_echange(jsonl: Path, budget: int = 400_000):
    """Le dernier message de chaque cote. On lit la QUEUE seulement : un transcript de
    session computer-use depasse 90 Mo, et c'est la fin qui dit sur quoi elle repart."""
    if not jsonl.exists():
        return None, None, 0
    taille = jsonl.stat().st_size
    with jsonl.open("rb") as fh:
        if taille > budget:
            fh.seek(taille - budget)
            fh.readline()  # ligne coupee par le seek
        brut = fh.read().decode("utf-8", "replace")
    du = da = None
    n = 0
    for ligne in brut.splitlines():
        ligne = ligne.strip()
        if not ligne.startswith("{"):
            continue
        try:
            rec = json.loads(ligne)
        except Exception:
            continue
        n += 1
        msg = rec.get("message") or {}
        role = msg.get("role") or rec.get("type")
        c = msg.get("content")
        txt = c if isinstance(c, str) else " ".join(
            b.get("text", "") for b in c if isinstance(b, dict) and b.get("type") == "text"
        ) if isinstance(c, list) else ""
        txt = re.sub(r"\s+", " ", txt).strip()
        if not txt or txt.startswith("<") or "system-reminder" in txt[:200]:
            continue
        if role == "user":
            du = txt
        elif role == "assistant":
            da = txt
    return du, da, n


def ecrire_prompt_reprise(dossier: Path, s: dict, jsonl: Path, lot: str) -> None:
    du, da, _ = dernier_echange(jsonl)
    titre, cli, cwd = s.get("title", "(sans titre)"), s["cli"], s.get("cwd", "")
    L = [
        f"# PROMPT DE REPRISE — {titre}", "",
        "| | |", "|---|---|",
        f"| **Session** | {titre} |",
        f"| **Dossier de travail (`cwd`)** | `{cwd}` |",
        f"| **Transcript local** | `{jsonl}` |",
        f"| **`cliSessionId`** | `{cli}` |",
        f"| **`sessionId`** | `{s.get('sessionId', '?')}` |",
        "| **A l'arrivee** | **REJOINDRE** — meme PC, store des titres PARTAGE entre "
        "comptes : la session est deja retrouvable. Chercher le titre exact **archivees "
        "comprises** AVANT de creer. Creer seulement si la recherche rend zero. |",
        f"| **Export** | {lot} |", "",
        "## Ce que la session faisait AVANT la migration", "",
        "> La migration est un intermede, jamais le sujet. Cette session repart sur SON chantier.", "",
    ]
    if du:
        L += ["**Dernier message de l'utilisateur :**", "", f"> {du[:900]}", ""]
    if da:
        L += ["**Dernier etat rendu par Claude :**", "", f"> {da[:900]}", ""]
    if not du and not da:
        L += ["*(queue du transcript illisible — lire le `.jsonl` directement)*", ""]
    lecteur = SKILL / "scripts" / "read_claude_session.py"
    L += [
        "## Le prompt a donner a la session", "", "```text",
        f"Tu reprends la session « {titre} ».", "",
        f"1. Charge D'ABORD la FIN de son transcript : {jsonl}",
        f'   (py "{lecteur}" "{jsonl}")',
        "2. Retrouve le PLAN en cours s'il y en a un (~/.claude/plans/, et les fichiers "
        "cites en fin de transcript ; regarde aussi fichiers-de-travail/ dans ce zip).",
        f"3. Charge les competences de son domaine, depuis {cwd} "
        "(CLAUDE.md du depot + /router-competence-outil-ia si l'owner n'est pas evident).",
        "4. Restitue UNE SEULE FOIS : sujet, etat, ce qui est fait, ce qui reste, prochaine action.",
        "5. Puis DEROULE sans redemander le go — l'objectif est deja valide.",
        "6. PLAN D'ABORD : pose le plan complet du RESTE (lots, preuves, acquis a ne pas rejouer,",
        "   ce qui reste a l'utilisateur : irreversible, gout produit, ses comptes). Valide d'avance.",
        "7. BOUCLE A LA TAILLE DU RESTE : `/loop <cadence> <competence>` dans CETTE session, visible,",
        "   si ton hote le propose. Un reste d'un ou deux tours ne prend pas de boucle : tu le finis.",
        "   Elle s'arrete quand le contrat est livre et PROUVE -- jamais avant, jamais a vide.",
        "```", "",
        "## Relance native (optionnelle, meme PC)", "", "```bash",
        f'cd "{cwd}"', f"claude --resume {cli}", "```", "",
        "---",
        "Lot produit par `/claude-sessions-migration`. "
        "Reinjection : `/claude-sessions-migration`.",
    ]
    (dossier / "PROMPT-REPRISE.md").write_text("\n".join(L), encoding="utf-8")


def zipper(dossier: Path, cible: Path) -> None:
    if cible.exists():
        cible.unlink()
    with zipfile.ZipFile(cible, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for p in sorted(dossier.rglob("*")):
            if p.is_file():
                z.write(p, p.relative_to(dossier).as_posix())


def controle(zpath: Path):
    """LE controle du skill : un transcript ET un PROMPT-REPRISE.md dont le chemin de
    transcript EXISTE. Rend (ok, motif)."""
    try:
        with zipfile.ZipFile(zpath) as z:
            noms = z.namelist()
            if not [n for n in noms if n.endswith(".jsonl")]:
                return False, "aucun transcript .jsonl"
            if "PROMPT-REPRISE.md" not in noms:
                return False, "PROMPT-REPRISE.md absent"
            m = re.search(r"\*\*Transcript local\*\* \| `([^`]+)`",
                          z.read("PROMPT-REPRISE.md").decode("utf-8"))
            if not m:
                return False, "PROMPT-REPRISE.md ne nomme aucun transcript"
            if not Path(m.group(1)).exists():
                return False, f"transcript nomme introuvable : {m.group(1)}"
            plans = [n for n in noms if n.startswith("fichiers-de-travail/")]
            return True, f"1 transcript, {len(plans)} fichier(s) de travail"
    except zipfile.BadZipFile:
        return False, "zip illisible"


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser(description="Un zip par session, chacun avec son PROMPT-REPRISE.md")
    ap.add_argument("--manifest", required=True, help="JSON du store sidebar (cf SKILL.md § Pont manifest)")
    ap.add_argument("--dest", required=True, help="Dossier du lot (un zip par session + LISEZ-MOI.md)")
    ap.add_argument("--cli", action="append", default=[], help="cliSessionId a exporter (repetable)")
    ap.add_argument("--cwd", default=None, help="Au lieu de --cli : toutes les sessions non archivees de ce cwd EXACT")
    ap.add_argument("--lot", default=None, help="Nom lisible du lot (defaut : la date)")
    ap.add_argument("--travail", default=str(TRAVAIL_DEFAUT),
                    help="Repertoire de travail COURT — MAX_PATH 260, cf docstring")
    a = ap.parse_args()

    lot = a.lot or date.today().isoformat()
    dest, travail = Path(a.dest), Path(a.travail)
    sessions = {s["cli"]: s for s in json.loads(Path(a.manifest).read_text(encoding="utf-8")) if s.get("cli")}

    if a.cwd:
        cibles = [c for c, s in sessions.items()
                  if str(s.get("cwd", "")).rstrip("\\/").lower() == a.cwd.rstrip("\\/").lower()
                  and not s.get("archived")]
    else:
        cibles = [c for c in a.cli if c in sessions]
        if len(cibles) != len(a.cli):
            print(f"ARRET : {len(a.cli) - len(cibles)} cliSessionId absent(s) du manifest.")
            return 2
    if not cibles:
        print("ARRET : aucune session selectionnee — le manifest ou le filtre est en cause.")
        return 2

    if travail.exists():
        shutil.rmtree(travail)
    travail.mkdir(parents=True)
    dest.mkdir(parents=True, exist_ok=True)

    # --- FALSIFIER LE CONTROLE AVANT DE LE CROIRE
    bidon = travail / "_temoin-negatif-vide.zip"
    with zipfile.ZipFile(bidon, "w"):
        pass
    ok_bidon, motif_bidon = controle(bidon)
    print(f"[TEMOIN NEGATIF] zip vide -> accepte={ok_bidon} ({motif_bidon})")
    if ok_bidon:
        print("ARRET : le controle accepte un zip vide, il ne vaut rien.")
        return 1

    resultats = []
    for cli in cibles:
        s = sessions[cli]
        d = travail / slug(s.get("title", ""), cli)
        d.mkdir(parents=True, exist_ok=True)
        mini = travail / f"m_{cli[:8]}.json"
        mini.write_text(json.dumps([s], ensure_ascii=False), encoding="utf-8")
        r = subprocess.run(
            [sys.executable, str(EXPORTEUR), "--sidebar", "--manifest", str(mini),
             "--flat", "--full", "--out", str(d)],
            capture_output=True, text=True, encoding="utf-8", errors="replace")
        if r.returncode != 0:
            queue = (r.stderr or r.stdout).strip().splitlines()[-1:] or ["(sans message)"]
            print(f"[NON] EXPORT ECHOUE  {s.get('title')} -> {queue[0]}")
            resultats.append((s, None, False, "export en echec"))
            continue
        jsonl = transcript_de(cli, s.get("cwd", ""))
        ecrire_prompt_reprise(d, s, jsonl, lot)
        cible = dest / f"migration-{slug(s.get('title', ''), cli)}_{lot}.zip"
        zipper(d, cible)
        ok, motif = controle(cible)
        print(f"[{'OK ' if ok else 'NON'}] {cible.stat().st_size / 1048576:7.1f} Mo  {cible.name}  ({motif})")
        resultats.append((s, cible, ok, motif))

    conformes = sum(1 for _, _, ok, _ in resultats if ok)
    lignes = [
        f"# Sessions Claude Code — lot `{lot}`", "",
        f"**{conformes} sessions, un zip chacune.** Ouvre celui qui t'interesse, rien a trier.", "",
        "1. Invoque **`/claude-sessions-migration`** et donne-lui ce dossier (ou un zip precis).",
        "2. Chaque zip porte son **`PROMPT-REPRISE.md`** : prompt exact, `cwd`, chemin local du transcript, dernier echange.",
        "3. Meme PC, store des titres PARTAGE entre comptes : ces sessions se **REJOIGNENT** "
        "(titre exact, archivees comprises) — on n'en cree une neuve que si la recherche rend zero.", "",
        "| Session | Zip | Poids |", "|---|---|---|",
    ]
    for s, cible, ok, motif in resultats:
        if ok and cible:
            lignes.append(f"| {s.get('title')} | `{cible.name}` | {cible.stat().st_size / 1048576:.1f} Mo |")
        else:
            lignes.append(f"| {s.get('title')} | **ECHEC — {motif}** | — |")
    lignes += [
        "", "## Ce que ces zips ne contiennent pas", "",
        "- **Le travail** : il voyage par **git**, pas par le zip.",
        "- **Les plans** hors-git, SAUF s'ils ont ete joints ensuite dans `fichiers-de-travail/` "
        "(`joindre_au_zip_ce_qui_ne_voyage_pas.py`). Un chemin de plan **cite** dans un transcript "
        "n'est pas un fichier joint.", "",
        "---",
        "Produit par `/claude-sessions-migration`. Rien n'a ete archive : exporter n'archive "
        "pas, et archiver reste le geste de l'utilisateur.",
    ]
    (dest / "LISEZ-MOI.md").write_text("\n".join(lignes), encoding="utf-8")
    shutil.rmtree(travail, ignore_errors=True)
    print(f"\nLOT : {dest}\nCONFORMES : {conformes}/{len(cibles)}")
    return 0 if conformes == len(cibles) else 2


if __name__ == "__main__":
    sys.exit(main())
