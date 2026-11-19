# Poser sa stratégie marketing : marché, concurrents, positionnement, plan

Avant de produire quoi que ce soit : le marché et les publics étudiés, les concurrents surveillés, le positionnement et les messages écrits, l'offre et le prix, le parcours client, puis le plan marketing présenté pour décision.

## Installer

```text
/plugin marketplace add Florentmaisoncelle/zerogravity-skills
/plugin install poser-sa-strategie-marketing@zerogravity
```

## Lancer

Dans Claude Code : `/poser-sa-strategie-marketing:poser-sa-strategie-marketing`, ou décrire simplement le besoin.

## Prérequis

Ce workflow s'appuie sur des compétences publiques, installées à part. Aucune n'est indispensable : si l'une manque, le workflow le dit et fait l'étape à la main. Faire l'étape à la main veut dire suivre sa règle de choix, écrire ce qu'elle doit rendre (dans le fichier de l'étape, ou dans la réponse quand le workflow n'a pas de dossier) et dire ce qui reste à la charge de la personne.

```text
/plugin marketplace add addyosmani/agent-skills
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin marketplace add anthropics/skills
/plugin marketplace add coreyhaines31/marketingskills
/plugin install agent-skills@addy-agent-skills
/plugin install document-skills@anthropic-agent-skills
/plugin install marketing-skills@marketingskills
/plugin install marketing@knowledge-work-plugins
/plugin install operations@knowledge-work-plugins
/plugin install product-management@knowledge-work-plugins
/plugin install small-business@knowledge-work-plugins
```

Les workflows cités ici sont dans le même dépôt (le dépôt s'ajoute une fois : `/plugin marketplace add Florentmaisoncelle/zerogravity-skills`) :

```text
/plugin install cadrer-un-chantier@zerogravity
/plugin install creer-un-site-web@zerogravity
/plugin install decider-une-strategie@zerogravity
/plugin install lancer-un-produit@zerogravity
/plugin install publier-sur-linkedin@zerogravity
```

## Licence

MIT. Les compétences tierces citées gardent leur licence et leur auteur : la liste des sources est dans le README du dépôt.

## Crédits

- `marketing-relier-le-contenu-aux-contrats` : retravaillée depuis https://github.com/ericosiu/ai-marketing-skills, Copyright (c) 2026 Single Grain, licence MIT, texte dans `skills/marketing-relier-le-contenu-aux-contrats/LICENSE-single-grain.txt`.
- `marketing-relire-un-changement` : retravaillée depuis https://github.com/ericosiu/ai-marketing-skills, Copyright (c) 2026 Single Grain, licence MIT, texte dans `skills/marketing-relire-un-changement/LICENSE-single-grain.txt`.
- `video-qui-sortent-du-lot` : retravaillée depuis https://github.com/ericosiu/ai-marketing-skills, Copyright (c) 2026 Single Grain, licence MIT, texte dans `skills/video-qui-sortent-du-lot/LICENSE-single-grain.txt`.
