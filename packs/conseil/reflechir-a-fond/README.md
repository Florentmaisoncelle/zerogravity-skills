# Réfléchir à fond avant d'agir sur un chantier complexe

Neuf étapes pour transformer un chantier complexe, transversal ou difficile à défaire en décision solide avant d'exécuter : verrouiller le mandat, poser le problème en entier, mesurer l'état réel, cartographier le système, trouver la cause structurelle, ouvrir au moins trois options, formuler une thèse qui peut échouer, la réfuter, puis rendre la décision. Le workflow ne remplace aucune méthode : il choisit la compétence d'analyse que le signal appelle.

## Installer

```text
/plugin marketplace add Florentmaisoncelle/zerogravity-skills
/plugin install reflechir-a-fond@zerogravity
```

## Lancer

Dans Claude Code : `/reflechir-a-fond:reflechir-a-fond`, ou décrire simplement le besoin.

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

## Licence

MIT. Les compétences tierces citées gardent leur licence et leur auteur : la liste des sources est dans le README du dépôt.
