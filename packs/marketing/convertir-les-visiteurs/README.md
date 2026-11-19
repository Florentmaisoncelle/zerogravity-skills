# Convertir les visiteurs : la page, le test, la ressource gratuite

Transformer le trafic en inscrits : le diagnostic de la page, le test d'une variante, la capture d'adresse et une ressource gratuite.

## Installer

```text
/plugin marketplace add Florentmaisoncelle/zerogravity-skills
/plugin install convertir-les-visiteurs@zerogravity
```

## Lancer

Dans Claude Code : `/convertir-les-visiteurs:convertir-les-visiteurs`, ou décrire simplement le besoin.

## Prérequis

Ce workflow s'appuie sur des compétences publiques, installées à part. Aucune n'est indispensable : si l'une manque, le workflow le dit et fait l'étape à la main. Faire l'étape à la main veut dire suivre sa règle de choix, écrire ce qu'elle doit rendre (dans le fichier de l'étape, ou dans la réponse quand le workflow n'a pas de dossier) et dire ce qui reste à la charge de la personne.

```text
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin marketplace add coreyhaines31/marketingskills
/plugin install design@knowledge-work-plugins
/plugin install marketing-skills@marketingskills
```

Les workflows cités ici sont dans le même dépôt (le dépôt s'ajoute une fois : `/plugin marketplace add Florentmaisoncelle/zerogravity-skills`) :

```text
/plugin install creer-un-site-web@zerogravity
/plugin install envoyer-des-e-mails@zerogravity
/plugin install lancer-un-produit@zerogravity
/plugin install referencer-son-site@zerogravity
```

## Licence

MIT. Les compétences tierces citées gardent leur licence et leur auteur : la liste des sources est dans le README du dépôt.

## Crédits

- `marketing-mesurer-un-test` : retravaillée depuis https://github.com/ericosiu/ai-marketing-skills, Copyright (c) 2026 Single Grain, licence MIT, texte dans `skills/marketing-mesurer-un-test/LICENSE-single-grain.txt`.
