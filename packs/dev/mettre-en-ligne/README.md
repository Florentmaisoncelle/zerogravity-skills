# Mettre en ligne et garder la main

Une sortie préparée (paliers, seuils, retour arrière écrit d'avance), le déploiement, puis l'app vérifiée en ligne sur ordinateur et sur téléphone.

## Installer

```text
/plugin marketplace add Gremelinn0/zerogravity-skills
/plugin install mettre-en-ligne@zerogravity
```

## Lancer

Dans Claude Code : `/mettre-en-ligne:mettre-en-ligne`, ou décrire simplement le besoin.

## Prérequis

Ce workflow s'appuie sur des compétences publiques, installées à part. Aucune n'est indispensable : si l'une manque, le workflow le dit et fait l'étape à la main. Faire l'étape à la main veut dire suivre sa règle de choix, écrire ce qu'elle doit rendre (dans le fichier de l'étape, ou dans la réponse quand le workflow n'a pas de dossier) et dire ce qui reste à la charge de la personne.

```text
/plugin marketplace add addyosmani/agent-skills
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin install agent-skills@addy-agent-skills
/plugin install engineering@knowledge-work-plugins
/plugin install stripe@claude-plugins-official
npx skills add vercel-labs/agent-skills --skill deploy-to-vercel -a claude-code
```

La commande `npx skills add` (CLI Vercel `skills`) demande Node.js 22.20 ou plus (vérifié le 06/11/2026, https://github.com/vercel-labs/skills). Claude Code installé avec l'installeur natif n'en a pas besoin.

Les workflows cités ici sont dans le même dépôt (le dépôt s'ajoute une fois : `/plugin marketplace add Gremelinn0/zerogravity-skills`) :

```text
/plugin install creer-une-app@zerogravity
/plugin install faire-evoluer-une-app@zerogravity
/plugin install tester-et-securiser@zerogravity
```

## Licence

MIT. Les compétences tierces citées gardent leur licence et leur auteur : la liste des sources est dans le README du dépôt.
