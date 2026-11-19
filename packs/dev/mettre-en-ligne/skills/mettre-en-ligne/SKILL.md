---
name: mettre-en-ligne
description: >-
  Quand on veut sortir une version en ligne et en garder la main → afficher l'état calculé depuis le dossier
  `mise-en-ligne/`, puis dérouler les trois étapes dans l'ordre : préparer la sortie avec son plan de retour arrière,
  déployer sur le projet existant, vérifier en ligne à l'adresse officielle, sur ordinateur et sur téléphone. Le
  déploiement prévu est celui de Vercel ; un autre hébergeur est un manque, dit franchement. Se lance par
  `/mettre-en-ligne:mettre-en-ligne`. Déclencheurs : « mets en ligne », « déploie cette version », « passe en
  production », « prépare la sortie avec un retour arrière », « où en est la mise en ligne ? ». Pas pour tester
  ou sécuriser avant (`/tester-et-securiser:tester-et-securiser`). Pas pour un défaut en production
  (`/faire-evoluer-une-app:faire-evoluer-une-app`).
---

# Mettre en ligne et garder la main

## Ce que ça résout

Mettre en ligne demande trois gestes dans l'ordre, et le plus dangereux est de ne faire que le deuxième :
déployer sans plan de retour, créer au passage un projet ou un alias que personne n'a demandé, ou annoncer
l'adresse technique du déploiement. Sans point d'entrée, chaque session déploie à sa manière. Ici : l'ordre,
l'état, la voie du dépôt respectée, et la vérification faite sur ce que le public verra.

**Résultat attendu** : une sortie préparée avec son plan de retour arrière écrit d'avance, la version en ligne
sur le projet existant, l'adresse officielle vérifiée sur ordinateur et sur téléphone ; un dossier `mise-en-ligne/`
qui dit à tout moment où on en est.

## Stratégie

1. **Une compétence, un seul endroit.** La préparation, le déploiement et la vérification ont chacun leur
   compétence. Pour la vérification en ligne, on rejoue le parcours principal déjà éprouvé par
   `/tester-et-securiser:tester-et-securiser` sur la version en ligne, au lieu d'en écrire un autre.
2. **L'état d'abord, toujours calculé** depuis les fichiers du dossier, jamais recopié.
3. **L'ordre protège la décision.** Pas de déploiement sans plan de retour écrit. Pas de mise en ligne sans le
   verdict « on met en ligne » de `/tester-et-securiser:tester-et-securiser` : sans verdict, ou avec « on ne met
   pas en ligne », on s'arrête et on le dit. Passer outre est un ordre de la personne, inscrit au
   journal sur la ligne de l'étape 2 (« déployé sans verdict, ordre de la personne »).
4. **Jamais un nouveau projet Vercel ni un nouvel alias sans demande.** Un déploiement se rattache au projet
   existant. Un alias neuf est une autre origine pour la connexion des utilisateurs : c'est un geste demandé, pas
   un effet de bord.
5. **La voie du dépôt déploie.** Quand le dépôt a déjà sa propre voie de mise en ligne (tâche planifiée,
   intégration continue), c'est elle qui déploie. On ne la double pas par un déploiement direct.
6. **Jamais la voie de secours de `deploy-to-vercel`.** Sans identifiants Vercel, cette compétence sait lancer
   `vercel deploy --temporary` : cela déploie vers un projet temporaire anonyme chez Vercel, qu'on peut réclamer
   ensuite par un lien (à ne pas partager) ; cela ne marche ni en intégration continue ni dans un dossier déjà lié à un
   projet (https://github.com/vercel-labs/agent-skills, vérifié le 06/11/2026). Ici elle est refusée par défaut : le
   projet sortirait de tous les comptes de la personne. Sans connexion Vercel valable, on essaie la session déjà
   ouverte, sinon on s'arrête et on dit laquelle manque.
7. **L'adresse officielle, jamais l'adresse technique du déploiement.** On donne le lien cliquable et son nom
   (« le site », « le brouillon »), pas l'adresse à suffixe changeant.
8. **Si l'app est faite pour un tiers** (un client, un employeur), c'est lui qui décide de l'ouvrir au public : on
   prépare, on déploie en brouillon, on vérifie, et on lui remet la main.
9. **Chaque passage laisse une trace** : l'état et ce qu'il a appris sont notés au journal, et une correction qui
   se répète devient une règle ou un test.

<!-- prerequis:debut -->
## Prérequis

Ce workflow s'appuie sur des compétences publiques, installées à part. Aucune n'est indispensable : si l'une manque, le workflow le dit et fait l'étape à la main. Faire l'étape à la main veut dire suivre sa règle de choix, écrire ce qu'elle doit rendre (dans le fichier de l'étape, ou dans la réponse quand le workflow n'a pas de dossier) et dire ce qui reste à la charge de la personne.

```text
/plugin marketplace add addyosmani/agent-skills
/plugin marketplace add addyosmani/web-quality-skills
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin install agent-skills@addy-agent-skills
/plugin install engineering@knowledge-work-plugins
/plugin install stripe@claude-plugins-official
/plugin install web-quality-skills@addy-web-quality-skills
npx skills add vercel-labs/agent-skills --skill deploy-to-vercel -a claude-code
```

La commande `npx skills add` (CLI Vercel `skills`) demande Node.js 22.20 ou plus (vérifié le 06/11/2026, https://github.com/vercel-labs/skills). Claude Code installé avec l'installeur natif n'en a pas besoin.

Les workflows cités ici sont dans le même dépôt (le dépôt s'ajoute une fois : `/plugin marketplace add Florentmaisoncelle/zerogravity-skills`) :

```text
/plugin install creer-une-app@zerogravity
/plugin install faire-evoluer-une-app@zerogravity
/plugin install tester-et-securiser@zerogravity
```
<!-- prerequis:fin -->

## Étapes

### 0. Le dossier, puis l'état (lecture seule)

**Le dossier.** Le workflow écrit dans `mise-en-ligne/`, à la racine du dépôt déployé, qu'il soit lancé seul ou appelé
par un autre workflow (`/creer-une-app:creer-une-app`, `/faire-evoluer-une-app:faire-evoluer-une-app`) : l'appelant
garde seulement une note qui renvoie vers ce dossier. Dossier absent ou vide : il n'y a encore rien de fait, l'état est
« étape 1 » et le dossier se crée au premier passage. Si le dossier courant n'est pas le dépôt que la tâche désigne, le
dire en une ligne et s'arrêter : rien ne se déploie avant.

**Le verdict des tests** se lit dans `tests/`, le dossier de `/tester-et-securiser:tester-et-securiser` : il est écrit
en première ligne du fichier de l'étape « parcours ». S'il manque, on le dit et on propose de lancer ce workflow d'abord.

**L'état**, calculé depuis le journal et les fichiers :

```text
Workflow        Mettre en ligne (dossier : mise-en-ligne/)
Étapes          01 ✓  02 -  03 -
Verdict des tests  on met en ligne (tests/, 2026-11-06)
Voie            <celle du dépôt : tâche planifiée, intégration continue, Vercel direct>
Dernière décision  2026-11-06 · 01 · plan de retour arrière écrit
Étape suivante  02 Déployer → deploy-to-vercel
```

- Le journal `mise-en-ligne/journal.md` a une ligne par décision :
  `AAAA-MM-JJ · NN · fait | en attente | sans objet | sautée | corrigée · <une phrase>`.
- Pour chaque étape, la dernière ligne du journal qui la nomme fait foi. `✓` : cette ligne dit `fait` ou `corrigée` et
  le fichier de l'étape existe. `s.o.` : elle dit `sans objet` ou `sautée` (l'étape n'est plus proposée). `-` : aucune
  ligne, ou le fichier manque.
- `corrigée` : l'étape est refaite après une correction ; elle reste ✓ et la ligne dit ce qui a changé. `sautée` : la
  personne a choisi de passer ; la ligne dit pourquoi.
- `en attente` : l'étape est préparée, mais elle dépend d'un geste ou d'une réponse qui arrive hors de la conversation. La ligne du journal dit ce qu'on attend et de qui. L'état l'affiche `att.` avec ce texte : l'étape n'est pas `✓`, parce que préparé n'est pas fait. Le workflow s'arrête là et le dit ; il n'invente jamais la suite (ni réponse, ni résultat, ni geste qu'on ne lui a pas confirmé). Quand la personne apporte ce qui est arrivé, la ligne `fait` suit. Ici : la demande explicite de la personne de passer en production (étape 2) et la période d'observation fixée à l'étape 1 (étape 3).
- L'étape suivante est la première étape `-` ou `att.`, dans l'ordre (devant une étape `att.`, on demande d'abord où en est l'attente). Si aucune ne l'est, la sortie est terminée, **si le verdict de `03-verification.md` est « en ligne, vérifié »**. Avec « retour arrière déclenché », la sortie n'est pas terminée : l'état dit « retour arrière fait, sortie à reprendre », le défaut rejoint `/faire-evoluer-une-app:faire-evoluer-une-app`, puis les étapes 2 et 3 sont refaites et inscrites `corrigée`. Pour une
  nouvelle sortie, on range l'ancienne : on déplace les fichiers de l'étape et `journal.md` dans
  `mise-en-ligne/archives/AAAA-MM-JJ/`, et on repart à l'étape 1.

Les fichiers sont dans `mise-en-ligne/` : `01-plan.md`, `02-deploiement.md`, `03-verification.md`.

**Une question n'est pas un ordre.** « Où en est la mise en ligne ? » : on donne l'état et la prochaine action,
puis on s'arrête. « Mets en ligne », « continue » ou « déroule » : on enchaîne jusqu'à la première étape en attente, puis on s'arrête et on le dit. La production se décide à la
demande explicite de la personne, le brouillon d'abord.

### 1. Lancer l'étape suivante

Lire l'étape dans le tableau ci-dessous, appliquer sa règle de choix, invoquer la compétence retenue, écrire dans
le fichier de l'étape sa sortie, inscrire `fait` au journal (ou `en attente`, voir plus haut), puis passer à la suivante sans redemander.

- **L'étape 2 s'ouvre par la voie du dépôt.** Chercher d'abord si le dépôt a la sienne (une tâche planifiée, une
  intégration continue, une règle écrite dans ses consignes). Si oui, c'est elle qui déploie : l'étape consiste à
  la déclencher et à lire son état. Sinon, le déploiement Vercel passe par le projet existant, en brouillon
  d'abord.
- **L'étape 3 est une vérification, pas un déploiement de plus.** Voir la méthode juste après le tableau. Un écart
  (l'adresse officielle ne montre pas ce que le brouillon montrait, une page casse sur téléphone, un seuil du plan est
  dépassé) déclenche le retour arrière écrit à l'étape 1. Le défaut rejoint ensuite
  `/faire-evoluer-une-app:faire-evoluer-une-app`.
- **À la fin de l'étape 3**, le workflow rend à celui qui l'a appelé l'adresse officielle et la dernière ligne de
  son journal ; c'est l'appelant qui inscrit sa propre étape au sien.

<!-- etapes:debut -->
| # | Étape | Compétences | Règle de choix |
|---|---|---|---|
| 1 | Préparer la sortie | `agent-skills:shipping-and-launch` | Le plan de retour arrière s'écrit avant de déployer, pas après la panne. Si l'app collecte des données personnelles, les mentions légales et la politique de confidentialité s'écrivent aussi avant la sortie, à la main. |
| 2 | Déployer | `deploy-to-vercel` · Automatiser la mise en ligne : `agent-skills:ci-cd-and-automation` · Ouvrir les services dont l'app a besoin : `stripe:stripe-projects` | Toujours le projet existant, jamais un nouveau sans qu'on le demande ; le brouillon d'abord. Jamais la voie de secours sans connexion de `deploy-to-vercel` (vercel deploy --temporary) : elle envoie le projet vers un projet temporaire anonyme chez Vercel, hors de tous les comptes de la personne. Quand le dépôt a déjà sa voie de mise en ligne (tâche planifiée, intégration continue), c'est elle qui déploie. Pour l'app d'un client, l'ouverture au public est son geste : si l'app est faite pour un tiers, c'est lui qui décide de l'ouvrir. |
| 3 | Vérifier en ligne | Lire la console et le réseau du site en ligne : `agent-skills:browser-testing-with-devtools` · Gérer un incident : `engineering:incident-response` · Auditer le site en ligne : `web-quality-skills:web-quality-audit` | L'adresse officielle, pas l'adresse technique du déploiement. Dans une fenêtre privée, on rejoue le parcours principal sur ordinateur puis sur téléphone, on lit la console et le réseau, on contrôle ce qui ne se voit pas en développement (adresses de retour de la connexion, variables de production, e-mails) et les seuils du plan. Un écart déclenche le retour arrière de l'étape 1. Manque : aucune compétence ne parcourt le site en ligne à votre place : la console et le réseau se lisent avec agent-skills:browser-testing-with-devtools si le serveur MCP Chrome DevTools est branché, le reste se fait à la main (méthode dans le SKILL.md, section « Vérifier en ligne »). |
<!-- etapes:fin -->

### Vérifier en ligne : la méthode

Aucune compétence ne parcourt le site en ligne à votre place. La vérification se fait dans cet ordre et s'écrit dans
`03-verification.md`, un pas par ligne (ok ou écart, avec une capture pour un écart) :

1. **L'adresse.** Ouvrir l'adresse officielle dans une fenêtre privée (ni cache, ni session déjà ouverte) : le
   certificat est valide, aucun avertissement du navigateur, et on voit un détail qui a changé dans cette sortie, preuve
   que c'est la nouvelle version.
2. **Le parcours principal**, de bout en bout, sur ordinateur puis sur téléphone (de préférence un vrai téléphone sur
   réseau mobile) : s'inscrire ou se connecter, faire l'action qui compte le plus, payer en mode test s'il y a un
   paiement.
3. **La console et le réseau.** Ouvrir les outils du navigateur pendant le parcours : aucune erreur rouge, aucune
   requête en échec (statut 4xx ou 5xx). Si le serveur MCP Chrome DevTools est branché,
   `agent-skills:browser-testing-with-devtools` peut le faire.
4. **Ce qui ne se voit pas en développement** : les adresses de retour de la connexion correspondent à l'adresse
   officielle, les variables de production sont en place (aucune clé de test là où il faut du réel), les e-mails de
   l'app partent, les pages légales s'ouvrent.
5. **Les seuils du plan.** Pendant la période d'observation fixée à l'étape 1, regarder les erreurs et la mesure
   choisie ; si un seuil est dépassé, le retour arrière se déclenche sans attendre.
6. **Le verdict**, en une phrase en tête du fichier : « en ligne, vérifié » ou « retour arrière déclenché », avec la
   liste des écarts.

### 2. Clore un passage

À la fin de chaque séance : l'état (fait, reste, prochaine action) au journal. Une compétence qui a déçu à une
étape se note aussi, pour rouvrir le choix.

## Pourquoi ces choix

- **Trois étapes, de la préparation à la vérification en ligne.** Le plan de retour arrière s'écrit avant de
  déployer, pas après la panne.
- **Une simple liste avant sortie ne suffit pas** : sans paliers d'ouverture ni seuils de retour arrière, elle ne
  protège pas la décision. `agent-skills:shipping-and-launch` les apporte, avec interrupteurs de fonctionnalité
  et suivi après la sortie.
- **La voie de secours sans connexion de `deploy-to-vercel` est refusée** (voir la stratégie, point 6).
- **La vérification en ligne réutilise le parcours de test** plutôt que d'en inventer un : même méthode, rejouée
  sur la version en ligne au lieu de la copie locale.

## Frontières

| Demande | Va à |
|---|---|
| Relire, sécuriser, parcourir l'app avant de sortir | `/tester-et-securiser:tester-et-securiser` |
| Un défaut en production, ou une fonctionnalité de plus à une app existante | `/faire-evoluer-une-app:faire-evoluer-une-app` |
| Créer une app de zéro | `/creer-une-app:creer-une-app` |

## Ce qui manque

- Un hébergeur autre que Vercel : la seule compétence de déploiement publique prévue ici est celle de Vercel.
  Pour un autre hébergeur, on suit à la main sa documentation, avec les mêmes règles (projet existant, brouillon
  d'abord, plan de retour écrit).
- Les mentions légales et la politique de confidentialité n'ont pas de compétence publique : elles s'écrivent à
  la main avant la sortie quand l'app collecte des données personnelles. Le RGPD s'applique aux traitements d'un
  établissement dans l'Union européenne et aux acteurs hors Union qui visent des personnes qui s'y trouvent (CNIL,
  https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre1#Article3, vérifié le 06/11/2026) ; ailleurs,
  se reporter à la loi locale.
- Parcourir le site en ligne n'a pas de compétence publique de bout en bout : voir la méthode ci-dessus, qui se fait à la
  main.
