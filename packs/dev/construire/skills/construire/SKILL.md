---
name: construire
description: >-
  Quand on a une spécification et une architecture écrites et qu'on veut les construire proprement → afficher
  l'état calculé depuis le dossier `construction/` du projet, puis dérouler les quatre étapes dans l'ordre :
  découper en tâches, construire chacune test d'abord, relire entre deux tâches, prouver avant de dire fini.
  Chaque étape va à la meilleure compétence publique ; seul le découpage en lots et en histoires se fait à la
  main. Se lance par `/construire:construire`. Déclencheurs : « construis ça à partir du plan », « découpe en
  tâches et développe », « implémente cette spécification, test d'abord », « code-le tâche par tâche », « où en
  est la construction ? ». Pas pour ajouter une fonctionnalité à une app existante ni corriger un défaut
  (`/faire-evoluer-une-app:faire-evoluer-une-app`). Pas pour relire le diff entier, sécuriser ou parcourir l'app
  (`/tester-et-securiser:tester-et-securiser`).
---

# Construire, tâche par tâche, test d'abord

## Ce que ça résout

Construire demande quatre gestes dans l'ordre, et la tentation est de les sauter : coder d'un trait sans plan,
écrire le test après le code, relire tout à la fin, dire « ça marche » sans avoir lancé la commande. Sans porte
d'entrée, chaque session de travail code à sa manière. Ici : l'ordre, l'état, la boucle choisie et ses interdits.

**Résultat attendu** : un plan de tâches, chaque tâche faite test d'abord et cochée seulement si son test passe,
chaque lot relu, une preuve lancée avant toute annonce ; des fichiers dans `construction/` qui disent à tout
moment où on en est.

**Les mots utilisés ici**
- **Test d'abord** : on écrit le test, on le voit échouer, puis on écrit le code minimal qui le fait passer.
- **Un sous-agent** est un assistant que Claude lance pour une seule tâche, avec son propre contexte.
- **Un lot** est un petit groupe de tâches qu'on relit ensemble.
- **Le diff** est l'ensemble des changements de code depuis le point de départ.

## Stratégie

1. **Une seule famille de compétences pour la boucle.** De la découpe à la preuve, tout vient de la même famille
   (Superpowers) : deux méthodes de construction pour le même plan finissent par diverger. On ne mélange pas deux
   méthodes sur un même plan.
2. **L'état d'abord, toujours calculé** depuis le dossier `construction/`, jamais recopié.
3. **L'ordre protège la décision** : pas de code sans tâche, pas de tâche cochée sans un test qui passe, pas
   d'annonce sans la sortie de la vérification lue. Un code écrit avant son test est jeté.
4. **Branches et copies de travail : un choix à poser.** Certaines compétences de la boucle proposent de créer une
   branche Git ou une copie de travail du dépôt (un « git worktree »). Ce workflow ne l'impose pas : on demande à la
   personne ce qu'elle préfère, une fois, au début, et on s'y tient. La fin de la boucle est la preuve de l'étape 4.
5. **Une seule validation.** Appelé par un autre workflow, celui-ci reprend sa validation (le cadrage, la
   fonctionnalité écrite, le défaut prouvé). Lancé seul, le plan de tâches de l'étape 1 est la seule validation ;
   ensuite tout se déroule. Restent à la personne : un goût produit non tranché, ses machines et ses comptes,
   l'irréversible.
6. **Chaque passage laisse une trace** : l'état et ce qu'il a appris sont notés au journal, et une correction
   qui se répète devient une règle ou un test.

<!-- prerequis:debut -->
## Prérequis

Ce workflow s'appuie sur des compétences publiques, installées à part. Aucune n'est indispensable : si l'une manque, le workflow le dit et fait l'étape à la main. Faire l'étape à la main veut dire suivre sa règle de choix, écrire ce qu'elle doit rendre (dans le fichier de l'étape, ou dans la réponse quand le workflow n'a pas de dossier) et dire ce qui reste à la charge de la personne.

```text
/plugin marketplace add Gremelinn0/zerogravity-skills
/plugin marketplace add JuliusBrussee/caveman
/plugin marketplace add addyosmani/agent-skills
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin install agent-skills@addy-agent-skills
/plugin install caveman@caveman
/plugin install entretenir-son-systeme@zerogravity
/plugin install product-management@knowledge-work-plugins
/plugin install superpowers@claude-plugins-official
```

Les workflows cités ici sont dans le même dépôt (le dépôt s'ajoute une fois : `/plugin marketplace add Gremelinn0/zerogravity-skills`) :

```text
/plugin install creer-un-agent-ia@zerogravity
/plugin install creer-un-site-web@zerogravity
/plugin install creer-une-app@zerogravity
/plugin install faire-evoluer-une-app@zerogravity
/plugin install mettre-en-ligne@zerogravity
/plugin install tester-et-securiser@zerogravity
```
<!-- prerequis:fin -->

## Étapes

### 0. Le dossier, puis l'état (lecture seule)

**Le dossier.** Le workflow écrit dans `construction/`, à la racine du dépôt où le code s'écrit, et dans nul autre
dossier : appelé par un autre workflow (une app, une évolution), il écrit quand même dans le sien, et l'appelant note
dans son propre dossier le résultat et l'endroit où lire `construction/`. Dossier absent ou vide : il n'y a encore rien
de fait, l'état est « étape 1 » et le dossier se crée au premier passage. Si le dossier courant n'est pas le dépôt que
la tâche désigne, le dire en une ligne et demander où il vit : rien ne s'écrit avant.

**Les entrées.** La spécification et l'architecture, ou la fonctionnalité et la carte du code existant, ou le
défaut prouvé. Lancé seul sans spécification, le workflow n'en invente pas : il renvoie à
`/creer-une-app:creer-une-app` ou à `/faire-evoluer-une-app:faire-evoluer-une-app`, qui les écrivent.

**L'état**, calculé depuis le journal et les fichiers :

```text
Workflow        Construire (dossier : construction/)
Étapes          01 ✓  02 -  03 -  04 -
Tâches          7 au plan · 3 cochées · 0 en cours
Dernière décision  2026-11-06 · 03 · lot 1 relu (tâches 1 à 3)
Étape suivante  02 Construire chaque tâche, test d'abord (tâche 4)
```

- Le journal `construction/journal.md` a une ligne par décision :
  `AAAA-MM-JJ · NN · fait | sans objet | sautée | corrigée · <une phrase>`.
- Les fichiers : `construction/construction-plan.md` (étape 1, une case à cocher par tâche, c'est lui qui donne les
  compteurs de la ligne « Tâches »), `construction/construction-taches.md` (étape 2 : par tâche, le test, sa sortie en
  échec puis en succès, et l'enregistrement Git), `construction/construction-relectures.md` (étape 3 : une section par
  lot relu, ses retours et ce qu'on en a fait), `construction/construction-verification.md` (étape 4 : la commande
  lancée et sa sortie).
- Pour chaque étape, la dernière ligne du journal qui la nomme fait foi. `✓` : cette ligne dit `fait` ou `corrigée`
  et le fichier de l'étape existe. `s.o.` : elle dit `sans objet` ou `sautée` (l'étape n'est plus proposée). `-` :
  aucune ligne, ou le fichier manque. `corrigée` : l'étape est refaite après une correction, elle reste `✓` et la
  ligne dit ce qui a changé. `sautée` : la personne a choisi de passer, la ligne dit pourquoi.
- **Les étapes 2 et 3 alternent par lot** (quelques tâches, puis leur relecture) : elles ne sont `✓` qu'à la fin
  du plan. L'étape 2 est `✓` quand toutes les cases du plan sont cochées et que le dernier lot est au journal ; l'étape 3
  est `✓` quand ce dernier lot est relu. Tant qu'une case reste vide, la dernière ligne du journal qui nomme 02 ou 03
  décide : `02` (lot construit, pas relu) donne l'étape suivante 03 ; `03` ou aucune donne 02 pour la tâche suivante.
  C'est la seule exception à la règle ci-dessous.
- L'étape suivante est la première étape `-`, dans l'ordre (sauf l'exception de l'alternance). Si aucune ne l'est, le
  workflow est terminé. Pour un nouveau passage (une autre évolution, une autre fonctionnalité), on range l'ancien : on
  déplace les fichiers de l'étape et `journal.md` dans `construction/archives/AAAA-MM-JJ/`, et on repart à l'étape 1.

**Une question n'est pas un ordre.** « Où en est la construction ? » : on donne l'état et la prochaine action,
puis on s'arrête. La commande de lancement, « continue » ou « déroule » : on enchaîne.

**Une demande au milieu du chemin** (« code la tâche 4 ») : l'étape 2 exige un plan. Sans `construction/construction-plan.md`,
on découpe d'abord. Jamais une ligne de code avant sa tâche.

### 1. Lancer l'étape suivante

Lire l'étape dans le tableau ci-dessous, appliquer sa règle de choix, invoquer la compétence retenue, écrire
dans le fichier de l'étape sa sortie, inscrire `fait` au journal, puis passer à la suivante sans redemander.

- **Appelé pour une correction**, le plan tient en une tâche : le test qui reproduit le défaut avec les mots de
  la personne, qui doit échouer pour la bonne raison, puis la correction. La relecture de l'étape 3 porte sur
  cette seule tâche.
- **La relecture du diff entier n'est pas ici** : elle appartient à `/tester-et-securiser:tester-et-securiser`.
  Ici on prouve la tâche, pas l'app.
- **À la fin de l'étape 4**, le workflow rend à celui qui l'a appelé la dernière ligne de son journal ; c'est
  l'appelant qui inscrit sa propre étape au sien.

<!-- etapes:debut -->
| # | Étape | Compétences | Règle de choix |
|---|---|---|---|
| 1 | Découper en tâches | `superpowers:writing-plans` · Planifier un sprint : `product-management:sprint-planning` | writing-plans sur la spécification et l'architecture déjà écrites. Le plan s'écrit dans le dossier du projet, dans `construction/construction-plan.md`, une case à cocher par tâche. Une tâche qui ne se vérifie pas seule se redécoupe. |
| 2 | Construire chaque tâche, test d'abord | `superpowers:subagent-driven-development` · `superpowers:test-driven-development` · `superpowers:executing-plans` · Coder une tâche : `agent-skills:source-driven-development` · Construire une tâche en restant dans le cadre : `caveman:lean-build` · Lancer plusieurs tâches en parallèle : `superpowers:dispatching-parallel-agents` | Une tâche à la fois, par un sous-agent, test d'abord ; elle n'est cochée que si son test passe. executing-plans seulement là où les sous-agents manquent. Jamais d'arbre de travail ni de branche nouvelle. Si une compétence propose de créer une branche ou une copie de travail du dépôt, on suit le choix posé à la personne au début. |
| 3 | Relire entre deux tâches | `superpowers:requesting-code-review` · `superpowers:receiving-code-review` · Simplifier le code sans changer son comportement : `agent-skills:code-simplification` | Une relecture par lot, pendant la construction, avant la tâche suivante. La relecture du diff entier se fait ensuite, dans la brique Tester et sécuriser. |
| 4 | Prouver avant de dire fini | `superpowers:verification-before-completion` · Vérifier avant de dire fini : `agent-skills:constraint-driven-development` · Prouver que c'est fini : `caveman:verify-and-stop` | Rien n'est annoncé fait sans la sortie de sa vérification ; un échec s'écrit tel quel, avec la sortie. |
<!-- etapes:fin -->

### 2. Clore un passage

À la fin de chaque séance : l'état (fait, reste, prochaine action) au journal. Une compétence qui a déçu à une
étape se note aussi, pour rouvrir le choix. Pour ranger ce qu'on a appris dans des compétences Claude Code,
`entretenir-son-systeme:capitaliser` est l'option publique ; sans elle, on note la leçon au journal.

## Frontières

| Demande | Va à |
|---|---|
| Créer une app, un SaaS, une plateforme de zéro | `/creer-une-app:creer-une-app` |
| Ajouter une fonctionnalité à une app existante, corriger un défaut | `/faire-evoluer-une-app:faire-evoluer-une-app` |
| Relire le diff, vérifier la sécurité, parcourir l'app | `/tester-et-securiser:tester-et-securiser` |
| Déployer | `/mettre-en-ligne:mettre-en-ligne` |
| Créer un agent ou un système IA | `/creer-un-agent-ia:creer-un-agent-ia` |
| Créer le site web | `/creer-un-site-web:creer-un-site-web` |

## Ce qui manque

- Le découpage en lots et en histoires n'a pas de compétence publique : il se fait à la main, avant le plan de
  tâches. Méthode courte : lister ce que la personne doit pouvoir faire à la fin (les histoires), les ranger dans
  l'ordre où chacune sert la suivante, puis regrouper en lots de trois à cinq tâches qu'on peut relire d'un coup.
- Si votre environnement ne lance pas de sous-agents, la boucle se joue dans une seule conversation, par lots avec
  points de contrôle (la compétence `superpowers:executing-plans` est faite pour ce cas).
