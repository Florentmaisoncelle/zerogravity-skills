---
name: cadrer-un-chantier
description: >-
  Quand un chantier est nouveau ou flou (une stratégie, une méthode, un système, un produit de zéro, un projet) et qu'on veut le cadrer avant de rien lancer → poser le problème, choisir la méthode de réflexion qui convient à la nature de la question, élargir les idées et étudier le marché si c'est un produit de zéro, écrire la méthode et le plan, les attaquer, faire valider une fiche de cadrage à sept cases, puis lancer. Quand un objectif tient en quelques lignes et doit être tenu dans la durée, le workflow rend le système entier en sept sorties. Tout s'écrit dans un dossier `cadrage/`, un fichier par étape, pour qu'on puisse reprendre à froid. Se lance par `/cadrer-un-chantier:cadrer-un-chantier`. Déclencheurs : « cadre ce travail », « pose la stratégie », « de zéro », « nouveau produit », « on part sur quoi », « avant de lancer », « ne lance rien », « planifie le chantier ». Ce qui manque : aucune compétence publique ne dresse la carte du problème, n'écrit la méthode et le plan, ni ne tient la fiche ; ces gestes se font à la main, décrits plus bas. Pas pour créer un agent ou un système IA de bout en bout (`/creer-un-agent-ia:creer-un-agent-ia`), pas pour une app de bout en bout (`/creer-une-app:creer-une-app`), pas pour une décision d'affaires seule (`/decider-une-strategie:decider-une-strategie`).
---

# Cadrer un chantier avant de le lancer

Règle de fond : rien ne se lance tant que la stratégie et la méthode ne sont pas claires. Un script, un test ou une page produits avant ce moment ressemblent à de l'avance. Ce sont des détours.

## Ce que ça résout

Un chantier nouveau part souvent dans la première direction plausible. Le travail produit a l'air sérieux : du code, des tests, des documents. Mais il répond à une question que personne n'a posée. Le coût arrive plus tard, quand il faut recadrer et tout reprendre.

Ce workflow fait l'inverse. Il fait poser le problème, choisit la méthode de réflexion qui convient, fait trancher la stratégie, écrire la méthode et le plan, puis les fait attaquer. Rien ne part avant la validation.

Le résultat : une fiche de cadrage dont chaque case est remplie, et un lancement qui part d'une base claire. Le workflow ne remplace aucune des méthodes qu'il appelle. Il tient l'ordre du cadrage et la porte.

## Stratégie

1. **Proportionner.** Une tâche simple, réversible et déjà cadrée : pas de porte, on fait. Un chantier (plusieurs étapes, plusieurs personnes ou outils, nouveau, ou difficile à défaire) : la porte entière.
2. **Le problème d'abord.** On ne choisit pas une solution sur une carte incomplète.
3. **Une méthode par nature de question.** On prend la plus petite qui peut changer la décision. Un chantier mêle souvent plusieurs natures : on les traite dans l'ordre stratégie, méthode, produit, plan.
4. **Partir de l'existant.** Les compétences, les scripts, les outils et les décisions passées se cherchent avant de concevoir du neuf.
5. **Les faits séparés des hypothèses.** Ce qui n'est pas mesuré s'écrit « non mesuré ».
6. **De vraies options avant une recommandation**, et le contre-cas avant la conclusion.
7. **La porte en dernier, et elle tient.** Sept cases. Une case vide : on la remplit, on ne lance pas.

<!-- prerequis:debut -->
## Prérequis

Ce workflow s'appuie sur des compétences publiques, installées à part. Aucune n'est indispensable : si l'une manque, le workflow le dit et fait l'étape à la main. Faire l'étape à la main veut dire suivre sa règle de choix, écrire ce qu'elle doit rendre (dans le fichier de l'étape, ou dans la réponse quand le workflow n'a pas de dossier) et dire ce qui reste à la charge de la personne.

```text
/plugin marketplace add Gremelinn0/zerogravity-skills
/plugin marketplace add addyosmani/agent-skills
/plugin marketplace add coreyhaines31/marketingskills
/plugin install agent-skills@addy-agent-skills
/plugin install superviser-ses-sessions@zerogravity
/plugin install marketing-skills@marketingskills
npx skills add bmad-code-org/BMAD-METHOD --skill bmad-brainstorming -a claude-code
```

La commande `npx skills add` (CLI Vercel `skills`) demande Node.js 22.20 ou plus (vérifié le 06/11/2026, https://github.com/vercel-labs/skills). Claude Code installé avec l'installeur natif n'en a pas besoin.

Les workflows cités ici sont dans le même dépôt (le dépôt s'ajoute une fois : `/plugin marketplace add Gremelinn0/zerogravity-skills`) :

```text
/plugin install creer-un-agent-ia@zerogravity
/plugin install creer-une-app@zerogravity
/plugin install decider-une-strategie@zerogravity
/plugin install reflechir-a-fond@zerogravity
```
<!-- prerequis:fin -->

## Où le cadrage s'écrit

Tout ce que le workflow produit vit dans un dossier `cadrage/` à la racine du projet, un fichier par étape. Il n'y a pas de calcul d'état : le dossier suffit pour reprendre à froid.

| Fichier | Écrit par | Contenu |
|---|---|---|
| `cadrage/00-cadre.md` | avant l'étape 1 | ce qu'on cherche à obtenir, pour qui, la décision à prendre, ce qui est déjà tranché, la taille (simple ou chantier) |
| `cadrage/01-probleme.md` | étape 1 | la carte du problème |
| `cadrage/02-methode-choisie.md` | étape 2 | la nature de la question, la méthode retenue et pourquoi, le résultat de cette méthode quand elle a tourné |
| `cadrage/03-idees.md` | étape 3 | au moins trois pistes, la retenue et pourquoi (produit de zéro seulement) |
| `cadrage/04-etude.md` | étape 4 | le marché, les concurrents, le domaine, sources citées (produit de zéro seulement) |
| `cadrage/05-methode-et-plan.md` | étape 5 | la méthode étape par étape et le plan d'exécution |
| `cadrage/sorties/1-objectif.md` à `7-suivi-et-cadence.md` | étape 5, mode « objectif vers système » | les sept sorties décrites plus bas, une par fichier |
| `cadrage/06-attaque.md` | étape 6 | les objections triées et le verdict |
| `cadrage/07-fiche-de-cadrage.md` | étape 7 | la fiche d'un écran, ses sept cases, le verdict, qui a validé et quand |
| `cadrage/08-lancement.md` | étape 8 | ce qui a été lancé, avec quelle cadence, et où se trouve le suivi |

**Reprendre à froid.** Dossier `cadrage/` absent : rien n'est encore cadré, on le crée au premier passage. Si le dossier courant n'est pas celui du projet, on le dit en une ligne et on demande où il vit : rien ne s'écrit avant. Dossier présent : si `08-lancement.md` existe, le cadrage est terminé : on dit où se trouve le suivi et on ne relance pas l'étape 8. Sinon on lit `07-fiche-de-cadrage.md` (verdict PRÊT À LANCER : on passe à l'étape 8 ; PAS PRÊT : on remplit les cases vides ; pas de validation de la personne : le verdict reste « en attente de validation », le workflow s'arrête là, le dit et ne lance rien), puis le fichier au plus haut numéro, et on reprend à l'étape suivante. Un agent qui découvre le chantier et ne reçoit que l'objectif et l'adresse du dossier `cadrage/` doit pouvoir continuer : si ce n'est pas le cas, un fichier manque.

Les données personnelles (noms, coordonnées de clients ou de candidats) n'entrent pas dans ce dossier : on les remplace par un code et la correspondance reste dans l'outil de la personne.

## Les étapes

<!-- etapes:debut -->
| # | Étape | Compétences | Règle de choix |
|---|---|---|---|
| 1 | Poser le problème | Faire dire ce que l'on veut vraiment : `agent-skills:interview-me` | Toujours d'abord, sauf pour un travail simple d'un seul objet. Manque : aucune compétence publique ne dresse la carte du problème (objets en jeu, ce que chacun ne fait pas, ce qui est tranché et mesuré, critère réel) : on la dresse à la main. |
| 2 | Choisir la méthode de réflexion | `decider-une-strategie` · `reflechir-a-fond` | Une décision d'affaires par /decider-une-strategie:decider-une-strategie ; un système ou une cause par /reflechir-a-fond:reflechir-a-fond ; une façon de faire étape par étape par l'étape 5 ; un produit de zéro par les étapes 3 et 4 ; un outil ou une compétence à trouver en cherchant d'abord ce qui est déjà installé, puis dans les annuaires publics. |
| 3 | Élargir les idées (pour un produit de zéro) | `bmad-brainstorming` · Durcir une idée avant de s'y engager : `agent-skills:idea-refine` | Élargir avant de choisir ; on garde les trois pistes dans la fiche, la retenue et pourquoi. |
| 4 | Étudier le marché (pour un produit de zéro) | Profiler les concurrents : `marketing-skills:competitor-profiling` · Comprendre les clients : `marketing-skills:customer-research` | Avant la fiche produit ; une étude qui ne cite pas ses sources ne compte pas. Manque : aucune compétence publique ne chiffre la taille du marché ni ses tendances : cette partie se fait à la main, avec des sources ouvertes et datées. |
| 5 | Écrire la méthode et le plan | à la main | Seulement quand la stratégie et la méthode sont claires. Pour un objectif confié en quelques lignes, la méthode rend les sept sorties du mode « objectif → système ». Manque : aucune compétence publique pour ce geste : il se fait à la main, avec la règle de l'étape. |
| 6 | Attaquer le plan | `agent-skills:doubt-driven-development` | Toujours avant la fiche ; un seul bloquant réel fait pivoter. L'attaque suit la méthode du pré-mortem : on suppose que le plan a échoué et on cherche pourquoi. |
| 7 | Faire valider la fiche de cadrage | à la main | Rien ne se lance tant que les sept cases ne sont pas remplies et validées. C'est ici que tombe la seule validation obligatoire du workflow. Manque : aucune compétence publique pour ce geste : il se fait à la main, avec la règle de l'étape. |
| 8 | Lancer | `claude-session-supervisor:loop-creator` | Une tâche longue ou répétée, ou une mission de bout en bout, se règle avec claude-session-supervisor:loop-creator ; un travail court s'exécute tout de suite. |
<!-- etapes:fin -->

## Le détail de chaque étape

### Avant tout : nommer le travail et sa taille

En une ligne chacun : ce qu'on cherche à obtenir ; pour qui ; la décision à prendre ; ce qui est déjà tranché. Puis la taille : **simple** (on fait, sans la porte) ou **chantier** (la porte entière). On l'écrit dans `cadrage/00-cadre.md`.

### Étape 1. Poser le problème

Aucune compétence publique ne dresse la carte du problème : on la dresse à la main et on l'écrit dans `cadrage/01-probleme.md`. Elle dit les objets en jeu et leur nombre, le rôle de chacun, ce que chacun ne fait pas, ce qui est déjà tranché, ce qui est mesuré, le critère réel, et ce qui n'est pas le problème. On la confronte aux sources, puis la personne la corrige. Pour faire dire ce que la personne veut vraiment, `agent-skills:interview-me` mène un entretien d'une question à la fois, jusqu'à une compréhension nette de l'intention de fond.

### Étape 2. Choisir la méthode selon la nature de la question

On écrit le choix, en une ou deux lignes, dans `cadrage/02-methode-choisie.md`.

| La question | La méthode | Ce qu'elle rend |
|---|---|---|
| Une décision d'affaires : marché, offre, priorités, investissement, argent | `/decider-une-strategie:decider-une-strategie` | des options, les hypothèses porteuses, une recommandation, ce qui la renverserait |
| Un système, une cause, une architecture, un défaut qui revient | `/reflechir-a-fond:reflechir-a-fond` | la cause, la carte du système, une décision |
| Une façon de faire, étape par étape : exploiter un levier, tenir un processus | écrire la méthode (étape 5) | une méthode dont chaque étape a son exécutant |
| Un produit de zéro | la chaîne produit (étapes 3 et 4) | une fiche produit, puis une spécification |
| Un outil ou une compétence à trouver | à la main : d'abord ce qui est déjà installé, puis les annuaires publics | ce qui existe, ou le verdict pour l'adopter |
| Une tâche ou un objectif confié en quelques lignes, à tenir dans la durée | le mode « objectif vers système » (étape 5) | le système entier, en sept sorties |
| Le plan d'exécution d'un travail déjà cadré | l'étape 5 | trois à six étapes vérifiables |

Une question technique qui bloque une décision d'affaires part à `/reflechir-a-fond:reflechir-a-fond`, bornée. Son résultat revient dans la décision. Une seule méthode tient une phase à la fois.

On n'annonce une méthode comme utilisée que si elle est installée et invoquée. Si elle manque, on le dit et on applique sa version courte décrite ici.

### Étapes 3 et 4. La chaîne produit (un produit de zéro)

Une app, un SaaS ou une plateforme à construire de bout en bout : `/creer-une-app:creer-une-app` tient toute la chaîne, de l'idée aux premiers clients, et appelle ce cadrage pour sa première étape.

1. **Les idées** (étape 3, `cadrage/03-idees.md`). Élargir avant de choisir, avec au moins trois pistes vraiment différentes : `bmad-brainstorming`. Pour durcir une idée brute avant de s'y engager : `agent-skills:idea-refine`. Le fichier garde les trois pistes, la retenue et pourquoi.
2. **L'étude** (étape 4, `cadrage/04-etude.md`). Le marché, les concurrents, le domaine, sources citées. Pour profiler des concurrents à partir de leurs adresses de sites : `marketing-skills:competitor-profiling`. Pour tirer des enseignements d'entretiens, d'avis ou de questionnaires clients : `marketing-skills:customer-research`. Aucune compétence publique ne chiffre la taille du marché ni ses tendances : cette partie se fait à la main, avec des sources ouvertes et datées. Une étude qui ne cite pas ses sources ne compte pas.
3. **La fiche produit.** La vision, les utilisateurs, le problème, les mesures de succès, le périmètre et ce qui n'en est pas.
4. **La spécification.** Les besoins, les parcours, les contraintes, les critères d'acceptation.
5. **L'architecture, puis le découpage en lots.**

Pour un logiciel, les points 4 et 5 sont les étapes 2 et 3 de `/creer-une-app:creer-une-app`, qui en porte les compétences : appelé depuis sa première étape, ce cadrage s'arrête à la fiche produit. La méthode BMAD (dépôt bmad-code-org/BMAD-METHOD), dont vient la compétence d'idéation, en porte une version plus longue (brief, spécification, architecture, découpage en lots, contrôle de préparation) : on le dit quand on s'en inspire.

### Étape 5. Écrire la méthode et le plan

Seulement quand la stratégie et la méthode sont claires. Aucune compétence publique pour ce geste : il se fait à la main, dans `cadrage/05-methode-et-plan.md`.

**La méthode.** Une méthode dit comment on fait, concrètement, étape par étape. Chaque étape remplit huit champs :

| Champ | La question |
|---|---|
| Déclencheur | Qu'est-ce qui lance l'étape ? |
| Entrée | Que reçoit-elle, sous quelle forme ? |
| Geste | Que fait-on, exactement ? |
| Exécutant | Qui le fait : un script, un agent (et son modèle), une compétence, une personne, un outil payant ? Pourquoi celui-là ? |
| Sortie | Que rend-elle, et où ? |
| Contrôle | Comment sait-on qu'elle est bien faite, sans faire confiance ? |
| Validation humaine | Qui relit ou valide, et à quel moment ? |
| Mesure | Quel chiffre dit qu'elle marche ? |

Pour la méthode entière, on écrit aussi : ses limites (ce qu'elle ne fait pas, les plafonds), ce qui existe déjà pour chaque étape, ce qui manque, et la règle de décision (garder, régler, arrêter, accélérer). Une étape sans exécutant ou sans contrôle n'est pas écrite.

Le choix de l'exécutant suit une règle simple : le plus simple qui sait faire.
- **Un script** pour un geste qui donne toujours le même résultat.
- **Un agent** (un assistant IA qui reçoit une consigne et travaille seul) quand il faut un jugement répété sur beaucoup d'éléments, un modèle plus petit, ou un contexte à part. Un agent ne questionne pas l'humain : la relecture reste à la personne.
- **Une compétence** pour le savoir-faire qu'on réutilise.
- **Une personne** pour ce qui engage : envoyer, signer, payer.
- **Un outil payant** pour ce qu'on ne sait pas faire soi-même à moindre coût.

**Le plan d'exécution** vient ensuite : trois à six étapes vérifiables, écrites seulement quand la stratégie et la méthode le sont.

**Le mode « objectif vers système ».** Quand un objectif ou une tâche est confié en quelques lignes, à tenir dans la durée (par exemple « un assistant qui relance mes factures impayées chaque semaine » ou « mets en place toute ma prospection »), le travail ne s'arrête pas à un petit plan. La personne donne l'objectif et, au plus, ses responsabilités et ses limites. Tout le reste se déduit, se cherche ou se tranche ici. Une question ne lui est posée que pour ce que les sources ne disent pas et qui lui revient : goût, choix irréversible, ses propres comptes.

Le mode rend sept sorties, chacune dans son fichier du dossier `cadrage/sorties/` : jamais un document de plus à côté.

| # | Sortie | Ce qu'elle dit | Fichier |
|---|---|---|---|
| 1 | L'objectif et sa mesure | les mots de la personne ; les chiffres qui le jugent ; ce qu'elle appelle un travail bien fait | `1-objectif.md` |
| 2 | La table d'autonomie | chaque famille d'actions rangée en quatre niveaux : fait seul ; fait si la consigne le demande ; demande avant ; rend la main (mot de passe, paiement, création de compte) | `2-autonomie.md` |
| 3 | Le rôle | qui conduit le travail (la personne ou un agent IA), ses responsabilités, ses limites, les agents qu'il dirige | `3-role.md` |
| 4 | La méthode | étape par étape, avec les huit champs : déclencheur, exécutant, contrôle | `4-methode.md` |
| 5 | La carte des compétences | pour chaque étape, la compétence qui porte le savoir-faire ; celles qui existent sont reliées, celles qui manquent sont cherchées (ce qui est installé, puis les annuaires publics), puis écrites | `5-competences.md` |
| 6 | Les cas qui se répètent | chaque situation qui reviendra (une réponse, un contact neuf, une alerte, la revue de fin de semaine) avec son déclencheur : un événement, une date ou un seuil ; sa marche à suivre est écrite une fois, chez celui qui fait le geste | `6-cas-qui-reviennent.md` |
| 7 | Le suivi et la cadence | où est écrit l'état du travail (une seule source, qu'on modifie avant tout outil), comment on le voit, le journal, la cadence, la règle de retour vers la personne (seulement pour décider ou montrer), et ce qu'on surveille pendant l'attente, seulement si cela peut changer une décision | `7-suivi-et-cadence.md` |

Comment on les construit :
1. **Le problème et l'existant d'abord.** La carte du problème, puis ce qui existe déjà (compétences, notes d'état, décisions passées, travaux antérieurs sur le sujet). Le travail passé se reprend, il ne se refait pas.
2. **La stratégie.** `/decider-une-strategie:decider-une-strategie` pour une décision d'affaires, `/reflechir-a-fond:reflechir-a-fond` pour l'architecture. De vraies options, une recommandation.
3. **Les méthodes du dehors.** Chercher dans les annuaires publics (GitHub, places de marché) les compétences et les méthodes qui font déjà ce geste. On reprend l'idée, avec son crédit.
4. **Les sept sorties**, écrites à leur place.
5. **Attaquer, deux fois.** D'abord l'attaque du système entier (étape 6). Ensuite un relecteur indépendant vérifie chaque objet nommé (fichier, script, tableau, tâche planifiée, compte) à son adresse, et chaque règle citée à sa source. Un objet qu'on dit absent se cherche avant de l'écrire. Contrôle : chaque objet que nomme le système a-t-il été lu là où le système dit qu'il est ?
6. **La fiche de cadrage** (étape 7), avec ses sept cases plus les sept sorties. Elle tient en un écran : une ligne par sortie (ce qui est tranché, et le fichier où elle vit), les décisions qui reviennent à la personne, sa part, puis la question. Le détail vit dans les sorties, jamais dans la fiche. Contrôle : la personne peut-elle dire oui ou non en lisant un seul écran ? Non : on coupe, et le reste part à sa place.
7. **Lancer** (étape 8). Plus aucune revalidation lot par lot.

Contrôle du mode entier : un agent qui découvre le chantier et ne reçoit que l'objectif et l'adresse du dossier `cadrage/` saurait-il reprendre le travail ? Non : une sortie manque. Et ce qu'on rend à la personne est-il un plan d'étapes, ou le système qui tiendra son objectif sans qu'elle le redise ? Un plan seul : le mode n'a pas tourné.

### Étape 6. Attaquer le plan

On l'écrit dans `cadrage/06-attaque.md`. On attaque la stratégie, la méthode et le plan tels qu'ils seront proposés, avec une seule question : qu'est-ce qui, dans ce plan, va nous faire échouer ? C'est la méthode du pré-mortem : on suppose que le plan a échoué dans un an et on cherche pourquoi. On trie les objections : ce qui bloque, ce qui se mitige, ce qu'on écarte. Un seul bloquant réel fait pivoter. Une mitigation entre dans le plan avant la validation. Le verdict est pivoter, durcir ou engager. De préférence, l'attaque vient d'un relecteur qui n'a pas écrit le plan (une autre personne, ou un agent au contexte neuf), et on ne lui donne jamais le verdict attendu.

`agent-skills:doubt-driven-development` outille ce geste : il fait relire une décision non triviale par un relecteur au contexte neuf, chargé de la réfuter. Il est écrit pour du code, mais la méthode vaut pour une décision de n'importe quel domaine. Sans lui, on fait l'attaque à la main, avec la règle de l'étape.

### Étape 7. La porte : la fiche de cadrage

La fiche s'écrit dans `cadrage/07-fiche-de-cadrage.md`.

```text
Fiche de cadrage : <le chantier>
1. Le problème, posé et validé : <la carte, ou son fichier> : oui / non
2. La décision : ses options, la recommandation, ce qui la renverserait : oui / non
3. La méthode, étape par étape, chaque étape avec son exécutant : oui / non
4. La mesure du succès : oui / non
5. Ce qu'on ne fait pas : oui / non
6. L'attaque du plan (pré-mortem) passée : oui / non
7. La validation de la personne qui décide, sur ce qui lui est réservé (qui, quand, où) : oui / non
Verdict : PRÊT À LANCER, ou PAS PRÊT (les cases vides, et le geste qui remplit chacune)
```

Une seule case à « non » donne PAS PRÊT. On remplit la case. On ne lance pas.

La personne valide sur une surface qu'elle lit : une page ou un plan court, jamais un fichier de travail. Si elle a demandé d'avancer sans l'attendre, la relecture par un autre agent peut remplir les cases 1 à 6. La case 7 reste à la personne pour un chantier nouveau. C'est ici, et pas avant, que tombe la seule validation obligatoire du workflow.

### Étape 8. Lancer

Seulement sur PRÊT À LANCER, et on note le lancement dans `cadrage/08-lancement.md` (ce qui part, avec quelle cadence, où se trouve le suivi). Une tâche longue ou répétée est réglée avec `claude-session-supervisor:loop-creator` : objectif mesurable, conditions d'arrêt, cadence, reprise d'une boucle arrêtée. Une boucle de Claude Code (commande loop) ne vit que tant que la session reste ouverte et expire après 7 jours (https://code.claude.com/docs/en/scheduled-tasks, vérifié le 06/11/2026). Pour une tâche qui doit tourner sans session ouverte, la commande schedule crée une tâche planifiée dans le cloud d'Anthropic, avec un intervalle minimal d'une heure (https://code.claude.com/docs/en/routines, vérifié le 06/11/2026). Un travail court s'exécute tout de suite. Le plan validé ne se rouvre pas sans fait nouveau.

## Ce qui fait échouer un cadrage

- Lancer « pour avancer » pendant que la stratégie se cherche encore.
- Empiler les méthodes : la plus petite qui change la décision suffit.
- Une seule option présentée comme évidente.
- Un chiffre inventé, ou une hypothèse écrite comme un fait.
- Une liste de plus à côté du cadre qui existe déjà : on range dans l'existant.
- Demander à la personne ce que les sources disent déjà.
- Annoncer une méthode qui n'a pas tourné.

## Ce qui manque

Aucune compétence publique ne couvre trois gestes de ce workflow : dresser la carte du problème, écrire la méthode et le plan, tenir la fiche de cadrage. La taille du marché et ses tendances n'ont pas non plus de compétence publique. Le workflow décrit ces gestes ci-dessus pour qu'on les fasse à la main.

## Frontières

| Voisin | Il fait | Ici |
|---|---|---|
| `/decider-une-strategie:decider-une-strategie` | une décision d'affaires | appelé pour la stratégie |
| `/reflechir-a-fond:reflechir-a-fond` | un système, une cause, une architecture | appelé pour le volet système |
| `/creer-une-app:creer-une-app` | une app de bout en bout, de l'idée aux premiers clients | il appelle ce cadrage pour sa première étape ; ce cadrage lui laisse la spécification et l'architecture |
| `/creer-un-agent-ia:creer-un-agent-ia` | créer un agent ou un système IA de bout en bout | il appelle la carte du problème, le mode « objectif vers système » et la chaîne produit pour ses premières étapes |
| `claude-session-supervisor:loop-creator` | régler la cadence et la reprise d'une tâche longue | reçoit le chantier une fois PRÊT À LANCER |
