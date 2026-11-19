# Fidéliser et faire recommander : parrainage, témoignages, rétention

Faire travailler les clients satisfaits : un programme de recommandation avec ses règles et sa mesure, des témoignages autorisés, les clients qui partent retenus, et un programme de fidélité quand il se justifie.

## Installer

```text
/plugin marketplace add Gremelinn0/zerogravity-skills
/plugin install fideliser-et-faire-recommander@zerogravity
```

## Lancer

Dans Claude Code : `/fideliser-et-faire-recommander:fideliser-et-faire-recommander`, ou décrire simplement le besoin.

## Prérequis

Ce workflow s'appuie sur des compétences publiques, installées à part. Aucune n'est indispensable : si l'une manque, le workflow le dit et fait l'étape à la main. Faire l'étape à la main veut dire suivre sa règle de choix, écrire ce qu'elle doit rendre (dans le fichier de l'étape, ou dans la réponse quand le workflow n'a pas de dossier) et dire ce qui reste à la charge de la personne.

```text
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin marketplace add coreyhaines31/marketingskills
/plugin install marketing-skills@marketingskills
/plugin install small-business@knowledge-work-plugins
```

Les workflows cités ici sont dans le même dépôt (le dépôt s'ajoute une fois : `/plugin marketplace add Gremelinn0/zerogravity-skills`) :

```text
/plugin install ameliorer-le-parcours-client@zerogravity
/plugin install organiser-sa-force-de-vente@zerogravity
/plugin install piloter-le-pipeline@zerogravity
/plugin install traiter-les-demandes-clients@zerogravity
```

## Licence

MIT. Les compétences tierces citées gardent leur licence et leur auteur : la liste des sources est dans le README du dépôt.
