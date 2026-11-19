---
name: creer-un-agent-ia
description: >-
  Quand on veut créer un agent ou un système IA qui travaille pour soi, en bâtir un chez un client, ou améliorer
  l'architecture d'un système qui existe → dérouler la méthode en sept étapes : poser le problème, répondre aux
  questions produit, choisir le type d'agent et dessiner l'architecture, construire, tester, mesurer, capitaliser.
  Une étape 0 tranche le chemin (pour soi, pour un client, système existant) et regarde l'existant. Plusieurs
  étapes se font à la main faute de compétence publique, et le workflow le dit. Se lance par
  `/creer-un-agent-ia:creer-un-agent-ia`. Déclencheurs : « crée-moi un agent qui… », « je veux un système
  qui… », « comment on fait un agent qui marche », « optimise l'architecture de ce système », « agent cloud ou
  local », « type d'agent », « agent n8n », « agent Make », « agent déclenché par un webhook », « agent
  WhatsApp ». Pas pour une app ou un SaaS avec des utilisateurs autour des agents (`/creer-une-app:creer-une-app`).
  Pas pour cadrer un chantier qui n'est pas un agent (`/cadrer-un-chantier:cadrer-un-chantier`).
---

# Créer un agent ou un système IA, du problème à la capitalisation

## Ce que ça résout

Créer un agent qui marche demande sept gestes dans l'ordre. Sans méthode, les questions produit sautent, le test se
réduit à « ça a l'air de marcher », et ce qu'un passage apprend ne sert pas au suivant. Ici : l'ordre, le choix du
chemin, les questions à poser, et un dernier geste qui laisse le système plus fort qu'avant le passage.

**Résultat attendu** : pour chaque agent ou système, les sept étapes passées dans l'ordre ; un cadrage validé une
seule fois ; un dernier geste de capitalisation.

**Les mots utilisés ici**
- Un **agent** est un programme piloté par un modèle d'IA : il choisit lui-même ses actions, avec des outils, pour atteindre un but.
- Un **MCP** (Model Context Protocol) est un standard pour brancher des outils à un agent : lire un service, écrire dans une base.
- Une **compétence** est un dossier de consignes que Claude charge au bon moment.
- **n8n** et **Make** sont des services en ligne où l'on assemble des scénarios (des suites d'actions) par blocs visuels.
- Un agent **local** tourne sur votre poste, avec votre abonnement ; un agent **cloud** tourne sur un serveur, à toute heure.

**Ce qui n'en est pas** :
- une app, un SaaS ou une plateforme avec des utilisateurs autour des agents : `/creer-une-app:creer-une-app`, qui
  appelle cette méthode pour son étape « agents » ;
- un chantier qui n'est ni un agent ni un système (une stratégie, une offre, un produit) :
  `/cadrer-un-chantier:cadrer-un-chantier` ;
- la cadence d'une tâche longue déjà cadrée : `superviser-ses-sessions:loop-creator`.

## Stratégie

- **Une porte, trois chemins, une seule table.** Pour soi, pour un client, ou pour un système qui existe. Le
  chemin se choisit à l'étape 0 ; les sept étapes restent les mêmes.
- **On enchaîne, on ne refait pas.** Le savoir-faire de chaque étape reste chez la compétence qui le porte. Une
  étape sans compétence publique se fait à la main, avec la règle de l'étape.
- **Les questions produit avant l'architecture.** Un agent conçu avant de savoir pour qui, contre quelle mesure et
  avec quel dernier clic humain se reconstruit.
- **Une validation**, à la fin de l'étape 2, sur une fiche d'un écran. Ensuite tout se déroule, jusqu'au résultat
  ouvert chez la personne.
- **Chaque passage se referme par la capitalisation**, même réussi : un passage sans correction le dit en une
  ligne, un passage corrigé laisse son amélioration.

<!-- prerequis:debut -->
## Prérequis

Ce workflow s'appuie sur des compétences publiques, installées à part. Aucune n'est indispensable : si l'une manque, le workflow le dit et fait l'étape à la main. Faire l'étape à la main veut dire suivre sa règle de choix, écrire ce qu'elle doit rendre (dans le fichier de l'étape, ou dans la réponse quand le workflow n'a pas de dossier) et dire ce qui reste à la charge de la personne.

```text
/plugin marketplace add Florentmaisoncelle/zerogravity-skills
/plugin marketplace add addyosmani/agent-skills
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin marketplace add anthropics/skills
/plugin marketplace add integromat/make-skills
/plugin marketplace add n8n-io/skills
/plugin marketplace add pydantic/skills
/plugin install agent-skills@addy-agent-skills
/plugin install atomic-agents@claude-plugins-official
/plugin install claude-api@anthropic-agent-skills
/plugin install entretenir-son-systeme@zerogravity
/plugin install superviser-ses-sessions@zerogravity
/plugin install consultant-ia@zerogravity
/plugin install cowork-plugin-management@knowledge-work-plugins
/plugin install engineering@knowledge-work-plugins
/plugin install example-skills@anthropic-agent-skills
/plugin install logfire@pydantic-skills
/plugin install make-skills@make-marketplace
/plugin install mcp-server-dev@claude-plugins-official
/plugin install n8n-skills@n8n-io
/plugin install operations@knowledge-work-plugins
/plugin install plugin-dev@claude-plugins-official
/plugin install product-management@knowledge-work-plugins
/plugin install project-artifact@claude-plugins-official
/plugin install skill-creator@claude-plugins-official
/plugin install small-business@knowledge-work-plugins
/plugin install superpowers@claude-plugins-official
npx skills add PostHog/skills --skill exploring-ai-failures -a claude-code
npx skills add bmad-code-org/BMAD-METHOD --skill bmad-architecture -a claude-code
npx skills add ericrisco/rsc-harness --skill automation-strategy -a claude-code
```

La commande `npx skills add` (CLI Vercel `skills`) demande Node.js 22.20 ou plus (vérifié le 06/11/2026, https://github.com/vercel-labs/skills). Claude Code installé avec l'installeur natif n'en a pas besoin.

Les workflows cités ici sont dans le même dépôt (le dépôt s'ajoute une fois : `/plugin marketplace add Florentmaisoncelle/zerogravity-skills`) :

```text
/plugin install cadrer-un-chantier@zerogravity
/plugin install creer-une-app@zerogravity
/plugin install consultant-ia@zerogravity
/plugin install reflechir-a-fond@zerogravity
```
<!-- prerequis:fin -->

## Étapes

### 0. Pour qui, et qu'est-ce qui existe déjà ?

Une phrase tranche le chemin : **pour soi**, **pour un client**, ou **un système qui existe**. Puis l'existant,
avant tout : les systèmes et compétences déjà en place, les notes et documents déjà écrits sur le sujet. Le travail
passé se reprend, il ne se refait pas.

### Le journal de l'agent

Ce workflow se déroule par méthode : il ne calcule pas d'état strict, mais il garde une mémoire pour reprendre.

- **Où** : un fichier par agent, `agents/<nom-court>/journal.md`, à la racine du dossier de travail du projet. Pour
  un client, dans le dossier de travail de ce client, sans donnée personnelle (des codes à la place des noms).
  Dossier absent : rien n'est fait, on commence par l'étape 0 et on crée le dossier au premier passage.
- **Ce qu'il contient** : une ligne par étape terminée, `AAAA-MM-JJ · NN · fait | en attente | sans objet | sautée | corrigée · <une phrase>`,
  et, à l'étape 7, un court bloc par passage avec quatre rubriques : le résultat, l'état (ce qui est décidé, ce qui
  reste, la prochaine action), la leçon et l'amélioration candidate.
- **En attente** : quand une étape dépend d'un geste ou d'une réponse qui arrive hors de la conversation (installer l'agent sur le poste ou dans le cloud, l'accord d'un client, l'essai de bout en bout joué par la personne, les semaines de mesure de l'étape 6), la ligne dit `en attente`, ce qu'on attend et de qui. Préparé n'est pas fait : le workflow s'arrête, le dit, et n'invente ni résultat ni suite. Quand la personne apporte ce qui est arrivé, la ligne `fait` suit.
- **Reprendre** : on lit la dernière ligne, on dit où on en est (et ce qu'on attend, si elle dit `en attente`), on propose l'étape suivante.

### Les sept étapes

Pour un système qui existe, `entretenir-son-systeme:optimise-systeme` prend le relais de plusieurs étapes : il
cible, mesure, arbitre, puis re-mesure sans perte. Il agit sur les règles, les compétences et les documents d'un
dépôt Claude Code : si le système n'est pas fait de cela, l'étape se fait à la main.

<!-- etapes:debut -->
| # | Étape | Compétences | Règle de choix |
|---|---|---|---|
| 1 | Poser le problème | `agent-skills:interview-me` · `agent-skills:idea-refine` · `superpowers:brainstorming` | Avant la première étape, l'étape 0 tranche le chemin en une phrase (pour soi, pour un client, ou un système qui existe) et regarde ce qui existe déjà : le registre des systèmes, les compétences (par skill-finder), le centre « Créer des agents et des systèmes IA », les sessions qui ont déjà travaillé le sujet, les notes et documents déjà écrits sur le sujet. Le travail passé se reprend, il ne se refait pas. Pour soi : le cadrage d'un chantier, première étape (`/cadrer-un-chantier:cadrer-un-chantier`). Pour un client : la mission se mène avec `/implementer-l-ia-en-entreprise:implementer-l-ia-en-entreprise` (cadrer-besoin, decouvrir-cas-usage quand le besoin n'est pas connu, auditer son processus) ; ce workflow-ci garde les choix propres à l'agent. Pour un système qui existe : cette compétence, puis la passe de cible et de diagnostic de entretenir-son-systeme:optimise-systeme, qui agit sur les règles, les compétences et les documents d'un dépôt Claude Code. |
| 2 | Les questions produit | `agent-skills:spec-driven-development` · `product-management:write-spec` · `product-management:brainstorm` · `cadrer-un-chantier` | Ne poser que ce que les sources ne disent pas. Tout ce qui est mécanique se tranche sans demander ; seuls le goût produit, l'irréversible et les comptes de la personne lui reviennent. Le raisonnement cher va là où l'ambiguïté compte, le contrôle mécanique reste en code. Pour un client : auditer-processus, rediger-cahier-des-charges (exigences) et chiffrer-rentabilite, avec `/implementer-l-ia-en-entreprise:implementer-l-ia-en-entreprise`. Pour un système qui existe : la mesure et la couverture de entretenir-son-systeme:optimise-systeme. |
| 3 | L'architecture | `engineering:system-design` · `agent-skills:context-engineering` · `bmad-architecture` · `creer-un-agent-ia:systeme-ia` · Trancher : un agent ou une automatisation : `automation-strategy` ; `creer-un-agent-ia:choisir-agent-ou-automatisation` · Trancher un choix d'architecture difficile à défaire : `engineering:architecture` ; `reflechir-a-fond` | Le type se choisit d'abord, par trois questions : qu'est-ce qui le réveille, qui s'en sert et à quelle heure, quelle part demande du jugement. Le local tourne sur un poste allumé, avec l'abonnement de son propriétaire. Dès qu'un client, un visiteur ou un outil doit le réveiller à toute heure, il passe en cloud. Un chemin connu d'avance reste un scénario avec une étape IA, souvent sur n8n ou Make, plutôt qu'un agent. Un agent qui échange avec des personnes dans l'Union européenne leur dit dès le premier message qu'il est une IA, sauf si c'est évident : article 50 du règlement (UE) 2024/1689, applicable depuis le 2 août 2026 (vérifié le 06/11/2026, détail dans `references/types-d-agents.md`). Le kit de la compétence de système suffit pour un système ordinaire, et `agent-skills:context-engineering` dit ce que chaque agent lit à chaque tour. Pour un choix dur : `/reflechir-a-fond:reflechir-a-fond` ou `bmad-architecture`. Pour un client : concevoir-solution et rediger-cahier-des-charges (spécification), avec `/implementer-l-ia-en-entreprise:implementer-l-ia-en-entreprise`. Pour un système qui existe : entretenir-son-systeme:optimise-systeme (trouver, arbitrer, concevoir). Un agent chef qui lance d'autres agents ne tourne qu'en tête de session : une sous-tâche ne peut pas en lancer une autre. Il doit avoir l'outil de lancement (nommé Agent) dans sa liste d'outils, et Claude Code limite par défaut l'imbrication à trois niveaux de sous-agents (vérifié le 06/11/2026, https://code.claude.com/docs/en/sub-agents). Il écrit d'abord son plan de travail dans un fichier, ce qui permet de reprendre si on le lance ailleurs. |
| 4 | Construire | `claude-api:claude-api` · `skill-creator:skill-creator` · `example-skills:mcp-builder` · Construire la solution d'un client en environnement d'essai : `agent-skills:incremental-implementation` ; `consultant-ia:construire-solution` · Agent local : un assistant dans sa session : `plugin-dev:agent-development` ; `plugin-dev:command-development` ; `plugin-dev:mcp-integration` · Agent local : une tâche qui revient : `superviser-ses-sessions:loop-creator` · Agent cloud en code : assistant ou déclenché par un événement : `creer-un-agent-ia:agents-cloud` · Agent sur n8n : assistant, planifié ou déclenché : `n8n-skills:n8n-workflow-lifecycle-official` ; `creer-un-agent-ia:n8n-workflow-builder` · Agent sur Make : assistant, planifié ou déclenché : `make-skills:make-endpoints` · Construire un serveur MCP : `mcp-server-dev:build-mcp-app` ; `mcp-server-dev:build-mcp-server` ; `mcp-server-dev:build-mcpb` · Construire un agent avec Atomic Agents : `atomic-agents:create-atomic-agent` ; `atomic-agents:create-atomic-tool` ; `atomic-agents:framework` ; `atomic-agents:new-app` · Créer un plugin : `cowork-plugin-management:cowork-plugin-customizer` ; `cowork-plugin-management:create-cowork-plugin` | Le kit de l'étape 3 dit les pièces à bâtir, chacune par sa compétence. Les compétences de l'agent s'écrivent avec skill-creator et passent leur porte de qualité à l'étape 5. Ses outils viennent de mcp-builder quand il doit agir dans un service. Une tâche qui revient se planifie sur le poste (planificateur de l'ordinateur) ; les routines passent par routine ; une tâche longue qui doit se réveiller seule prend la cadence de `superviser-ses-sessions:loop-creator`, logée au cadrage d'un chantier. Le code passe par claude-api:claude-api quand l'agent vit dans une app. Le tableau de bord se bâtit à l'étape 6, avec la mesure qu'il affiche. Pour un agent livré à un client : l'installation s'écrit pour un agent de code, avec ce qui reste à la personne et ce qu'il vérifie avant de continuer ; l'identité du client vient de l'appel entrant et les délais du code, jamais du modèle ; les pages légales sont servies depuis la configuration réelle. Pour un client, avec `/implementer-l-ia-en-entreprise:implementer-l-ia-en-entreprise` : après le plan de déploiement (planifier-deploiement), consultant-ia:construire-solution bâtit par tranches en environnement d'essai, sur des données fictives ou anonymisées, et écrit 80-construction dans le dossier de mission ; une solution qui est une app passe par le workflow Créer une app. Rien ne touche un outil réel à cette étape ; la mise en service reste à consultant-ia:piloter-mise-en-service. Pour un système qui existe : les compétences propriétaires des objets touchés. |
| 5 | Tester | `agent-skills:doubt-driven-development` · `engineering:testing-strategy` · `consultant-ia:tester-solution` · `entretenir-son-systeme:skill-quality-guard` · Évaluer la partie IA : `logfire:logfire-evals` · Chercher la cause d'un échec n8n : `n8n-skills:n8n-debugging-official` | Quatre preuves, dans cet ordre. D'abord les cas de test et les évaluations écrits à l'étape 4 (ceux de skill-creator pour une compétence, ceux de mcp-builder pour un outil), puis la porte de qualité de chaque compétence. Ensuite les contrôles testés par sabotage : on casse exprès ce qu'ils gardent, et ils doivent signaler l'erreur. Puis un pré-mortem (on imagine que l'agent a échoué et on en cherche les causes) et un relecteur au contexte neuf, séparé de celui qui a produit, qui rend du vérifiable : l'affirmation, le verdict, la source, la correction à faire. Enfin un essai de bout en bout : l'agent fait sa tâche sur son modèle prévu, dans une conversation neuve et sur un faux environnement (jamais un vrai compte), car cet essai trouve ce que les tests ne voient pas. Pour un client, avec `/implementer-l-ia-en-entreprise:implementer-l-ia-en-entreprise` : consultant-ia:tester-solution fait la recette critère par critère, évalue la partie IA à part et rend un verdict (prêt, prêt avec réserves, pas prêt), écrit dans 85-recette, puis la mise en service se pilote. Une recette réussie ne prouve pas que l'IA est bonne, et l'inverse. Pour un système qui existe : la re-mesure de entretenir-son-systeme:optimise-systeme. |
| 6 | Mettre en service | `agent-skills:shipping-and-launch` · `engineering:deploy-checklist` · `operations:runbook` · `consultant-ia:piloter-mise-en-service` | Après une recette au verdict prêt (85-recette). Le retour arrière existe avant chaque action sur un outil réel, et la bascule se décide par écrit ; une solution que personne n'utilise n'est pas en service. Pour un client : consultant-ia:piloter-mise-en-service écrit 90-mise-en-service dans le même dossier de mission ; une fois validée au journal, la mesure (95) repart au pack conseil avec mesurer-gains. Pour son propre système : la mise en service se résume à brancher l'agent sur son vrai environnement, avec son retour arrière. |
| 7 | Mesurer | Publier une page du hub interne : `project-artifact:project-artifact` ; `creer-un-agent-ia:dashboards-hub-master` · Mesurer : `agent-skills:observability-and-instrumentation` ; `entretenir-son-systeme:optimise-systeme` · Évaluer l'agent sur des cas réels : `exploring-ai-failures` | D'abord ce que « marcher » veut dire, en deux à quatre questions. Puis l'agent instrumenté pour y répondre, l'usage et le coût compris. Le tableau de bord affiche le chiffre du but et son point de départ ; le système lui-même se mesure avec entretenir-son-systeme:optimise-systeme. Pour un client : mesurer-gains, qui juge le gain observé et non les traces de l'outil. Pour un système qui existe : la re-mesure sans perte de entretenir-son-systeme:optimise-systeme. |
| 8 | Capitaliser : le flywheel | `agent-skills:documentation-and-adrs` · `superpowers:writing-skills` · `creer-un-agent-ia:router-capitalisation` · `entretenir-son-systeme:capitaliser` · Ranger une leçon dans les règles toujours chargées : `entretenir-son-systeme:clean-rules-cleanup` | Même un passage sans correction le dit en une ligne. Une correction propre à la tâche reste avec elle, une réutilisable entre dans la méthode, une vérifiable devient un contrôle. On promeut avec prudence : une fois une observation, deux fois un motif, répétée une règle candidate, confirmée une règle, une compétence, un test ou de la mémoire. La même erreur corrigée deux fois change la méthode, pas seulement la sortie. Chaque échec instructif garde sa tâche, sa mauvaise sortie et l'attendu, rejoués à chaque changement du système. Pour un client : le journal de mission du pack, puis creer-un-agent-ia:router-capitalisation. La mesure du flywheel (acceptation du premier coup, erreurs qui reviennent, temps de relecture, coût par résultat accepté) n'est pas encore faite : il faut une trentaine de passages. |
<!-- etapes:fin -->

**Le chemin « client »** s'appuie sur `/implementer-l-ia-en-entreprise:implementer-l-ia-en-entreprise`, qui mène la
mission chez un client de bout en bout : cadrer son besoin (et découvrir d'abord ses cas d'usage s'il n'est pas
connu), auditer son processus, écrire les exigences, chiffrer la rentabilité, concevoir et spécifier, construire en
environnement d'essai, tester, mettre en service, mesurer le gain observé. Ce workflow-ci ajoute les choix propres à
l'agent (type, architecture, test, capitalisation) ; il ne refait pas la mission.

**Le type d'agent se choisit à l'étape 3, avant de construire.** Six types (assistant, planifié, déclenché par un
événement, lecteur de documents, plusieurs agents, scénario avec une étape IA), local ou cloud, sur n8n, Make ou
en code : `references/types-d-agents.md`. Contrôle : *qu'est-ce qui le réveille, et le poste sera-t-il allumé ?*

**Un agent qui parle à des personnes dans l'Union européenne dit qu'il est une IA, dès le premier message**, sauf si
c'est évident (article 50 du règlement (UE) 2024/1689, applicable depuis le 2 août 2026, vérifié le 06/11/2026 ;
`references/types-d-agents.md`, section « Dire que c'est une IA »). Un agent sur WhatsApp :
`references/agent-sur-whatsapp.md`, à lire avant l'étape 3.

**L'essai de bout en bout, à l'étape 5.** Certains défauts n'apparaissent qu'en faisant tourner l'agent. Contrôle :
*l'agent, sur son modèle prévu, a-t-il fait la tâche dans une conversation neuve, sur un faux environnement ?* Quatre
règles qui en découlent :

- **Une sortie d'outil dit la raison, pas seulement le résultat.** Un outil qui répond « rien trouvé » ou « refusé »
  sans dire pourquoi (destinataire inactif, droit manquant) laisse l'agent inventer ou abandonner.
- **Un mode qui agit pour de vrai ne s'active jamais par omission.** Envoyer, écrire, payer : l'agent part par
  défaut en mode d'essai (un banc d'essai sur un faux environnement), et le mode réel demande un choix écrit.
- **Un petit modèle a besoin de la forme exacte des commandes.** Si l'agent tourne sur un modèle léger, ses consignes
  donnent un exemple complet de chaque commande, sinon il multiplie les appels.
- **Les verrous s'éprouvent avec l'agent livré.** Les restrictions d'outils et les crochets (hooks, petits programmes
  que Claude Code lance avant ou après une action) ne se testent qu'avec l'agent tel qu'il sera livré, ses réglages
  chargés : un essai sans eux ne prouve rien sur les garde-fous.

**Agents cloud.** Tout agent hébergé a besoin d'une clé, d'un plafond de budget, de traces et d'un moyen de le
couper. Donner des outils à un agent qui passe par l'API : `references/outils-agent-cloud.md`. Pour un agent qui
répond à partir de nombreux documents, un modèle puissant mène la conversation et des sous-agents plus petits lisent
les documents.

**Plusieurs agents sous un chef.** Un agent chef lance d'autres agents (des sous-agents) : il doit avoir l'outil de
lancement, nommé Agent, dans sa liste d'outils. Claude Code limite par défaut l'imbrication à trois niveaux de
sous-agents (vérifié le 06/11/2026, https://code.claude.com/docs/en/sub-agents). Le chef écrit sa feuille de route
dans un fichier avant de lancer quoi que ce soit, pour qu'on puisse reprendre s'il s'arrête. Ce qui se calcule (un
seuil, un ordre de priorité) se fait dans un script testé, jamais par le modèle.

### Les questions produit (étape 2)

Ne poser que ce que les sources ne disent pas ; chaque réponse a sa maison.

1. **Pour qui, et quel résultat continu ?** Le but dans les mots de la personne.
2. **Comment saura-t-on que ça marche ?** La mesure, chiffrée, et son point de départ.
3. **Quel est le dernier clic humain ?** Ce que le système ne fait jamais seul : la table d'autonomie à quatre
   niveaux de `/cadrer-un-chantier:cadrer-un-chantier`.
4. **Quelles sources, et quelle mémoire unique ?** Où le système lit ; où il écrit son état.
5. **Qu'est-ce qui déclenche chaque action ?** Un événement, une date ou un seuil.
6. **Que coûte une erreur, et qui la voit ?** Le risque, le relecteur, le retour arrière.
7. **Combien ça coûte à faire tourner ?** Le modèle et l'effort de chaque étape : le raisonnement cher là où
   l'ambiguïté compte, le reste au plus simple, le contrôle mécanique en code.
8. **Qu'est-ce qui existe déjà, ici ou dehors ?** Chercher avant de construire.

Tranché ici ce qui est mécanique ; à la personne seulement le goût produit, l'irréversible, ses comptes. La fiche
de cadrage d'un écran est celle de `/cadrer-un-chantier:cadrer-un-chantier`.

### La capitalisation (étape 7)

- **Chaque passage laisse quatre choses** dans le journal de l'agent : le résultat ; l'état (ce qui est décidé, ce
  qui reste, la prochaine action) ; la leçon (ce qu'il a fallu corriger) ; l'amélioration candidate.
- **Chaque correction se classe** : propre à la tâche, elle reste avec la tâche ; réutilisable, elle entre dans la
  méthode ; vérifiable, elle devient un contrôle.
- **Chaque amélioration a son propriétaire** : une règle passe par `entretenir-son-systeme:clean-rules-cleanup`
  et son registre des motifs ; une compétence par `entretenir-son-systeme:capitaliser`, puis
  `entretenir-son-systeme:skill-quality-guard` ; un test rejoint les cas de test de la compétence ; de la
  mémoire va dans l'état du système ou la mémoire du projet.
- **La même erreur corrigée deux fois** : on change la méthode, plus seulement la sortie.
- **On promeut avec prudence** : une fois, une observation ; deux fois, un motif ; répétée, une règle candidate ;
  confirmée, une règle, une compétence, un test ou de la mémoire. Le but est de progresser, pas d'empiler des
  règles.
- **La bibliothèque d'échecs** : chaque échec qui a révélé une faiblesse garde sa tâche, sa mauvaise sortie et
  l'attendu. On la rejoue à chaque changement du système et on compte : corrigés, encore en échec, nouvelles
  régressions.
- **Le modèle propose, un humain valide** : après un échec, diagnostiquer la cause (consigne ou contexte
  manquant, compétence faible, test absent, outil mal décrit, permission, preuve insuffisante, demande
  ambiguë), proposer la plus petite amélioration réutilisable, la faire relire, l'intégrer, puis rejouer
  l'échec.
- **Le relecteur est séparé** de celui qui produit, et il rend du vérifiable : l'affirmation, le verdict, la
  source, la correction à faire.
- **La mesure** : le taux d'acceptation du premier coup, le taux d'erreurs qui reviennent, le temps de relecture
  humaine, le coût par résultat accepté, la part des corrections devenues infrastructure. Suivis sur plusieurs
  passages, ces chiffres disent s'il y a une amélioration continue ou seulement de l'automatisation.

### Pages de référence

- `references/types-d-agents.md` : les six types, local ou cloud, n8n, Make ou code, où construire chacun.
- `references/outils-agent-cloud.md` : donner des outils à un agent qui passe par l'API.
- `references/agent-sur-whatsapp.md` : ce que dit la politique de WhatsApp Business, consentement, file d'attente
  durable, effacement.

## Frontières

- Cadrer un chantier qui n'est pas un agent ni un système : `/cadrer-un-chantier:cadrer-un-chantier`.
- Un choix d'architecture difficile à défaire : `/reflechir-a-fond:reflechir-a-fond`.
- Une app, un SaaS ou une plateforme autour des agents : `/creer-une-app:creer-une-app`.
- Brancher des outils et des agents dans une entreprise, en mission chez un client :
  `/implementer-l-ia-en-entreprise:implementer-l-ia-en-entreprise`.
- Armer la cadence d'une tâche longue : `superviser-ses-sessions:loop-creator`.

## Ce qui manque

- Poser le problème, les questions produit (hors la fiche de cadrage), l'architecture d'un agent pour soi et la
  capitalisation n'ont pas de compétence publique : ces gestes se font à la main, avec la règle de l'étape.
- Construire un agent cloud en code, l'exploiter, un agent sur Make ou sur WhatsApp : pas de compétence publique,
  voir les pages de référence. Pour n8n, une compétence officielle couvre le cycle d'un flux, pas les nœuds d'agent.
