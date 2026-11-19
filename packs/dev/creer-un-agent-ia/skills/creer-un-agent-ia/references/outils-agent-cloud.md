# Donner des outils à un agent cloud (un agent qui passe par l'API Claude)

À lire aux étapes 3 et 4 de `/creer-un-agent-ia:creer-un-agent-ia`. `claude-api:claude-api` fait autorité pour les
noms exacts des paramètres et les en-têtes bêta ; cette page ne garde que le raisonnement.

## Ce que « cloud » veut dire ici

Un agent cloud est **un programme qui appelle l'API Claude depuis un serveur** (Vercel, Supabase, ou les serveurs
d'Anthropic avec Managed Agents). Il tourne sans personne devant un écran, et il sert les visiteurs d'un site ou
les clients d'une offre. Ce n'est ni Claude Desktop, ni Claude Code, ni Claude dans Chrome : ces trois-là sont des
applications pilotées par une personne, sur son poste, avec son compte. Elles reçoivent des outils par les
connecteurs et les MCP de l'application, pas par un appel à l'API.

## Le principe

Un agent qui passe par l'API ne touche jamais un outil lui-même. Le code de l'application lui présente une liste
d'outils ; Claude dit lequel appeler et avec quoi ; le code (ou Anthropic) l'exécute et rend le résultat ; Claude
continue. Tout passe par un seul point d'entrée : l'API des messages.

Chaque outil est un petit bloc JSON : un nom, une description qui dit quand s'en servir, et le schéma de ce qu'il
attend. La description est la partie qui compte le plus : c'est elle qui fait choisir le bon outil.

## Les quatre sortes d'outils, de la moins chère à la plus lourde

| Sorte | Qui l'exécute | Ce qu'il faut faire | Exemple |
|---|---|---|---|
| Outil fourni par Anthropic (outil serveur) | Anthropic | l'activer dans l'appel, rien à coder | recherche web, lecture d'une page, exécution de code |
| MCP existant, en ligne | Anthropic s'y connecte | donner l'adresse du MCP et sa clé, plus une ligne qui active ses outils (connecteur MCP, en bêta) | le MCP d'un outil de notes pour écrire une page |
| Outil maison | le code de l'application | décrire l'outil en JSON et écrire la fonction (souvent une dizaine de lignes) | une fonction qui appelle l'API publique « Recherche d'entreprises » à partir d'un numéro SIREN |
| Son propre MCP | un petit serveur en ligne | regrouper ses outils maison dans un MCP (`example-skills:mcp-builder`), réutilisable par tous les agents | un MCP maison qui expose une recherche, une fiche entreprise et un calcul de score |

Une API publique n'est pas un outil : c'est une adresse. Elle devient un outil quand on l'enveloppe dans un bloc
JSON et une fonction.

## Les règles de choix

1. **L'outil le plus étroit possible pour un agent public.** Un MCP de développeur (celui d'une base de données,
   par exemple) donne accès à toute la base : un visiteur peut pousser l'agent à lire les données d'un autre
   client. Un agent exposé sur un site reçoit des outils qui ne font qu'une chose, en lecture quand c'est possible.
2. **Le calcul déterministe sort du modèle.** Une note, un total, une règle fixe se calculent dans un script appelé
   comme outil, pas par le modèle. L'agent garde la recherche, le script garde la note.
3. **Un MCP doit être en ligne.** Le connecteur MCP de l'API se branche sur une adresse web, pas sur un serveur qui
   tourne sur le PC.
4. **Les clés ne vont jamais dans le prompt.** Elles restent côté serveur (outil maison) ou dans un coffre
   (Managed Agents).

## En masse : un agent, beaucoup de clients

Deux voies, selon qui fait tourner la boucle :

- **L'API et ses outils** (`claude-api:claude-api`, Tool Runner) : on héberge soi-même le code et la boucle. Le plus
  souple ; on garde la main sur chaque appel (validation humaine, journal, coût).
- **Managed Agents** (toujours en bêta au 06/11/2026, avec un en-tête de version à fournir : « managed-agents-2026-04-01 ») : Anthropic fait tourner l'agent, ses outils, ses MCP et un espace de travail par
  session, et garde les clés dans un coffre que l'agent ne voit pas. On crée l'agent une fois (une configuration
  versionnée), puis une session par client ou par tâche. C'est la voie naturelle pour déployer le même agent chez de
  nombreux clients.

## Chercher dans des documents (RAG)

Faire chercher l'agent dans des documents avant qu'il réponde est un outil comme un autre : une fonction de
recherche interroge une base vectorielle (pgvector dans Supabase, ou un service dédié quand le volume dépasse les
millions de passages), ou bien le MCP de la base, s'il est en ligne. Anthropic ne fournit pas les vecteurs
(embeddings) : il faut un second service, ou l'inférence intégrée de la base. Prix et offres gratuites à vérifier à
la source avant de chiffrer.

## n8n ou l'API ?

Tout ce que fait un agent n8n (appels HTTP, base vectorielle, mémoire, code, MCP), un agent API le fait aussi. n8n
fournit la plomberie toute faite : intégrations branchées avec leurs connexions aux comptes, déclencheurs, relances,
historique, écran visuel. L'API donne la main sur chaque appel (coût, validation humaine, sécurité) et le
déploiement en masse par Managed Agents. Le pont : n8n peut exposer un workflow comme un MCP, que l'agent appelle
comme un outil, pour qu'un agent se serve d'un flux déterministe. Le choix complet : `types-d-agents.md`.

## Références officielles (ouvertes et vérifiées le 06/11/2026)

- Outils d'un agent API : https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview
- Managed Agents, vue d'ensemble : https://platform.claude.com/docs/en/managed-agents/overview
- Managed Agents, démarrage : https://platform.claude.com/docs/en/managed-agents/quickstart
- Managed Agents, connecteur MCP et clés en coffre : https://platform.claude.com/docs/en/managed-agents/mcp-connector

## Ce qui reste à vérifier avant un vrai déploiement

- Les noms exacts des paramètres et des en-têtes bêta : toujours dans `claude-api:claude-api` ou dans la documentation officielle ci-dessus, jamais de mémoire (une bêta change).
- La disponibilité selon la plateforme (API Anthropic, AWS, Google, Microsoft).
- Le dernier clic humain : ce que l'agent ne fait jamais seul chez un client.
