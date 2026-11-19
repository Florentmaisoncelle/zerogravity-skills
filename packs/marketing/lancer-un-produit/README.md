# Lancer un produit : le plan, les annuaires, les stores, la presse

Un lancement de bout en bout : le plan, l'annonce et Product Hunt, les messages contrôlés, les annuaires et les fiches des stores, la traduction, la presse, les partenaires et les événements.

## Installer

```text
/plugin marketplace add Florentmaisoncelle/zerogravity-skills
/plugin install lancer-un-produit@zerogravity
```

## Lancer

Dans Claude Code : `/lancer-un-produit:lancer-un-produit`, ou décrire simplement le besoin.

## Prérequis

Ce workflow s'appuie sur des compétences publiques, installées à part. Aucune n'est indispensable : si l'une manque, le workflow le dit et fait l'étape à la main. Faire l'étape à la main veut dire suivre sa règle de choix, écrire ce qu'elle doit rendre (dans le fichier de l'étape, ou dans la réponse quand le workflow n'a pas de dossier) et dire ce qui reste à la charge de la personne.

```text
/plugin marketplace add addyosmani/agent-skills
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin marketplace add coreyhaines31/marketingskills
/plugin install agent-skills@addy-agent-skills
/plugin install marketing-skills@marketingskills
/plugin install marketing@knowledge-work-plugins
npx skills add bmad-code-org/BMAD-METHOD --skill bmad-prfaq -a claude-code
```

La commande `npx skills add` (CLI Vercel `skills`) demande Node.js 22.20 ou plus (vérifié le 06/11/2026, https://github.com/vercel-labs/skills). Claude Code installé avec l'installeur natif n'en a pas besoin.

Les workflows cités ici sont dans le même dépôt (le dépôt s'ajoute une fois : `/plugin marketplace add Florentmaisoncelle/zerogravity-skills`) :

```text
/plugin install envoyer-des-e-mails@zerogravity
/plugin install poser-sa-strategie-marketing@zerogravity
/plugin install publicite-payante@zerogravity
/plugin install trouver-ses-prochains-clients@zerogravity
```

## Licence

MIT. Les compétences tierces citées gardent leur licence et leur auteur : la liste des sources est dans le README du dépôt.
