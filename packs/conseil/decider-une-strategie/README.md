# Décider d'une stratégie d'affaires, la recommandation d'abord

Huit étapes de conseil en stratégie pour une décision d'affaires floue (marché, offre, produit, investissement, priorités) : poser la décision, la structurer, séparer les faits des hypothèses, comparer de vraies options, éprouver le contre-cas, puis recommander d'abord. C'est une discipline de raisonnement : presque toutes les étapes sont menées par le workflow lui-même, et chaque étape sans compétence à appeler le dit.

## Installer

```text
/plugin marketplace add Florentmaisoncelle/zerogravity-skills
/plugin install decider-une-strategie@zerogravity
```

## Lancer

Dans Claude Code : `/decider-une-strategie:decider-une-strategie`, ou décrire simplement le besoin.

## Prérequis

Ce workflow s'appuie sur des compétences publiques, installées à part. Aucune n'est indispensable : si l'une manque, le workflow le dit et fait l'étape à la main. Faire l'étape à la main veut dire suivre sa règle de choix, écrire ce qu'elle doit rendre (dans le fichier de l'étape, ou dans la réponse quand le workflow n'a pas de dossier) et dire ce qui reste à la charge de la personne.

```text
/plugin marketplace add addyosmani/agent-skills
/plugin install agent-skills@addy-agent-skills
```

Les workflows cités ici sont dans le même dépôt (le dépôt s'ajoute une fois : `/plugin marketplace add Florentmaisoncelle/zerogravity-skills`) :

```text
/plugin install cadrer-un-chantier@zerogravity
/plugin install consultant-ia@zerogravity
/plugin install poser-sa-strategie-marketing@zerogravity
/plugin install reflechir-a-fond@zerogravity
```

## Licence

MIT. Les compétences tierces citées gardent leur licence et leur auteur : la liste des sources est dans le README du dépôt.
