---
name: claude-sessions-migration
description: >-
  LA compétence unique des sessions Claude Code qui voyagent. Trois gestes. ① RETROUVER et RELANCER
  une session disparue — autre compte Claude sur CE PC, sidebar vide, session morte (contexte plein) —
  SANS export préalable : le store sur disque est partagé entre comptes (`list_sessions` ne les voit
  pas, `--sidebar` si) ; un chip par session, Claude lit le transcript et reprend le fil.
  ② EXPORTER / INVENTORIER les `~/.claude/projects/*.jsonl` — sauvegarde avant bascule de compte,
  index, zip pour un AUTRE PC — zéro token, zéro compte actif. ③ TRANSPORTER par git
  (`.claude-sessions/` committé, petit dépôt privé) puis réinjecter ailleurs, remap automatique du
  username. Triggers : "/claude-sessions-migration", "retrouve / récupère / relance mes sessions",
  "elle est sur mon autre compte", "j'ai changé de compte Claude", "plus de crédits reprends mes
  sessions", "session morte contexte plein", "exporte / sauvegarde mes sessions", "je migre ces
  sessions", "migration compte Claude", "emmène mes sessions sur l'autre PC", "réinjecte le zip",
  "sync / photographie / snapshot les sessions de ce dépôt", "transporte mes sessions par git".
  🖼️ Un SCREENSHOT de la sidebar avec « je migre » / « je change de compte » / « sur mon autre
  compte » = ICI, immédiatement — jamais un handoff.
---

# Sessions Claude Code — retrouver, relancer, exporter, transporter

> 🧭 **UNE SEULE COMPÉTENCE, TROIS GESTES.** Depuis la version 0.2.0 du pack, les deux compétences
> `claude-sessions-export` et `claude-sessions-import` sont **fondues ici**, et le transport par git
> (petits dépôts privés) les rejoint. Rien n'a été retiré : chaque geste garde sa partie.
>
> | Partie | Le geste |
> |---|---|
> | **§ ①** | **RETROUVER & RELANCER** une session disparue sur CE PC (autre compte Claude, sidebar vide, session morte) — 0 crédit, aucun export — et **réinjecter** un bundle venu d'ailleurs |
> | **§ ②** | **EXPORTER / INVENTORIER** — sauvegarde, index, zip pour un autre PC |
> | **§ ③** | **TRANSPORTER PAR GIT** — snapshot dans `.claude-sessions/`, pull et relance de l'autre côté |
>
> Le cas se lit dans la PORTE D'ENTRÉE juste en dessous ; ne jamais commencer par une partie.

## 🧭 PORTE D'ENTRÉE — établir le cas AVANT de toucher à quoi que ce soit

> ⚠️ **Ce bloc est le premier geste, quel que soit ce qu'on te demande.** Les gestes qui suivent
> (§ ①, § ②, § ③) se ressemblent et font des choses **opposées** ; le seul vrai piège du sujet est de
> partir dans le mauvais. On établit le cas ici, puis on va au bon §.

### 1. Déduire d'abord — la demande contient presque toujours la réponse

Ne jamais ouvrir par un interrogatoire : la plupart des formulations tranchent déjà.

| Ce que dit l'utilisateur | Cas |
|---|---|
| « sur ce PC », « un autre compte », « je ne la vois plus », « ma sidebar est vide », « session morte / contexte plein » — ou il **nomme** simplement une session | **A** |
| il parle d'un `.zip`, d'une **clé USB**, de « l'autre PC », « mon portable », « celui du bureau » | **B** |
| « je vais changer de compte / de PC », « sauvegarde », « avant que je parte », « au cas où » | **C** |

Signal clair → **annoncer le cas en une ligne et avancer**. Pas de question.

### 2. Demander seulement si c'est réellement ambigu — UNE question

Au moindre doute, poser la question (via `AskUserQuestion`), parce que se tromper de branche coûte
bien plus cher que dix secondes :

> **« La session que tu veux récupérer, elle est sur CE PC, ou sur un AUTRE PC ? »**
> A — sur ce PC, mais je ne la vois plus · B — sur un autre PC · C — je veux juste sauvegarder avant de partir

### 3. Les trois cas

**A — Elle est sur CE PC, mais je ne la vois plus.** *(le plus fréquent)*
Autre compte Claude, sidebar vide après une bascule de compte, session morte (contexte plein).
→ **§ ① ci-dessous**, tout de suite, § 📸 Méthode capture d'écran.
**Aucun export n'est nécessaire — ni maintenant, ni rétroactivement.** Les fichiers de session sont
sur le disque, liés au compte **Windows** et non au compte Claude, et le store des titres est
**partagé entre les comptes**. C'est le cas qu'on rate le plus souvent, en croyant à tort qu'il
faut d'abord avoir exporté.

**B — Elle est sur un AUTRE PC.**
Là, il faut réellement transporter un fichier. Trois gestes, dans l'ordre :
1. **Sur le PC d'origine** → **§ ② EXPORTER** : il produit un `.zip`.
2. **Copier ce `.zip`** sur une clé USB (ou tout autre transport : dossier partagé, cloud, ou `/claude-sessions-migration` § ③ pour les petits dépôts git).
3. **Sur le PC d'arrivée** → **§ ① ci-dessous** (réinjection) en pointant le `.zip`.

   La clé USB est **parfaitement légitime ici** — c'est exactement le cas pour lequel elle existe.

**C — Je pars, je veux juste une sauvegarde.**
Bascule de compte, réinstallation, prudence.
→ **§ ② EXPORTER** seul, § ⚡ Recettes recette 0 ou 1. Zéro token, aucun abonnement actif requis.
Nuance à dire pour éviter la fausse inquiétude : sur le **même PC**, cet export est une **assurance**,
pas un péage — le cas A fonctionnera de toute façon sans lui. Il devient vraiment indispensable dès
qu'on quitte la machine (cas B) ou qu'on risque de perdre le disque.

> Le principe commun aux trois : **Claude lit la session et reprend le fil.** L'utilisateur ne tape
> aucune commande, aucun identifiant — il dit où il en est, et on s'occupe du reste.

> ⛔ **RÈGLE D'OR — UNE SESSION = UNE SESSION, JAMAIS DE FORK/DOUBLON.**
> 1. **On spawn TOUS les chips D'UN COUP, dans le MÊME tour** — zéro lot, zéro pause, zéro « je reviendrai finir ». **Le rationnement 5-par-5 côté Claude est ABOLI (2026-07-16)** : il n'a jamais rien protégé (10 chips OK le 2026-06-20, 12 OK le 2026-07-16) et c'est LUI qui faisait oublier la moitié des sessions. Le « 5 par 5 » n'est PAS une limite de spawn : c'est une consigne **pour l'USER au moment de CLIQUER** → cf 🖐️ ci-dessous.
> 2. Chaque chip lance **UNE session propre** — jamais un fork, jamais un doublon.
> 3. **Si la session existe DÉJÀ / est vivante** (visible dans la sidebar, trackée) → on **POSTE le message DEDANS** (`send_message`, l'outil de message entre sessions de Claude Desktop), on ne la rouvre pas, on ne la re-crée pas. On ne spawne un chip **que** pour une session qui n'a **pas** déjà sa fenêtre vivante.
> 4. **ZÉRO LECTURE DE CONTENU ICI.** Relancer = un lookup MÉCANIQUE `titre → chemin .jsonl` (dict local, quelques lignes), puis `spawn_task`. Point. **Jamais** de `parse_session`/dump de métadonnées (nb messages, dates, aperçu du 1er message) ni de lecture du transcript **dans cette session orchestratrice** — ni pour "vérifier", ni pour "un meilleur titre" (le titre vient déjà de la sidebar). Le contenu se lit **UNE SEULE FOIS**, DANS le chip, à son ouverture. Le relire ici = payer deux fois la même lecture pour zéro décision utile.
>
> *(Jurisprudence 2026-07-10 : forks en masse sur le même PC = doublons inutiles = à ne jamais refaire. « Une session = une session. » — Jurisprudence 2026-07-15 : dump `parse_session` (métadonnées) d'une session déjà résolue, juste avant de spawner son chip = gaspillage pur. L'utilisateur : « 2K token pr relancer une session mdr c une blague ? ». Dès que titre+cwd+chemin `.jsonl` sont connus → spawn IMMÉDIAT, zéro étape de plus.)*

> 🖐️ **LE « 5 PAR 5 » EST UN RAPPEL VÉNÈRE À SERVIR À L'USER — PAS UN RATIONNEMENT DE MES SPAWNS (gravé 2026-07-16).**
> **Moi** : je spawn **TOUTES** les sessions de la liste, d'un coup, tour unique. Mon job de lancement est fini là.
> **Lui** : c'est **au CLIC** que le paquet doit être petit. Donc **toute réponse qui livre des chips de relance se termine par un rappel EXPLICITE et bien visible** (pas une note de bas de page) :
> - ⚠️ **« CLIQUE-LES 5 PAR 5 MAX — attends que le paquet précédent affiche `✅ contexte chargé` avant d'en lancer 5 de plus. »**
> - ⚠️ **« Si une session n'a pas démarré, ou est repartie à vide → relance CE chip-là, lui seul. »** (repère de panne : 1er message ≠ « Reprends la session … » ⇒ ratée, cf ⏳ ci-dessous.)
> - ⛔ **INTERDIT de rationner MES spawns « pour aider »** — c'est exactement ce qui a produit l'oubli : je m'auto-limitais à 5, je ne revenais jamais finir, et des sessions restaient au tapis **en silence**. Un chip en trop se dismisse d'un clic ; une session jamais lancée, personne ne la voit.
>
> *(Jurisprudence 2026-07-16 : rationnement 5-par-5 côté Claude → 5/12 lancées, puis 12/13 (Pricing oubliée). L'utilisateur : « ça a déjà marché très bien… toi tu oublies complètement de te réactiver, donc on enlève ça, et on met juste un rappel bien vénère à l'utilisateur de les valider 5 par 5… tu as oublié la moitié des sessions, frérot, je n'ai pas que ça à branler. »)*

> ⏳ **NE LANCE PAS LA SESSION TROP VITE — sinon elle est PERDUE.** Quand tu cliques un chip / rouvres une session importée, le **tout 1er message en haut de la session** doit être **« Reprends la session « &lt;titre&gt; » … »** — c'est LUI qui recharge tout le contexte (lecture du `.jsonl`). **Laisse l'IA finir de charger** : elle répond **« ✅ contexte chargé »** + un résumé **avant** que tu écrives.
>
> 🚨 **Repère de panne** : si tu vois **autre chose en haut** (juste `go`, ton propre texte, un message tronqué) au lieu de « Reprends la session « … » » → le chargement a été **coupé / tapé par-dessus** → l'IA repart **À VIDE** (elle ne sait plus quelle session elle est, elle devine faux) → **session perdue, à RELANCER**. Ne tape **rien** tant que le « Reprends la session « … » » + le **feu vert** (« ✅ contexte chargé ») ne sont pas affichés.


# § ① RETROUVER & RELANCER — et réinjecter un bundle

### 📸 MÉTHODE CAPTURE D'ÉCRAN — même PC, changement de compte (la plus simple, 0 crédit)

> 🔑 **Le cas normal, dit clairement** : ces sessions étaient TOUTES ouvertes sur un **AUTRE compte Claude**, sur CE MÊME PC (compte A vidé → tu passes sur B). Elles ne sont PAS liées au compte Claude mais à ta session **Windows** → le nouveau compte les retrouve toutes en local. La capture sert juste à dire **lesquelles** relancer ; le travail (retrouver + rouvrir via chips) se fait sur le **compte cible** (celui qui a des crédits). C'est exactement ce que l'utilisateur fait quand il change de compte.
>
> ↔️ **Symétrie export → import (à dire à l'utilisateur)** : si quelqu'un **exporte** ses sessions via `/claude-sessions-migration` § ②, on le prévient que **l'import se fait depuis son AUTRE compte Claude** via `/claude-sessions-migration` § ① — jamais sur le compte qu'il quitte (celui-là n'a plus de crédits, c'est justement la raison du transfert).

**Quand l'utiliser** : tu es sur le **même PC** et tu as **changé de compte Claude** (ex : le compte A n'a plus de crédits, tu passes sur B). Tes sessions sont liées à ta **session Windows**, **pas** au compte Claude → elles sont **déjà là**, le compte B peut les rouvrir. **Aucun crédit consommé sur le compte A** (screenshoter est gratuit), **aucune clé USB**, **aucun export**.

**👤 Côté toi (débutant) — 3 gestes :**
1. Sur le **compte A** : fais une **capture d'écran de ta sidebar** Claude Code (les sessions à garder).
2. Passe sur le **compte B** (même PC).
3. Donne la capture à Claude et dis : *« relance ces sessions »*. C'est tout.

**🤖 Côté Claude (ce que JE fais sur le compte cible)** :
1. **Lire les titres** de sessions dans la capture (vision).
   - ⚠️ **JAMAIS présumer qu'une ligne est un INTERTITRE** parce qu'elle est en MAJUSCULES / sans emoji : un **titre de session** peut y ressembler à s'y méprendre. Une ligne n'est un intertitre **que si AUCUNE session du store ne porte ce titre** — ça se **vérifie** à l'étape 2, ça ne se devine pas à l'œil. En cas de doute → on la traite comme une session (un chip en trop se dismisse ; une session oubliée, personne ne la voit).
   - *(Jurisprudence 2026-07-16 : `PRICING - PAUSE` classée « intertitre » par ressemblance avec `MARKETING` juste au-dessus — qui, lui, en était vraiment un. Résultat : session oubliée, 12 lancées sur 13. L'utilisateur : « Tu as oublié la session PRicing, voilà. » Le contrôle coûte un grep ; l'oubli est silencieux.)*
2. **Les retrouver en local** (même utilisateur Windows → mêmes fichiers) — **UNE commande, celle-ci** :
   ```powershell
   py -3.12 ${CLAUDE_PLUGIN_ROOT}/skills/claude-sessions-migration/scripts/export_claude_sessions.py --sidebar --dry-run   # titre EXACT -> cliSessionId -> cwd
   ```
   → matcher chaque titre de la capture à son `cliSessionId` + `cwd`. Puis étape 3, direct.

   > 🚨 **`py -3.12`, JAMAIS `py` nu — sinon l'outil MENT en silence** (gravé 2026-07-25, ça a coûté une session entière). `py` honore le shebang `#!/usr/bin/env python3` du script et route vers un Python 3.14 qui **ne voit pas `%APPDATA%`** → le script répond **« [sidebar] Store introuvable »** alors que le store est là et plein. C'est un **zéro d'environnement** : indistinguable d'un vrai « pas de sessions ». **Témoin qui tranche en 3 s** : `py -3.12 -c "import os;from pathlib import Path;print(Path(os.environ['APPDATA'],'Claude','claude-code-sessions').exists())"` → `True` alors que le script dit introuvable ⇒ c'est l'instrument, pas le store. *(Le piège jumeau est documenté côté export depuis le 2026-06-02 ; il manquait ICI, donc une session entrée par l'import ne le voyait jamais.)*

   > ⛔ **« Store introuvable » ⇒ on RÉPARE l'instrument, on ne se rabat JAMAIS sur un scan des `.jsonl` par titre.** Ce fallback figurait ici et il est **structurellement impossible** : **le titre de la sidebar n'existe PAS dans le `.jsonl`** — il vit uniquement dans le store (`local_*.json`, champ `.title`, relié au fichier par `.cliSessionId`). Un `.jsonl` ne porte que le 1er message. *(Prouvé 2026-07-25 : 1648 sessions listées depuis `~/.claude/projects/`, grep « quotas » ⇒ 2 hits de sous-agents sans rapport ; la vraie session s'appelait « 🗄️ supabase — Quotas ✔️ - EXPORTED », chaîne absente de tout `.jsonl`. Idem pour l'INDEX global : il titre au 1er message, pas au titre sidebar.)* Instrument réparé = la session sort en quelques secondes. Voie de secours si `-3.12` ne suffit pas : le **pont manifest** PowerShell (`/claude-sessions-migration` § ② § Pont manifest), jamais le scan par titre.

   > 🔑 **Le store sur DISQUE est PARTAGÉ entre comptes — c'est la sidebar AFFICHÉE qui est filtrée par compte.** C'est *pour ça* que cette méthode marche. Prouvé live le 2026-07-25 : la session quotas d'un **autre compte** est **absente** de `list_sessions` (vue du compte courant) et **présente** dans le store lu sur disque (1328 enregistrements). ⇒ **l'outil de recherche cross-comptes = la lecture du store** (`--sidebar`, qui lit `%APPDATA%\Claude\claude-code-sessions\**\local_*.json`) ; **`list_sessions` ne voit jamais les autres comptes** et son silence ne prouve rien. Tranche l'hypothèse (a) laissée ouverte dans `/claude-sessions-migration` § ② § Multi-comptes.

   - ⛔ **STOP dès que titre+`cwd`+id sont résolus.** Pas de lecture du `.jsonl` trouvé, pas de `parse_session()`/comptage messages/aperçu « pour vérifier avant de spawner » — zéro utilité, ça double juste la lecture que le chip fera lui-même (cf ⛔ Règle d'or point 4 en tête de skill).
3. Pour **TOUTES** les sessions trouvées, **d'un coup, même tour** (aucun rationnement — cf ⛔ Règle d'or point 1) : **si elle est déjà vivante** (fenêtre ouverte / trackée) → **`send_message` DEDANS** (l'outil de message entre sessions de Claude Desktop), pas de nouvelle session ; **sinon** → **spawner UN chip** (Mode B, cf § 🎰 chips) = **une session propre** (jamais un fork/doublon) qui **lit le `.jsonl` LOCAL** et reprend le fil :
   - `title` = le titre d'origine (celui de la capture).
   - `cwd` = le dossier du projet de la session.
   - `prompt` (self-contained) — **1re ligne visible en haut** = *« Reprends la session « <titre> » — ⏳ je charge le contexte, n'écris rien… »*, PUIS *charge depuis le `.jsonl` local (`~/.claude/projects/<cwd-encodé>/<id>.jsonl`, via `read_claude_session.py` ou lecture directe) → affiche « ✅ contexte chargé » + résume 3 lignes → reprends le fil* **+ le bloc « MÉTHODE DE REPRISE » (§ 🎰, quatrième phrase) : plan, boucle à la taille du reste, arrêt quand c'est fini — jamais « attends instructions ».** **Chemins ABSOLUS.** (Repère de panne : si l'user voit `go`/autre chose à la place → 1er message coupé, à relancer.)
4. Tu **cliques** sur chaque chip → la session repart avec **tout son contexte**.

> ⚙️ **Base technique (pourquoi ça marche sans crédits)** : `~/.claude/projects/<cwd-encodé>/<id>.jsonl` = 1 fichier / session, **lié au compte Windows** (jamais au compte Claude). Même PC + même utilisateur Windows = **mêmes fichiers**, quel que soit le compte Claude connecté. La capture d'écran sert **uniquement** à dire à Claude **lesquelles** relancer. Le travail (retrouver + rouvrir) se fait **sur le compte cible**, qui, lui, a des crédits.
>
> 🔎 **Nuance multi-comptes (honnête)** : selon que le *store* de la sidebar est partagé ou rechargé par compte (question encore ouverte, cf `/claude-sessions-migration` § ② § Multi-comptes), l'étape 2 passe par le store **ou** par le scan direct des `.jsonl`. Les deux chemins sont ci-dessus → robuste dans les deux cas.

### 🎯 Objectif (ce que ça résout)

Reprendre des sessions Claude Code exportées ailleurs **sur ce PC**, sans dépendre du compte
connecté. Claude Code range chaque session ici :

```
~/.claude/projects/<cwd-encodé>/<sessionId>.jsonl
```

où `<cwd-encodé>` = le chemin de travail avec **chaque caractère non-alphanumérique remplacé
par `-`** (vérifié : `C:\Users\<toi>\Projets\mon-projet` →
`C--Users-<toi>-Projets-mon-projet`). **Le piège** : le nom d'utilisateur
change souvent d'un PC à l'autre → le dossier encodé change → une copie naïve atterrit au
mauvais endroit et `claude --resume` ne retrouve rien. Ce skill lit le `cwd` d'origine **dans
chaque .jsonl**, le **remappe**, l'encode, et dépose le fichier au bon endroit.

Outil : [`scripts/import_claude_sessions.py`](${CLAUDE_PLUGIN_ROOT}/skills/claude-sessions-migration/scripts/import_claude_sessions.py) (fonction
`import_bundle()` réutilisable).

> 🔑 **Transport par clé USB (cas migration de compte/PC).** L'export `/claude-sessions-migration` § ②
> sort un `.zip` (rangé `<année>/<projet>/<date>/<projet>_<date>.zip`) → copié sur la clé. Sur l'AUTRE PC,
> l'utilisateur dit simplement **« récupère les sessions »** / **« importe la dernière migration »** et Claude
> **trouve le `.zip` tout seul sur la clé** (la lettre du lecteur change d'un PC à l'autre — NE PAS présumer `D:`).
> Mode B par défaut : Claude lit le zip et reprend le fil (rien à réinjecter). Aucun token, aucun réseau, aucun compte requis.

**Trouver le zip d'export tout seul sur une clé USB** (lecteurs amovibles, lettre variable) :

```powershell
$sys = $env:SystemDrive   # lecteur systeme (C:) a exclure du scan
Get-CimInstance Win32_LogicalDisk | Where-Object { $_.DeviceID -ne $sys -and $_.DriveType -in 2,3 } | ForEach-Object {
  Get-ChildItem ($_.DeviceID + "\") -Recurse -Depth 2 -Filter "*.zip" -ErrorAction SilentlyContinue |
    Where-Object { $_.Name -match 'sessions|mon-projet|sidebar|migration' }
} | Sort-Object LastWriteTime -Descending | Select-Object -First 1 -ExpandProperty FullName
```
→ Claude prend le **plus récent** et le passe à `read_claude_session.py` (Mode B, lecture+reprise) ou
`import_claude_sessions.py` (réinjection). Une clé USB peut apparaître en `DriveType=2` (amovible) **ou** `3`
(fixe, selon le contrôleur) → on scanne les deux, hors lecteur système. Rien trouvé (clé pas branchée /
éjectée) → demander le chemin à l'utilisateur. Vérifié 2026-06-20 : retourne vide quand la clé est éjectée (OK).

### 🅱️ Mode B — Claude LIT le fichier et reprend (mode ACTUEL, « pour commencer »)

Le `.zip` contient les conversations **en clair** → **pas besoin de réinjecter quoi que ce soit** :
Claude lit la session et **continue le travail** avec tout le contexte. Le plus simple, dispo tout
de suite, ne touche à rien sur le PC. C'est « le boulot de Claude ».

Sur l'autre PC, l'utilisateur dit *« reprends la session X (du zip) »* → Claude exécute :

```powershell
py ${CLAUDE_PLUGIN_ROOT}/skills/claude-sessions-migration/scripts/read_claude_session.py "<chemin>\sessions-export.zip"               # liste (TES titres sidebar)
py ${CLAUDE_PLUGIN_ROOT}/skills/claude-sessions-migration/scripts/read_claude_session.py "<chemin>\sessions-export.zip" "LGM-CHROME"  # lit le transcript complet
py ${CLAUDE_PLUGIN_ROOT}/skills/claude-sessions-migration/scripts/read_claude_session.py "%USERPROFILE%\.claude\projects\<cwd-encodé>\<id>.jsonl"  # .jsonl LOCAL direct (même PC / capture d'écran) — PAS besoin de zip
```
→ recherche par **titre de sidebar** OU par id, accepte `.zip`, un dossier bundle, **ou un `.jsonl`
local direct** (le chemin canonique du chip Mode B « capture d'écran » — même PC, aucun zip à bâtir),
**aucune écriture**. Claude ingère le transcript et reprend le fil. (Outil : `scripts/read_claude_session.py`.)

> ⚠️ **Ne fait PAS « pop » la session dans la sidebar Claude Desktop** — c'est voulu : en Mode B
> c'est Claude qui porte la mémoire, pas la GUI. Pour un vrai pop natif → **Mode A (à venir)**.

### 🎰 Relancer EN SÉRIE via CHIPS (autonome — le mode pour plusieurs sessions)

Quand l'utilisateur veut relancer PLUSIEURS sessions (« relance mes sessions du zip », « les épinglées »,
ou il en nomme) : Claude **spawne un chip par session** → l'utilisateur **clique**, il ne tape rien, et
la session repart avec **tout son contexte**. C'est le « balance toutes les chips » de l'utilisateur.

> 🖐️ **On spawn TOUT d'un coup** (aucun rationnement côté Claude — cf ⛔ Règle d'or point 1), et **on
> termine la réponse par le RAPPEL VÉNÈRE à L'utilisateur : « clique-les 5 PAR 5 max, attends le `✅ contexte
> chargé` du paquet avant les 5 suivants ; une session pas partie → relance CE chip-là »**. Et **une
> session vivante ne se re-spawne pas** : si elle est déjà ouverte/trackée → **`send_message` dedans**
> (`send_message`), pas un nouveau chip. Un chip = **une session propre**, jamais un fork/doublon.

> 🏷️ **LE `title` D'UN CHIP DEVIENT LE TITRE RÉEL DE LA SESSION — donc c'est TA convention de nommage des sessions qui s'applique, jamais celle de l'outil (gravé 2026-08-15).**
> Retour d'usage, en voyant arriver sept sessions nommées en phrase française : *« pourquoi tu ne respectes pas l'architecture des noms ? C'est hyper important de vraiment très bien nommer les sessions. Double petit emoji au début, bien choisi. Et des noms vraiment très très très courts, mais équivoquants. »*
>
> ```
> <ÉTAT> <emoji cible> <CODE court MAJUSCULE> — <suffixe>
> ```
> `⏯🚀 STRIPE — Parcours d'achat` — et **pas** `Relancer Pré-prod Stripe parcours d'achat`.
>
> ⚠️ **Le piège est dans la description de l'outil, pas dans l'oubli.** `spawn_task` demande un titre « impératif, commençant par un verbe » — c'est juste pour un chip de correction mécanique, et **faux pour une session de travail**. Ici le chip n'est pas une tâche, c'est **une session qui va vivre des semaines dans la sidebar**. La convention du dépôt prime toujours sur celle de l'outil.
> - **L'emoji cible** : celui de la session d'origine si c'est une relance (il existe déjà, on ne le réinvente pas), sinon le marqueur `<!-- session: … -->` du `CLAUDE.md` du dossier concerné.
> - **L'état initial est `⏯`** — elle naît en cours.
> - **Deux sessions qui partagent un préfixe** (`⏯📝 DICTEE — Batch chunks` / `— Save clipboard`) : le dire **dans les deux prompts**, sinon elles se prennent l'une pour l'autre et fusionnent par réflexe.
>
> **Rattrapage si c'est déjà parti** : `set_session_title` pour celles qui ont **démarré** (ça marche, leur titre est `auto`) · **dismiss + respawn** pour les chips **pas encore cliqués**. *Coût réel du jour : 7 chips, 1 renommage + 6 respawns.*

> 🗺️ **LE LIVRABLE D'UNE MIGRATION EST LA TABLE DE MAPPING, VALIDÉE — PAS LES CHIPS (gravé 2026-08-15, après y avoir passé une soirée).**
> Retour d'usage : *« tu es censé me faire le mapping et me dire : ok, telle session migrée, elle va dans telle session. Et si je valide, je valide, c'est tout ce que je veux savoir. C'est ça que tu es censé me sortir et rien d'autre. »*
>
> **Une ligne par session du paquet, deux colonnes** : la session migrée → **où elle va**. Trois destinations possibles, et une seule par ligne :
> | Destination | Quand |
> |---|---|
> | **une session vivante nommée** | son sujet est déjà porté sur le compte cible → on **fusionne** (`send_message` dedans), on n'ouvre rien |
> | **nouvelle session** | aucune session vivante ne porte le sujet → chip |
> | **rien** | l'utilisateur a marqué de ne pas la migrer (un `🚫` dans le titre, par exemple) |
>
> **On sort la table, on s'arrête, il valide ou corrige des lignes. ENSUITE seulement on exécute.** Spawner avant validation, c'est lui coller quinze chips à trier — le travail qu'on était censé lui épargner.
> - ❌ Écrire « déjà retiré » dans la table : elle dit **où ça va**, pas ce que j'ai fait de mon côté. Une table de mapping ne raconte pas mes gestes.
> - ❌ Produire un document de méthode à la place du mapping. Il ne veut pas la méthode, il veut les lignes.
>
> 🔎 **LE CROISEMENT SE FAIT SUR TOUT LE STORE, PAS SUR LA SIDEBAR DU COMPTE COURANT (gravé 2026-08-15).** Retour d'usage : *« tu m'as fait trop de nouvelles sessions. Il y en a trop. Il y a plein de sessions qui existent déjà localement. »* Mesuré le jour même : croiser avec les **sessions vivantes du compte courant** (≈ 80) donnait 11 « nouvelles sessions » ; croiser avec **le store entier** (1515 fiches, tous comptes, **archivées comprises**) en a démasqué **deux qui existaient déjà** — dont le backend, que l'utilisateur a repéré à l'œil avant moi. **Une session archivée qui porte le sujet compte** : elle prouve que le sujet a un foyer, et rouvrir à côté d'elle fabrique le doublon.

> 🕳️ **UN TITRE COURT EST INVISIBLE À TOUT MATCHER PAR RECOUVREMENT — et le zéro qu'il rend a l'air d'un vrai zéro (gravé 2026-08-25).**
> Le croisement du § ci-dessus se fait par **titre**, et un matcher par recouvrement de mots exige
> presque toujours un minimum de mots communs (2, typiquement) pour écarter le bruit. **Une session
> nommée d'un seul mot significatif ne peut alors JAMAIS être appariée** : aucun titre au monde ne
> partage deux mots avec `SCROLL`. Le seuil ne rate pas de temps en temps — il exclut cette classe
> entière, par construction, en silence.
> ⚠️ **Pourquoi c'est vicieux ici plutôt qu'ailleurs** : le zéro est **exact** au sens de
> l'instrument, et il tombe dans la seule branche qui coûte cher — « aucun jumeau → nouvelle
> session ». Le résultat n'est pas une mesure douteuse, c'est un **doublon fabriqué**, précisément
> ce que la règle d'or « une session = une session » existe pour empêcher.
> **Le geste** : un titre de **moins de deux mots significatifs** ne se croise pas par recouvrement —
> on le cherche par **sous-chaîne** (son mot rare contre les titres du lot, et l'inverse), et au
> doute on demande plutôt que de spawner.
>
> 🪞 **ET LE CONTRÔLE QUI TRANCHE N'EST PAS DANS L'INSTRUMENT, IL EST DANS TON PROPRE TEXTE.**
> C'est le seul point qui aurait sauvé le cas inaugural : le prompt du chip **nommait la session
> jumelle à la main** — « une session `⏸🧭 SCROLL` est vivante, dis si tu devrais verser ton contenu
> chez elle » — pendant que le croisement, lui, déclarait « aucun voisin ». Les deux ont été écrits
> dans la même passe, par la même session, et c'est l'instrument qui a gagné.
> **Le contrôle, décidable, avant tout `spawn_task`** : *ai-je nommé quelque part, en clair, une
> session qui porte ce sujet ?* Oui → **l'instrument a tort**, on n'ouvre rien. Une contradiction
> entre ce qu'on écrit et ce qu'on mesure n'est jamais un détail de forme : c'est un des deux qui
> est faux, et le seul moment où l'on peut encore le savoir gratuitement.
> *Cas inaugural : `⏯🧭 LOGS-SCROLL` spawné à côté de `⏸🧭 SCROLL`, qui venait de recevoir le mandat
> du chantier scrolling une heure plus tôt — par la même session.*

> 🧾 **UNE FUSION DOIT PRODUIRE UN RÉCAPITULATIF — sinon on empile deux contextes qui se contredisent, et personne ne le voit (gravé 2026-08-15).**
> Retour d'usage : *« elle doit vraiment RESTITUER le contexte, entre ce qu'elle a compris, et faire en sorte que l'utilisateur puisse reprendre la session facilement en comprenant le contexte CUMULÉ des deux sessions, et éventuellement les incohérences, les contradictions. On a deux sessions qui ont été fusionnées, qui se contredisent potentiellement — il faut faire le point, il faut faire le récap et être sûr que tout est clair. »*
>
> **C'est le livrable de la fusion**, et il vaut pour la session **receveuse**, pas pour moi. Le `send_message` qui verse une session dans une autre **demande explicitement les cinq points suivants**, dans cet ordre :
> 1. **Ce que portait la session versée** — son sujet, son état, ses décisions.
> 2. **Ce que portait la session receveuse** sur ce même sujet.
> 3. **Le contexte CUMULÉ** — l'état réel une fois les deux additionnés. C'est ce que l'utilisateur lira pour reprendre.
> 4. **Les CONTRADICTIONS, nommées.** Deux sessions qui ont travaillé en parallèle sur un sujet ont presque toujours divergé : une décision prise ici et défaite là, une mesure refaite avec un autre résultat, un ticket clos d'un côté et vivant de l'autre. **Une fusion silencieuse est une fusion qui ment** : elle donne l'illusion d'un état unique là où il y en a deux.
> 5. **Ce qui reste, dédupliqué** — pas la concaténation des deux listes.
>
> ⚠️ **Charger n'est pas restituer.** Une session qui dit *« contexte chargé »* et enchaîne n'a rien prouvé : le témoin d'une fusion réussie, c'est **le récap lisible par l'utilisateur**, pas l'accusé de lecture.
> - ❌ Verser une session dans une autre sans demander ce récap. ❌ Un récap qui liste ce que chacune faisait sans jamais dire ce qui **diverge**.

> 🧬 **UN EXPORT CONTIENT DEUX NATURES DE SESSIONS — les traiter pareil est LE défaut (gravé 2026-08-15).**
> Retour d'usage : *« ça, c'est les sessions qui appartiennent au chantier, mais c'est les VIEILLES sessions dont il faut qu'elles dégagent. On était censé les clôturer proprement et intégrer leur travail dans les chantiers, et router vers les sessions existantes qui travaillent sur le chantier, en répartissant bien le travail. »*
>
> | Nature | Comment la reconnaître | Ce qu'on en fait |
> |---|---|---|
> | **Vieille session de chantier** | **une session VIVANTE porte déjà son sujet** sur le compte cible | on ne la relance **pas**. On la **clôture proprement** — son travail intégré au chantier, son sujet routé vers la session vivante — protocole de clôture du `CLAUDE.md` racine : le sujet entre d'abord dans le système, et on **prouve** où il vit maintenant |
> | **Session à reprendre** | aucune session vivante ne porte le sujet | chip, avec son transcript |
>
> **Le discriminant est mécanique** : croiser chaque titre du paquet avec la liste des sessions **vivantes** du compte cible. Ce croisement se fait **avant** la table, c'est lui qui la remplit.
> ⚠️ **Relancer une vieille session de chantier, c'est rouvrir un doublon sur un sujet déjà porté** — exactement ce que la règle d'or « une session = une session » interdit, mais par l'autre bout : ici le doublon ne naît pas d'un fork, il naît d'un **tri manquant**.

Procédure (Claude exécute) :
1. **Lister** les sessions du bundle/zip + leur `cwd` :
   `py ${CLAUDE_PLUGIN_ROOT}/skills/claude-sessions-migration/scripts/read_claude_session.py "<zip>"` (titres SIDEBAR) ; le `cwd` par session se lit dans
   l'export (header de section `INDEX-SIDEBAR.md`, ou champ `cwd` du transcript).
   - ✅ Ce lookup = liste de titres + `cwd` + id, RIEN d'autre.
   - ❌ **N'insère PAS d'étape 1bis** « je vérifie le contenu / la taille / la date avant de spawner » —
     `parse_session()`, comptage messages, aperçu du 1er message = zéro utilité ici (titre + cwd
     suffisent au `spawn_task`), ça ne fait que payer une lecture pour rien (cf ⛔ Règle d'or point 4).
     Dès que titre+cwd+id sont connus pour une session → étape 2 direct, pas de détour.
2. Pour CHAQUE session retenue → `spawn_task` :
   - **title** = le **nom d'origine** (titre sidebar) — l'utilisateur y tient.
   - **cwd** = le **dossier du projet** de la session (rooté au bon endroit, sinon le travail
     reprend au mauvais endroit ; omis si = dépôt courant).
   - **prompt** (Mode B, self-contained). ⚠️ **Sa 1re ligne = le repère que l'user DOIT voir en haut
     de la session** — commence LITTÉRALEMENT par « **Reprends la session « <titre> »** — ⏳ je charge le
     contexte, n'écris rien… », PUIS charge :
     `py "<abs>\tools\read_claude_session.py" "<zip>" "<id8>"` → affiche **« ✅ contexte chargé »** + résume
     3 lignes → reprends le fil → attends instructions. **Chemins ABSOLUS** (le chip tourne dans un autre
     cwd / worktree). Si l'user voit `go`/un autre texte à la place de cette 1re ligne = 1er message coupé →
     import raté, à relancer.
   > 🧠 **LE TRANSCRIPT N'EST PAS UN PRÉAMBULE, C'EST UNE SOURCE — et le prompt DOIT le dire (gravé 2026-08-15).**
   > Retour d'usage : *« tu leur demandes de bien bien bien récupérer le plan, de bien charger le contexte de la session, et d'aller TOUJOURS chercher dans le contexte de la session s'il y a des questions, des informations à aller chercher. Tout est dans le putain de contexte de la session. On ne se ferait pas chier à migrer la session autrement. »*
   >
   > **C'est la RAISON D'ÊTRE de la migration**, et c'est le point qu'on rate le plus : un prompt qui dit seulement *« lis ton transcript »* obtient une session qui le **survole une fois**, en tire un résumé de trois lignes, puis travaille de mémoire — c'est-à-dire exactement comme une session neuve, qui redemande ce qui est déjà décidé et refait ce qui est fait. **Le coût de la migration est alors payé pour rien.**
   >
   > **Les trois phrases à mettre dans CHAQUE prompt de chip**, en plus du chargement initial :
   > 1. **Charge ton contexte AVANT toute action** — avant `git pull`, avant de répondre : ton transcript **et** tes plans (`~/.claude/plans/`). Puis dis en une ligne combien de fichiers de travail tu as chargés — sans ce témoin, rien ne distingue une session qui a lu d'une session qui a ignoré.
   > 2. **Ton transcript reste consultable pendant TOUT ton travail.** À la moindre question — pourquoi telle décision, qu'est-ce qui a déjà été essayé, quel était le verdict, où en était la mesure — **tu y retournes le lire** (`grep` sur le `.jsonl`, ou relecture ciblée du passage). Tu ne devines pas, et tu ne redemandes pas à l'utilisateur ce qui est déjà écrit dans tes propres tours.
   > 3. **Le système habituel s'AJOUTE, il ne remplace pas** : compétences, fiches de fonctionnalités, fiches par plateforme, `CLAUDE.md`. Le transcript dit *ce qui s'est passé dans CETTE session* ; les documents disent *ce qui est vrai pour le produit*. Les deux, jamais l'un à la place de l'autre.
   >

   > 🧭 **LA QUATRIÈME PHRASE — la reprise va JUSQU'AU BOUT, avec une boucle à la taille du reste (gravé 2026-09-13).**
   > Une session relancée qui recharge son contexte puis **attend** a coûté la migration pour rien : elle
   > s'arrête au premier lot, ou elle redemande un go que tu as déjà donné en la relançant. Le prompt de
   > reprise porte donc, en plus des trois phrases, **le mandat et sa cadence** — le bloc à coller tel quel :
   >
   > ```text
   > ## MÉTHODE DE REPRISE — jusqu'au bout, à la taille du reste
   > 1. Tu prends le mandat de bout en bout, **plan d'abord** — pose le plan complet du RESTE (lots,
   >    ordre, preuves attendues, acquis à ne pas rejouer, ce qui reste à l'utilisateur : irréversible ·
   >    goût produit · ses comptes). Le plan est validé d'avance : tu n'attends aucun go.
   > 2. Une boucle **à la taille du reliquat**, dans CETTE session, visible (`/loop <cadence> <compétence>`
   >    si ton hôte le propose ; sinon une reprise explicite à chaque tour). Un reste qui tient en un ou deux
   >    tours ne prend pas de boucle : tu le finis. Plusieurs lots en prennent une, avec un cap.
   > 3. La boucle **s'arrête quand le contrat est livré et prouvé** — pas avant (pas sur le premier lot),
   >    pas après (jamais à vide, jamais « pour faire joli »). Fin = preuves rendues · travail commité et
   >    poussé, vérifié par le contenu sur le distant · titre passé à ✔️.
   > ```
   >
   > **Le contrôle, décidable, avant d'envoyer un prompt de reprise** : *nomme-t-il le mandat, le plan, la
   > boucle dimensionnée et le critère de fin ?* Un des quatre manque → la session s'arrêtera trop tôt ou
   > tournera à vide. Même bloc dans un message à une session déjà vivante (elle a un titre, pas un mandat).
   > Le dimensionnement — cadence, cap, « pas de boucle » — est **le jugement de la session relancée** : on
   > lui donne le reste et le critère, elle choisit la taille.
   >
   > 🎚️ **LE PRÉFIXE D'ÉTAT DU TITRE CALIBRE LE MESSAGE — une session CLÔTURÉE n'a rien à reprendre (gravé 2026-08-25).**
   > Retour d'usage : *« si c'est une session qui est clôturée, ça ne sert à rien de s'affoler. C'est juste du
   > ménage, on s'organise bien — mais ça ne sert à rien qu'elle fasse quoi que ce soit. Elle reçoit le
   > message, elle dit ok, et c'est bon. Le truc est déjà validé, avec le petit logo. »*
   >
   > Le titre **porte déjà l'information**, et le bloc ci-dessus l'ignorait : il prescrivait le même
   > prompt lourd pour les trois états. Envoyer trente mégaoctets de transcript à recharger et cinq
   > points de restitution à une session `✔️` fait travailler quelqu'un sur un sujet **fermé** — le
   > coût est réel, et le résultat est nul.
   >
   > | État dans le titre | Le message |
   > |---|---|
   > | **`✔️`** — clôturé, validé | **court** : prends acte, range ce qui traîne chez toi, **ne relance rien, ne recharge pas ton transcript**. Un « ok » suffit. |
   > | `⏯` `⏸` `⚠️` ou pas d'état | le prompt complet ci-dessus — chargement, restitution, contradictions |
   >
   > **Le contrôle, décidable, avant d'écrire un prompt de reprise** : *le titre porte-t-il `✔️` ?*
   > Oui → c'est du ménage, pas une reprise. ⚠️ Un état **composé** se lit sur son PREMIER symbole :
   > `⏯✔️⚖️` commence par `⏯`, donc la session est **en cours** — c'est un travail validé à
   > l'intérieur d'un chantier vivant, pas un chantier clos.
   >
   > 📚 **ET LE PROMPT FAIT CHARGER LA DOC, PAS SEULEMENT LE TRANSCRIPT.** Retour d'usage, le même jour :
   > *« je te l'ai expliqué quinze milliards de fois — il faut prompter un minimum les sessions quand
   > tu vas les relancer, pour qu'elles chargent bien la doc. »* Le point 3 ci-dessus le dit déjà en
   > principe ; ce qui manquait, c'est de **NOMMER** les surfaces dans le prompt. Un prompt qui écrit
   > « le système habituel s'ajoute » obtient une session qui ne charge rien : trop vague pour
   > déclencher un geste. **On nomme la compétence propriétaire du sujet** (`/ma-competence-du-sujet`…) **et sa fiche produit** (`docs/<feature>.md`, ou l'équivalent chez toi), à l'adresse exacte.

   > ❌ Un prompt de chip qui dit « lis ton transcript » et rien de plus. ❌ Une session reprise qui pose à l'utilisateur une question dont la réponse est dans ses propres tours.

3. L'utilisateur clique → session relancée, contexte préservé, chip consommé (sort de la liste).

> Chaque chip = sa session (worktree isolé) → relance de plusieurs en parallèle.
> Jurisprudence : 10 chips épinglés spawnés le 2026-06-20 (test live, rootés par projet).

### 🔁 Reprise native CLI (`claude --resume`) — copie des `.jsonl`

> Recopie les `.jsonl` au bon endroit → `claude --resume <id>` marche **depuis un terminal**, mais
> ne pop pas non plus dans la sidebar (voir Mode A). Surtout utile pour les transferts en masse.

```powershell
# Depuis un .zip exporté (le cas normal). Pointe direct sur le .zip, ça l'extrait tout seul.
py ${CLAUDE_PLUGIN_ROOT}/skills/claude-sessions-migration/scripts/import_claude_sessions.py "<chemin>\sessions-export.zip"

# Aperçu sans rien écrire (montre les dossiers cibles + le remap auto vers CE PC)
py ${CLAUDE_PLUGIN_ROOT}/skills/claude-sessions-migration/scripts/import_claude_sessions.py "<chemin>\sessions-export.zip" --dry-run

# Depuis un dossier bundle (non zippé)
py ${CLAUDE_PLUGIN_ROOT}/skills/claude-sessions-migration/scripts/import_claude_sessions.py "<dossier-bundle>"

# Remap de chemin explicite (si le projet vit ailleurs sur le PC cible)
py ${CLAUDE_PLUGIN_ROOT}/skills/claude-sessions-migration/scripts/import_claude_sessions.py "<zip>" --remap "Utilisateur=Administrateur"

# Écraser une session déjà présente (sinon elle est skippée = idempotent)
py ${CLAUDE_PLUGIN_ROOT}/skills/claude-sessions-migration/scripts/import_claude_sessions.py "<zip>" --force
```

### 🧭 Le remap (le cœur du truc)

- **PC → PC, username différent** (cas normal) : **aucun flag**. `--auto-user` (ON par défaut)
  remappe le segment `\Users\<ancien>\` (ou `/Users/`, `/home/`) vers l'utilisateur courant.
  Ex : un export fait sous `Utilisateur` s'importe sous `Administrateur` automatiquement.
- **Même PC (relancer ici, ré-injection à l'identique)** : ajouter **`--no-auto-user`** pour un
  mapping EXACT (les sessions retombent sur leurs dossiers existants → toutes **skippées** =
  déjà là = resumables, zéro doublon). C'est ce qu'on a utilisé pour le test.
- **Cas spécial** (drive/chemin différent) : `--remap "ANCIEN=NOUVEAU"` (répétable).

### ▶️ Relancer une session après import

```powershell
cd "<dossier du projet>"
claude --resume <sessionId>
```

- `REPRISE-IMPORT.md` (écrit à côté du .zip) liste les commandes **déjà remappées**, par projet.
- ⚠️ Le **projet doit exister** au bon chemin sur ce PC (git clone / même arborescence) : le
  script ne pose que les `.jsonl`, il ne recrée pas les projets.

### 🔒 Garde-fous

- **Idempotent** : relancer ne duplique rien (session déjà présente = skip, sauf `--force`).
- **Aucune écriture en `--dry-run`** (juste l'aperçu).
- Session sans `cwd` lisible → ignorée (comptée `sans cwd`), jamais déposée au hasard.

### 🅰️ Mode A — pop natif dans la sidebar (À VENIR, pas encore construit)

Faire **apparaître (« pop »)** la session dans la sidebar Claude Desktop + reprise native. La
sidebar n'est PAS pilotée par les `.jsonl` mais par un store séparé
(`%APPDATA%\Claude\claude-code-sessions\<fenêtre>\local_*.json`). Donc Mode A devra, en plus de
copier le `.jsonl`, **recréer l'entrée `local_*.json`** (sessionId + cliSessionId + cwd remappé +
titre) — l'export capture déjà ces métadonnées (manifest sidebar). ⚠️ écrit dans le store de CD
pendant qu'il tourne → à tester live + probable redémarrage de CD pour rafraîchir la liste.
**Décision tranchée 2026-06-20 : on fait Mode B d'abord, Mode A ensuite.**

### ✅ Validé

Round-trip Mode B prouvé sur données réelles (2026-06-20) : export 117 sessions → `.zip` (~157 Mo)
→ `read_claude_session.py` liste les 117 (titres sidebar) + ressort un transcript complet par
titre/id. Côté copie : import sur le `.zip` → 117 mappées vers les bons dossiers (13 projets).
🧪 Reste à confirmer sur un **2e PC réel** : Claude reprend bien le fil depuis le transcript lu
(Mode B) ; et plus tard le pop natif (Mode A).

**Cross-comptes, même PC — PROUVÉ live 2026-07-25.** l'utilisateur nomme une session ouverte sur un
**autre compte** (« la session quotas »), sans capture, sans export préalable : `--sidebar` (avec
`py -3.12`) la sort du store en quelques secondes → chip Mode B sur son `.jsonl` local. **Aucun
export n'avait été fait au préalable et ça marche quand même** — la nuance du § Multi-comptes de
`/claude-sessions-migration` § ② (« protocole export-avant OBLIGATOIRE ») vaut pour l'**affichage**, pas
pour la **retrouvabilité** : le disque garde tout, le store aussi.
🧪 À confirmer : que ça tienne quand le compte d'origine a été **résilié** (pas seulement quitté).

### Sources canoniques (routing)

- Compétence sœur (produit le .zip) : **`/claude-sessions-migration` § ②**
- Script : `scripts/import_claude_sessions.py` (`import_bundle()`)
- Encodage `cwd` + doctrine : `/claude-sessions-migration` § ② (§ Réinjecter)


# § ② EXPORTER — sauvegarde, index, zip

> # 🛑 AVANT TOUT : ON DEMANDE À LA SESSION DE TERMINER SON TRUC
>
> *Retour d'usage, 2026-09-12, après quatre passes où cette compétence a raté ça : « il faut que tu
> demandes à la session de terminer son truc. »*
>
> **L'ordre des trois gestes, et il ne s'inverse jamais :**
>
> | | Geste | Ce qui casse si on saute |
> |---|---|---|
> | 1 | **Lui écrire de TERMINER** | — |
> | 2 | **Exporter** | un zip qui s'arrête au milieu d'une phrase |
> | 3 | **Archiver** | le travail en vol meurt sans rien laisser |
>
> **« Terminer » ne veut PAS dire « laisser courir »** — *« elle arrête immédiatement, coupe ces
> trucs, et c'est tout. Elle essaie de capitaliser sur ce qui a été fait. »* Le message à lui
> envoyer, c'est exactement ces quatre verbes :
>
> **COUPE** ce qui tourne · **ÉCRIS dans la conversation** ce que le travail de fond a **déjà**
> produit (verdicts, chiffres, **chemins** des fichiers, ce qui reste ouvert) · **COMMITE** ta
> passation chez l'owner · puis affiche **`✅ PRÊTE À L'EXPORT`**.
>
> **Pourquoi l'écriture, et pas seulement l'arrêt** : *un export ne copie que la CONVERSATION*. Le
> résultat d'un workflow ou d'un sous-agent **n'existe pas dans le `.jsonl` tant que la session ne
> l'y a pas écrit**. Couper sans faire écrire perd exactement ce qu'on voulait sauver.
>
> **LE CONTRÔLE, avant de lancer le moindre export** : *ai-je le marqueur `✅ PRÊTE À L'EXPORT` de
> cette session ?* Non → je n'exporte pas, je lui écris. ⚠️ **Un refus d'`archive_session` est le
> garde-fou, pas un obstacle** — et **`isRunning: false` ne suffit pas**, une session hors tour peut
> garder une tâche de fond enregistrée.
>
> Détail, mesures et jurisprudence : **§ 🗃️ EXPORTER, C'EST ARCHIVER** plus bas.

### 🎯 Objectif (le problème que ça résout)

L'utilisateur a des centaines de sessions Claude Code. Les archiver une par une (wrapup / migration / Notion)
**coûte des tokens** et exige un **abonnement actif**. Or **toutes ses sessions sont déjà en local** :

```
~/.claude/projects/<projet-encodé>/<sessionId>.jsonl   (1 fichier = 1 session)
```

Point clé **non négociable à rappeler** : ces fichiers **ne dépendent PAS du compte Claude connecté**.
Changer de compte sur le même PC = mêmes fichiers accessibles. Donc **les exporter / indexer =
lecture de fichiers locaux, ZÉRO token consommé, pas besoin d'abonnement actif**. C'est l'inverse du
wrapup. Ne jamais proposer un wrapup payant juste pour « retrouver / archiver » des sessions : utiliser
ce skill.

Outil : [`scripts/export_claude_sessions.py`](${CLAUDE_PLUGIN_ROOT}/skills/claude-sessions-migration/scripts/export_claude_sessions.py) (autonome, relançable
sur n'importe quelle machine, aucun appel réseau).

### 🗃️ EXPORTER, C'EST ARCHIVER — un seul geste, une seule passe (gravé 2026-09-12)

> **Retour d'usage** : *« si on l'exporte, il faut que tu l'archives. Si elle n'a pas bougé, on archive. »*

Un export rendu **sans** l'archivage laisse la session dans la barre latérale : au tour suivant elle
est re-mesurée, re-rapportée, parfois ré-exportée. Le lot n'a alors **pas d'état** — chaque passe
recompte les mêmes, et c'est l'utilisateur qui paie la redite.

**La règle, en trois temps qui ne se séparent pas :**

1. **Mesurer et REMONTER la liste avant de partir** — titre, poids du transcript, et l'état de son
   export : *jamais exportée* · *exportée et à jour* · *export périmé*.
   *« Il faut que tu me remontes bien tout ce qu'on va exporter. »*
2. **Exporter** — un zip par session, son `PROMPT-REPRISE.md` (§ ci-dessous).
3. **Archiver dans la même passe**, juste après le contrôle du zip. Une session qui **n'a pas bougé**
   depuis son dernier export s'archive **directement**, sans ré-export.

#### 🛑 MAIS D'ABORD : UNE SESSION QUI A DU TRAVAIL EN VOL NE S'EXPORTE PAS (gravé 2026-09-12)

> **Retour d'usage** : *« si elles n'ont pas terminé, si elles ont un truc en cours, faut pas les exporter
> avant qu'elles soient terminées. Il faut leur demander de terminer. Capitaliser dans la session ce
> qui a été fait — parce que là, la tâche en arrière-plan, ça s'est perdu quand on fait l'export. »*

**Deux faits, et c'est leur composition qui coûte :**

1. **L'export ne copie QUE la conversation.** Un workflow de fond, un sous-agent, une mesure lancée :
   leur résultat **n'existe pas dans le `.jsonl` tant que la session ne l'y a pas écrit**. Exporter
   avant la restitution rend un zip qui s'arrête au milieu d'une phrase.
2. **L'archivage TUE le processus** — donc la tâche de fond meurt sans jamais rien écrire.
   *Mesuré le 2026-09-12 : un workflow `micro-signal-partage` à **6 agents, 1,2 M de jetons,
   34 minutes**, phases `Refuter` 3/3 et `Cartographier` 2/3, `Concevoir` et `Juger` pas commencées.
   L'archiver l'aurait effacé en entier.*

**La procédure, dans cet ordre, et elle ne se raccourcit pas :**

1. **Lui écrire** — pas l'exporter : *« **coupe ce qui tourne, maintenant**. Tu n'attends pas la fin,
   tu ne relances rien. Tu écris **dans CETTE conversation** ce que le travail de fond a **DÉJÀ**
   produit — le verdict des phases terminées, leurs chiffres et leurs preuves, les **chemins** des
   fichiers (un chemin survit, un lien vers un artefact non), et ce qui reste ouvert faute d'avoir
   fini. Puis ta passation chez l'owner, et tu **commites**. Enfin : `✅ PRÊTE À L'EXPORT`. »*
2. **Attendre ce marqueur.** Pas l'accusé de réception : le marqueur.
3. **Alors** exporter, contrôler le zip, archiver.

⛔ **On COUPE, on n'attend pas la fin** — Retour d'usage, le soir même : *« elle arrête immédiatement, coupe
ces trucs, et c'est tout. Elle essaie de capitaliser sur ce qui a été fait. »* La première version de
cette règle disait « laisse-la finir » : sur un parc de soixante sessions et un compte qui expire,
attendre une demi-heure par session ne tient pas — et la valeur est dans ce qui est **déjà produit**,
pas dans les phases qui n'ont pas commencé. *Cas mesuré : `Refuter` 3/3 et deux tiers de
`Cartographier` étaient acquis ; `Concevoir` et `Juger` n'avaient pas démarré.*

⚠️ **Ce qui a sauvé la mise ce jour-là, c'est l'app, pas la règle** : `archive_session` **refuse**
sur une session qui a un agent, une tâche de fond ou un message en file. Ce refus n'est pas un
obstacle à contourner — **c'est le garde-fou**. Le lire comme « réessaie plus tard » est déjà la
faute. ⛔ Et ne **jamais** désépingler pour forcer : le `pinned` protège aussi.

🩹 **Une session archivée par erreur se RESSORT** (`unarchive_session`) : la conversation est
intacte. Ce qui ne revient pas, c'est la tâche de fond — elle est à relancer, et la session doit
l'écrire cette fois.

#### Le contrôle, décidable, avant d'exporter une session

*Cette session a-t-elle un travail en cours — `isRunning`, un workflow, un sous-agent, un message en
file ?* Oui → **je ne l'exporte pas, je lui écris.**
⚠️ **Et `isRunning: false` ne suffit pas** : une session peut être hors tour avec une tâche de fond
toujours enregistrée. Le témoin fiable est le **refus d'`archive_session`**, pas le drapeau.

#### 📏 L'export périmé — le seul cas où « déjà exportée » est un faux ami

Comparer la taille du `.jsonl` **dans le zip** à sa taille **actuelle sur le disque**. Plus grand
aujourd'hui = la session a continué à travailler depuis, et le zip livre un état mort.
*Mesuré : `🎯 Répondre` exportée à 9,6 Mo pesait 122 Mo au moment de la vérification.*
Un export périmé se **refait** avant d'archiver ; il ne se signale pas.

#### Le contrôle, décidable, en fin de passe

*Reste-t-il, dans les groupes traités, une session que j'ai exportée et pas archivée ?*
Oui → la passe n'est pas finie. Le compter **par le groupe**, pas de mémoire.

---

### 🧭 L'INVENTAIRE VIENT DE L'APP, JAMAIS DU STORE SUR DISQUE (gravé 2026-09-12)

Seule l'app sait ce qu'il y a dans la barre latérale de l'utilisateur et dans quel groupe :

```
mcp__ccd_sidebar__list_groups                                           → les groupes, dans l'ordre
mcp__ccd_session_mgmt__list_sessions(group=<id>, include_archived=true) → groupe par groupe
```

⚠️ `list_sessions` **sans `group`** ne rend que les plus récentes : un groupe dont la dernière
activité date de trois semaines **n'y apparaît pas du tout**, et son absence se lit comme une
disparition. Toujours interroger **groupe par groupe**.

⚠️ **Le store sur disque ne dit PAS le compte.** `%APPDATA%\Claude\claude-code-sessions\` contient
plusieurs sous-arbres — ils ne correspondent **pas** à des comptes. Mesuré le 2026-09-12 : le groupe
`CC` portait deux sessions dont les fiches vivaient dans **deux sous-arbres différents**, même compte,
même barre latérale. En déduire « celle-là n'est pas sur ce compte » était **faux**, et ça lui a été
rendu comme un fait vérifié. Verbatim : *« Tous les éléments que je te donne sont sur ce compte. »*

Le store reste la bonne source pour ce que l'app ne donne pas — `cliSessionId`, `cwd`, `isArchived`
d'une fiche **déjà identifiée**. Jamais pour décider **ce qui existe**.

⚠️ **Un `archive_session` qui répond « Session not found » ne prouve rien sur le compte** : il dit
que **cet identifiant-là** n'est pas une session que l'app tient. Deux sessions au **même titre**
portent des `cliSessionId` différents — *le titre n'a jamais été un identifiant*. Reprendre le
`sessionId` depuis `list_sessions`, jamais depuis une fiche du store choisie au jugé.

---

### 🎁 LA FORME DE LIVRAISON — UN ZIP PAR SESSION, ET CHACUN PORTE SON PROMPT (gravé 2026-08-25)

> **Retour d'usage** : *« quand moi je fais slash export d'une session, il y a plein de fichiers et tout, et
> du coup c'est le bordel, et je pense que les sessions derrière elles vont avoir du mal à retrouver
> leur petit. (…) Tu fais un zip par session avec tous les éléments, le prompt, les plans, tout ce
> qu'il y avait. Et la compétence, elle oublie tout le temps de me donner un petit prompt de
> redémarrage, et ça c'est dommage aussi. »*

Les deux défauts sont **le même** : un export qui rend un tas au lieu d'un objet **repris**. Un lot
fusionné et un lot sans mode d'emploi obligent tous les deux le repreneur à **reconstituer** ce que
l'exporteur savait déjà. Or l'exporteur tient le titre, le `cwd`, le chemin du transcript et l'état
du chantier : ne pas les écrire, c'est les faire redécouvrir.

#### La règle, en deux points

1. **UN ZIP PAR SESSION.** Jamais un zip fourre-tout, même quand elles partent ensemble. Un zip = une
   session = un objet qu'on ouvre et qu'on reprend, sans trier. Bénéfice mesuré au passage : la
   session obèse s'isole au lieu de contaminer le lot (*cas inaugural : `RECHERCHE - PLATEFORMES`,
   119 Mo de captures base64, faisait à elle seule le poids des douze*).
2. **CHAQUE ZIP PORTE SON `PROMPT-REPRISE.md`** — le prompt exact à donner à la session, son `cwd`,
   le **chemin local** de son transcript, et **ce qu'il faut faire d'elle à l'arrivée** :
   `CRÉER` (aucune session du sujet là-bas) ou `REJOINDRE` (le sujet est déjà porté, **et son titre a
   pu changer**, donc on cherche — archivées comprises — avant de créer, sinon on fabrique le
   doublon). Le corps du prompt est celui de `/claude-sessions-migration` § ① § chips :
   charger **la fin du transcript d'abord** · retrouver **le plan** · charger les compétences ·
   restituer une fois · **dérouler sans redemander le go**.
   Plus, à la racine du lot, un **`LISEZ-MOI.md`** de quelques phrases qui dit au repreneur d'invoquer
   **`/claude-sessions-migration` § ①** et où regarder. Quelques phrases, pas un manuel : la
   compétence fait le travail, le mot d'accompagnement évite juste qu'on parte de zéro.

#### Le contrôle, décidable, avant de rendre un export

*Chaque zip contient-il **un** transcript **et** un `PROMPT-REPRISE.md` dont le chemin de transcript
existe sur le disque ?* Non → l'export n'est pas fini.
⚠️ **Et ce contrôle se falsifie** avant d'être cru : lui donner un zip **vide**
et exiger qu'il le **refuse**. Un contrôle incapable de dire NON ne vaut pas son OUI.

- ❌ Un zip unique pour N sessions « parce que ça part ensemble ».
- ❌ Rendre un chemin de zip sans le prompt qui va avec — c'est le défaut historique, et il est
  invisible : le zip a l'air complet, il l'est même, mais personne ne sait quoi en faire.

#### ⚙️ La règle a désormais son OUTIL — `exporter_un_zip_par_session.py`

```bash
py ${CLAUDE_PLUGIN_ROOT}/skills/claude-sessions-migration/scripts/exporter_un_zip_par_session.py \
   --manifest <json> --dest <dossier du lot> --cli <id> [--cli <id> ...]
# ou, pour tout un scope :  --cwd "C:\...\mon-depot"   (cwd EXACT, sous-dossiers exclus)
```

Il appelle `export_claude_sessions.py --sidebar --manifest` **une fois par session**, écrit chaque
`PROMPT-REPRISE.md` (prompt exact · `cwd` · chemin local du transcript · **le dernier échange réel**
de la session, lu dans la queue du `.jsonl` — c'est lui qui dit sur quoi elle repart), zippe, puis
**vérifie** — en falsifiant d'abord le contrôle sur un zip vide. Enchaîner ensuite
`joindre_au_zip_ce_qui_ne_voyage_pas.py` zip par zip, pour les plans.

> 🩹 **Pourquoi il a fallu l'écrire : la règle du 2026-08-25 était DOCTRINE SANS CODE.** Mesuré le
> 2026-09-03 — `grep -n "PROMPT-REPRISE\|par_session"` sur `export_claude_sessions.py` rendait
> **zéro** : l'exporteur ne sait produire qu'un bundle **fusionné**. Chaque session refabriquait donc
> le pilote à la main, donc chaque session pouvait l'oublier. *Une règle qu'aucun outil n'exécute est
> une règle qu'on applique de mémoire* — et le § ci-dessus décrit précisément un défaut qu'on ne voit
> pas quand il se produit.

> 🪤 **MAX_PATH 260 — l'exporteur échoue en disant « fichier absent ».** `write_session_md` compose le
> nom du `.md` depuis le **titre brut** (emoji, accents, points). Sous un dossier de sortie profond —
> un scratchpad de session fait déjà ~140 caractères — le chemin dépasse 260 et Windows rend un
> `FileNotFoundError`, qui se lit comme « le fichier n'existe pas », jamais comme « le chemin est trop
> long ». Mesuré le 2026-09-03 : **2 sessions sur 9** tombaient là-dessus, et seules celles au titre
> long. D'où `--travail`, qui force un répertoire de travail **court** (défaut `%LOCALAPPDATA%\Temp\ccx`).

### 📦 CE QUE LE ZIP CONTIENT — la conversation, JAMAIS le travail (mesuré 2026-08-15)

Un export contient le **transcript** (la conversation entière), les métadonnées de session et les
journaux de l'application. Il ne contient **rien de ce que la session a produit** : aucun fichier de
ton dépôt, et — le cas qui coûte cher — **aucun plan**.

Le travail, lui, voyage normalement par git. Mais tout ce qu'une session produit n'est pas suivi par
git : un **plan** vit sous `~/.claude/plans/`, un dossier généralement ignoré par git. Un plan ne
voyage donc **ni par git, ni par le zip** — il meurt avec la machine.

⚠️ **Le piège est silencieux, et c'est ce qui le rend cher** : le transcript **cite** le chemin du
plan, souvent des milliers de fois. On voit son nom partout dans l'export et on en conclut qu'il est
dedans. *Un chemin cité n'est pas un fichier joint.*

#### Le geste, dans cet ordre

1. **Dissoudre d'abord** — c'est la vraie réponse, pas le script. Un plan se range comme le reste :
   la **méthode** dans la compétence qui la porte, l'**état** chez son propriétaire (un manifeste, un
   registre, une doc), le reste en feuille de route. Un plan joint à un zip reste un plan que
   personne ne relira.
2. **Puis joindre ce qui n'a pas pu l'être** :
   ```bash
   py ${CLAUDE_PLUGIN_ROOT}/skills/claude-sessions-migration/scripts/joindre_au_zip_ce_qui_ne_voyage_pas.py <zip> --dry-run
   ```
   Le critère est à **trois conditions** : la session le **cite** · il **existe** · **git ne le
   transporte pas**. La troisième évite de dupliquer ton dépôt dans chaque zip — une seconde copie,
   plus vieille, que quelqu'un finira par croire.

⚠️ **À adapter chez toi** : le script filtre par **liste blanche de racines** — `.claude/plans` (
standard) et le dossier où vivent tes dépôts, écrit `PROJECTS` par défaut. Change-le en tête du
script pour le tien (`code`, `dev`, `repos`…), sinon seuls les plans seront joints.

*Pourquoi une liste blanche et pas une liste noire : la liste noire a été essayée, puis jetée. Sur
une trentaine de chemins cités elle retenait la licence de Git, un inventaire de paquets et un
fichier de toolchain — des fichiers d'installation qu'un message d'erreur avait cités au passage.
**Le bruit d'un transcript est illimité ; les endroits où vit le travail sont en petit nombre et
connus.***

### 🖥️ Règle d'usage — migration entre COMPTES = MÊME PC, jamais de navette USB inter-PC (gravé 2026-07-09)

Cas d'usage réel quand l'utilisateur **change de compte Claude** (abo résilié → nouveau compte) : il **migre
ses sessions d'un compte à l'autre TOUJOURS sur le MÊME PC**. Sur un même PC les `.jsonl` sont sur le
disque, **liés au compte Windows, PAS au compte Claude** → changer de compte = **simple re-login, les
fichiers restent**. **Rien à transférer.**

**Ne JAMAIS lui imposer un transfert `.zip` par clé USB entre ses 2 PC.** L'utilisateur a **accès simultané à
ses 2 PC en bureau à distance** → il ne branche pas de clé sur un PC distant, il fait le switch de compte
**localement sur chaque PC**. Pour du léger (un doc, un prompt), la **navette Ctrl+C / Ctrl+V** entre les
2 bureaux remote suffit — pas de paranoïa, pas d'exports lourds.

**⚠️ TRANCHÉ (vécu réel 2026-07-09) : changer de compte Claude = tu ne REVOIS pas tes sessions.**
La sidebar Claude Desktop se recharge **PAR COMPTE** → le nouveau compte affiche une sidebar **VIDE** des
anciennes sessions. **NE JAMAIS dire « ça s'affichera après login » : c'est faux, la sidebar sort vide.**

> 🔧 **AFFICHAGE ≠ RETROUVABILITÉ — correction du 2026-07-25 (ce bloc sur-promettait).** L'ancienne
> rédaction disait « tu NE retrouves PAS tes sessions » et « le protocole export/revive **n'est PAS
> optionnel** ». **Faux, prouvé live** : l'utilisateur a nommé une session ouverte sur un **autre compte**,
> **aucun export n'avait été fait**, et elle est ressortie en quelques secondes → chip → contexte
> complet rechargé. **Ce qui est vide, c'est la VUE ; le disque, lui, garde tout** — et le **store
> `local_*.json` est PARTAGÉ entre comptes** (la session de l'autre compte y était ; `list_sessions`,
> filtré par compte, ne la voyait pas). ⇒ tranche l'hypothèse **(a)** du § Multi-comptes plus bas.
> **Donc** : l'export d'avant-bascule reste une **assurance recommandée** (si le store se corrompt, si
> on change de PC, si un compte est résilié), **pas** un prérequis à la retrouvabilité. Pour
> **retrouver/relancer** une session sur ce PC — export ou pas — la compétence est
> **`/claude-sessions-migration` § ①** (§ capture d'écran), jamais celle-ci.

**Protocole migration inter-COMPTES (même PC), NE PLUS redemander :**
1. **AVANT de changer de compte — export filet, en assurance** (`--flat --zip` vers Downloads, ou
   `--active` depuis le harness). Zéro token, pas besoin d'abo actif. Pas un prérequis à la
   retrouvabilité (cf § PORTE D'ENTRÉE cas A : le disque et le store des titres survivent au
   changement de compte tout seuls) — mais une vraie assurance si le store se corrompt ou si un
   compte est un jour résilié.
2. **Login nouveau compte** → sidebar **vide** (attendu, normal).
3. **Revive** : relancer les sessions en **chips depuis le disque / le bundle** (`read_claude_session.py`
   lit les `.jsonl` déjà locaux → chaque chip recharge son contexte). C'est **LE geste normal**, pas l'exception.
4. **Clé USB / transfert inter-PC = seulement PC↔PC réellement séparés**, jamais pour un changement de
   compte sur la même machine (là tout est déjà sur le disque).

### 🧹 Ménage à CHAQUE export — REMPLACER l'ancien, jamais toucher au reste (règle d'usage gravée 2026-06-22)

À chaque export vers une **destination de transfert** (clé USB, dossier de migration) : faire le ménage
**dans la même passe**. On ne garde qu'**UN** export courant à cet endroit, pas une pile d'anciens.

1. **Lister la destination AVANT** d'écrire/supprimer (inventaire).
2. **Copier** le nouveau zip + le **renommer avec le préfixe `migration-` OBLIGATOIRE** :
   `migration-<scope>_<date>.zip` (ex `migration-mon-projet_2026-06-22.zip`).
   ⚠️ **Sans `migration-` en tête, l'utilisateur NE retrouve PAS ses migrations** — tout export/migration de
   sessions DOIT commencer par `migration-` (verbatim 2026-06-22, NON négociable).
3. **Supprimer UNIQUEMENT l'ancien export** : les artefacts produits par CE skill —
   `migration-*.zip`, `mon-projet_*.zip`, `claude-sessions*.zip`, `REPRISE*.md`, `INDEX-SIDEBAR.md`, `LISEZ-MOI.md`.
   Delete **fichier-par-fichier** (`[System.IO.File]::Delete`), **jamais** `-Recurse`.

> 🛑 **Garde-fou NON négociable** : ne JAMAIS toucher aux autres fichiers/dossiers de la destination.
> La destination contient très probablement des dossiers personnels sans rapport — **intouchables**.
> On supprime le SEUL ancien export identifié par son nom, rien d'autre. C'est une autorisation explicite
> de suppression **strictement limitée aux artefacts de ce skill** (ça lève le défaut archive-first
> global UNIQUEMENT pour ce cas précis, sur demande explicite de l'utilisateur).

Formulé par l'utilisateur à l'origine de la règle : *« nettoie bien l'ancien fichier sans supprimer les
bons fichiers, juste l'ancien export, on renomme bien le nouvel export… il faut faire le ménage à chaque
fois… j'ai d'autres dossiers là-dedans, n'y touche pas. »*

### ⚡ Recettes (commandes prêtes)

```powershell
# 0) ⭐⭐ MIGRATION SIMPLE (PC→PC, l'usage courant) : UN seul .zip, dans les TÉLÉCHARGEMENTS.
#    Toujours au même endroit, facile à retrouver. Le script imprime le chemin exact.
py ${CLAUDE_PLUGIN_ROOT}/skills/claude-sessions-migration/scripts/export_claude_sessions.py --sidebar --flat --zip --out "$env:USERPROFILE\Downloads\claude-sessions"
#    -> %USERPROFILE%\Downloads\claude-sessions.zip   (réinjection sur l'autre PC : /claude-sessions-migration § ①)

# 1) ⭐ SIDEBAR (mode recommandé) : RANGEMENT AUTO + .zip propre PAR DÉFAUT.
#    Sort UN dossier par export :  <out>/<année>/<projet>/<date_nom>/<projet>_<date>.zip
#    (le .zip contient jsonl/ bruts + md/ lisibles + INDEX-SIDEBAR.md + REPRISE.md ; bundle temp auto-nettoyé)
py ${CLAUDE_PLUGIN_ROOT}/skills/claude-sessions-migration/scripts/export_claude_sessions.py --sidebar --out "$env:USERPROFILE\Documents\Migration compte Claude"
py ${CLAUDE_PLUGIN_ROOT}/skills/claude-sessions-migration/scripts/export_claude_sessions.py --sidebar --project mon-projet --out "<dossier>"      # 1 SEUL dépôt (dossier = son nom)
py ${CLAUDE_PLUGIN_ROOT}/skills/claude-sessions-migration/scripts/export_claude_sessions.py --sidebar --export-name sidebar-active --out "<dossier>" # suffixe lisible du dossier d'export
py ${CLAUDE_PLUGIN_ROOT}/skills/claude-sessions-migration/scripts/export_claude_sessions.py --sidebar --dry-run                                      # voir la liste sans rien écrire
py ${CLAUDE_PLUGIN_ROOT}/skills/claude-sessions-migration/scripts/export_claude_sessions.py --sidebar --include-archived --out "<dossier>"           # inclure les archivées
py ${CLAUDE_PLUGIN_ROOT}/skills/claude-sessions-migration/scripts/export_claude_sessions.py --sidebar --days 3 --out "<dossier>"                     # actives (focus) des 3 derniers jours
py ${CLAUDE_PLUGIN_ROOT}/skills/claude-sessions-migration/scripts/export_claude_sessions.py --sidebar --flat --out "<dossier>"                       # ANCIEN comportement : fichiers en vrac dans <dossier> (+ --zip pour zipper)
#    NB : `non-archivé` = sessions ACTIVES/OUVERTES (Claude Desktop auto-archive les vieilles).
#    Tri = `lastFocusedAt` (dernière OUVERTURE dans l'UI = ordre sidebar réel), PAS `lastActivityAt` (faussé par l'auto-sync git).
#    Le .zip se réinjecte sur l'autre PC avec la compétence sœur : /claude-sessions-migration § ①

# 1bis) ⭐ SIDEBAR EXACTE (la capture au mot près) : sélection par TITRE/ID via manifest.
#    Le store NE contient PAS le flag épinglé ni l'ordre visible (cf § Multi-comptes) -> le seul moyen
#    100% fidèle à un SCREENSHOT = filtrer les sessionId/cliSessionId voulus dans le manifest, puis :
#    PowerShell : ne garder que les enregistrements dont .cli est dans ta liste -> .sidebar-manifest-sel.json (dans le dossier courant)
py ${CLAUDE_PLUGIN_ROOT}/skills/claude-sessions-migration/scripts/export_claude_sessions.py --sidebar --manifest ".sidebar-manifest-sel.json" --export-name sidebar-active --out "<dossier>"

# 2) INDEX global de TOUTES les sessions (vue d'ensemble tous projets)
py ${CLAUDE_PLUGIN_ROOT}/skills/claude-sessions-migration/scripts/export_claude_sessions.py
#    -> ~/.claude/sessions-export/INDEX.md

# 3) MIGRATION par récence (FALLBACK si pas de Claude Desktop) — titres = 1er message, pas custom
py ${CLAUDE_PLUGIN_ROOT}/skills/claude-sessions-migration/scripts/export_claude_sessions.py --active --days 10 --per-project 15 --out "<dossier>"

# 4) Export complet LISIBLE d'un projet (relire sans Claude Code)
py ${CLAUDE_PLUGIN_ROOT}/skills/claude-sessions-migration/scripts/export_claude_sessions.py --full --project mon-projet
```

#### Le mode `--sidebar` (la source de vérité)

C'est LE bon mode : il lit directement le store de la sidebar Claude Desktop
(`%APPDATA%/Claude/claude-code-sessions/<fenêtre>/local_<id>.json`, un fichier par session) qui
contient le **titre exact** (`.title`), le projet (`.cwd`), l'état (`.isArchived`), et surtout le
**lien vers le vrai fichier JSONL via `.cliSessionId`** (= le nom du `.jsonl` dans `~/.claude/projects/`).
Résultat = ta sidebar au mot près, pas une approximation par récence.

> 🔧 **Pont manifest (cas particulier)** : si le process qui lance le script ne peut pas lire `%APPDATA%`
> (ex : Claude Code dans le harness, qui voit `~/.claude` mais pas `~/AppData`), passer par un manifest :
> PowerShell extrait le store → JSON, puis `py ... --sidebar --manifest .sidebar-manifest.json`.
> Le snippet PowerShell d'extraction est dans la section « Pont manifest » plus bas. En usage normal
> (dans ton propre terminal), `--sidebar` seul suffit, pas besoin de manifest.

> ⚠️ **Piège `py` → Python Store** (vu le 2026-06-02) : si `--sidebar` répond « Store introuvable »
> alors que Claude Desktop EST installé, c'est souvent que le lanceur `py` a résolu le shebang vers un
> **Python Microsoft Store** (virtualisé, aveugle à `%APPDATA%`). Le store est bien là (PowerShell le voit),
> ce Python-là non. Fix : forcer un vrai Python —
> `& "$env:LOCALAPPDATA\Programs\Python\Python312\python.exe" ${CLAUDE_PLUGIN_ROOT}/skills/claude-sessions-migration/scripts/export_claude_sessions.py --sidebar`
> — ou `--manifest`. Le message d'erreur du script le rappelle désormais.

> ℹ️ `--active` reste un **fallback** par récence (dernière activité réelle via `ts_end`, pas le `mtime`
> faussé par l'auto-sync). À n'utiliser que si Claude Desktop n'est pas sur le PC.

### 📂 Ce que produit le mode `--sidebar`

**Par défaut (RANGÉ)** — 1 dossier par export, 1 seul `.zip` propre (rien en vrac) :

```
<dossier de sortie>/
  <année>/<projet>/<date>_<nom>/<projet>_<date>.zip      ex: 2026/mon-projet/2026-06-20_1754_sidebar-active/mon-projet_2026-06-20_1754.zip
```

Le `.zip` contient le bundle complet (le `--export-name` ajoute le suffixe `_<nom>` au dossier daté) :

```
  INDEX-SIDEBAR.md        récap (par projet) = ta sidebar
  REPRISE.md              comment relancer chaque session (commandes prêtes)
  jsonl/<projet>/<id>.jsonl    copies brutes (pour reprendre / cross-PC)
  md/<projet>/<date>_<titre>_<id8>.md   versions lisibles, titre = titre sidebar (Utilisateur ↔ Claude)
```

**Avec `--flat`** — ancien comportement : `INDEX-SIDEBAR.md` + `REPRISE.md` + `jsonl/` + `md/` écrits
directement dans `<dossier de sortie>` (+ `--zip` pour un `<dossier>.zip` frère). À éviter dans un dossier
déjà peuplé (il zipperait le contenu voisin).

### 🌿 TRANSPORT PAR GIT — le bundle voyage dans le dépôt, pas sur une clé

> Procédure complète (EXPORT · REVIVE · mémo · garde-fous) : **§ ③** plus bas — même script, même
> bundle ; ici le pourquoi et la recette courte.

> 📦 Un **véhicule** de plus pour le même export : `.zip` à recopier d'un côté, commit git de l'autre.
> Même script, mêmes sessions, même job.

**Quand ce transport plutôt que le `.zip`** : petit dépôt **privé**, déjà sur GitHub, peu de sessions.
Le bundle est committé dans le dépôt → il voyage tout seul avec le `git pull`, zéro copie manuelle.
Gros volume ou dépôt non-git → rester sur le `.zip` des recettes ci-dessus.

#### ⬆️ Snapshot d'un NIVEAU → commit + push

> 🎯 **1 niveau égale 1 scope, et on respecte les sous-dossiers.** On photographie **uniquement** les
> sessions du dossier courant, pas celles de ses sous-dossiers. Chaque sous-dossier qui a son propre
> `CLAUDE.md` est un scope séparé, synchronisé depuis lui-même.

```bash
TARGET="$(pwd)"
SKILL="<dossier-de-la-compétence>/scripts"   # là où ce SKILL.md est installé

python "$SKILL/export_claude_sessions.py" --active --exact --cwd "$TARGET" --days 36500 --flat --md-only \
  --out "$TARGET/.claude-sessions"

git -C "$TARGET" add .claude-sessions CLAUDE.md
git -C "$TARGET" commit -m "chore(sessions): snapshot sessions Claude Code (niveau $(basename "$TARGET"))"
git -C "$TARGET" push
```

- **`--exact --cwd` est le filtre par DÉFAUT**, et `--project` ne peut pas le remplacer : le `cwd` d'un
  sous-dossier **contient toujours** le chemin du parent, donc un filtre sous-chaîne l'aspire. Bug prouvé
  le 2026-06-22 — `--project "Antigravity"` à la racine ramenait les 5 buckets, 49 sessions fusionnées.
- **`--md-only` est le défaut recommandé** : que les `.md` lisibles, pas les `.jsonl` bruts, donc zéro
  screenshot base64. Une session computer-use passe de **88 Mo à 2 Mo**. Besoin du `claude --resume`
  natif (rare) → retirer le flag, en acceptant le poids.
- **Idempotent** : le re-export efface puis réécrit le bundle, on ne committe que le delta.
- `--sidebar` donne les titres exacts mais lit `%APPDATA%`, **invisible au harness** — le réserver à un
  run depuis le terminal de l'utilisateur ; en skill, `--active --exact` marche partout.

#### 📌 Le mémo posé dans le `CLAUDE.md` du dépôt

À poser dans `<dépôt>/CLAUDE.md` (créer le fichier s'il manque). Auto-chargé à chaque session du dépôt,
donc **n'importe quel compte ou PC sait où chercher** sans hook. Idempotent via son marqueur — déjà
présent, on rafraîchit entre les marqueurs, on ne re-pose pas.

```markdown
<!-- claude-sessions-sync:memo -->
## 🗂️ Historique de mes sessions Claude Code — dans `.claude-sessions/`

Ce dépôt transporte ses sessions Claude Code dans **`.claude-sessions/`** (transport git, section « 🌿 TRANSPORT PAR GIT » du skill global global `/claude-sessions-migration` § ②). C'est l'historique de mes sessions ici, quel que soit le compte ou le PC.

- **Au démarrage, quand je reprends le fil** → le consulter d'abord : `python <dossier-de-la-compétence>/scripts/read_claude_session.py ".claude-sessions"` (liste), ou lire `.claude-sessions/md/*.md`. Récupérer le contexte AVANT de repartir de zéro.
- **Re-snapshot** après du travail → `/claude-sessions-migration` § ② § TRANSPORT PAR GIT. **Récupérer ailleurs** → `/claude-sessions-migration` § ①.
<!-- /claude-sessions-migration § ③:memo -->
```

#### ⬇️ Reprendre à l'arrivée

`git pull` récupère `.claude-sessions/`, puis la relance vit chez la compétence sœur
**`/claude-sessions-migration` § ①** (elle lit un bundle comme un `.zip`, même Mode B, mêmes chips).
Ne pas ré-implémenter la relance ici.

#### 🔒 Garde-fous propres à ce transport

- ⚠️ **Dépôts PRIVÉS uniquement.** Un `.jsonl` peut contenir des jetons, des chemins, du contenu
  sensible. Pousser un secret, c'est le publier.
- **Mesurer avant de pousser.** git garde **chaque version** à chaque re-sync — un bundle lourd bloate
  le dépôt définitivement. Contrôle : `du -sh <niveau>/.claude-sessions` et
  `find <niveau>/.claude-sessions -type f -size +50M`. Dizaines de Mo → repasser au `.zip` hors-git.
- **Session sans `cwd` lisible** → ignorée, jamais déposée au hasard.

> 🧪 **Posé, à confirmer** : le scoping par niveau est **prouvé sur données réelles**
> (2026-06-22 — racine antigravity 17 sessions, `vente-marketing/` 21, zéro fuite de sous-dossier), et
> le round-trip des 3 scripts est prouvé (2026-06-21). **Jamais validé** : un aller-retour réel PC1 vers
> PC2 avec `git pull` puis relance. Tant que ce n'est pas fait, ce transport n'est pas « terminé ».

### ▶️ Reprendre / relancer une session proprement

Une session se reprend **en local, sans dépendre du compte** :

```powershell
cd "<dossier du projet>"          # ex: cd "C:\Users\<toi>\Projets\mon-projet"
claude --resume <sessionCLI>
```

- Le `sessionCLI` (= `cliSessionId`, le nom du fichier `.jsonl`) est dans `INDEX-SIDEBAR.md` / `REPRISE.md`.
- **Cross-PC** : ne plus copier les `.jsonl` à la main → utiliser le **script d'import** ci-dessous
  (`scripts/import_claude_sessions.py`), qui place chaque session au bon endroit en remappant le chemin.
- `REPRISE.md` liste tout ça, groupé par projet, prêt à copier-coller.

> 🆘 **Débloquer une session MORTE (« contexte plein », plus accessible) — même PC** (vécu 2026-06-21, session « 📖 chat_reader CD — kARAOKE », 9 Mo / 2751 lignes). Le `.jsonl` reste **intact** → le travail n'est PAS perdu. **La voie qui marche, en 30 s = chip Mode B via `/claude-sessions-migration` § ①** : spawn UN chip rooté dans le bon dossier (`cwd`), qui **recharge tout le contexte** via `scripts/read_claude_session.py` et reprend le fil. **Zéro terminal, zéro login, zéro `/resume`.** C'est la 1re (et seule) chose à faire pour une session morte sur CE PC.
>
> ⛔ **Pièges PROUVÉS 2026-06-21 — NE PAS y retourner** (j'ai brûlé 1 h dessus) : (1) **`/resume` natif n'est PAS dispo dans Claude Desktop** (réponse « pas disponible ici / erreur ») — il ne marche qu'en CLI terminal pur. (2) **Terminal externe = cul-de-sac auth** : ce `claude.exe` (`%APPDATA%\Claude\claude-code\<v>\`) est **managé par Claude Desktop** (`CLAUDE_CODE_SDK_HAS_HOST_AUTH_REFRESH=1`, vrai jeton frais dans `%APPDATA%\Claude\buddy-tokens.json`). Le `~/.claude/.credentials.json` standalone est **expiré** et les logins terminal **ne le réparent pas** → « autorisation invalide » en boucle, quel que soit le compte. → pour une session morte, **toujours le chip Mode B `/claude-sessions-migration` § ①**, jamais le terminal ni `/resume`. Doc humaine miroir : page Notion « 🔁 Relancer mes sessions » § Session plantée.

### ♻️ Réinjecter / réimporter → compétence sœur `/claude-sessions-migration` § ①

L'import (réinjecter un `.zip` ou un bundle → `claude --resume` sur ce PC ou un autre, avec remap
auto du username) vit dans sa **propre compétence** : **`/claude-sessions-migration` § ①**. En une ligne :

```powershell
py ${CLAUDE_PLUGIN_ROOT}/skills/claude-sessions-migration/scripts/import_claude_sessions.py "<chemin>\sessions-export.zip"        # PC→PC : remap auto
py ${CLAUDE_PLUGIN_ROOT}/skills/claude-sessions-migration/scripts/import_claude_sessions.py "<zip>" --no-auto-user                # même PC : mapping exact
```

Détails (remap, dry-run, force, REPRISE) = skill `/claude-sessions-migration` § ①.

### 🔧 Pont manifest (si `%APPDATA%` inaccessible au process)

Snippet PowerShell qui extrait le store sidebar → JSON, à utiliser avec `--sidebar --manifest` :

```powershell
$dir = "$env:APPDATA\Claude\claude-code-sessions"
$byId = @{}
foreach ($f in (Get-ChildItem $dir -Recurse -Filter "local_*.json")) {
  try { $j = Get-Content $f.FullName -Raw -Encoding UTF8 | ConvertFrom-Json } catch { continue }
  if (-not $j.sessionId) { continue }
  $foc = 0; if ($j.lastFocusedAt)  { $foc  = $j.lastFocusedAt }    # ordre sidebar réel
  $act = 0; if ($j.lastActivityAt) { $act  = $j.lastActivityAt }   # faussé par auto-sync
  $rec = [ordered]@{ sessionId=$j.sessionId; cli=$j.cliSessionId; cwd=$j.cwd; title=$j.title; archived=[bool]$j.isArchived; exempt=[bool]$j.autoArchiveExempt; focused=$foc; last=$act }
  $score = $foc; if ($score -eq 0) { $score = $act }
  $prev = $byId[$j.sessionId]; $pScore = 0; if ($prev) { $pScore = $prev.focused; if ($pScore -eq 0) { $pScore = $prev.last } }
  if (-not $prev -or $score -gt $pScore) { $byId[$j.sessionId] = $rec }
}
$abs = (Join-Path $PWD.Path ".sidebar-manifest.json")
[System.IO.File]::WriteAllText($abs, (@($byId.Values) | ConvertTo-Json -Depth 4), (New-Object System.Text.UTF8Encoding($false)))
py ${CLAUDE_PLUGIN_ROOT}/skills/claude-sessions-migration/scripts/export_claude_sessions.py --sidebar --manifest ".sidebar-manifest.json" --out "<dossier>"
```

> Pour la **SIDEBAR EXACTE d'un screenshot** (recette 1bis) : après avoir construit `.sidebar-manifest.json`,
> garder seulement les sessions voulues (par titre ou `cli`) dans `.sidebar-manifest-sel.json`, puis exporter
> avec `--manifest ".sidebar-manifest-sel.json"`. C'est la seule méthode 100% fidèle (le store n'a ni flag
> épinglé ni ordre visible, cf § Multi-comptes).

### 🧹 Mieux organiser des sessions « en pagaille »

- `INDEX.md` global = vue d'ensemble (tous projets, triés par récence) → repérer les doublons (mêmes
  chantiers relancés N fois), les sessions mortes, ce qui reste à finir.
- Plusieurs sessions au même titre = reprises successives → garder la plus récente (`ts_end`).
- Les 744 sessions `subagents/` + `wf_*` sont du bruit interne (exclues par défaut) — ne pas les
  exporter sauf besoin de debug.
- Pour archiver un chantier fini : son `.md` lisible + son `.jsonl` suffisent (pas de wrapup payant).

### 🔍 Multi-comptes — TRANCHÉ côté vécu (le comportement pratique)

> ✅ **TRANCHÉ (vécu réel 2026-07-09) : changer de compte = sidebar VIDE, sessions PAS retrouvées.**
> En pratique c'est le comportement de l'hypothèse **(b)** : sous un autre compte on **ne revoit pas** ses
> sessions → le protocole **export-avant / revive-après est OBLIGATOIRE** (cf § Règle migration ci-dessus).
> Le détail technique ci-dessous (fichiers locaux, empreinte de store) reste à confirmer, mais **ne change
> RIEN à la conduite : on ne compte JAMAIS sur l'affichage auto après un changement de compte.**

> ⚠️ **Question ouverte non tranchée.** Avec plusieurs comptes Claude sur la même machine : la sidebar
> d'un projet (mode Code) peut afficher ~15 sessions alors que l'export `--sidebar` en sort beaucoup
> plus (ex 48 non-archivées sur un seul dépôt). **Deux explications possibles, pas encore départagées :**
> (a) les sessions « en trop » sont juste **plus anciennes** (hors de la vue du haut de sa sidebar),
> (b) elles viennent de **ses autres comptes** (le store local mélangerait les comptes).

**Constats techniques établis :**

1. **Pas de flag `isPinned` ni d'ordre de sidebar dans les fichiers** (`local_*.json`). Re-vérifié 2026-06-20 :
   **0/923** occurrence de `isPinned`. Donc `--sidebar` exporte **toutes les non-archivées** (un sur-ensemble sûr),
   pas exactement les ~15 affichées. **Seul moyen 100% fidèle à un screenshot = recette 1bis (manifest filtré
   par titre/`cli`).**
   - ✅ **NOUVEAU 2026-06-20 — `lastFocusedAt` existe** (+ `lastFocusedAt`, `autoArchiveExempt`, `titleSource`
     dans le store). C'est la **dernière OUVERTURE dans l'UI** = bien plus proche de l'ordre sidebar que
     `lastActivityAt` (que l'auto-sync git gonfle). **Le tri par défaut utilise désormais `lastFocusedAt`**
     (`_recency()` dans le script). Ça **ne reproduit pas exactement** la vue (le simple fait de cliquer/scroller
     la sidebar bump `lastFocusedAt`), mais l'ordre est juste.
   - **Penche vers l'explication (a)** : triées par `lastFocusedAt`, les sessions du screenshot remontent en tête
     et les « en trop » ont un focus plus ancien = ce sont surtout des sessions **plus vieilles hors-vue**, pas
     d'autres comptes (à confirmer par le protocole d'empreinte ci-dessous). `autoArchiveExempt` est quasi
     toujours absent (1 cas) → inutilisable comme sélecteur.
2. **Pas de champ « compte » dans les fichiers** (ni `local_*.json`, ni JSONL). Impossible d'étiqueter
   « cette session = compte X » par lecture de fichiers. Piste feature future : lire le compte **affiché
   dans Claude Desktop** (« F · Pro » en bas) via UIA, comme on lit le compte dans Chrome.
3. **« Tout est en local »** = vrai au niveau fichiers (`~/.claude/projects/`, lié au **compte Windows**).
   Mais c'est **ce PC uniquement** — une session faite sur un autre PC n'est ici que si synchronisée (git).

**Protocole de vérification (à dérouler à la prochaine session depuis un autre compte) :**

```powershell
# 1) Sur le compte ACTUEL (produit une empreinte dans account-snapshots/)
py ${CLAUDE_PLUGIN_ROOT}/skills/claude-sessions-migration/scripts/export_claude_sessions.py --status --label "compte-1" --out "<dossier>"
# 2) Se déconnecter, se reconnecter sur un AUTRE compte Claude dans Claude Desktop, puis :
py ${CLAUDE_PLUGIN_ROOT}/skills/claude-sessions-migration/scripts/export_claude_sessions.py --status --label "compte-2" --out "<dossier>"
# 3) Comparer les EMPREINTES (champ fingerprint des 2 JSON dans account-snapshots/) :
#    - MEME empreinte  -> le store est PARTAGE (1 seul store local, tous comptes mélangés)
#                         => les sessions « en trop » sont juste plus anciennes (explication a).
#    - empreinte DIFFERENTE -> le store est RECHARGE par compte
#                         => chaque compte a ses sessions (explication b), et --sidebar par compte = correct.
```

Chaque `--status` dépose son empreinte dans `account-snapshots/`. Au prochain run depuis un autre compte
→ refaire `--status`, comparer les deux empreintes, et **trancher (a) ou (b)**.

### 🔧 Paramètres du script

| Flag | Effet |
|------|-------|
| `--sidebar` | ⭐ Lit le store Claude Desktop (titres custom + lien JSONL). Sort **toutes les non-archivées** (sur-ensemble de la sidebar visible — le flag « épinglé » n'est pas dans les fichiers, cf § Multi-comptes) |
| `--include-archived` | Avec `--sidebar` : inclut aussi les sessions archivées |
| `--manifest PATH` | Avec `--sidebar`/`--status` : lit la liste depuis ce JSON au lieu du store `%APPDATA%` (cf Pont manifest) |
| `--status` | Capture une **empreinte** du store (`account-snapshots/`) pour comparer entre comptes Claude (cf § Multi-comptes) |
| `--label TEXTE` | Avec `--status` : étiquette du compte au moment de la capture (ex `compte-F-pro`) |
| (aucun) | Index global `INDEX.md` de toutes les vraies sessions |
| `--active` | Fallback par récence (si pas de Claude Desktop) : jsonl + md + INDEX-ACTIVE + REPRISE |
| `--days N` | Fenêtre de récence. `--sidebar` : par `lastFocusedAt` (ordre sidebar). `--active` : par `ts_end`, défaut 7 |
| `--per-project N` | Garde les N sessions les plus récentes de chaque projet |
| `--limit N` | Cap global des N sessions les plus récentes (marche aussi avec `--sidebar`) |
| `--export-name TXT` | `--sidebar`/`--active` rangés : suffixe lisible du dossier d'export daté (ex `sidebar-active`) |
| `--flat` | `--sidebar`/`--active` : **désactive** le rangement auto → écrit en vrac dans `--out` (ancien comportement). Combine avec `--zip` |
| `--zip` | Avec `--flat` : compresse en `<out>.zip`. **Sans `--flat`, inutile** (le rangement auto zippe déjà) |
| `--dry-run` | Compte + liste sans rien écrire (calibrage) |
| `--full` | Génère un `.md` lisible par session |
| `--project TEXTE` | Ne traite que les projets dont le chemin contient ce texte |
| `--include-subagents` | Inclut les sessions internes subagents/workflows |
| `--out CHEMIN` | Sortie. Par défaut = **racine du rangement** `<out>/<année>/<projet>/<export>/` (sauf `--flat`). Défaut `~/.claude/sessions-export/` |

### Sources canoniques (routing)

- Script export : `scripts/export_claude_sessions.py`
- Script import / réinjection : `scripts/import_claude_sessions.py` (testé : remap, dédoublonnage, `--force`, auto-user, encodage worktree)
- Retrouver / relancer une session sur CE PC (aucun export requis) : `/claude-sessions-migration` § ①


# § ③ TRANSPORT PAR GIT — petits dépôts privés

> Le POURQUOI de ce véhicule et sa recette courte sont au **§ ② → 🌿 TRANSPORT PAR GIT** ; ici la
> procédure complète (EXPORT · REVIVE, mémo posé dans le `CLAUDE.md` du dépôt, garde-fous).

### 🎯 Objectif (le problème que ça résout)

L'utilisateur a **plusieurs comptes Claude × 2 PC** = autant d'environnements différents. Les mêmes
sessions sont parfois à droite, parfois à gauche, parfois introuvables (il faut se reconnecter
à un compte juste pour aller chercher un truc). But : **photographier les sessions d'un petit
dépôt et les transporter sans friction**.

`/claude-sessions-migration` § ② résout déjà ça, mais **transport = un `.zip` à recopier** (clé USB,
download). Pour ses **petits dépôts** (peu de sessions, déjà sur GitHub — « ses trucs à lui »,
pas des applications), c'est plus simple de **passer par git** : la session est **committée
dans le dépôt** → elle voyage toute seule avec le `git pull`. Zéro zip, zéro copie manuelle.

> **Quand CE skill vs `/claude-sessions-migration` § ② ?**
> - **CE skill** = petit dépôt git, peu de sessions, on veut le **transport git** (commit/push/pull).
> - **`/claude-sessions-migration` § ②** = gros volume, transfert hors-git (clé USB/`.zip`), ou pas un dépôt git.

Self-contained : les 3 scripts vivent **dans le skill** (`scripts/`, stdlib only) → marche depuis
**n'importe quel dépôt**. Source canonique des scripts = ce plugin (`scripts/`, une seule copie).

### 🧭 Deux verbes : EXPORT (snapshot+push) · REVIVE (pull+relance)

C'est Claude qui exécute (l'utilisateur ne tape rien). Détecter le verbe d'après ce qu'il dit :
- « sauvegarde / photographie / pousse les sessions de ce dépôt » → **EXPORT**.
- « récupère / relance / reprends les sessions de ce dépôt » (souvent après changement de PC) → **REVIVE**.

Le bundle vit dans **`<dossier-niveau>/.claude-sessions/`** (raw, git-diffable) — **un par niveau**
(racine et/ou sous-dossier à `CLAUDE.md`), jamais fusionné :
`jsonl/` (sessions brutes) · `md/` (lisibles) · `INDEX-ACTIVE.md` · `REPRISE.md`.

---

### ⬆️ EXPORT — snapshot des sessions de CE niveau → commit/push

> 🎯 **1 niveau = 1 scope. On RESPECTE les sous-dossiers.** On photographie **UNIQUEMENT les sessions
> du dossier courant**, PAS celles de ses sous-dossiers. Chaque sous-dossier qui a son propre `CLAUDE.md`
> est un **scope séparé**, synchronisé **depuis lui-même** (logique fractale — un scope par dossier qui porte son `CLAUDE.md` :
> 1 dossier-`CLAUDE.md` = 1 chantier). Lancé à la **racine** du dépôt → seulement les sessions de niveau
> racine (le « global » du dépôt). Lancé dans `vente-marketing/` → seulement celles de `vente-marketing/`.
> l'utilisateur gère ses sous-dossiers lui-même → à un niveau donné, on ne touche QUE ce niveau.

```bash
# 1) Le scope = le dossier courant, son niveau SEUL (pas les sous-dossiers).
TARGET="$(pwd)"
SKILL="<dossier-de-la-compétence>/scripts"

# 2) Snapshot EXACT de ce niveau, LÉGER (lit ~/.claude/projects — accessible au harness).
#    --exact --cwd "$TARGET" = STRICT (exclut les sous-dossiers) · --md-only = sans jsonl/screenshots · --days 36500 = sans limite.
python "$SKILL/export_claude_sessions.py" --active --exact --cwd "$TARGET" --days 36500 --flat --md-only \
  --out "$TARGET/.claude-sessions"

# 3) Poser le MÉMO dans le CLAUDE.md de CE niveau (Claude : cf § Mémo dépôt ci-dessous).
#    Idempotent via le marqueur <!-- claude-sessions-sync:memo --> ; créer CLAUDE.md s'il manque.

# 4) Commit + push (Claude exécute — dépôt PRIVÉ uniquement, cf garde-fous).
git -C "$TARGET" add .claude-sessions CLAUDE.md
git -C "$TARGET" commit -m "chore(sessions): snapshot sessions Claude Code + mémo (niveau $(basename "$TARGET"))"
git -C "$TARGET" push
```

- **`--exact --cwd "$TARGET"` = le filtre par DÉFAUT.** Strict : ne prend que les sessions dont le `cwd`
  est EXACTEMENT `$TARGET`. Cross-shell OK (Windows `C:\…` ↔ Git Bash `/c/…` réconciliés). **Pourquoi pas
  `--project` ?** Un filtre sous-chaîne ne peut PAS dire « ce niveau, pas les sous-dossiers » : le `cwd` d'un
  sous-dossier CONTIENT toujours le chemin du parent → il serait aspiré (bug 2026-06-22 : `--project
  "Antigravity"` à la racine aspirait les 5 buckets = 49 sessions fusionnées). `--exact` règle ça.
- **`--md-only` = défaut recommandé (LÉGER, sans screenshots).** N'embarque que les `.md` lisibles,
  **pas les `.jsonl` bruts** → **zéro screenshot/base64 ni junk** (une session computer-use passe de
  ~88 Mo à ~2 Mo). Revive = **Mode B** (Claude lit le `.md`, le reader a un fallback md). Besoin du
  `claude --resume` natif (rare) → **enlever `--md-only`** pour embarquer aussi les jsonl (⚠️ lourd).
- **`--project "<sous-chaîne>"` existe encore = mode subtree** (ce dossier **+ tous ses sous-dossiers**,
  fusionnés en UN bundle). À n'utiliser QUE pour tout aspirer explicitement (⚠️ volume, cf garde-fous).
  Sinon **toujours `--exact`**.
- Re-export = **idempotent** : le script efface `jsonl/`+`md/` de `.claude-sessions/` puis ré-écrit
  l'état courant → on commit juste le delta.
- `--sidebar` (titres exacts custom) est **mieux MAIS** lit `%APPDATA%` → **invisible au harness**. Le
  réserver à un run depuis le **terminal de l'utilisateur** ; en mode skill, `--active --exact` est la voie
  fiable partout (lit `~/.claude/projects`).

#### Tout le dépôt d'un coup — un bundle SÉPARÉ par niveau (optionnel)

Respecte la structure : racine = sessions racine, **chaque sous-dossier à `CLAUDE.md` = son propre
`.claude-sessions/`**. Aucune fusion (≠ `--project` subtree).

```bash
SKILL="<dossier-de-la-compétence>/scripts"
ROOT="$(git -C "$(pwd)" rev-parse --show-toplevel)"
# niveau racine
python "$SKILL/export_claude_sessions.py" --active --exact --cwd "$ROOT" --days 36500 --flat --md-only --out "$ROOT/.claude-sessions"
git -C "$ROOT" add "$ROOT/.claude-sessions"
# chaque sous-dossier qui a SON propre CLAUDE.md (= un scope)
find "$ROOT" -mindepth 2 -name CLAUDE.md -not -path '*/.*' -not -path '*/node_modules/*' | while read -r md; do
  sub="$(dirname "$md")"
  python "$SKILL/export_claude_sessions.py" --active --exact --cwd "$sub" --days 36500 --flat --md-only --out "$sub/.claude-sessions"
  git -C "$ROOT" add "$sub/.claude-sessions"
done
git -C "$ROOT" commit -m "chore(sessions): snapshot par niveau (racine + sous-dossiers)"
git -C "$ROOT" push
```

### 📌 Mémo auto-posé dans le `CLAUDE.md` du dépôt (« il sait où chercher »)

À l'EXPORT (étape 3), poser CE bloc dans `<dépôt>/CLAUDE.md` (créer le fichier s'il manque). Auto-chargé
à chaque session du dépôt → **n'importe quel compte/PC sait aller chercher `.claude-sessions/`** sans hook
**Idempotent** : marqueur `<!-- claude-sessions-sync:memo -->`
déjà présent → ne pas re-poser (rafraîchir entre les marqueurs si le contenu a changé).

```markdown
<!-- claude-sessions-sync:memo -->
## 🗂️ Historique de mes sessions Claude Code — dans `.claude-sessions/`

Ce dépôt transporte ses sessions Claude Code dans **`.claude-sessions/`** (sync par git, skill global global `/claude-sessions-migration` § ③). C'est l'historique de mes sessions ici, **quel que soit le compte/PC**.

- **Au démarrage / quand je reprends le fil** → le consulter d'abord : `python <dossier-de-la-compétence>/scripts/read_claude_session.py ".claude-sessions"` (liste), ou lire `.claude-sessions/md/*.md` (texte clair). Récupérer le contexte AVANT de repartir de zéro.
- **Consolider léger, sans se prendre la tête** : doublons (même chantier relancé sur un autre compte), ce qui est fini / à finir. Pas de gros ménage.
- **Re-snapshot** après du travail → `/claude-sessions-migration` § ③ (export). **Récupérer ailleurs** → `/claude-sessions-migration` § ③ (revive).
<!-- /claude-sessions-migration § ③:memo -->
```

### ⬇️ REVIVE — git pull → relance propre des sessions

Sur l'autre PC / compte / clone frais du dépôt :

```bash
REPO_DIR="$(pwd)"; SKILL="<dossier-de-la-compétence>/scripts"
git -C "$REPO_DIR" pull          # récupère .claude-sessions/ committé par l'EXPORT
```

**Mode B (défaut, recommandé — rien à réinjecter, ne touche pas `~/.claude`)** : Claude **lit** le
transcript depuis le bundle et **reprend le fil**.

```bash
python "$SKILL/read_claude_session.py" "$REPO_DIR/.claude-sessions"            # LISTE les sessions
python "$SKILL/read_claude_session.py" "$REPO_DIR/.claude-sessions" "<titre|id8>"  # lit 1 transcript
```

#### 🎰 Relance propre EN CHIPS (le « lancer proprement les sessions » que veut l'utilisateur)

> **AVANT de spawn un chip (réutiliser le vivant, 2026-06-22)** : `list_sessions` (capacité de Claude Desktop) → une session VIVANTE couvre-t-elle déjà ce sujet au bon dépôt ? → **`send_message`** plutôt qu'un chip neuf (zéro doublon, toujours confirmé). On ne spawn un chip REVIVE que pour ce qui n'a PAS de session vivante. (`list_sessions` puis `send_message` : parler à la session vivante avant d'en créer une).

Pour relancer les sessions du dépôt comme des chips cliquables (1 chip = 1 session, l'utilisateur clique,
rien à taper) — Claude exécute :

1. **Lister** : `python "$SKILL/read_claude_session.py" "$REPO_DIR/.claude-sessions"` (titres + id8 + projet).
2. Pour CHAQUE session retenue → `spawn_task` :
   - **title** = le titre d'origine de la session.
   - **cwd** = `$REPO_DIR` (rooté dans le dépôt, sinon le travail reprend
     au mauvais endroit). Omettre si = dépôt courant.
   - **prompt** (self-contained, chemins ABSOLUS car le chip tourne ailleurs) :
     « Reprends « <titre> » → charge le contexte :
     `python "<ABS>/.claude-sessions/.. → read_claude_session.py" "<ABS>\.claude-sessions" "<id8>"`
     → résume en 3 lignes → reprends le fil → attends mes instructions ».
3. L'utilisateur clique → session relancée avec tout son contexte.

**Réinjection native (option, pour `claude --resume` au terminal)** — remet les `.jsonl` dans
`~/.claude/projects` avec remap auto du username (Administrateur ↔ Utilisateur) :

```bash
python "$SKILL/import_claude_sessions.py" "$REPO_DIR/.claude-sessions"            # remap auto vers CE PC
python "$SKILL/import_claude_sessions.py" "$REPO_DIR/.claude-sessions" --dry-run  # aperçu sans rien écrire
# puis :  cd "$REPO_DIR" ; claude --resume <id>
```

> L'outil de sessions de Claude Desktop (`list_sessions`, `send_message`, chips) fait DEUX choses qui complètent ce skill : (1) **démarrer des sessions
> FRAÎCHES** par dossier `CLAUDE.md`, (2) **PARLER à une session VIVANTE** (`send_message`, toujours
> confirmé) au lieu de dupliquer. **Réflexe REVIVE : AVANT de spawn un chip ici, demande à `list_sessions`
> si une session vivante couvre déjà ce sujet** (`list_sessions`) → si oui, on lui PARLE plutôt qu'un
> chip. On ne crée du neuf que pour du vraiment nouveau. Renvoi de balle export ↔ sessions (2026-06-22).

### 🔒 Garde-fous

- ⚠️ **Dépôts PRIVÉS uniquement.** Un `.jsonl` de session peut contenir des bouts sensibles (tokens,
  chemins, contenu). Vérifier que le remote est privé avant le push. Pousser un secret = publier
  (CLAUDE.md global global : « envoyer à un service externe = publier »).
- **Petits dépôts / peu de sessions — MESURER avant de pousser.** Une session **computer-use**
  (screenshots base64) pèse facilement **50 MB+ à elle seule**, et git garde **chaque version** à chaque
  re-sync = bloat permanent du dépôt. Le scoping **par niveau** (`--exact`) limite déjà beaucoup. Avant
  push, vérifier : `du -sh <niveau>/.claude-sessions` + `find <niveau>/.claude-sessions -type f -size +50M`.
  Bundle lourd (dizaines de Mo, ou un fichier > 50 MB) → préférer le `.zip` hors-git de `/claude-sessions-migration` § ②.
- **Idempotent** : re-export écrase proprement le bundle ; import skippe les sessions déjà présentes
  (sauf `--force`). Session sans `cwd` lisible → ignorée, jamais déposée au hasard.
- **Aucun token, aucun réseau** hors git : pur fichiers locaux + `git push/pull`.

> 🧪 **À valider live** : le scoping **par niveau** (`--exact`) est **prouvé** sur données réelles
> (2026-06-22 : racine antigravity → 17 sessions · `vente-marketing/` → 21 · zéro fuite de sous-dossier).
> Le round-trip des 3 scripts est **prouvé** (export → list Mode B → import dry-run, 2026-06-21). Reste à
> confirmer sur un **2ᵉ PC / autre compte réel** : EXPORT+push depuis PC1 → `git pull` + REVIVE (chips
> Mode B) depuis PC2 reprend bien le fil. Tant que pas fait → « posé, à confirmer », pas « terminé ».


### Sources canoniques (routing)

- Scripts (vendorés) : `scripts/export_claude_sessions.py` · `scripts/import_claude_sessions.py` · `scripts/read_claude_session.py` (les trois vivent dans `scripts/` de cette compétence)
- Cousins (transport `.zip` local) : `/claude-sessions-migration` § ② + `/claude-sessions-migration` § ①
- Relance par dossier (sessions FRAÎCHES) **et réutilisation d'une session VIVANTE** (`send_message`, anti-doublon) : les outils de sessions de Claude Desktop (`list_sessions`, `send_message`) — on relit le vivant avant de créer.
- Rooter les chips dans le bon dépôt · prompt self-contained
