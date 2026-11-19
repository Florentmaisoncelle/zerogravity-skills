---
name: piloter-le-pipeline
description: >-
  Quand on veut piloter son pipeline commercial (revue du pipeline, CRM en désordre, affaires bloquées ou endormies, prévision du trimestre, motifs de gain et de perte, extensions chez les clients) → affiche l'état de la revue calculé depuis le dossier de la semaine `pipeline/AAAA-Sww/`, puis déroule sept étapes dans l'ordre : le CRM au propre, la revue, les blocages, les relances, la prévision, les gains et pertes, les extensions. Ce qui manque est dit franchement (le contrôle des oppositions avant une relance). Se lance par `/piloter-le-pipeline:piloter-le-pipeline`. Déclencheurs : « revue du pipeline », « nettoyer le CRM », « doublons CRM », « affaires bloquées », « relancer les affaires qui dorment », « prévision commerciale », « forecast », « gagné perdu », « pourquoi je perds des affaires », « extension client ». Pas pour une affaire précise jusqu'à la signature : `/conclure-une-vente:conclure-une-vente`. Pas pour retenir des clients qui partent : `/fideliser-et-faire-recommander:fideliser-et-faire-recommander`.
---

# Piloter son pipeline, la revue commerciale de la semaine

## Ce que ce workflow résout

Un pipeline (la liste des affaires en cours, avec leur étape) se dégrade sans bruit : des doublons, des affaires sans prochaine étape, des dates qui glissent, une prévision tirée au jugé. Des compétences savent montrer leurs calculs et refuser d'inventer, d'autres remettent le CRM au propre sans jamais supprimer. Ici : une revue dans l'ordre, chaque semaine, du CRM propre à la prévision, puis les leçons et les extensions.

**Résultat attendu** : chaque semaine, un CRM fiable, un pipeline revu, chaque affaire bloquée avec son plan, les affaires endormies relancées après accord, une prévision chiffrée à faire valider, les motifs de gain et de perte sourcés, les extensions classées par preuve.

## Stratégie

1. **L'état d'abord**, toujours calculé depuis les fichiers de la semaine, `pipeline/AAAA-Sww/`, jamais recopié.
2. **Un choix par étape.** Chaque étape a sa compétence par défaut et sa règle de choix, dans la table plus bas, qui vient de `references/workflow.json`.
3. **L'ordre protège la décision** : pas de prévision sur un CRM sale, pas de relance sans vérifier les oppositions, pas de fusion ni de suppression sans accord. Sauter une étape reste possible sur demande ; le journal dit laquelle et pourquoi.
4. **Une validation de départ, à l'étape 1** : les règles de nettoyage du CRM. Une fois ces règles validées, le travail se déroule, mais chaque fusion ou suppression d'une fiche reste soumise à un accord. Restent toujours humains : arbitrer la prévision, envoyer chaque relance, décider d'une extension.
5. **Tout texte qui sort au nom de l'entreprise** est relu avant d'être montré, et rien ne part sans validation.
6. **Chaque passage se clôt au journal** : ce qui est fait, ce qui reste, la prochaine action.

<!-- prerequis:debut -->
## Prérequis

Ce workflow s'appuie sur des compétences publiques, installées à part. Aucune n'est indispensable : si l'une manque, le workflow le dit et fait l'étape à la main. Faire l'étape à la main veut dire suivre sa règle de choix, écrire ce qu'elle doit rendre (dans le fichier de l'étape, ou dans la réponse quand le workflow n'a pas de dossier) et dire ce qui reste à la charge de la personne.

```text
/plugin marketplace add Gremelinn0/zerogravity-skills
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin marketplace add coreyhaines31/marketingskills
/plugin install consultant-ia@zerogravity
/plugin install marketing-skills@marketingskills
/plugin install sales@knowledge-work-plugins
/plugin install small-business@knowledge-work-plugins
```

Les workflows cités ici sont dans le même dépôt (le dépôt s'ajoute une fois : `/plugin marketplace add Gremelinn0/zerogravity-skills`) :

```text
/plugin install conclure-une-vente@zerogravity
/plugin install fideliser-et-faire-recommander@zerogravity
/plugin install organiser-sa-force-de-vente@zerogravity
/plugin install trouver-ses-prochains-clients@zerogravity
```
<!-- prerequis:fin -->

## Étapes

### 0. Le dossier, puis l'état (lecture seule)

**Le dossier.** Une semaine, un dossier : `pipeline/AAAA-Sww/` (par exemple `pipeline/2026-S45/`), à la racine du dossier de l'entreprise, avec son propre journal et ses propres fichiers. Une nouvelle semaine repart donc proprement à l'étape 1. Dossier `pipeline/` absent ou vide : il n'y a encore rien de fait, l'état est « étape 1 » et le dossier de la semaine en cours se crée au premier passage. La semaine par défaut est la plus récente qui n'est pas terminée, ou celle que la personne nomme. Si elle est antérieure à la semaine en cours, on le dit et on demande : la terminer, ou la clore (une ligne `sautée` au journal pour chaque étape restante) et ouvrir la semaine en cours. Si toutes les semaines sont terminées, on crée celle de la semaine en cours. Si le dossier courant n'est pas celui de l'entreprise, le dire en une ligne et demander où il vit : rien ne s'écrit avant.

**Les données.** Les chiffres viennent du CRM ou de son export ; les noms des contacts restent dans le CRM : le dossier de la semaine n'en garde aucun, mais les compétences appelées peuvent lire le CRM et y écrire (la remise au propre de l'étape 1 compare et fusionne des contacts, après validation). Sans CRM, un tableur suffit, avec une ligne par affaire : entreprise, montant, étape, date de la dernière activité, prochaine étape, date de clôture prévue. La prévision de la semaine précédente, `pipeline/<semaine précédente>/05-prevision.md`, sert de point de comparaison à l'étape 5 si elle existe ; sinon on le dit et on prévoit sans comparaison.

**L'état**, calculé depuis le journal et les fichiers de la semaine :

```text
Semaine            2026-S45
Étapes             01 ✓  02 ✓  03 -  04 -  05 -  06 -  07 -
Dernière décision  <date> · 02 · fait · revue du pipeline
Étape suivante     03 Débloquer les affaires qui stagnent → sales:deal-advance-gap
```

- Le journal `pipeline/AAAA-Sww/journal.md` a une ligne par décision : `AAAA-MM-JJ · NN · fait | en attente | sans objet | sautée | corrigée · <une phrase>`.
- Pour chaque étape, la dernière ligne du journal qui la nomme fait foi. `✓` : cette ligne dit `fait` ou `corrigée` et le fichier de l'étape existe. `s.o.` : elle dit `sans objet` ou `sautée` (l'étape n'est plus proposée). `-` : aucune ligne, ou le fichier manque.
- `corrigée` : l'étape est refaite après une correction ; elle reste ✓ et la ligne dit ce qui a changé. `sautée` : la personne a choisi de passer ; la ligne dit pourquoi.
- `en attente` : l'étape est préparée, mais elle dépend d'un geste ou d'une réponse qui arrive hors de la conversation. La ligne du journal dit ce qu'on attend et de qui. L'état l'affiche `att.` avec ce texte : l'étape n'est pas `✓`, parce que préparé n'est pas fait. Le workflow s'arrête là et le dit ; il n'invente jamais la suite (ni réponse, ni résultat, ni geste qu'on ne lui a pas confirmé). Quand la personne apporte ce qui est arrivé, la ligne `fait` suit. Ici : la validation d'une fusion ou d'une suppression de contacts (étape 1), l'envoi des relances par la personne et les réponses qu'elles appellent (étape 4), les validations du responsable commercial (étapes 3, 5, 6 et 7).
- L'étape suivante est la première étape `-` ou `att.`, dans l'ordre (devant une étape `att.`, on demande d'abord où en est l'attente). Si aucune ne l'est, la revue de la semaine est terminée, et on peut ouvrir la suivante.

**Une question n'est pas un ordre.** « Où en est mon pipeline ? » : on affiche l'état et la prochaine action, puis on s'arrête. « Piloter mon pipeline », « continue » ou « déroule » : on enchaîne jusqu'à la première étape en attente, puis on s'arrête et on le dit.

**Une demande au milieu du chemin** (« fais ma prévision »). L'étape 5 exige un CRM propre (étape 1) et une revue (étape 2). Sans elles, on fait d'abord le contrôle en lecture seule avec `sales:crm-hygiene-check`, on dit ce qui fausse la prévision, puis on prévoit en le signalant.

### 1. Lancer l'étape suivante

Lire l'étape dans la table, appliquer sa règle de choix, invoquer la compétence retenue, écrire sa sortie dans le fichier de l'étape, inscrire « fait » au journal (ou `en attente`, voir plus haut), puis passer à la suivante sans redemander. Une étape qui porte un « Manque » le dit franchement, avec le geste humain qui le comble.

<!-- etapes:debut -->
| # | Étape | Compétences | Règle de choix |
|---|---|---|---|
| 1 | Remettre le CRM au propre | `small-business:crm-autopilot` · `sales:crm-hygiene-check` · `sales:update-opportunity` · `consultant-ia:auditer-crm` · Clôturer sa journée commerciale : `sales:end-of-day` | crm-autopilot pour les doublons et les trous ; crm-hygiene-check pour les règles des affaires ; update-opportunity applique ce qui a été validé. Une fusion ou une suppression se soumet, jamais ne s'exécute seule. |
| 2 | Revoir le pipeline | `sales:pipeline-review` · `sales:deal-signals` · Faire le point du jour et de la semaine : `sales:daily-briefing` ; `sales:weekly-wrap` · Voir le pipeline de l'équipe : `sales:team-pipeline` | La revue une fois par semaine ; la veille de deal-signals entre deux revues, avec des seuils réglés sur la durée du cycle de vente. |
| 3 | Débloquer les affaires qui stagnent | `sales:deal-advance-gap` · `sales:stakeholder-map` | deal-advance-gap sur chaque affaire signalée par la revue ; stakeholder-map quand le blocage est un décideur absent. Les actions et les engagements se font valider par le responsable commercial. |
| 4 | Relancer les affaires endormies | à la main | La partie relance de l'étape 1 : les affaires sans activité depuis quatorze jours ou à échéance dépassée, un message dans la voix du vendeur. Les oppositions, la fréquence et le consentement se vérifient avant chaque envoi. Manque : pas de compétence propre à cette étape : la partie relance de small-business:crm-autopilot (étape 1) peut la porter, et le contrôle des oppositions et de la fréquence se fait à la main avant chaque envoi. |
| 5 | Prévoir le chiffre | `sales:deal-review` · `sales:deal-slip-scenario` · `sales:forecast` | Dans l'ordre : deal-review qualifie les hypothèses, deal-slip-scenario chiffre les scénarios, forecast écrit le récit. L'arbitrage reste au responsable commercial. |
| 6 | Comprendre pourquoi on gagne et on perd | `sales:win-loss-review` · `marketing-skills:sales-enablement` · `marketing-skills:customer-research` | win-loss-review pour les chiffres ; les entretiens par customer-research ; l'analyse des motifs par la partie gains et pertes de sales-enablement. Les conclusions se soumettent à la direction commerciale. |
| 7 | Développer les clients en place | `sales:expansion-whitespace` · `sales:customer-health` · `sales:renewal-radar` · Écrire le plan d'un compte stratégique : `sales:account-plan` | sales:customer-health et sales:renewal-radar disent quand ; sales:expansion-whitespace dit quoi. Seules les offres déjà approuvées se proposent ; le responsable du compte confirme, le client décide. |
<!-- etapes:fin -->

### 2. Clore un passage

À la fin de chaque séance, on note au journal l'état (fait, reste, prochaine action) et les décisions prises. Une compétence qui a déçu à une étape se note aussi : on rouvre alors le choix de cette étape.

## Ce qui manque

- **Le contrôle des oppositions et de la fréquence avant une relance** (étape 4) : aucune compétence publique ne le fait. On le branche à la main sur le fichier de référence des contacts du client (désinscriptions, refus, dernier contact), avant chaque envoi.

## Frontières

Les workflows cités ici se trouvent dans le même dépôt de plugins que celui-ci.

| Demande | Va à |
|---|---|
| Une affaire précise jusqu'à la signature | `/conclure-une-vente:conclure-une-vente` |
| Trouver de nouveaux prospects | `/trouver-ses-prochains-clients:trouver-ses-prochains-clients` |
| Auditer le CRM en profondeur (champs, automatisations, tableaux de bord) | `consultant-ia:auditer-crm`, en lecture seule |
| L'objectif de revenu et la capacité de l'équipe | `/organiser-sa-force-de-vente:organiser-sa-force-de-vente` |
| Retenir des clients qui partent, les faire recommander | `/fideliser-et-faire-recommander:fideliser-et-faire-recommander` |
