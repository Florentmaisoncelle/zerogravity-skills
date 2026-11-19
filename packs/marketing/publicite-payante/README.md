# Faire de la publicité payante : la créa, la pub vidéo, les campagnes

La publicité de bout en bout : les visuels et les textes de la pub, la pub vidéo, puis les campagnes lancées et pilotées sur Meta et Google.

## Installer

```text
/plugin marketplace add Florentmaisoncelle/zerogravity-skills
/plugin install publicite-payante@zerogravity
```

## Lancer

Dans Claude Code : `/publicite-payante:publicite-payante`, ou décrire simplement le besoin.

## Prérequis

Ce workflow s'appuie sur des compétences publiques, installées à part. Aucune n'est indispensable : si l'une manque, le workflow le dit et fait l'étape à la main. Faire l'étape à la main veut dire suivre sa règle de choix, écrire ce qu'elle doit rendre (dans le fichier de l'étape, ou dans la réponse quand le workflow n'a pas de dossier) et dire ce qui reste à la charge de la personne.

```text
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin marketplace add coreyhaines31/marketingskills
/plugin marketplace add heygen-com/hyperframes
/plugin install hyperframes@hyperframes
/plugin install marketing-skills@marketingskills
/plugin install marketing@knowledge-work-plugins
/plugin install small-business@knowledge-work-plugins
```

Les workflows cités ici sont dans le même dépôt (le dépôt s'ajoute une fois : `/plugin marketplace add Florentmaisoncelle/zerogravity-skills`) :

```text
/plugin install envoyer-des-e-mails@zerogravity
/plugin install faire-une-video@zerogravity
/plugin install lancer-un-produit@zerogravity
/plugin install poser-sa-strategie-marketing@zerogravity
/plugin install trouver-ses-prochains-clients@zerogravity
```

## Licence

MIT. Les compétences tierces citées gardent leur licence et leur auteur : la liste des sources est dans le README du dépôt.
