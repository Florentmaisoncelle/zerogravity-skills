# Référencer son site : être trouvé dans Google et cité par les IA

Le référencement qui tourne : l'audit et les priorités, les requêtes qui achètent, la technique et l'indexation, les pages optimisées, les articles qui se classent, le maillage, les liens, la visibilité dans les réponses des IA, et le suivi qui dit quoi faire ensuite. Méthode d'Éric Djavid (32 agents SEO) adaptée aux outils gratuits.

## Installer

```text
/plugin marketplace add Gremelinn0/zerogravity-skills
/plugin install referencer-son-site@zerogravity
```

## Lancer

Dans Claude Code : `/referencer-son-site:referencer-son-site`, ou décrire simplement le besoin.

## Prérequis

Ce workflow s'appuie sur des compétences publiques, installées à part. Aucune n'est indispensable : si l'une manque, le workflow le dit et fait l'étape à la main. Faire l'étape à la main veut dire suivre sa règle de choix, écrire ce qu'elle doit rendre (dans le fichier de l'étape, ou dans la réponse quand le workflow n'a pas de dossier) et dire ce qui reste à la charge de la personne.

```text
/plugin marketplace add addyosmani/web-quality-skills
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin marketplace add coreyhaines31/marketingskills
/plugin install marketing-skills@marketingskills
/plugin install marketing@knowledge-work-plugins
/plugin install small-business@knowledge-work-plugins
/plugin install web-quality-skills@addy-web-quality-skills
```

Les workflows cités ici sont dans le même dépôt (le dépôt s'ajoute une fois : `/plugin marketplace add Gremelinn0/zerogravity-skills`) :

```text
/plugin install convertir-les-visiteurs@zerogravity
/plugin install creer-un-site-web@zerogravity
/plugin install lancer-un-produit@zerogravity
```

## Licence

MIT. Les compétences tierces citées gardent leur licence et leur auteur : la liste des sources est dans le README du dépôt.

## Crédits

- `seo-search-console` : retravaillée depuis https://github.com/ericosiu/ai-marketing-skills, Copyright (c) 2026 Single Grain, licence MIT, texte dans `skills/seo-search-console/LICENSE-single-grain.txt`.
