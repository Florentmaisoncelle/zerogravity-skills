---
name: tester-et-securiser
description: >-
  Quand on veut savoir si son code peut sortir (« teste mon app », « relis mon code », « vérifie la sécurité avant de
  mettre en ligne », « est-ce que je peux mettre ça en ligne ? ») → afficher l'état calculé depuis le dossier `tests/`,
  puis dérouler les trois étapes dans l'ordre (relire le code, vérifier la sécurité, lancer l'app et la parcourir)
  jusqu'à un verdict écrit : on met en ligne, ou pas. Annonce le coût du scan de sécurité en profondeur avant de le
  lancer. Dit franchement ce qui se fait à la main : lancer l'app, la conformité aux règles sur les données
  personnelles. Se lance par `/tester-et-securiser:tester-et-securiser`. Déclencheurs : « tester l'app », « relire le
  code », « revue de code », « audit de sécurité », « tester avant de déployer », « verdict de mise en ligne ». Pas pour
  corriger un défaut déjà connu (/faire-evoluer-une-app:faire-evoluer-une-app). Pas pour écrire le code
  (/construire:construire). Pas pour déployer (/mettre-en-ligne:mettre-en-ligne).
---

# Tester et sécuriser : de « ça marche chez moi » au verdict, on met en ligne ou pas

## Ce que ce workflow résout

Tester demande trois gestes dans l'ordre, et les compétences installées se recouvrent : plusieurs relisent du code,
plusieurs parlent de sécurité, et aucune ne dit quand s'arrêter. Sans porte d'entrée, une session relit le code,
déclare « c'est bon » sans avoir lancé l'app, ou lance un scan de sécurité coûteux sans prévenir. Ici : l'ordre,
l'état, le choix tranché, et un verdict écrit qui décide de la suite.

**Résultat attendu** : le diff entier relu (le diff est l'ensemble des changements de code), les failles vérifiées
une à une, l'app vue en train de marcher sur ses parcours clés, et une première ligne de
`tests/tests-parcours.md` qui dit « on met en ligne » ou « on ne met pas en ligne ».

## Stratégie

1. **Une seule relecture et une seule couche de sécurité par niveau.** Pour relire le diff entier, une compétence
   par défaut (`code-review:code-review`) ; les deux autres (`caveman:caveman-review`, `engineering:code-review`) la
   remplacent quand elle n'est pas installée, jamais en plus : relire deux fois le même diff n'apporte rien de démontré.
   Pour la sécurité, chaque niveau a la sienne : le lot, la profondeur avant la première mise en ligne, une API, les
   dépendances.
2. **L'état d'abord, toujours calculé** depuis le journal et les fichiers du dossier `tests/`, jamais recopié.
3. **L'ordre protège la décision** : pas de verdict sans avoir lancé l'app, pas de première mise en ligne sans le scan
   de sécurité en profondeur. Chaque défaut confirmé se corrige avant l'étape suivante, test d'abord (la boucle de
   `/construire:construire`).
4. **Un verdict « on ne met pas en ligne » arrête le workflow parent.** Il s'écrit en première ligne de
   `tests/tests-parcours.md` avec sa raison en une phrase ; le workflow qui a appelé celui-ci ne passe pas à sa mise en
   ligne tant que le verdict n'est pas « on met en ligne ». Après correction, l'étape refaite s'inscrit `corrigée` au
   journal et le verdict se rend de nouveau.
5. **Le scan en profondeur annonce son coût.** Le coût de `claude-security:claude-security` en jetons n'est pas mesuré ici :
   avant de lancer le scan, on dit à la personne qu'il peut être long et coûteux, jamais après.
6. **Pas de seconde validation.** Appelé par un workflow, celui-ci reprend sa validation ; lancé seul, il déroule sans
   revalider. Restent à la personne : la décision de mettre en ligne quand le verdict est favorable mais risqué, et la
   conformité (étape 2).
7. **Chaque passage se ferme au journal** : une correction devient une règle, un test ou une ligne du workflow.

**Comptes et clés que certaines compétences demandent** (rien de tout cela n'est nécessaire pour les autres) :
- `42crunch-api-security-testing` : le dépôt dit que le plugin lance des scans contre des API en marche ; les comptes et
  jetons qu'il demande ne sont pas précisés sur la page du dépôt (https://github.com/42Crunch-AI/claude-plugins, lue le
  06/11/2026) : à vérifier dans son README avant de compter dessus ;
- ai-plugins (celui d'Endor Labs) : son étape d'installation vérifie l'authentification, l'espace de travail et l'outil
  `endorctl` (https://github.com/endorlabs/ai-plugins, lu le 06/11/2026) ; le détail des comptes est à vérifier dans son
  README ;
- `claude-security:claude-security` : coût en jetons non mesuré (voir le point 5).
Sans ces prérequis, on passe à la compétence suivante du niveau ou on fait l'étape à la main.

`playwright-cli` seul demande Node.js 18 ou plus (https://github.com/microsoft/playwright-cli, lu le 06/11/2026) ; la commande `npx skills add` qui l'installe demande Node.js 22.20 ou plus (voir les prérequis).

<!-- prerequis:debut -->
## Prérequis

Ce workflow s'appuie sur des compétences publiques, installées à part. Aucune n'est indispensable : si l'une manque, le workflow le dit et fait l'étape à la main. Faire l'étape à la main veut dire suivre sa règle de choix, écrire ce qu'elle doit rendre (dans le fichier de l'étape, ou dans la réponse quand le workflow n'a pas de dossier) et dire ce qui reste à la charge de la personne.

```text
/plugin marketplace add Florentmaisoncelle/zerogravity-skills
/plugin marketplace add JuliusBrussee/caveman
/plugin marketplace add addyosmani/agent-skills
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin install 42crunch-api-security-testing@claude-plugins-official
/plugin install agent-skills@addy-agent-skills
/plugin install ai-plugins@claude-plugins-official
/plugin install caveman@caveman
/plugin install entretenir-son-systeme@zerogravity
/plugin install claude-security@claude-plugins-official
/plugin install code-review@claude-plugins-official
/plugin install engineering@knowledge-work-plugins
npx skills add bmad-code-org/BMAD-METHOD --skill bmad-qa-generate-e2e-tests -a claude-code
npx skills add microsoft/playwright-cli --skill playwright-cli -a claude-code
```

La commande `npx skills add` (CLI Vercel `skills`) demande Node.js 22.20 ou plus (vérifié le 06/11/2026, https://github.com/vercel-labs/skills). Claude Code installé avec l'installeur natif n'en a pas besoin.

Les workflows cités ici sont dans le même dépôt (le dépôt s'ajoute une fois : `/plugin marketplace add Florentmaisoncelle/zerogravity-skills`) :

```text
/plugin install construire@zerogravity
/plugin install creer-un-site-web@zerogravity
/plugin install creer-une-app@zerogravity
/plugin install faire-evoluer-une-app@zerogravity
/plugin install mettre-en-ligne@zerogravity
```
<!-- prerequis:fin -->

## Étapes

### 0. Le dossier, puis l'état (lecture seule)

**Le dossier.** Le workflow écrit dans `tests/`, à la racine du dépôt testé, et dans nul autre dossier : appelé par un
autre workflow (une app, une évolution), il écrit quand même dans le sien, et l'appelant note dans son propre
dossier le verdict et l'endroit où lire `tests/`. Dossier absent ou vide : il n'y a encore rien de fait, l'état est
« étape 1 » et le dossier se crée au premier passage. Si le dossier courant n'est pas le dépôt que la tâche désigne, le
dire en une ligne et demander où il vit : rien ne s'écrit avant.

**L'état**, calculé depuis le journal et les fichiers :

```text
Workflow        Tester et sécuriser (dossier : tests/)
Étapes          01 ✓  02 ✓  03 -
Verdict         pas encore rendu
Dernière décision  2026-11-06 · 02 · fait · aucune faille confirmée
Étape suivante  03 Lancer l'app et la parcourir → lancer l'app à la main, puis agent-skills:browser-testing-with-devtools
```

- Le journal `tests/journal.md` a une ligne par décision :
  `AAAA-MM-JJ · NN · fait | en attente | sans objet | sautée | corrigée · <une phrase>`.
- Les fichiers : `tests/tests-relecture.md` (étape 1), `tests/tests-securite.md` (étape 2), `tests/tests-parcours.md`
  (étape 3, avec le verdict en première ligne).
- Pour chaque étape, la dernière ligne du journal qui la nomme fait foi. `✓` : cette ligne dit `fait` ou `corrigée`
  et le fichier de l'étape existe. `s.o.` : elle dit `sans objet` ou `sautée` (l'étape n'est plus proposée). `-` :
  aucune ligne, ou le fichier manque.
- `Verdict` se lit sur la première ligne de `tests/tests-parcours.md` : `Verdict : on met en ligne` ou
  `Verdict : on ne met pas en ligne, <raison>` ; « pas encore rendu » tant que l'étape 3 n'est pas faite.
- `en attente` : l'étape est préparée, mais elle dépend d'un geste ou d'une réponse qui arrive hors de la conversation. La ligne du journal dit ce qu'on attend et de qui. L'état l'affiche `att.` avec ce texte : l'étape n'est pas `✓`, parce que préparé n'est pas fait. Le workflow s'arrête là et le dit ; il n'invente jamais la suite (ni réponse, ni résultat, ni geste qu'on ne lui a pas confirmé). Quand la personne apporte ce qui est arrivé, la ligne `fait` suit. Ici : le lancement de l'app et son parcours, joués par la personne ou par un outil de navigateur branché (étape 3).
- L'étape suivante est la première étape `-` ou `att.`, dans l'ordre (devant une étape `att.`, on demande d'abord où en est l'attente). Si aucune ne l'est, le workflow est terminé **si le verdict
  est « on met en ligne »**. Pour un nouveau passage (une autre évolution, une autre fonctionnalité), on range l'ancien :
  on déplace les fichiers de l'étape et `journal.md` dans `tests/archives/AAAA-MM-JJ/`, et on repart à l'étape 1.
- **Verdict négatif, trois étapes `✓`** : le workflow n'est pas terminé. L'étape suivante est « corriger, puis refaire
  l'étape que la raison du verdict désigne, puis l'étape 3 pour rendre un nouveau verdict ». Chaque étape refaite
  s'inscrit `corrigée` au journal (elle reste `✓`, et la ligne dit ce qui a changé). Tant que la première ligne de
  `tests/tests-parcours.md` dit « on ne met pas en ligne », l'état reste celui-ci.

```text
Workflow        Tester et sécuriser (dossier : tests/)
Étapes          01 ✓  02 ✓  03 ✓
Verdict         on ne met pas en ligne, un mot de passe apparaît en clair dans un journal de l'app
Dernière décision  2026-11-06 · 03 · fait · verdict négatif
Étape suivante  corriger, puis refaire 02 Vérifier la sécurité et 03 (nouveau verdict)
```

**Une question n'est pas un ordre.** « Où en sont les tests ? » → l'état, le verdict s'il existe et la prochaine
action, puis on s'arrête. La commande `/tester-et-securiser:tester-et-securiser`, « continue » ou « déroule » → on
enchaîne jusqu'à la première étape en attente, puis on s'arrête et on le dit.

**Une demande au milieu du chemin** (« vérifie juste la sécurité ») : on fait l'étape demandée, on l'inscrit au
journal, et on dit que le verdict n'est pas rendu tant que les autres étapes ne sont pas faites.

### 1. Lancer l'étape suivante

Lire l'étape dans le tableau ci-dessous, appliquer sa **règle de choix**, invoquer la compétence retenue, écrire
dans le fichier de l'étape sa sortie, inscrire `fait` au journal (ou `en attente`, voir plus haut), puis passer à la suivante sans redemander. Quatre
précisions :

- **Sur le bon périmètre** : le diff entier d'une fonctionnalité ou d'une app neuve ; seulement le diff de la
  correction et le parcours qui était cassé quand `/faire-evoluer-une-app:faire-evoluer-une-app` appelle ce workflow
  pour un défaut.
- **Le scan en profondeur** ne se lance pas à chaque passage : avant la première mise en ligne, puis à chaque
  changement de la connexion, du paiement ou des données de personnes. Une fonctionnalité qui n'y touche pas se
  contente de la vérification du lot.
- **La conformité est un manque déclaré** : aucune compétence ne la couvre. Elle dépend du pays et du public. Pour
  des données de personnes dans l'Union européenne, le RGPD s'applique aux traitements d'un établissement dans l'Union
  et aux acteurs hors Union qui visent des personnes dans l'Union (CNIL, https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre1#Article3,
  vérifié le 06/11/2026) ; ailleurs, à vérifier. À l'étape 2, on relit ce que le cadrage a décidé et on pose six
  questions à la main : quelles données de personnes l'app garde, où elles sont stockées, qui y accède, combien de
  temps elles sont conservées, comment les personnes sont informées et comment elles peuvent demander l'accès ou
  l'effacement. Ce qui n'est pas couvert se dit, et reste à la personne qui porte l'app, avec son juriste ou son
  délégué à la protection des données.
- **À la fin de l'étape 3**, ce workflow rend à l'appelant son verdict et la dernière ligne de son journal ; c'est
  l'appelant qui inscrit sa propre étape au sien, et seulement si le verdict est « on met en ligne ».

<!-- etapes:debut -->
| # | Étape | Compétences | Règle de choix |
|---|---|---|---|
| 1 | Relire le code | `code-review:code-review` · Relire le code : `caveman:caveman-review` ; `engineering:code-review` | Sur le diff entier, une fois la construction finie, avec une seule compétence : la compétence par défaut, ou à sa place l'une des deux autres si elle n'est pas installée. Chaque défaut confirmé se corrige avant l'étape suivante. |
| 2 | Vérifier la sécurité | `security-review` · `claude-security:claude-security` · Tester la sécurité d'une API : `42crunch-api-security-testing:42crunch-api-security-testing` ; `42crunch-api-security-testing:42crunch-audit` ; `42crunch-api-security-testing:42crunch-scan` · Surveiller les failles des dépendances : `ai-plugins:ai-sast-remediation` ; `ai-plugins:dependency-reviewer` ; `ai-plugins:sca-remediation` ; `ai-plugins:vulnerability-explainer` | security-review sur chaque lot ; claude-security en profondeur avant la première mise en ligne, puis à chaque changement de la connexion, du paiement ou des données d'un client. Les comptes et jetons que demandent les compétences 42Crunch et ai-plugins sont à vérifier dans leur README avant de compter dessus (voir le SKILL.md). Manque : la conformité (RGPD, accès aux boîtes mail des clients) : aucune compétence ; la question se pose au cadrage et se vérifie ici. la conformité aux règles sur les données personnelles (par exemple le RGPD pour des personnes dans l'Union européenne) : aucune compétence ; la question se pose au cadrage et se vérifie ici avec six questions à la main. |
| 3 | Lancer l'app et la parcourir | `playwright-cli` · Écrire les tests de bout en bout : `bmad-qa-generate-e2e-tests` · Parcourir l'app dans un vrai navigateur : `agent-skills:browser-testing-with-devtools` | On lance l'app soi-même (aucune compétence publique : à la main) ; agent-skills:browser-testing-with-devtools pour la parcourir dans un vrai navigateur et rendre le verdict avant chaque mise en ligne ; playwright-cli quand un parcours doit être rejoué à chaque version. Un verdict « on ne met pas en ligne » arrête le workflow, et il se rend de nouveau après correction. |
<!-- etapes:fin -->

### 2. Clore un passage

À la fin de chaque séance, on écrit l'état au journal : ce qui est fait, ce qui reste, la prochaine action, le verdict.
Si `entretenir-son-systeme:capitaliser` est installée (elle range ce qu'on a appris dans des compétences Claude
Code), elle s'en charge. Sinon, on note les décisions dans le journal. Une compétence qui a déçu à une étape se
signale au journal, pour rouvrir le choix de cette étape.

## Choix de méthode

- Trois étapes, de la relecture au verdict. Le verdict est un livrable écrit, pas une impression : sans lui, le
  workflow parent ne met rien en ligne.
- **Pas de stratégie de test générale** : le test d'abord de `/construire:construire` et le verdict du parcours dans
  le navigateur la remplacent.
- **Les tests de bout en bout se rejouent avec `playwright-cli`, pas avec un serveur MCP** : d'après le dépôt de Microsoft
  (https://github.com/microsoft/playwright-cli, vérifié le 06/11/2026), pour un agent de code la ligne de commande consomme
  moins de jetons que les schémas d'outils et les arbres d'accessibilité d'un serveur MCP. Le même dépôt réserve le serveur
  MCP aux boucles qui ont besoin d'un état persistant.

## Ce qui manque

- **Lancer l'app** : aucune compétence publique, on le fait à la main (démarrer l'app et la voir marcher avant tout
  verdict).
- **La conformité** (données personnelles) : aucune compétence installée ne la couvre ; les six questions de la
  section « Lancer l'étape suivante » la préparent, sans jamais la simuler.

## Frontières

| Demande | Va à |
|---|---|
| Corriger un défaut déjà connu, ajouter une fonctionnalité à une app existante | `/faire-evoluer-une-app:faire-evoluer-une-app` |
| Écrire ou construire le code | `/construire:construire` |
| Déployer, vérifier en ligne | `/mettre-en-ligne:mettre-en-ligne` |
| Mesurer la vitesse, l'accessibilité ou le référencement d'un site | `/creer-un-site-web:creer-un-site-web` |
| Créer une app de zéro | `/creer-une-app:creer-une-app` |
