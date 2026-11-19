# Traiter les demandes clients, du premier message à la réponse

Six étapes dans l'ordre : trier et affecter chaque demande, répondre sur une commande, répondre sur une facture ou un abonnement, résoudre ou escalader une demande technique, écrire la réponse et la faire valider, puis transformer les questions qui reviennent en articles d'aide. La meilleure compétence à chaque étape ; quand une étape n'a pas encore la sienne, sa fiche le dit.

## Installer

```text
/plugin marketplace add Florentmaisoncelle/zerogravity-skills
/plugin install traiter-les-demandes-clients@zerogravity
```

## Lancer

Dans Claude Code : `/traiter-les-demandes-clients:traiter-les-demandes-clients`, ou décrire simplement le besoin.

## Prérequis

Ce workflow s'appuie sur des compétences publiques, installées à part. Aucune n'est indispensable : si l'une manque, le workflow le dit et fait l'étape à la main. Faire l'étape à la main veut dire suivre sa règle de choix, écrire ce qu'elle doit rendre (dans le fichier de l'étape, ou dans la réponse quand le workflow n'a pas de dossier) et dire ce qui reste à la charge de la personne.

```text
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin install customer-support@knowledge-work-plugins
/plugin install sales@knowledge-work-plugins
/plugin install small-business@knowledge-work-plugins
```

Les workflows cités ici sont dans le même dépôt (le dépôt s'ajoute une fois : `/plugin marketplace add Florentmaisoncelle/zerogravity-skills`) :

```text
/plugin install accueillir-un-nouveau-client@zerogravity
/plugin install ameliorer-le-parcours-client@zerogravity
/plugin install conclure-une-vente@zerogravity
/plugin install envoyer-des-e-mails@zerogravity
/plugin install fideliser-et-faire-recommander@zerogravity
```

## Licence

MIT. Les compétences tierces citées gardent leur licence et leur auteur : la liste des sources est dans le README du dépôt.
