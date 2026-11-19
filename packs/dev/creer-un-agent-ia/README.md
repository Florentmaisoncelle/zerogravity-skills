# Créer un agent ou un système IA, du problème au flywheel

Huit étapes dans l'ordre pour un agent ou un système IA qui marche : poser le problème, répondre aux questions produit, choisir le type d'agent et dessiner l'architecture, construire, tester, mettre en service, mesurer, puis garder la leçon pour que le passage suivant parte plus fort. L'agent peut tourner en local, sur votre poste, ou en cloud, à toute heure : en code, ou sur n8n et Make. Trois chemins sur la même table : son propre système (celui modélisé ici), celui d'un client (Pack Consultant IA) ou un système qui existe (optimisation). Une étape 0 tranche le chemin et regarde l'existant avant la première.

## Installer

```text
/plugin marketplace add Florentmaisoncelle/zerogravity-skills
/plugin install creer-un-agent-ia@zerogravity
```

## Lancer

Dans Claude Code : `/creer-un-agent-ia:creer-un-agent-ia`, ou décrire simplement le besoin.

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

## Licence

MIT. Les compétences tierces citées gardent leur licence et leur auteur : la liste des sources est dans le README du dépôt.
