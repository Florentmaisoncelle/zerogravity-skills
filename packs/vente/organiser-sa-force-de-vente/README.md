# Organiser sa force de vente : objectif, équipe, incitation, partenaires

Le plan commercial de l'année : l'objectif de revenu et la capacité qu'il demande, les rôles de l'équipe, le plan d'incitation, les partenaires qui apportent des affaires, puis l'adoption du nouveau fonctionnement. Deux étapes restent sans bonne compétence, et la page le dit.

## Installer

```text
/plugin marketplace add Florentmaisoncelle/zerogravity-skills
/plugin install organiser-sa-force-de-vente@zerogravity
```

## Lancer

Dans Claude Code : `/organiser-sa-force-de-vente:organiser-sa-force-de-vente`, ou décrire simplement le besoin.

## Prérequis

Ce workflow s'appuie sur des compétences publiques, installées à part. Aucune n'est indispensable : si l'une manque, le workflow le dit et fait l'étape à la main. Faire l'étape à la main veut dire suivre sa règle de choix, écrire ce qu'elle doit rendre (dans le fichier de l'étape, ou dans la réponse quand le workflow n'a pas de dossier) et dire ce qui reste à la charge de la personne.

```text
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin marketplace add coreyhaines31/marketingskills
/plugin install human-resources@knowledge-work-plugins
/plugin install marketing-skills@marketingskills
/plugin install operations@knowledge-work-plugins
/plugin install product-management@knowledge-work-plugins
/plugin install sales@knowledge-work-plugins
```

Les workflows cités ici sont dans le même dépôt (le dépôt s'ajoute une fois : `/plugin marketplace add Florentmaisoncelle/zerogravity-skills`) :

```text
/plugin install fideliser-et-faire-recommander@zerogravity
/plugin install lancer-un-produit@zerogravity
/plugin install piloter-le-pipeline@zerogravity
/plugin install recruter@zerogravity
```

## Licence

MIT. Les compétences tierces citées gardent leur licence et leur auteur : la liste des sources est dans le README du dépôt.
