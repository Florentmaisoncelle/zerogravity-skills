# Les types d'agents : quoi construire, où il tourne, sur quoi

À lire à l'étape 3 de `/creer-un-agent-ia:creer-un-agent-ia`. Un agent n'est pas seulement local : il existe aussi
des agents cloud, qui font ce qu'on fait avec n8n ou Make. Pour leur donner des outils : `outils-agent-cloud.md`.

## Trois questions, dans l'ordre

1. **Qu'est-ce qui le réveille ?** Une personne qui lui parle, une date, ou un événement extérieur.
2. **Qui s'en sert, à quelle heure ?** Soi-même devant son poste, ou un client, un visiteur, un outil, à toute heure.
3. **Quelle part demande du jugement ?** Si le chemin est connu d'avance, c'est un scénario avec une étape IA, pas
   un agent : moins cher, plus sûr, plus simple à reprendre.

## Les six types

| Type | Ce qu'il fait | Avec n8n ou Make | En local (sur le poste) | En cloud, sans n8n ni Make |
|---|---|---|---|---|
| **Assistant** | on lui parle, il répond et agit | nœud AI Agent et déclencheur de chat ; Make AI Agents | une session Claude Code, un sous-agent, une compétence | API Claude avec ses outils derrière un site ; Managed Agents, une session par client |
| **Planifié** | revient à heure fixe, fait sa tâche, laisse son résultat | déclencheur planifié ; planification d'un scénario | une tâche planifiée du poste, la commande loop dans une session ouverte (elle s'arrête avec la session et expire après 7 jours) | tâche planifiée dans le cloud d'Anthropic (commande schedule, intervalle minimal d'une heure) ; fonction serveur et tâche planifiée de la base |
| **Déclenché par un événement** | un formulaire, un mail, un CRM ou un paiement le réveille | déclencheur webhook ou applicatif | à éviter : l'événement se perd si le poste dort | fonction serveur qui reçoit l'événement et appelle l'API ou ouvre une session Managed Agents |
| **Lecteur de documents** (RAG) | cherche dans une base avant de répondre | base vectorielle et outil de recherche branchés à l'agent | une compétence qui lit un dossier | un outil de recherche dans une base vectorielle (voir `outils-agent-cloud.md`) |
| **Plusieurs agents** | un chef répartit, des spécialistes font | un agent appelle d'autres workflows comme outils | sous-agents d'une session Claude Code | Managed Agents multi-agents : un chef puissant, des lecteurs plus petits |
| **Scénario avec une étape IA** | un chemin fixe, l'IA classe, résume ou extrait à un endroit | c'est leur terrain : un scénario et un nœud IA | un script et un appel en ligne de commande | du code et un appel à l'API, sortie structurée |

Ces types se combinent : un assistant peut lancer un scénario, un agent planifié peut lire des documents.

## Local ou cloud

| Prendre le local quand… | Prendre le cloud quand… |
|---|---|
| le poste est allumé aux heures utiles | il doit répondre à toute heure |
| une personne suit le travail et donne le dernier clic | un visiteur, un client ou un autre outil s'en sert |
| il lit des fichiers du poste, ou pilote une application ou un navigateur connecté | ses données vivent dans des outils en ligne |
| l'abonnement de son propriétaire couvre l'usage | on le déploie chez plusieurs clients, avec un budget par client |

Un agent local coûte l'abonnement et s'arrête avec le poste. Un agent cloud coûte à l'usage et demande une clé, un
plafond de budget, des traces et un moyen de le couper.

## n8n, Make, ou du code

| Choisir | Quand |
|---|---|
| **n8n ou Make** | beaucoup d'outils à brancher avec leurs comptes, un chemin surtout fixe, un client qui veut voir et reprendre son flux sans développeur |
| **Du code et l'API** | la main sur chaque appel : coût, validation humaine, sécurité, agent public sur un site |
| **Managed Agents** | le même agent chez beaucoup de clients, un espace de travail par session, clés dans un coffre |
| **Les deux** | l'agent décide, le flux n8n exécute : n8n expose un workflow comme un outil MCP, l'agent l'appelle |

Le prix et les capacités de n8n, de Make et de l'API se revérifient le jour du choix.

## Les briques d'un agent cloud chez un client

À prévoir pour chaque agent déclenché ou planifié, et à essayer contre un vrai compte avant tout usage réel :

| Brique | Ce qu'elle garantit |
|---|---|
| Webhook entrant | signature vérifiée, anti-doublon, reprise après échec |
| Connecteur par client | OAuth ou clé par compte, gardés dans un coffre |
| File de validation | l'agent propose ses écritures, une personne valide d'un clic par lot |
| Banc d'essai sur faux environnement | essayer un agent sans toucher un vrai compte |

Pour chaque agent, écrire aussi ce qu'il ne fait pas et qui le fait.

## Dire que c'est une IA

Dans l'Union européenne, tout système d'IA qui échange directement avec une personne le lui dit : c'est l'article 50
du règlement (UE) 2024/1689, applicable depuis le 2 août 2026 (texte : https://eur-lex.europa.eu/legal-content/FR/TXT/HTML/?uri=CELEX:32024R1689 ;
[FAQ de la Commission](https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act) ;
vérifié le 06/11/2026). Le règlement (UE) 2026/1744 de juillet 2026 ne reporte pas cet article : il laisse seulement jusqu'au 2 décembre 2026
aux systèmes qui génèrent des contenus de synthèse et étaient déjà sur le marché avant le 2 août 2026 pour se mettre
en conformité avec le marquage des contenus (article 50, paragraphe 2). Hors de l'Union, les règles diffèrent : à vérifier.

- **Qui** : tout système qui échange directement avec une personne ; pas un traitement de fond ni un échange entre
  machines.
- **Quand** : au début du premier échange, clairement, de façon accessible.
- **Exception** : ce qui est évident pour une personne normalement informée et attentive. L'exception se lit
  restrictivement : dans le doute, le dire.
- **Sanction** : l'article 99, paragraphe 4, prévoit jusqu'à 15 M€ ou 3 % du chiffre d'affaires mondial annuel, le plus
  élevé des deux (le plus bas pour les PME). Montants lus sur un site non officiel (https://artificialintelligenceact.eu/article/99/) : à confirmer sur EUR-Lex.

Contrôle : *le premier message de cet agent dit-il qu'il est une IA ?* Un cas de test le vérifie à l'étape 5.

## Trois réflexes d'un agent livré à un client

1. **Une installation écrite pour un agent de code** : ce qu'il fait seul, ce qui reste à la personne, ce qu'il
   vérifie avant de passer à la suite. Le client ne lit pas un mode d'emploi, son agent le suit.
2. **Ce que le modèle ne décide pas** : l'identité du client vient de l'appel entrant, jamais de ce que dit le
   modèle, et les délais se calculent dans le code. Sinon, un message piégé change de client ou de date.
3. **Des pages légales servies depuis la configuration réelle** : elles disent ce que l'agent fait vraiment, et ne
   peuvent pas s'en écarter.

## Où construire chaque type

| Type | Compétences |
|---|---|
| Agent local | `plugin-dev:agent-development`, `skill-creator:skill-creator`, `superviser-ses-sessions:loop-creator` pour une tâche longue |
| Agent cloud en code | `claude-api:claude-api` ; les outils : `outils-agent-cloud.md` |
| n8n | `n8n-skills:n8n-workflow-lifecycle-official` pour le cycle d'un flux ; le nœud AI Agent à la main ; ou `/implementer-l-ia-en-entreprise:implementer-l-ia-en-entreprise` |
| WhatsApp | aucune compétence ; avant tout : `agent-sur-whatsapp.md` |
| Make | aucune compétence retenue ici ; les agents se construisent dans Make |

## Ce qui reste à vérifier

- Les libellés des nœuds n8n et de Make AI Agents : à relire dans leur documentation avant de les citer.
- Les faits de cette page sur la commande loop, la commande schedule et l'article 50 ont été vérifiés le 06/11/2026 ; les prix et capacités de n8n, de Make et de l'API se revérifient le jour du choix.
