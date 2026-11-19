# Piloter son pipeline et développer ses clients

La revue commerciale de la semaine : un CRM propre, le pipeline revu, les affaires débloquées ou relancées, la prévision chiffrée, les leçons des affaires gagnées et perdues, et les extensions chez les clients en place.

## Installer

```text
/plugin marketplace add Florentmaisoncelle/zerogravity-skills
/plugin install piloter-le-pipeline@zerogravity
```

## Lancer

Dans Claude Code : `/piloter-le-pipeline:piloter-le-pipeline`, ou décrire simplement le besoin.

## Prérequis

Ce workflow s'appuie sur des compétences publiques, installées à part. Aucune n'est indispensable : si l'une manque, le workflow le dit et fait l'étape à la main. Faire l'étape à la main veut dire suivre sa règle de choix, écrire ce qu'elle doit rendre (dans le fichier de l'étape, ou dans la réponse quand le workflow n'a pas de dossier) et dire ce qui reste à la charge de la personne.

```text
/plugin marketplace add Florentmaisoncelle/zerogravity-skills
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin marketplace add coreyhaines31/marketingskills
/plugin install consultant-ia@zerogravity
/plugin install marketing-skills@marketingskills
/plugin install sales@knowledge-work-plugins
/plugin install small-business@knowledge-work-plugins
```

Les workflows cités ici sont dans le même dépôt (le dépôt s'ajoute une fois : `/plugin marketplace add Florentmaisoncelle/zerogravity-skills`) :

```text
/plugin install conclure-une-vente@zerogravity
/plugin install fideliser-et-faire-recommander@zerogravity
/plugin install organiser-sa-force-de-vente@zerogravity
/plugin install trouver-ses-prochains-clients@zerogravity
```

## Licence

MIT. Les compétences tierces citées gardent leur licence et leur auteur : la liste des sources est dans le README du dépôt.
