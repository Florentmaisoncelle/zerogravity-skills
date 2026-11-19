# Construire, tâche par tâche, test d'abord

Le plan découpé en petites tâches vérifiables, chacune construite test d'abord par un sous-agent, relue avant la suivante, et prouvée avant d'être annoncée finie.

## Installer

```text
/plugin marketplace add Florentmaisoncelle/zerogravity-skills
/plugin install construire@zerogravity
```

## Lancer

Dans Claude Code : `/construire:construire`, ou décrire simplement le besoin.

## Prérequis

Ce workflow s'appuie sur des compétences publiques, installées à part. Aucune n'est indispensable : si l'une manque, le workflow le dit et fait l'étape à la main. Faire l'étape à la main veut dire suivre sa règle de choix, écrire ce qu'elle doit rendre (dans le fichier de l'étape, ou dans la réponse quand le workflow n'a pas de dossier) et dire ce qui reste à la charge de la personne.

```text
/plugin marketplace add Florentmaisoncelle/zerogravity-skills
/plugin marketplace add JuliusBrussee/caveman
/plugin marketplace add addyosmani/agent-skills
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin install agent-skills@addy-agent-skills
/plugin install caveman@caveman
/plugin install entretenir-son-systeme@zerogravity
/plugin install product-management@knowledge-work-plugins
/plugin install superpowers@claude-plugins-official
```

Les workflows cités ici sont dans le même dépôt (le dépôt s'ajoute une fois : `/plugin marketplace add Florentmaisoncelle/zerogravity-skills`) :

```text
/plugin install creer-un-agent-ia@zerogravity
/plugin install creer-un-site-web@zerogravity
/plugin install creer-une-app@zerogravity
/plugin install faire-evoluer-une-app@zerogravity
/plugin install mettre-en-ligne@zerogravity
/plugin install tester-et-securiser@zerogravity
```

## Licence

MIT. Les compétences tierces citées gardent leur licence et leur auteur : la liste des sources est dans le README du dépôt.
