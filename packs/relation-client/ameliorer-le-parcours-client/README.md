# Améliorer le parcours client : satisfaction, clients à risque, retours, parcours

Cinq étapes dans l'ordre : transformer la satisfaction en actions suivies, repérer les clients à risque et préparer leur rétention, transformer les retours en priorités produit, cartographier le parcours et corriger ses frictions, et, quand les données sont sensibles, cadrer les autorisations avant toute automatisation. Chaque étape finit par une action, avec un responsable.

## Installer

```text
/plugin marketplace add Florentmaisoncelle/zerogravity-skills
/plugin install ameliorer-le-parcours-client@zerogravity
```

## Lancer

Dans Claude Code : `/ameliorer-le-parcours-client:ameliorer-le-parcours-client`, ou décrire simplement le besoin.

## Prérequis

Ce workflow s'appuie sur des compétences publiques, installées à part. Aucune n'est indispensable : si l'une manque, le workflow le dit et fait l'étape à la main. Faire l'étape à la main veut dire suivre sa règle de choix, écrire ce qu'elle doit rendre (dans le fichier de l'étape, ou dans la réponse quand le workflow n'a pas de dossier) et dire ce qui reste à la charge de la personne.

```text
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin install operations@knowledge-work-plugins
/plugin install product-management@knowledge-work-plugins
/plugin install sales@knowledge-work-plugins
/plugin install small-business@knowledge-work-plugins
```

Les workflows cités ici sont dans le même dépôt (le dépôt s'ajoute une fois : `/plugin marketplace add Florentmaisoncelle/zerogravity-skills`) :

```text
/plugin install accueillir-un-nouveau-client@zerogravity
/plugin install fideliser-et-faire-recommander@zerogravity
/plugin install piloter-le-pipeline@zerogravity
/plugin install traiter-les-demandes-clients@zerogravity
```

## Licence

MIT. Les compétences tierces citées gardent leur licence et leur auteur : la liste des sources est dans le README du dépôt.
