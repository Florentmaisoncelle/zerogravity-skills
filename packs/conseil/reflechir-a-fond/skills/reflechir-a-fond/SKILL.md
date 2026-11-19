---
name: reflechir-a-fond
description: >-
  Quand un chantier complexe, transversal, structurel ou difficile à défaire commence, quand une IA part trop vite, quand on veut prendre de la hauteur, aller à la racine ou challenger un plan, et quand un défaut découvert en plein travail vaut pour d'autres cas que le sien → imposer un sas de réflexion, sans rien modifier tant que la demande n'a pas dit d'analyser puis d'exécuter : verrouiller l'autorisation, poser le problème en entier, reconstituer la réalité, cartographier le système, descendre à la cause structurelle, ouvrir au moins trois options, formuler une thèse qui peut échouer, la réfuter, puis rendre la décision. Se lance par `/reflechir-a-fond:reflechir-a-fond`. Déclencheurs : « réfléchis avant d'agir », « prends de la hauteur », « attends, ne fonce pas », « vision globale », « chantier de fond », « va à la racine ». Ce qui manque : aucune compétence publique pour verrouiller l'autorisation, poser le problème, cartographier ni formuler la thèse ; ces gestes se font à la main. Pour réfuter, `agent-skills:doubt-driven-development` fait relire la décision par un relecteur au contexte neuf ; sans elle, la réfutation se fait à la main. Pas pour trancher une décision d'affaires (`/decider-une-strategie:decider-une-strategie`) ni pour cadrer un chantier neuf de bout en bout (`/cadrer-un-chantier:cadrer-un-chantier`).
---

# Réfléchir à fond avant d'agir

## Mission

Transformer une demande complexe en **décision solide avant exécution**.

Ce workflow ne remplace aucune méthode de réflexion. Il diagnostique la nature du problème, choisit les bonnes compétences, les enchaîne, synthétise leurs conclusions et applique l'autorisation donnée par le demandeur. Il possède le **processus de réflexion**, jamais la vérité du domaine.

**L'autorisation (le mandat).** C'est ce que le demandeur a permis de faire. Il y en a deux :

- **Réflexion seule** : on observe, on analyse, on rend un dossier. Rien n'est modifié. Une simple demande d'audit ou de réflexion est toujours de ce type.
- **Analyse puis exécution** : le demandeur a dit expressément, dans sa demande, d'analyser puis d'exécuter sans le solliciter à chaque pas. Dans ce cas, la relecture par un autre agent (ou une autre personne) remplace les validations de routine du demandeur : la décision lui est rendue, et l'exécution continue dans le même élan. Une décision que le demandeur s'est réservée (un choix de goût, de prix, un engagement financier ou juridique), un gel demandé ou une action sensible non autorisée ne bloquent que la branche concernée.

On vérifie l'autorisation du moment, pas un ancien « vas-y » donné pour autre chose. Une relecture expressément demandée prime. Une fois le plan écrit sous « analyse puis exécution », on ne redemande pas un second accord.

## Ce que ça corrige

Une IA peut produire beaucoup de travail juste tout en visant une mauvaise unité, une mauvaise cause ou un périmètre fragmenté. Le défaut n'est alors ni la vitesse ni la qualité locale : c'est l'absence d'un moment où elle doit prouver qu'elle a compris **le système qui fabrique le problème**.

On refuse notamment :

- un plan organisé par fichiers quand le problème traverse une capacité entière ;
- une solution choisie avant la mesure de l'état réel ;
- un symptôme traité comme une cause ;
- une documentation, une compétence ou un tableau de bord pris pour une preuve que le système tourne ;
- une première idée raffinée sans espace de solutions concurrentes ;
- un plan validé par son propre auteur sans attaque adversariale ;
- un « on verra au fil de l'eau » qui cache un inventaire incomplet ou une dette sans responsable.

## Quand s'arrêter en plein travail

Les déclencheurs habituels visent un chantier qui commence, ou une demande de hauteur. Il en existe un troisième : un défaut découvert au milieu d'un travail. On est tenté de le noter et de continuer. Il faut au contraire se poser une question à chaque mesure :

**Ce que je viens de constater est-il vrai pour d'autres cas que celui que je traite ?**

- **Oui** : c'est un défaut de mécanisme (la même erreur, le même oubli, la même mauvaise source reviendront ailleurs). On s'arrête. On pose le défaut par écrit, on cherche sa cause avec ce workflow, on fait relire l'analyse par un autre agent ou une autre personne, et seulement ensuite on corrige partout où il se reproduit.
- **Non** : c'est propre au cas traité. On le corrige là et le travail continue.

Pour chercher la cause, on commence par les endroits qui prétendent déjà répondre à la question (la liste qui dit « qui fait quoi », la page qui dit « ce qui est terminé », le tableau de bord), plutôt que par le détail : la racine d'un défaut de mécanisme y vit presque toujours.

## Niveau de profondeur

| Niveau | Situation | Traitement minimal |
|---|---|---|
| D1, ciblé | décision non triviale mais locale et réversible | cadrage, une méthode principale, pré-mortem rapide |
| D2, structurel | plusieurs domaines, responsables ou sources ; refonte difficile à défaire | mesure, carte du système, deux méthodes complémentaires, pré-mortem |
| D3, critique | architecture centrale, migration massive, stratégie produit ou coût élevé | D2 plus des angles indépendants, des critères de non-perte et une relecture indépendante ; validation de la personne qui décide seulement pour une décision qu'elle s'est réservée |

Le **pré-mortem** consiste à supposer que le plan a échoué, puis à chercher pourquoi. Une invocation explicite de ce workflow implique au moins D2. Pour une tâche triviale, réversible et déjà spécifiée, on ne l'invoque pas par automatisme.

## Choisir la compétence d'analyse

On ne charge pas tout rituellement. On prend la plus petite chaîne qui couvre le problème, puis on rend visible ce qui a été activé et pourquoi.

| Signal dominant | Compétence principale | Rôle exact |
|---|---|---|
| bug réel, récidive, contournement, cause inconnue | à la main | prouver le flux de bout en bout et nommer la cause structurelle |
| le sujet est son propre dispositif Claude Code : fichiers de règles, compétences, documents qui le pilotent | `entretenir-son-systeme:optimise-systeme` | mesurer l'ensemble avant de le juger, puis l'améliorer dans l'ordre ; hors de ce cas (une entreprise, une application, un processus), elle ne s'applique pas |
| architecture, responsabilités ou source de vérité (l'endroit qui fait foi pour une information) | à la main | cartographier, puis produire un design sans rien modifier |
| plan, refonte ou trajectoire pas encore engagée | pré-mortem (étape 8) : `agent-skills:doubt-driven-development` si elle est installée, sinon à la main | attaquer la thèse et rendre pivoter, durcir ou engager |
| priorité ou arbitrage sur un produit ou une offre | `/decider-une-strategie:decider-une-strategie` | préparer la décision d'affaires ; elle reste à la personne qui décide (le dirigeant, ou le responsable du produit) ; pas de relais en cascade : si c'est ce workflow qui nous a appelé, on lui rend la main |
| risque de sécurité, de droit, d'argent ou autre domaine spécialisé | la compétence experte du domaine, ou un professionnel (juriste, expert-comptable, spécialiste sécurité) | apporter la lentille du spécialiste, sans l'inventer ici |
| espace de solutions trop étroit, une seule idée qu'on raffine | `product-management:brainstorm` | ouvrir des options réellement concurrentes avant l'étape 6 |
| chiffres de l'état réel nécessaires (volumes, coûts, délais) | à la main | mesurer au lieu d'estimer, à l'étape 3 |
| responsable ou outil inconnu | à la main : ce qui est déjà installé, puis les annuaires publics | trouver la compétence vivante avant de fabriquer une méthode |

Chaînes usuelles. **Elles se terminent toutes par la relecture de ce qui a réellement été fait, jamais par le pré-mortem.**

- **Bug profond** : cause prouvée, options de correction, pré-mortem du plan, relecture.
- **Refonte d'un dispositif de règles et de compétences** : `entretenir-son-systeme:optimise-systeme`, carte locale, pré-mortem du plan, relecture.
- **Décision de produit ou d'entreprise** : faits du décideur, alternatives, pré-mortem du projet.

### Le pré-mortem n'est pas la fin de la chaîne : la relecture vient après

Les deux ne mesurent pas la même chose, et aucune ne remplace l'autre. Le pré-mortem attaque une thèse pas encore exécutée : *qu'est-ce qui, dans ce plan, va nous faire échouer ?* La relecture lit ce qui a réellement été produit, cumul compris : *qu'est-ce qui, dans ce résultat, est déjà faux ?* Un plan peut être excellent et son exécution introduire un défaut que le pré-mortem, par construction, ne pouvait pas voir.

| Quand | Quoi | Comment |
|---|---|---|
| avant d'engager, sur la thèse | pré-mortem adversarial | étape 8 : `agent-skills:doubt-driven-development` si elle est installée, sinon à la main |
| après exécution, sur le cumul | relecture d'ensemble | voir ci-dessous |

La relecture vient en dernier, une seule fois, sur l'ensemble : pas une relecture par vague. C'est précisément parce qu'elle couvre le cumul qu'elle attrape ce que des relectures fragmentées manquent. Elle dépend de la nature du travail :

- **Du code remis par une pull request** (une demande de fusion sur GitHub) : `code-review:code-review` relit cette pull request avec plusieurs agents spécialisés. Elle ne sert qu'à cela.
- **Du code sans pull request** : relecture par une autre personne, ou par un agent au contexte neuf à qui l'on donne le diff et les critères du plan.
- **Hors code** (un document, une offre, un processus, une organisation) : quelqu'un qui n'a pas produit le travail relit le résultat réel contre les critères PASS et ABORT du plan, et dit pour chacun s'il est tenu.

Une compétence non installée n'est jamais simulée ni déclarée invoquée. On distingue « présente sur le disque », « découverte » et « réellement invocable », puis on poursuit avec la meilleure méthode disponible en annonçant la limite.

<!-- prerequis:debut -->
## Prérequis

Ce workflow s'appuie sur des compétences publiques, installées à part. Aucune n'est indispensable : si l'une manque, le workflow le dit et fait l'étape à la main. Faire l'étape à la main veut dire suivre sa règle de choix, écrire ce qu'elle doit rendre (dans le fichier de l'étape, ou dans la réponse quand le workflow n'a pas de dossier) et dire ce qui reste à la charge de la personne.

```text
/plugin marketplace add Florentmaisoncelle/zerogravity-skills
/plugin marketplace add addyosmani/agent-skills
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin install agent-skills@addy-agent-skills
/plugin install entretenir-son-systeme@zerogravity
/plugin install code-review@claude-plugins-official
/plugin install engineering@knowledge-work-plugins
/plugin install enterprise-search@knowledge-work-plugins
/plugin install operations@knowledge-work-plugins
/plugin install product-management@knowledge-work-plugins
/plugin install superpowers@claude-plugins-official
npx skills add bmad-code-org/BMAD-METHOD --skill bmad-agent-analyst -a claude-code
npx skills add bmad-code-org/BMAD-METHOD --skill bmad-brainstorming -a claude-code
```

La commande `npx skills add` (CLI Vercel `skills`) demande Node.js 22.20 ou plus (vérifié le 06/11/2026, https://github.com/vercel-labs/skills). Claude Code installé avec l'installeur natif n'en a pas besoin.

Les workflows cités ici sont dans le même dépôt (le dépôt s'ajoute une fois : `/plugin marketplace add Florentmaisoncelle/zerogravity-skills`) :

```text
/plugin install cadrer-un-chantier@zerogravity
/plugin install decider-une-strategie@zerogravity
```
<!-- prerequis:fin -->

## Où le dossier de décision s'écrit

Ce workflow n'a pas d'état à calculer : il rend un dossier de décision à la fin. Pour qu'une autre tâche puisse le reprendre sans la conversation, le dossier s'enregistre dans un fichier `reflexion/<sujet>.md` (un fichier par réflexion, daté dans son en-tête), créé au premier passage si le dossier `reflexion/` est absent. Si le dossier courant n'est pas celui du projet, on le dit en une ligne et on demande où le mettre : rien ne s'écrit avant. Ce n'est pas un registre permanent : le dossier ne se met pas à jour après coup, une nouvelle réflexion donne un nouveau fichier. Quand la décision attend quelqu'un d'autre (le dirigeant, un spécialiste, un client), le dossier le dit en tête sous « En attente : ce qu'on attend, de qui ». Le workflow s'arrête là : il ne devine pas cette décision et n'invente pas la suite.

## Les étapes

<!-- etapes:debut -->
| # | Étape | Compétences | Règle de choix |
|---|---|---|---|
| 1 | Verrouiller l'exécution | Relever la demande et ce qui est déjà décidé : `superpowers:brainstorming` | Une demande d'audit ou de réflexion seule ne change rien. Sous un mandat « analyse puis exécute » (par exemple un travail confié à loop-creator sur le même objectif), la revue d'un agent remplace les validations humaines de routine et on ne redemande pas d'accord une fois le plan écrit ; une décision produit réservée, un gel ou une action sensible non autorisée ne bloquent que leur seule branche. La profondeur se choisit tôt : ciblé (D1), structurel (D2) ou critique (D3) ; une invocation explicite vaut au moins D2, et une tâche triviale, réversible et déjà spécifiée n'appelle pas ce workflow. Sous « analyse puis exécution », que le demandeur a écrit expressément dans sa demande, la relecture par un autre agent remplace ses validations de routine et on ne redemande pas d'accord une fois le plan écrit ; une décision qu'il s'est réservée, un gel ou une action sensible non autorisée ne bloquent que leur seule branche. |
| 2 | Poser le problème en entier | Faire dire le problème, une question à la fois : `agent-skills:interview-me` | Obligatoire. Si la cinquième ligne (la preuve que c'est mieux) ne s'écrit pas, le chantier n'est pas encore cadré. Sous mandat autonome (« analyse puis exécution »), le pilote tranche lui-même les ambiguïtés réversibles. |
| 3 | Reconstituer la réalité | Chercher dans toutes les sources : `enterprise-search:knowledge-synthesis` ; `enterprise-search:search` ; `enterprise-search:search-strategy` · Prouver chaque constat avant de l'affirmer : `superpowers:verification-before-completion` ; `agent-skills:source-driven-development` | On cherche le vivant (le code qui tourne, ses consommateurs, ses responsables réels) plutôt que la documentation. Un zéro ne compte qu'avec un témoin positif. Si une preuve exige une modification, on ne la fabrique pas pendant la réflexion : on déclare la preuve manquante et on l'ajoute au plan. Manque : aucune compétence publique ne mesure l'usage réel d'un système quelconque (invocations, coûts, ce qu'on n'appelle plus, sur l'historique des sessions) : la baseline se mesure à la main, de façon reproductible. |
| 4 | Cartographier le système | Dessiner la chaîne de bout en bout : `engineering:system-design` · Dire qui possède quoi dans la chaîne : `operations:process-doc` | On travaille par tranche de capacité, pas par dossier ni par type de fichier. Manque : aucune compétence ne trace cette carte : le workflow la dessine lui-même. |
| 5 | Descendre jusqu'à la structure | `entretenir-son-systeme:optimise-systeme` · Remonter à la cause d'un défaut qui revient : `superpowers:systematic-debugging` | Le signal dominant choisit la compétence, et la chaîne la plus courte qui couvre le problème : un défaut qui revient se traque à la main, en prouvant le flux de bout en bout et en nommant la cause structurelle ; le propre dispositif Claude Code de la personne (règles, compétences, documents) va à entretenir-son-systeme:optimise-systeme ; un responsable ou un outil inconnu se cherche d'abord dans ce qui est installé, puis dans les annuaires publics. Un arbitrage produit va au responsable produit du projet, un arbitrage sur une offre à /decider-une-strategie:decider-une-strategie (sauf si c'est lui qui nous a appelé), un risque de sécurité, de droit ou d'argent à la compétence experte du domaine ou à un professionnel. On cite sa conclusion sans recopier sa méthode. Une compétence absente de l'hôte n'est jamais simulée ni déclarée invoquée : on poursuit avec la meilleure méthode disponible en annonçant la limite. Manque : aucune compétence publique ne traque la cause d'un défaut qui revient : on la cherche à la main. |
| 6 | Ouvrir avant de converger | `product-management:brainstorm` · Élargir les options avant de choisir : `agent-skills:idea-refine` ; `bmad-brainstorming` | Trois options au moins quand l'enjeu est structurel ou critique ; une idée unique qu'on raffine ne compte pas. L'ouverture se fait avant de choisir, jamais après. |
| 7 | Construire une thèse qui peut échouer | Formuler la thèse et ses critères PASS et ABORT : `product-management:write-spec` ; `agent-skills:spec-driven-development` | Un plan qui ne peut pas échouer dans sa formulation n'est pas testable. Manque : aucune compétence n'écrit cette thèse : le workflow la formule lui-même. |
| 8 | Réfuter avant d'engager | `agent-skills:doubt-driven-development` · Attaquer la thèse avec un regard neuf : `agent-skills:doubt-driven-development` ; `operations:risk-assessment` | On l'applique à la version du plan qui sera réellement proposée, jamais à une première idée qu'il ne ferait que bénir, et on ne donne jamais au relecteur le verdict attendu. Un bloquant concret impose de pivoter ; une mitigation entre dans le plan avant d'engager. |
| 9 | Rendre la décision au bon responsable | Prévoir la relecture d'ensemble d'un code remis par pull request : `code-review:code-review` · Écrire le dossier de décision : `agent-skills:documentation-and-adrs` ; `engineering:architecture` | Le dossier est suffisant seulement si une autre tâche, sans la conversation, peut comprendre le problème, retrouver les faits, voir pourquoi les alternatives sont écartées, réfuter la recommandation avec les mêmes critères, exécuter sans inventer de décision et savoir quand s'arrêter. Le workflow ne code pas, ne documente pas le produit et ne rend pas de verdict de test. La relecture d'ensemble dépend du travail : code remis par une pull request, code-review:code-review ; code sans pull request, relecture par une autre personne ou un agent au contexte neuf ; hors code, relecture du résultat contre les critères PASS et ABORT par quelqu'un qui ne l'a pas produit. |
<!-- etapes:fin -->

## Le détail de chaque étape

### 1. Verrouiller l'exécution

Annoncer la phase de réflexion et l'autorisation : réflexion seule, ou analyse suivie d'exécution. Relever la demande actuelle, les décisions déjà validées, le travail en cours et les exclusions. Une autorisation générale ne remplace pas le périmètre précis de la décision en cours.

### 2. Poser le problème en entier

Aucune compétence publique : à la main. On dresse la **table des objets en jeu** : combien il y en a, le rôle de chacun, ce que chacun ne fait pas, ce qui est déjà tranché, ce qui est déjà mesuré, le critère réel, et ce qui n'est pas le problème. On la confronte aux sources et à une critique avant la suite. Le point à ne jamais sauter : combien d'objets distincts sont en jeu. Une carte qui en porte deux là où il y en a trois est fausse d'un cran, et chaque raisonnement qui s'en suit, même juste, répond à la mauvaise question. Sous « analyse puis exécution », on tranche soi-même les ambiguïtés réversibles.

Puis on écrit séparément :

1. le symptôme ou l'insatisfaction exprimée ;
2. le résultat que cherche réellement le demandeur ;
3. le système capable de produire ce résultat ;
4. la décision à prendre maintenant ;
5. ce qui prouverait objectivement que la situation est meilleure.

Si le point 5 est impossible à écrire, le chantier n'est pas encore cadré.

### 3. Reconstituer la réalité

- Lire les sources qui font foi et leur hiérarchie avant les synthèses.
- Mesurer une baseline (une mesure de départ) reproductible ; ne jamais coder un total historique en dur.
- Séparer fait, hypothèse, contradiction, inconnu et décision.
- Chercher le vivant : ce qui tourne réellement, ses utilisateurs, ses responsables réels, plutôt que la documentation.
- Distinguer l'absence réelle d'un instrument qui ne voit rien : un zéro exige un témoin positif (avant d'affirmer qu'il n'y a aucun X, on montre que la recherche trouve bien un X qui existe).

Pour retrouver une information dispersée dans plusieurs outils, voir les compétences de recherche listées dans le tableau : elles cherchent dans les outils connectés à Claude (messagerie, stockage de documents, suivi de projet, chat). Sans outil connecté, elles ne trouvent rien : on cherche alors à la main dans les dossiers de la personne. Quand une preuve exigerait une modification, on ne la fabrique pas pendant ce sas : on déclare la preuve manquante et on l'inclut dans le plan d'exécution.

### 4. Cartographier le système

Aucune compétence ne trace cette carte : on la dessine à la main. La chaîne utile de bout en bout :

`entrée → mécanismes → responsables → sources de vérité → exécution → preuve → décision`

On nomme les frontières, les dépendances transverses, les utilisateurs de chaque élément, les boucles de rétroaction (ce qui revient influencer l'entrée), les états cachés, les règles qui doivent toujours rester vraies et les points où l'information est copiée, perdue ou transformée. On travaille par tranche de capacité (ce que le système sait faire), pas automatiquement par dossier ni par type de fichier.

### 5. Descendre à la structure

Ne pas s'arrêter à « le document est faux », « la compétence est trop grosse » ou « l'agent oublie ». Poser les pourquoi jusqu'au choix de système qui rend la récidive possible : mauvais responsable, contrôle absent, signal infiable, unité de travail erronée, autorité dupliquée, déclencheur muet, boucle sans rappel, validation non indépendante.

On active ici la compétence principale choisie dans le tableau, et on cite sa conclusion sans recopier sa méthode.

### 6. Ouvrir avant de converger

Au moins trois options réellement distinctes quand l'enjeu est D2 ou D3 :

- statu quo assumé ou réduction du périmètre ;
- amélioration minimale ;
- correction structurelle.

Pour chaque option : bénéfice, coût, rayon d'effet, réversibilité, dette restante et signal de succès. Les options faibles sont écartées par écrit, pour empêcher leur retour sous un autre nom.

### 7. Construire une thèse qui peut échouer

Aucune compétence n'écrit cette thèse : on la formule à la main.

> En changeant **X** dans le système **Y**, nous obtiendrons **Z**, mesuré par **M**, sans perdre **N**.

On liste les hypothèses, les inconnues, les préconditions, les éléments à recâbler, le retour arrière et les critères PASS (le plan a réussi) et ABORT (on arrête). Un plan qui ne peut pas échouer dans sa formulation n'est pas testable.

### 8. Réfuter avant d'engager

Pour toute décision D2 ou D3, on attaque la thèse et la version du plan qui sera réellement proposée, par un pré-mortem. Si possible, on confie l'attaque à des angles indépendants (plusieurs agents ou personnes qui ne se parlent pas), et on ne donne jamais au relecteur le verdict attendu. `agent-skills:doubt-driven-development` outille ce geste : il fait relire une décision non triviale par un relecteur au contexte neuf, chargé de la réfuter. Il est écrit pour du code, mais la méthode vaut pour toute décision ; sans lui, on le fait à la main. Un bloquant concret impose de pivoter. Une mitigation entre dans le plan avant d'engager. Le bruit est écarté par écrit.

### 9. Rendre la décision au bon responsable

On présente le dossier de décision ci-dessous et on l'enregistre dans `reflexion/<sujet>.md`. En réflexion seule, on s'arrête sur la restitution. Sous « analyse puis exécution », on rend la décision à celui qui a lancé la réflexion et on poursuit l'exécution autorisée dans le même tour, sans redemander d'accord sur le plan. On isole seulement une vraie décision réservée, sans bloquer les branches indépendantes.

Et on nomme la relecture d'ensemble dans le plan proposé, à sa place : en dernier, sur le cumul, selon la nature du travail (voir plus haut). Un plan qui ne dit pas quand il sera relu se termine sur le pré-mortem, c'est-à-dire sur une thèse jamais confrontée à ce qui a réellement été produit. `code-review:code-review` est la bonne porte quand le travail est du code remis par une pull request.

## Format de sortie

```text
Autorisation : réflexion seule | analyse puis exécution
Demande exprimée : <ce qui a été demandé>
Vrai problème : <le problème système en une phrase>
Profondeur et périmètre : <D1|D2|D3, inclusions et exclusions>
Compétences activées : <noms, pourquoi, ordre>
Faits mesurés : <baseline, preuves et sources>
Inconnus et hypothèses : <ce qui n'est pas encore prouvé>
Carte du système : <chaîne et responsabilités>
Racine ou motif structurel : <cause qui explique la récidive>
Options : <minimum 3 en D2/D3, avec arbitrages>
Réfutation : <bloquants, mitigations, bruit écarté>
Recommandation : <thèse durcie>
PASS / ABORT : <mesures terminales>
Plan proposé : <petites vagues finies, responsables et preuves>
Suite : <premier lot et responsable ; ou décision réellement réservée>
```

## Critère de qualité

La réflexion est suffisante seulement si une autre tâche, sans la conversation, peut :

1. comprendre le vrai problème ;
2. retrouver les faits et leurs sources ;
3. expliquer pourquoi les alternatives ont été écartées ;
4. réfuter la recommandation avec les mêmes critères ;
5. exécuter le plan sans inventer une décision ;
6. dire objectivement quand arrêter.

Sinon, on approfondit avant de conclure. Une lacune réparable ne se transforme pas en demande de validation.

## Anti-patterns

- Exécuter « pour avancer » pendant que le problème est encore reformulé.
- Charger toutes les compétences de réflexion sans diagnostic de pertinence.
- Remplacer l'analyse par une longue liste de fichiers ou de petites anomalies.
- Confondre quantité de changements et profondeur de correction.
- Produire une solution unique puis demander au pré-mortem de la bénir.
- Employer un relecteur comme co-auteur du plan qu'il doit juger.
- Présenter une proposition comme une décision de la personne qui décide.
- Laisser une dette « plus tard » sans responsable, condition de reprise ni état terminal.

## Ce qui manque

- Aucune compétence publique ne couvre le verrouillage de l'autorisation, la table des objets, la carte du système, la thèse ni la réfutation (hors l'aide de `agent-skills:doubt-driven-development`) : le workflow décrit ces gestes pour qu'on les fasse à la main.
- Aucune compétence publique ne mesure l'état réel d'un système quelconque : la baseline se mesure à la main, de façon reproductible.
- Aucune compétence par défaut pour chercher dans toutes les sources : les compétences de recherche du tableau aident quand des outils sont connectés, sans être une réponse complète.

## Frontières

- Ce workflow ne code pas, ne documente pas le produit et ne rend pas de verdict de test.
- Il ne remplace ni la recherche de cause, ni `entretenir-son-systeme:optimise-systeme`, ni le pré-mortem. Il choisit lequel appeler.
- Il ne tient pas de registre permanent : chaque réflexion donne un dossier daté, qui ne se met pas à jour ensuite.
- Une décision d'affaires (marché, offre, priorités, argent) va à `/decider-une-strategie:decider-une-strategie`, qui lui renvoie en retour une seule question technique bornée.
- Un chantier neuf, flou, à cadrer de bout en bout, va à `/cadrer-un-chantier:cadrer-un-chantier`, qui appelle ce workflow pour le volet système, cause ou architecture.
- Quand un autre workflow a appelé cette réflexion (par exemple `/cadrer-un-chantier:cadrer-un-chantier`), on lui rend les options, les preuves, la décision et le prochain lot ; on n'ouvre pas un second plan. Sinon, on rend au demandeur, en retrouvant le responsable du domaine. Une décision de réflexion seule n'est pas une autorisation implicite d'exécution.
