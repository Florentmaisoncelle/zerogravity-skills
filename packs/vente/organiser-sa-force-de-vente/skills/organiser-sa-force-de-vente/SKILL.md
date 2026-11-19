---
name: organiser-sa-force-de-vente
description: >-
  Quand on veut organiser sa force de vente (fixer un objectif de chiffre réaliste, dimensionner la capacité commerciale, répartir les rôles de l'équipe, écrire un plan de commissions, trouver des apporteurs d'affaires, faire adopter un nouveau processus de vente) → affiche l'état du plan calculé depuis le dossier `plan-commercial/`, puis déroule cinq étapes dans l'ordre : l'objectif et la capacité, les rôles, l'incitation, les partenaires, l'adoption. Ce qui manque est dit franchement (le plan de revenus par quota et territoire, le plan d'incitation et le droit du travail). Se lance par `/organiser-sa-force-de-vente:organiser-sa-force-de-vente`. Déclencheurs : « plan commercial », « objectif de revenu », « capacité commerciale », « rôles de l'équipe commerciale », « plan de commission », « plan d'incitation », « apporteurs d'affaires », « partenariats commerciaux », « faire adopter le process de vente ». Pas pour recruter un commercial : `/recruter:recruter`. Pas pour le parrainage de clients : `/fideliser-et-faire-recommander:fideliser-et-faire-recommander`. Pas pour une campagne avec un partenaire : `/lancer-un-produit:lancer-un-produit`.
---

# Organiser sa force de vente : l'objectif, l'équipe, l'incitation et les partenaires

## Ce que ce workflow résout

Organiser une équipe commerciale demande cinq gestes dans l'ordre, et les compétences existantes en couvrent trois, souvent en morceaux. Sans méthode, on invente un plan de commissions sans droit du travail, ou on fixe un objectif sans regarder les conversions réelles. Ici : l'ordre, les morceaux qui existent, et deux trous dits franchement (le plan de revenus par quota et territoire, le plan d'incitation).

**Résultat attendu** : un objectif de revenu tiré des conversions réelles, les rôles et les escalades de l'équipe, un plan d'incitation simulé et validé par les ressources humaines et un juriste, des partenaires cadrés, puis un changement adopté par un pilote.

## Stratégie

1. **L'état d'abord**, toujours calculé depuis les fichiers de `plan-commercial/`, jamais recopié.
2. **Un choix par étape.** Chaque étape a sa compétence par défaut et sa règle de choix, dans la table plus bas, qui vient de `references/workflow.json`.
3. **L'ordre protège la décision** : pas d'incitation sans objectif, pas de généralisation sans pilote (un essai sur un petit groupe). Sauter une étape reste possible sur demande ; le journal dit laquelle et pourquoi.
4. **Une validation de départ, à l'étape 1** : l'objectif et ses scénarios, validés par la personne qui dirige l'entreprise avec celle qui suit les ventes et celle qui tient les comptes. Ensuite le travail se déroule, avec trois accords humains qui ne se délèguent pas : la validation du plan d'incitation par les ressources humaines, la paie et un juriste avant toute annonce (étape 3) ; l'accord de partenariat, signé par une personne (étape 4) ; l'arbitrage des rôles par le dirigeant (étape 2).
5. **Tout texte qui sort au nom de l'entreprise** est relu avant d'être montré, et rien ne part sans validation.
6. **Chaque passage se clôt au journal** : ce qui est fait, ce qui reste, la prochaine action.

<!-- prerequis:debut -->
## Prérequis

Ce workflow s'appuie sur des compétences publiques, installées à part. Aucune n'est indispensable : si l'une manque, le workflow le dit et fait l'étape à la main. Faire l'étape à la main veut dire suivre sa règle de choix, écrire ce qu'elle doit rendre (dans le fichier de l'étape, ou dans la réponse quand le workflow n'a pas de dossier) et dire ce qui reste à la charge de la personne.

```text
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin marketplace add coreyhaines31/marketingskills
/plugin install human-resources@knowledge-work-plugins
/plugin install marketing-skills@marketingskills
/plugin install operations@knowledge-work-plugins
/plugin install product-management@knowledge-work-plugins
/plugin install sales@knowledge-work-plugins
```

Les workflows cités ici sont dans le même dépôt (le dépôt s'ajoute une fois : `/plugin marketplace add Florentmaisoncelle/zerogravity-skills`) :

```text
/plugin install fideliser-et-faire-recommander@zerogravity
/plugin install lancer-un-produit@zerogravity
/plugin install piloter-le-pipeline@zerogravity
/plugin install recruter@zerogravity
```
<!-- prerequis:fin -->

## Étapes

### 0. Le dossier, puis l'état (lecture seule)

**Le dossier.** Le plan vit dans le dossier de l'entreprise : `plan-commercial/` à sa racine, avec son journal `journal.md`. Il n'y a qu'un plan à la fois. Il porte les rôles et les règles, jamais la rémunération nominative d'une personne. Dossier absent ou vide : il n'y a encore rien de fait, l'état est « étape 1 » et le dossier se crée au premier passage. Si le dossier courant n'est pas celui de l'entreprise, le dire en une ligne et demander où elle vit : rien ne s'écrit avant.

**L'état**, calculé depuis le journal et les fichiers de `plan-commercial/` :

```text
Plan               2026
Étapes             01 ✓  02 ✓  03 -  04 -  05 -
Dernière décision  <date> · 02 · fait · rôles validés par le dirigeant
Étape suivante     03 Écrire le plan d'incitation (à la main, avec un juriste)
```

- Le journal `plan-commercial/journal.md` a une ligne par décision : `AAAA-MM-JJ · NN · fait | en attente | sans objet | sautée | corrigée · <une phrase>`.
- Pour chaque étape, la dernière ligne du journal qui la nomme fait foi. `✓` : cette ligne dit `fait` ou `corrigée` et le fichier de l'étape existe. `s.o.` : elle dit `sans objet` ou `sautée` (l'étape n'est plus proposée). `-` : aucune ligne, ou le fichier manque.
- `corrigée` : l'étape est refaite après une correction ; elle reste ✓ et la ligne dit ce qui a changé. `sautée` : la personne a choisi de passer ; la ligne dit pourquoi.
- `en attente` : l'étape est préparée, mais elle dépend d'un geste ou d'une réponse qui arrive hors de la conversation. La ligne du journal dit ce qu'on attend et de qui. L'état l'affiche `att.` avec ce texte : l'étape n'est pas `✓`, parce que préparé n'est pas fait. Le workflow s'arrête là et le dit ; il n'invente jamais la suite (ni réponse, ni résultat, ni geste qu'on ne lui a pas confirmé). Quand la personne apporte ce qui est arrivé, la ligne `fait` suit. Ici : les validations de la personne et des spécialistes (étapes 1 à 3), les réponses des partenaires (étape 4) et l'adoption par l'équipe (étape 5).
- L'étape suivante est la première étape `-` ou `att.`, dans l'ordre (devant une étape `att.`, on demande d'abord où en est l'attente). Si aucune ne l'est, le plan est terminé. Pour le réviser (chaque année, ou après un changement d'équipe), on refait l'étape concernée dans son fichier et le journal reçoit une ligne `corrigée` avec la date et ce qui change.

**Une question n'est pas un ordre.** « Où en est mon plan commercial ? » : on affiche l'état et la prochaine action, puis on s'arrête. « Organiser ma force de vente », « continue » ou « déroule » : on enchaîne jusqu'à la première étape en attente, puis on s'arrête et on le dit.

**Une demande au milieu du chemin** (« fais-moi un plan de commissions »). L'étape 3 exige l'objectif de l'étape 1. Sans `01-objectif.md`, on pose d'abord l'objectif et la capacité, on les fait valider, puis on écrit les règles, en disant qu'aucune compétence publique de la liste ne connaît le droit du travail français.

### 1. Lancer l'étape suivante

Lire l'étape dans la table, appliquer sa règle de choix, invoquer la compétence retenue, écrire sa sortie dans le fichier de l'étape, inscrire « fait » au journal (ou `en attente`, voir plus haut), puis passer à la suivante sans redemander. Une étape qui porte un « Manque » le dit franchement, avec le geste humain qui le comble.

<!-- etapes:debut -->
| # | Étape | Compétences | Règle de choix |
|---|---|---|---|
| 1 | Fixer l'objectif de revenu et la capacité | `operations:capacity-plan` · `sales:pipeline-review` | Partir du terrain (les conversions réelles), puis des objectifs du dirigeant ; comparer les scénarios avec la direction commerciale et la finance (la personne qui suit les ventes et celle qui tient les comptes), et versionner le plan approuvé. operations:capacity-plan donne la capacité, sales:pipeline-review la couverture. Manque : aucune compétence ne construit un plan de revenus par quota, montée en puissance et territoire : à fabriquer. En attendant, la capacité et la couverture se calculent séparément. |
| 2 | Répartir les rôles de l'équipe | `operations:process-doc` · `human-resources:org-planning` · `operations:status-report` · Préparer un point individuel avec un commercial : `sales:rep-context` | process-doc pour les rôles et les escalades ; org-planning quand plusieurs organisations se comparent ; status-report pour le point récurrent. La direction arbitre. Le dirigeant arbitre. |
| 3 | Écrire le plan d'incitation | à la main | Des règles simples à vérifier, simulées sur les cas limites avant d'être annoncées. Le plan se valide avec les ressources humaines, la paie et un juriste avant toute annonce. Manque : aucune compétence publique ne conçoit des règles de commission, ne simule les cas limites ni ne suit les exceptions ; aucune compétence de la liste ne couvre le droit du travail ni la paie en France : à faire à la main, avec un juriste et la personne qui tient la paie, en attendant de fabriquer cette compétence. |
| 4 | Trouver les partenaires qui apportent des affaires | `marketing-skills:co-marketing` · `marketing-skills:referrals` | co-marketing pour choisir et cadrer ; referrals pour la rémunération d'un apporteur. L'accord et le partage de données se valident par une personne. |
| 5 | Faire adopter le nouveau fonctionnement | `operations:change-request` · Tenir les parties prenantes informées : `product-management:stakeholder-update` | Un pilote avant la généralisation ; la mesure des usages décide de la suite, avec les responsables et les vendeurs concernés. operations:change-request cadre le changement, product-management:stakeholder-update tient les personnes concernées informées. |
<!-- etapes:fin -->

### 2. Clore un passage

À la fin de chaque séance, on note au journal l'état (fait, reste, prochaine action) et les décisions prises. Une compétence qui a déçu à une étape se note aussi : on rouvre alors le choix de cette étape.

## Ce qui manque

- **Le plan de revenus par quota, montée en puissance et territoire** (étape 1) : aucune compétence publique ne le construit. La capacité et la couverture se calculent séparément, puis on assemble le plan à la main avec la personne qui suit les ventes et celle qui tient les comptes.
- **Le plan d'incitation** (étape 3) : aucune compétence publique ne conçoit les règles de commission, ne simule les cas limites ni ne suit les exceptions. Aucune compétence de la liste ne couvre le droit du travail ni la paie en France : on écrit des règles simples, on les simule à la main sur les cas limites, puis un juriste et la personne qui tient la paie les valident avant toute annonce.

## Frontières

Les workflows cités ici se trouvent dans le même dépôt de plugins que celui-ci.

| Demande | Va à |
|---|---|
| Recruter un commercial | `/recruter:recruter` |
| La revue du pipeline de la semaine | `/piloter-le-pipeline:piloter-le-pipeline` |
| Une campagne avec des partenaires | `/lancer-un-produit:lancer-un-produit` |
| Le parrainage de clients | `/fideliser-et-faire-recommander:fideliser-et-faire-recommander` |
