# Recruter un collaborateur, de la fiche de poste à son arrivée

Cinq étapes dans l'ordre : décider d'embaucher, écrire le paquet de recrutement, trier et répondre à tous les candidats, faire l'offre, préparer l'arrivée. La meilleure compétence à chaque étape, et ce qui manque dit franchement.

## Installer

```text
/plugin marketplace add Gremelinn0/zerogravity-skills
/plugin install recruter@zerogravity
```

## Lancer

Dans Claude Code : `/recruter:recruter`, ou décrire simplement le besoin.

## Prérequis

Ce workflow s'appuie sur des compétences publiques, installées à part. Aucune n'est indispensable : si l'une manque, le workflow le dit et fait l'étape à la main. Faire l'étape à la main veut dire suivre sa règle de choix, écrire ce qu'elle doit rendre (dans le fichier de l'étape, ou dans la réponse quand le workflow n'a pas de dossier) et dire ce qui reste à la charge de la personne.

```text
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin install human-resources@knowledge-work-plugins
/plugin install operations@knowledge-work-plugins
/plugin install small-business@knowledge-work-plugins
```

Les workflows cités ici sont dans le même dépôt (le dépôt s'ajoute une fois : `/plugin marketplace add Gremelinn0/zerogravity-skills`) :

```text
/plugin install cadrer-un-chantier@zerogravity
/plugin install creer-une-app@zerogravity
/plugin install organiser-sa-force-de-vente@zerogravity
```

## Licence

MIT. Les compétences tierces citées gardent leur licence et leur auteur : la liste des sources est dans le README du dépôt.
