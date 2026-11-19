---
name: implementer-l-ia-en-entreprise
description: >-
  Pour un consultant ou un indépendant en mission chez un client, qui veut implémenter l'IA ou l'automatisation de bout en bout (« où l'IA peut-elle nous aider ? », « on veut automatiser la relance des factures », « une mission IA chez ce client », « audit IA puis mise en place », « où en est la mission ? ») → enchaîner les cinq étapes : le conseil, mené par la porte du pack de conseil en IA (`consultant-ia:router-conseiller-une-mission-ia`, de la découverte au plan), puis construire en essai, tester, mettre en service et faire adopter, mesurer le gain. Se lance par `/implementer-l-ia-en-entreprise:implementer-l-ia-en-entreprise`. Déclencheurs : « mission IA », « implémenter l'IA en entreprise », « stratégie d'automatisation pour un client ». Pas pour créer son propre agent ou système (`/creer-un-agent-ia:creer-un-agent-ia`), ni pour trancher une stratégie d'entreprise (`/decider-une-strategie:decider-une-strategie`).
---

# Implémenter l'IA en entreprise : de l'idée à la solution mesurée, chez un client

Ce workflow est fait pour **un consultant ou un indépendant en mission chez un client**. Il sort donc du public « gérer sa propre
petite entreprise » des autres workflows du dépôt : une personne d'une entreprise peut aussi s'en servir pour mener sa propre
mission interne, mais il suppose un rôle de conseil (cadrer, diagnostiquer, recommander, mettre en service). Pour créer
son propre agent, voir `/creer-un-agent-ia:creer-un-agent-ia`.

## Ce que ça résout

Une mission d'IA se perd de deux façons : on part sur une solution avant d'avoir compris le travail réel, ou on annonce des gains qu'on n'a jamais mesurés. Ici, la chaîne qui traverse les packs : le conseil (pack consultant-ia), puis la construction, la recette et la mise en service, puis la mesure, plus des compagnons d'autres éditeurs quand ils sont installés.

**Résultat attendu** : un client dont le besoin est cadré, la solution choisie et chiffrée, construite en essai, recettée (c'est-à-dire acceptée sur des critères écrits), mise en service avec son retour arrière, adoptée, et dont le gain est mesuré sur relevés réels.

**Les mots utilisés ici**
- **Cas** : un processus précis à traiter (par exemple la relance des factures), qui a son propre dossier.
- **Recette** : l'acceptation de la solution sur des critères écrits à l'avance.
- **Pilote** : une première mise en service limitée à un petit groupe, sous surveillance renforcée.
- **Porte** : une condition à constater avant de démarrer une étape (par exemple « les relevés de départ existent »).
- **Pré-mortem** : on imagine que le projet a échoué et on en cherche les causes avant de commencer.
- **Exploitant** : la personne qui fera vivre la solution après la mission.

## Stratégie

1. **La table des étapes plus bas fait foi.** Elle donne, pour chaque étape, la compétence et la règle de choix.
2. **Le conseil n'est pas redit ici.** Sa porte est `consultant-ia:router-conseiller-une-mission-ia` : elle calcule l'état de la mission depuis le dossier `mission/`, tranche la porte d'entrée (un besoin qui se nomme en une phrase, ou une découverte d'abord), lance chaque étape de conseil de la découverte au plan et tient le journal des décisions. Pour savoir où en est une mission, on la lance : elle affiche l'état et la prochaine étape, puis s'arrête.
3. **Deux modes.** Avec un consultant, la personne et lui déroulent la chaîne. Sans consultant dans la conversation (la personne répond seule à un agent), l'agent mène le conseil par écrit ; un consultant relit le chiffrage, la spécification et le plan avant que la personne les valide ; construire, tester, mettre en service et mesurer ne se font pas dans ce mode.
4. **Le pack consultant-ia est la base de ce workflow.** Il est publié à part, installé avec les prérequis. Sans lui, chaque étape se fait à la main : la règle de choix dit ce que l'étape doit produire et comment.
5. **Une compétence, un seul endroit.** Une compétence d'un autre workflow (le mode opératoire, la demande de changement) est citée là où elle vit, jamais recopiée.
6. **L'ordre protège la décision.** Pas de comparaison de solutions sans exigences, pas de chiffrage d'une option non décrite, pas de construction sans plan validé, pas de mise en service sans recette, pas de gain déclaré sans relevé.
7. **Une validation, au cadrage.** Ensuite on déroule, étape par étape, chaque livrable validé par la personne avant la suivante. Restent au client : chaque action sur son outil réel, le feu vert du pilote, la bascule.
8. **Les compagnons d'autres éditeurs sont facultatifs.** Ils s'installent à part, et leurs conditions d'emploi (accès, licence, garde des traces) sont dans `references/compagnons-a-installer.md` ; trois d'entre eux (automation-strategy, exploring-ai-failures, querying-posthog-data) s'installent avec `npx`, et leurs commandes sont dans ce fichier.
9. **Tout texte qui sort au nom de l'entreprise cliente se relit avant d'être envoyé.** À la fin de chaque passage, la décision est notée au journal.

<!-- prerequis:debut -->
## Prérequis

Ce workflow s'appuie sur des compétences publiques, installées à part. Aucune n'est indispensable : si l'une manque, le workflow le dit et fait l'étape à la main. Faire l'étape à la main veut dire suivre sa règle de choix, écrire ce qu'elle doit rendre (dans le fichier de l'étape, ou dans la réponse quand le workflow n'a pas de dossier) et dire ce qui reste à la charge de la personne.

```text
/plugin marketplace add Florentmaisoncelle/zerogravity-skills
/plugin marketplace add addyosmani/agent-skills
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin marketplace add integromat/make-skills
/plugin marketplace add n8n-io/skills
/plugin marketplace add pydantic/skills
/plugin install agent-skills@addy-agent-skills
/plugin install consultant-ia@zerogravity
/plugin install engineering@knowledge-work-plugins
/plugin install logfire@pydantic-skills
/plugin install make-skills@make-marketplace
/plugin install n8n-skills@n8n-io
/plugin install operations@knowledge-work-plugins
/plugin install product-management@knowledge-work-plugins
/plugin install skill-creator@claude-plugins-official
/plugin install superpowers@claude-plugins-official
npx skills add PostHog/skills --skill exploring-ai-failures -a claude-code
npx skills add PostHog/skills --skill querying-posthog-data -a claude-code
npx skills add ericrisco/rsc-harness --skill automation-strategy -a claude-code
```

La commande `npx skills add` (CLI Vercel `skills`) demande Node.js 22.20 ou plus (vérifié le 06/11/2026, https://github.com/vercel-labs/skills). Claude Code installé avec l'installeur natif n'en a pas besoin.

Les workflows cités ici sont dans le même dépôt (le dépôt s'ajoute une fois : `/plugin marketplace add Florentmaisoncelle/zerogravity-skills`) :

```text
/plugin install cadrer-un-chantier@zerogravity
/plugin install creer-un-agent-ia@zerogravity
/plugin install decider-une-strategie@zerogravity
/plugin install organiser-sa-force-de-vente@zerogravity
/plugin install reflechir-a-fond@zerogravity
```
<!-- prerequis:fin -->

## Étapes

### 1. Lancer l'étape suivante

Pour le conseil (étape 1), lancer `consultant-ia:router-conseiller-une-mission-ia`. Ensuite, lire l'étape dans la table, appliquer sa règle de choix, invoquer la compétence retenue avec le chemin du dossier du cas, écrire sa sortie dans le fichier de l'étape, faire trancher la personne, puis inscrire sa décision au journal, au format du pack, avant de passer à la suivante. La construction et la recette (étapes 2 et 3) sont sans objet quand la stratégie retient de ne rien construire.

<!-- etapes:debut -->
| # | Étape | Compétences | Règle de choix |
|---|---|---|---|
| 1 | Conseiller : de la découverte au plan de déploiement | `consultant-ia:router-conseiller-une-mission-ia` · Écrire la spécification de la solution : `product-management:write-spec` ; `agent-skills:spec-driven-development` · Évaluer les risques avant de construire : `operations:risk-assessment` · Mettre le processus à plat avant d'automatiser : `operations:process-doc` ; `operations:process-optimization` | Le conseil se mène par la porte du pack ; ses étapes, leurs compétences et leurs fichiers vivent sur sa page (« Conseiller une mission IA ») et ne se redisent pas ici. On ne construit qu'avec le plan (70-plan.md) validé au journal. Sans consultant dans la conversation, le parcours s'arrête au plan. |
| 2 | Construire dans un environnement d'essai | Construire un scénario n8n : `n8n-skills:n8n-workflow-lifecycle-official` · Agir directement dans les applications d'un compte Make (Endpoints) : `make-skills:make-endpoints` · Construire par tranches contrôlables : `agent-skills:incremental-implementation` ; `agent-skills:source-driven-development` ; `agent-skills:documentation-and-adrs` ; `consultant-ia:construire-solution` | La construction se fait par le workflow « Créer un agent IA » (étape Construire), qui lit 60-specification.md et 70-plan.md et écrit 80-construction.md dans le même dossier de mission. Rien ne touche un outil réel à cette étape, et elle ne s'ouvre que si le plan (70-plan.md) est validé au journal. Le tronc est commun à toutes les plateformes ; l'outil retenu à la stratégie d'automatisation décide de l'adaptateur. Pour un agent écrit en code : `/creer-un-agent-ia:creer-un-agent-ia`. Construire un scénario Make lui-même se fait à la main dans Make (le dépôt integromat/make-skills propose d'autres compétences pour cela, que ce workflow ne liste pas). Sans objet quand la stratégie retient de ne rien construire. |
| 3 | Tester et recetter | `skill-creator:skill-creator` · Écrire le plan de recette : `engineering:testing-strategy` · Chercher la cause d'un échec n8n : `n8n-skills:n8n-debugging-official` · Passer la recette et rendre le verdict : `superpowers:verification-before-completion` ; `superpowers:systematic-debugging` ; `consultant-ia:tester-solution` · Évaluer la partie IA sur un jeu étiqueté : `logfire:logfire-evals` | La recette se fait par le workflow « Créer un agent IA » (étape Tester), qui écrit 85-recette.md dans le même dossier. Une recette réussie ne prouve pas que l'IA est bonne, et l'inverse : les deux se jugent séparément, avec les seuils de la spécification. Elle ne s'ouvre que si la construction est déclarée prête pour la recette au journal. Sans objet quand la stratégie retient de ne rien construire. |
| 4 | Mettre en service et faire adopter | Déployer un assistant IA dans une équipe : `consultant-ia:deployer-assistant-ia` · Préparer la bascule et le retour arrière : `engineering:deploy-checklist` ; `agent-skills:shipping-and-launch` ; `operations:change-request` ; `consultant-ia:piloter-mise-en-service` · Annoncer le changement à l'équipe : `product-management:stakeholder-update` · Transférer à un exploitant nommé : `operations:runbook` | La mise en service se fait par le workflow « Créer un agent IA » (étape Mettre en service), qui lit 85-recette.md et écrit 90-mise-en-service.md dans le même dossier de mission ; validée au journal, la mesure (95) revient ici avec mesurer-gains. Elle ne s'ouvre que si le verdict de la recette est « prêt » ou « prêt avec réserves », validé au journal. Quand rien n'est construit (construction et recette sans objet), il n'y a pas de recette : elle s'ouvre sur le plan (70-plan.md) validé au journal. Le retour arrière existe avant l'action, et la bascule se décide par écrit. L'adoption fait partie de la mise en service : une solution que personne n'utilise n'est pas en service. |
| 5 | Mesurer le gain et maintenir | `consultant-ia:router-conseiller-une-mission-ia` · Relever le gain réel et les coûts sur relevés : `consultant-ia:mesurer-gains` · Rendre compte du gain et des risques au client : `operations:status-report` · Maintenir la solution et traiter les incidents : `engineering:incident-response` ; `agent-skills:observability-and-instrumentation` | La mesure se mène par la porte du pack ; son étape (« Mesurer le gain », la neuvième de « Conseiller une mission IA »), ses tâches et leurs compétences vivent sur sa page et ne se redisent pas ici. Elle ne s'ouvre que si la bascule est inscrite au journal. |
<!-- etapes:fin -->

### 2. Clore un passage

On inscrit la décision au journal (format du pack), puis on note ce que le passage a appris. Un cas se clôt après la mesure, par une ligne du journal qui nomme la décision finale.

## Pourquoi cet ordre

- Les fichiers de la mission sont numérotés dans l'ordre du travail (10, 20, 30, 40, 50, 60, 70, 80, 85, 90, 95) : les six premiers jusqu'au plan viennent du conseil, les trois suivants de la construction, de la recette et de la mise en service, le dernier de la mesure.
- Le conseil passe la main à la construction avec le plan validé ; la mesure revient au conseil, qui compare les relevés au chiffrage de départ.

## Ce qui manque

- Les compagnons d'autres éditeurs (n8n, Make, évaluation, mesure) sont facultatifs et installés à part.

## Frontières

| Demande | Va à |
|---|---|
| Créer son propre agent ou système IA | `/creer-un-agent-ia:creer-un-agent-ia` |
| Trancher une question de stratégie d'entreprise | `/decider-une-strategie:decider-une-strategie` |
| Enquêter sur un système ou une cause technique | `/reflechir-a-fond:reflechir-a-fond` |
| Cadrer un chantier avant d'agir | `/cadrer-un-chantier:cadrer-un-chantier` |
| Choisir, installer ou refondre un CRM | hors de ce workflow ; seul l'audit d'un CRM est une tâche du conseil |
