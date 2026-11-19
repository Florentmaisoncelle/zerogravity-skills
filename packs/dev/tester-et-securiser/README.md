# Tester et sécuriser

Le code relu, la sécurité vérifiée à chaque lot puis en profondeur avant la mise en ligne, l'app lancée et parcourue dans le navigateur jusqu'à un verdict : on met en ligne, ou pas.

## Installer

```text
/plugin marketplace add Florentmaisoncelle/zerogravity-skills
/plugin install tester-et-securiser@zerogravity
```

## Lancer

Dans Claude Code : `/tester-et-securiser:tester-et-securiser`, ou décrire simplement le besoin.

## Prérequis

Ce workflow s'appuie sur des compétences publiques, installées à part. Aucune n'est indispensable : si l'une manque, le workflow le dit et fait l'étape à la main. Faire l'étape à la main veut dire suivre sa règle de choix, écrire ce qu'elle doit rendre (dans le fichier de l'étape, ou dans la réponse quand le workflow n'a pas de dossier) et dire ce qui reste à la charge de la personne.

```text
/plugin marketplace add Florentmaisoncelle/zerogravity-skills
/plugin marketplace add JuliusBrussee/caveman
/plugin marketplace add addyosmani/agent-skills
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin install 42crunch-api-security-testing@claude-plugins-official
/plugin install agent-skills@addy-agent-skills
/plugin install ai-plugins@claude-plugins-official
/plugin install caveman@caveman
/plugin install entretenir-son-systeme@zerogravity
/plugin install claude-security@claude-plugins-official
/plugin install code-review@claude-plugins-official
/plugin install engineering@knowledge-work-plugins
npx skills add bmad-code-org/BMAD-METHOD --skill bmad-qa-generate-e2e-tests -a claude-code
npx skills add microsoft/playwright-cli --skill playwright-cli -a claude-code
```

La commande `npx skills add` (CLI Vercel `skills`) demande Node.js 22.20 ou plus (vérifié le 06/11/2026, https://github.com/vercel-labs/skills). Claude Code installé avec l'installeur natif n'en a pas besoin.

Les workflows cités ici sont dans le même dépôt (le dépôt s'ajoute une fois : `/plugin marketplace add Florentmaisoncelle/zerogravity-skills`) :

```text
/plugin install construire@zerogravity
/plugin install creer-un-site-web@zerogravity
/plugin install creer-une-app@zerogravity
/plugin install faire-evoluer-une-app@zerogravity
/plugin install mettre-en-ligne@zerogravity
```

## Comptes demandés par certaines compétences

La sécurité d'une API (42Crunch) lance des scans contre une API en marche ; la surveillance des dépendances (ai-plugins, Endor Labs) vérifie à l'installation l'authentification, l'espace de travail et l'outil `endorctl`. Les comptes et jetons exacts ne sont pas confirmés ici : à vérifier dans le README de chaque plugin.

## Licence

MIT. Les compétences tierces citées gardent leur licence et leur auteur : la liste des sources est dans le README du dépôt.
