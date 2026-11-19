# Faire évoluer une app : une fonctionnalité de plus ou un défaut corrigé

Six étapes pour une app qui existe déjà, à deux entrées : partir de la demande (la fonctionnalité écrite, ou le défaut reproduit et sa cause prouvée), comprendre le code qui l'accueille, construire test d'abord, tester, mettre en ligne, documenter.

## Installer

```text
/plugin marketplace add Florentmaisoncelle/zerogravity-skills
/plugin install faire-evoluer-une-app@zerogravity
```

## Lancer

Dans Claude Code : `/faire-evoluer-une-app:faire-evoluer-une-app`, ou décrire simplement le besoin.

## Prérequis

Ce workflow s'appuie sur des compétences publiques, installées à part. Aucune n'est indispensable : si l'une manque, le workflow le dit et fait l'étape à la main. Faire l'étape à la main veut dire suivre sa règle de choix, écrire ce qu'elle doit rendre (dans le fichier de l'étape, ou dans la réponse quand le workflow n'a pas de dossier) et dire ce qui reste à la charge de la personne.

```text
/plugin marketplace add JuliusBrussee/caveman
/plugin marketplace add addyosmani/agent-skills
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin install agent-skills@addy-agent-skills
/plugin install caveman@caveman
/plugin install engineering@knowledge-work-plugins
/plugin install feature-dev@claude-plugins-official
/plugin install superpowers@claude-plugins-official
npx skills add bmad-code-org/BMAD-METHOD --skill bmad-prd -a claude-code
```

La commande `npx skills add` (CLI Vercel `skills`) demande Node.js 22.20 ou plus (vérifié le 06/11/2026, https://github.com/vercel-labs/skills). Claude Code installé avec l'installeur natif n'en a pas besoin.

Les workflows cités ici sont dans le même dépôt (le dépôt s'ajoute une fois : `/plugin marketplace add Florentmaisoncelle/zerogravity-skills`) :

```text
/plugin install construire@zerogravity
/plugin install creer-un-agent-ia@zerogravity
/plugin install creer-un-site-web@zerogravity
/plugin install creer-une-app@zerogravity
/plugin install mettre-en-ligne@zerogravity
/plugin install tester-et-securiser@zerogravity
```

## Licence

MIT. Les compétences tierces citées gardent leur licence et leur auteur : la liste des sources est dans le README du dépôt.
