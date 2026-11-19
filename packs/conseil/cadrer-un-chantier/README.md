# Cadrer un chantier avant de le lancer

Une stratégie, une méthode, un système ou un produit de zéro : poser le problème, choisir la bonne méthode de réflexion, écrire le plan, l'attaquer, le faire valider une fois, puis lancer.

## Installer

```text
/plugin marketplace add Florentmaisoncelle/zerogravity-skills
/plugin install cadrer-un-chantier@zerogravity
```

## Lancer

Dans Claude Code : `/cadrer-un-chantier:cadrer-un-chantier`, ou décrire simplement le besoin.

## Prérequis

Ce workflow s'appuie sur des compétences publiques, installées à part. Aucune n'est indispensable : si l'une manque, le workflow le dit et fait l'étape à la main. Faire l'étape à la main veut dire suivre sa règle de choix, écrire ce qu'elle doit rendre (dans le fichier de l'étape, ou dans la réponse quand le workflow n'a pas de dossier) et dire ce qui reste à la charge de la personne.

```text
/plugin marketplace add Florentmaisoncelle/zerogravity-skills
/plugin marketplace add addyosmani/agent-skills
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin marketplace add coreyhaines31/marketingskills
/plugin install agent-skills@addy-agent-skills
/plugin install superviser-ses-sessions@zerogravity
/plugin install marketing-skills@marketingskills
/plugin install operations@knowledge-work-plugins
/plugin install product-management@knowledge-work-plugins
/plugin install superpowers@claude-plugins-official
npx skills add bmad-code-org/BMAD-METHOD --skill bmad-brainstorming -a claude-code
```

La commande `npx skills add` (CLI Vercel `skills`) demande Node.js 22.20 ou plus (vérifié le 06/11/2026, https://github.com/vercel-labs/skills). Claude Code installé avec l'installeur natif n'en a pas besoin.

Les workflows cités ici sont dans le même dépôt (le dépôt s'ajoute une fois : `/plugin marketplace add Florentmaisoncelle/zerogravity-skills`) :

```text
/plugin install creer-un-agent-ia@zerogravity
/plugin install creer-une-app@zerogravity
/plugin install decider-une-strategie@zerogravity
/plugin install reflechir-a-fond@zerogravity
```

## Licence

MIT. Les compétences tierces citées gardent leur licence et leur auteur : la liste des sources est dans le README du dépôt.
