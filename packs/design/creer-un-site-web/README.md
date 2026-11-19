# Créer le site web

Neuf étapes dans l'ordre : la carte des pages, le texte, la direction artistique, les composants, le référencement, la vitesse, l'accessibilité, la mesure et la conversion. La vitesse et l'accessibilité se mesurent, elles ne se jugent pas à l'œil.

## Installer

```text
/plugin marketplace add Florentmaisoncelle/zerogravity-skills
/plugin install creer-un-site-web@zerogravity
```

## Lancer

Dans Claude Code : `/creer-un-site-web:creer-un-site-web`, ou décrire simplement le besoin.

## Prérequis

Ce workflow s'appuie sur des compétences publiques, installées à part. Aucune n'est indispensable : si l'une manque, le workflow le dit et fait l'étape à la main. Faire l'étape à la main veut dire suivre sa règle de choix, écrire ce qu'elle doit rendre (dans le fichier de l'étape, ou dans la réponse quand le workflow n'a pas de dossier) et dire ce qui reste à la charge de la personne.

```text
/plugin marketplace add addyosmani/agent-skills
/plugin marketplace add addyosmani/web-quality-skills
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin marketplace add coreyhaines31/marketingskills
/plugin marketplace add pbakaus/impeccable
/plugin install agent-skills@addy-agent-skills
/plugin install design@knowledge-work-plugins
/plugin install frontend-design@claude-plugins-official
/plugin install impeccable@impeccable
/plugin install marketing-skills@marketingskills
/plugin install modern-web-guidance@claude-plugins-official
/plugin install web-quality-skills@addy-web-quality-skills
npx skills add bmad-code-org/BMAD-METHOD --skill bmad-ux -a claude-code
npx skills add vercel-labs/agent-skills --skill composition-patterns -a claude-code
npx skills add vercel-labs/agent-skills --skill react-best-practices -a claude-code
npx skills add vercel-labs/agent-skills --skill web-design-guidelines -a claude-code
```

La commande `npx skills add` (CLI Vercel `skills`) demande Node.js 22.20 ou plus (vérifié le 06/11/2026, https://github.com/vercel-labs/skills). Claude Code installé avec l'installeur natif n'en a pas besoin.

Les workflows cités ici sont dans le même dépôt (le dépôt s'ajoute une fois : `/plugin marketplace add Florentmaisoncelle/zerogravity-skills`) :

```text
/plugin install convertir-les-visiteurs@zerogravity
/plugin install creer-un-agent-ia@zerogravity
/plugin install creer-une-app@zerogravity
/plugin install faire-evoluer-une-app@zerogravity
/plugin install mettre-en-ligne@zerogravity
/plugin install referencer-son-site@zerogravity
/plugin install tester-et-securiser@zerogravity
```

## Licence

MIT. Les compétences tierces citées gardent leur licence et leur auteur : la liste des sources est dans le README du dépôt.
