# Créer une web app ou une plateforme agentique

De l'idée aux premiers clients : onze étapes dans l'ordre, la meilleure compétence à chacune, et les grosses étapes (le site, la construction, les tests, la mise en ligne) sur leur propre page.

## Installer

```text
/plugin marketplace add Gremelinn0/zerogravity-skills
/plugin install creer-une-app@zerogravity
```

## Lancer

Dans Claude Code : `/creer-une-app:creer-une-app`, ou décrire simplement le besoin.

## Prérequis

Ce workflow s'appuie sur des compétences publiques, installées à part. Aucune n'est indispensable : si l'une manque, le workflow le dit et fait l'étape à la main. Faire l'étape à la main veut dire suivre sa règle de choix, écrire ce qu'elle doit rendre (dans le fichier de l'étape, ou dans la réponse quand le workflow n'a pas de dossier) et dire ce qui reste à la charge de la personne.

```text
/plugin marketplace add addyosmani/agent-skills
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin marketplace add anthropics/skills
/plugin marketplace add coreyhaines31/marketingskills
/plugin install agent-skills@addy-agent-skills
/plugin install auth0@knowledge-work-plugins
/plugin install claude-api@anthropic-agent-skills
/plugin install engineering@knowledge-work-plugins
/plugin install marketing-skills@marketingskills
/plugin install product-management@knowledge-work-plugins
/plugin install stripe@claude-plugins-official
/plugin install supabase@claude-plugins-official
npx skills add bmad-code-org/BMAD-METHOD --skill bmad-architecture -a claude-code
npx skills add bmad-code-org/BMAD-METHOD --skill bmad-prd -a claude-code
npx skills add bmad-code-org/BMAD-METHOD --skill bmad-prfaq -a claude-code
npx skills add bmad-code-org/BMAD-METHOD --skill bmad-product-brief -a claude-code
npx skills add bmad-code-org/BMAD-METHOD --skill bmad-ux -a claude-code
```

La commande `npx skills add` (CLI Vercel `skills`) demande Node.js 22.20 ou plus (vérifié le 06/11/2026, https://github.com/vercel-labs/skills). Claude Code installé avec l'installeur natif n'en a pas besoin.

Les workflows cités ici sont dans le même dépôt (le dépôt s'ajoute une fois : `/plugin marketplace add Gremelinn0/zerogravity-skills`) :

```text
/plugin install cadrer-un-chantier@zerogravity
/plugin install construire@zerogravity
/plugin install creer-un-agent-ia@zerogravity
/plugin install creer-un-site-web@zerogravity
/plugin install faire-evoluer-une-app@zerogravity
/plugin install lancer-un-produit@zerogravity
/plugin install mettre-en-ligne@zerogravity
/plugin install tester-et-securiser@zerogravity
/plugin install trouver-ses-prochains-clients@zerogravity
```

## Licence

MIT. Les compétences tierces citées gardent leur licence et leur auteur : la liste des sources est dans le README du dépôt.
