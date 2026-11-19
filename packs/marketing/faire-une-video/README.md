# Faire une vidéo : choisir la méthode, écrire, tourner ou générer, monter, publier

Une vidéo de bout en bout : la méthode choisie selon son coût, le script validé, le tournage ou l'avatar, les plans animés, le montage et les sous-titres, puis la publication.

## Installer

```text
/plugin marketplace add Florentmaisoncelle/zerogravity-skills
/plugin install faire-une-video@zerogravity
```

## Lancer

Dans Claude Code : `/faire-une-video:faire-une-video`, ou décrire simplement le besoin.

## Prérequis

Ce workflow s'appuie sur des compétences publiques, installées à part. Aucune n'est indispensable : si l'une manque, le workflow le dit et fait l'étape à la main. Faire l'étape à la main veut dire suivre sa règle de choix, écrire ce qu'elle doit rendre (dans le fichier de l'étape, ou dans la réponse quand le workflow n'a pas de dossier) et dire ce qui reste à la charge de la personne.

```text
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin marketplace add coreyhaines31/marketingskills
/plugin marketplace add heygen-com/hyperframes
/plugin install hyperframes@hyperframes
/plugin install marketing-skills@marketingskills
/plugin install small-business@knowledge-work-plugins
```

Les workflows cités ici sont dans le même dépôt (le dépôt s'ajoute une fois : `/plugin marketplace add Florentmaisoncelle/zerogravity-skills`) :

```text
/plugin install lancer-un-produit@zerogravity
/plugin install publicite-payante@zerogravity
/plugin install publier-sur-linkedin@zerogravity
```

## Licence

MIT. Les compétences tierces citées gardent leur licence et leur auteur : la liste des sources est dans le README du dépôt.

## Crédits

- `video-declinaison-des-moments` : retravaillée depuis https://github.com/ericosiu/ai-marketing-skills, Copyright (c) 2026 Single Grain, licence MIT, texte dans `skills/video-declinaison-des-moments/LICENSE-single-grain.txt`.
- `video-idee-de-short` : retravaillée depuis https://github.com/ericosiu/ai-marketing-skills, Copyright (c) 2026 Single Grain, licence MIT, texte dans `skills/video-idee-de-short/LICENSE-single-grain.txt`.
- `video-tester-trois-ouvertures` : retravaillée depuis https://github.com/ericosiu/ai-marketing-skills, Copyright (c) 2026 Single Grain, licence MIT, texte dans `skills/video-tester-trois-ouvertures/LICENSE-single-grain.txt`.
- `video-titre-et-miniature` : retravaillée depuis https://github.com/ericosiu/ai-marketing-skills, Copyright (c) 2026 Single Grain, licence MIT, texte dans `skills/video-titre-et-miniature/LICENSE-single-grain.txt`.
