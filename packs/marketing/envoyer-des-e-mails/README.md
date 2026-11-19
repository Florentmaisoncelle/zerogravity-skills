# Envoyer des e-mails : les parcours automatiques, la newsletter, les SMS

Les e-mails qui accompagnent les inscrits : les parcours automatiques (accueil, relances, résiliation), la newsletter avec le consentement, la délivrabilité, et les SMS.

## Installer

```text
/plugin marketplace add Gremelinn0/zerogravity-skills
/plugin install envoyer-des-e-mails@zerogravity
```

## Lancer

Dans Claude Code : `/envoyer-des-e-mails:envoyer-des-e-mails`, ou décrire simplement le besoin.

## Prérequis

Ce workflow s'appuie sur des compétences publiques, installées à part. Aucune n'est indispensable : si l'une manque, le workflow le dit et fait l'étape à la main. Faire l'étape à la main veut dire suivre sa règle de choix, écrire ce qu'elle doit rendre (dans le fichier de l'étape, ou dans la réponse quand le workflow n'a pas de dossier) et dire ce qui reste à la charge de la personne.

```text
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin marketplace add coreyhaines31/marketingskills
/plugin install marketing-skills@marketingskills
/plugin install marketing@knowledge-work-plugins
```

Les workflows cités ici sont dans le même dépôt (le dépôt s'ajoute une fois : `/plugin marketplace add Gremelinn0/zerogravity-skills`) :

```text
/plugin install fideliser-et-faire-recommander@zerogravity
/plugin install lancer-un-produit@zerogravity
/plugin install publicite-payante@zerogravity
/plugin install trouver-ses-prochains-clients@zerogravity
```

## Licence

MIT. Les compétences tierces citées gardent leur licence et leur auteur : la liste des sources est dans le README du dépôt.
