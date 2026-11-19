# Accueillir un nouveau client, de la signature à sa première réussite

Quatre étapes dans l'ordre : définir la première réussite du client et la checklist d'accueil, ouvrir le parcours et préparer les accès, écrire le message de bienvenue, contrôler l'activation à une semaine et à un mois. La meilleure compétence à chaque étape ; les accès et la mise en service se font à la main.

## Installer

```text
/plugin marketplace add Florentmaisoncelle/zerogravity-skills
/plugin install accueillir-un-nouveau-client@zerogravity
```

## Lancer

Dans Claude Code : `/accueillir-un-nouveau-client:accueillir-un-nouveau-client`, ou décrire simplement le besoin.

## Prérequis

Ce workflow s'appuie sur des compétences publiques, installées à part. Aucune n'est indispensable : si l'une manque, le workflow le dit et fait l'étape à la main. Faire l'étape à la main veut dire suivre sa règle de choix, écrire ce qu'elle doit rendre (dans le fichier de l'étape, ou dans la réponse quand le workflow n'a pas de dossier) et dire ce qui reste à la charge de la personne.

```text
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin marketplace add coreyhaines31/marketingskills
/plugin install marketing-skills@marketingskills
/plugin install operations@knowledge-work-plugins
```

Les workflows cités ici sont dans le même dépôt (le dépôt s'ajoute une fois : `/plugin marketplace add Florentmaisoncelle/zerogravity-skills`) :

```text
/plugin install ameliorer-le-parcours-client@zerogravity
/plugin install conclure-une-vente@zerogravity
/plugin install recruter@zerogravity
/plugin install traiter-les-demandes-clients@zerogravity
```

## Licence

MIT. Les compétences tierces citées gardent leur licence et leur auteur : la liste des sources est dans le README du dépôt.
