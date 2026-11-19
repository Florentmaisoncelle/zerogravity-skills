---
name: creer-une-app
description: >-
  Quand on veut créer une application, un SaaS, une web app ou une plateforme d'agents de bout en bout → afficher
  l'état du projet calculé depuis le dossier `projet-app/`, puis dérouler les onze étapes dans l'ordre (cadrer,
  spécifier, architecture, site web, back-end, agents IA, paiement, construire, tester, mettre en ligne, lancer et
  trouver ses clients), chacune par la meilleure compétence publique ou par le workflow frère qui la porte, avec une
  règle de choix quand plusieurs compétences font la même chose. Le site se prépare hors ligne à l'étape 4 ; ses
  mesures en ligne (vitesse, accessibilité, référencement) se rejouent après la mise en ligne. Dit franchement ce qui
  se fait à la main : le nom et le domaine, la vérification avant de construire. Se lance par
  `/creer-une-app:creer-une-app`. Déclencheurs : « créer une app », « créer un SaaS », « créer une web app »,
  « créer une plateforme », « plateforme d'agents », « lancer mon app », « de l'idée au lancement », « où en est mon
  app ». Pas pour un agent seul, sans app autour (/creer-un-agent-ia:creer-un-agent-ia). Pas pour une stratégie ou
  une offre (/cadrer-un-chantier:cadrer-un-chantier). Pas pour une fonctionnalité de plus ni pour un défaut
  (/faire-evoluer-une-app:faire-evoluer-une-app). Pas pour un site vitrine seul (/creer-un-site-web:creer-un-site-web).
---

# Créer une app, un SaaS ou une plateforme d'agents, de l'idée aux premiers clients

## Ce que ce workflow résout

Créer une app demande onze gestes dans l'ordre, et pour chacun plusieurs compétences installées font à peu près la
même chose. Sans point d'entrée, chaque session part de la compétence qu'elle connaît, saute le cadrage ou le test,
et on réexplique à chaque fois. Ici : l'ordre, l'état, le choix tranché. Les quatre grosses étapes (le site, la
construction, les tests, la mise en ligne) ont chacune leur workflow frère, que « ajouter une fonctionnalité » et
« corriger un défaut » réutilisent.

**Résultat attendu** : une app cadrée, construite, testée, en ligne et lancée ; un dossier `projet-app/` qui dit à
tout moment où on en est ; une seule validation de la personne qui porte le projet, à la fiche de cadrage (fin de
l'étape 1).

## Stratégie

1. **Les étapes, leurs compétences et leurs règles de choix** sont dans `references/workflow.json`, d'où le tableau
   plus bas est tiré. En cas de désaccord, c'est ce fichier qui fait foi.
2. **Une compétence, un seul endroit.** Chaque compétence n'apparaît qu'à une étape. Quand un workflow frère existe
   pour un groupe (cadrage, site web, agents, construction, tests, mise en ligne, acquisition), l'étape cite ce
   workflow, jamais ses membres.
3. **L'état d'abord, toujours calculé** depuis les fichiers de `projet-app/`, jamais recopié.
4. **L'ordre protège la décision** : pas de site avant la spécification, pas de construction sans architecture, pas de
   mise en ligne sans le verdict « on met en ligne » de l'étape des tests. Sauter une étape reste possible sur
   demande ; le journal dit laquelle et pourquoi.
5. **Une seule validation**, à la fin de l'étape 1 : la fiche de cadrage. Ensuite tout se déroule jusqu'au résultat.
   Restent à la personne : le goût produit non tranché, le paiement réel, un compte à créer, une publication publique.
6. **Un site se mesure en ligne, pas sur une maquette.** À l'étape 4, le site se limite à ce qui existe hors ligne : la
   carte des écrans, le texte, le design, les composants et le plan de suivi. Les mesures qui supposent un site en
   ligne (trace de vitesse, accessibilité en direct, référencement) se jouent après la mise en ligne de l'étape 10,
   quand on relance `/creer-un-site-web:creer-un-site-web` au début de l'étape 11.
7. **Chaque passage se ferme au journal** : une correction devient une règle, un test ou une ligne du workflow.

<!-- prerequis:debut -->
## Prérequis

Ce workflow s'appuie sur des compétences publiques, installées à part. Aucune n'est indispensable : si l'une manque, le workflow le dit et fait l'étape à la main. Faire l'étape à la main veut dire suivre sa règle de choix, écrire ce qu'elle doit rendre (dans le fichier de l'étape, ou dans la réponse quand le workflow n'a pas de dossier) et dire ce qui reste à la charge de la personne.

```text
/plugin marketplace add addyosmani/agent-skills
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin marketplace add anthropics/skills
/plugin marketplace add coreyhaines31/marketingskills
/plugin install agent-skills@addy-agent-skills
/plugin install auth0@knowledge-work-plugins
/plugin install claude-api@anthropic-agent-skills
/plugin install engineering@knowledge-work-plugins
/plugin install marketing-skills@marketingskills
/plugin install product-management@knowledge-work-plugins
/plugin install stripe@claude-plugins-official
/plugin install supabase@claude-plugins-official
npx skills add bmad-code-org/BMAD-METHOD --skill bmad-architecture -a claude-code
npx skills add bmad-code-org/BMAD-METHOD --skill bmad-prd -a claude-code
npx skills add bmad-code-org/BMAD-METHOD --skill bmad-prfaq -a claude-code
npx skills add bmad-code-org/BMAD-METHOD --skill bmad-product-brief -a claude-code
npx skills add bmad-code-org/BMAD-METHOD --skill bmad-ux -a claude-code
```

La commande `npx skills add` (CLI Vercel `skills`) demande Node.js 22.20 ou plus (vérifié le 06/11/2026, https://github.com/vercel-labs/skills). Claude Code installé avec l'installeur natif n'en a pas besoin.

Les workflows cités ici sont dans le même dépôt (le dépôt s'ajoute une fois : `/plugin marketplace add Gremelinn0/zerogravity-skills`) :

```text
/plugin install cadrer-un-chantier@zerogravity
/plugin install construire@zerogravity
/plugin install creer-un-agent-ia@zerogravity
/plugin install creer-un-site-web@zerogravity
/plugin install faire-evoluer-une-app@zerogravity
/plugin install lancer-un-produit@zerogravity
/plugin install mettre-en-ligne@zerogravity
/plugin install tester-et-securiser@zerogravity
/plugin install trouver-ses-prochains-clients@zerogravity
```
<!-- prerequis:fin -->

Les compétences du site ont leurs propres commandes, dans `/creer-un-site-web:creer-un-site-web`.

## Étapes

### 0. Le dossier, puis l'état (lecture seule)

**Le dossier.** L'app vit dans son propre dépôt, jamais dans celui d'un autre produit, et son dossier d'état est
`projet-app/` à la racine de ce dépôt. Dossier absent ou vide : il n'y a encore rien de fait, l'état est « étape 1 » et
le dossier se crée au premier passage. Si le dossier courant appartient à un autre produit, le dire en une ligne : le
dépôt se nomme à la fiche de cadrage et se crée à sa validation (`git init`) ; avant cette validation, rien ne
s'écrit, la fiche se travaille dans la conversation. Si le dossier courant n'est pas celui du projet et qu'on ne sait
pas où il vit, demander : rien ne s'écrit avant.

**L'état**, calculé depuis le journal et les fichiers :

```text
Projet          mon-app
Étapes          01 ✓  02 ✓  03 -  04 -  05 -  06 s.o.  07 -  08 -  09 -  10 -  11 -
Dernière décision  2026-11-06 · 02 · document produit écrit
Étape suivante  03 L'architecture et les données → bmad-architecture
```

- Le journal `projet-app/journal.md` a une ligne par décision :
  `AAAA-MM-JJ · NN · fait | en attente | sans objet | sautée | corrigée · <une phrase>`.
- Pour chaque étape, la dernière ligne du journal qui la nomme fait foi. `✓` : cette ligne dit `fait` ou `corrigée` et
  le fichier de l'étape existe. `s.o.` : elle dit `sans objet` ou `sautée` (l'étape n'est plus proposée). `-` : aucune
  ligne, ou le fichier manque.
- `corrigée` : l'étape est refaite après une correction ; elle reste ✓ et la ligne dit ce qui a changé. `sautée` : la
  personne a choisi de passer ; la ligne dit pourquoi. `sans objet` : tranché à la fiche de cadrage (étapes 6 et 7).
- `en attente` : l'étape est préparée, mais elle dépend d'un geste ou d'une réponse qui arrive hors de la conversation. La ligne du journal dit ce qu'on attend et de qui. L'état l'affiche `att.` avec ce texte : l'étape n'est pas `✓`, parce que préparé n'est pas fait. Le workflow s'arrête là et le dit ; il n'invente jamais la suite (ni réponse, ni résultat, ni geste qu'on ne lui a pas confirmé). Quand la personne apporte ce qui est arrivé, la ligne `fait` suit. Ici : la validation de la fiche de cadrage (étape 1), la décision d'un tiers d'ouvrir l'app au public quand elle est faite pour lui (étape 10), et les envois que la personne fait pour trouver ses clients (étape 11).
- L'étape suivante est la première étape `-` ou `att.`, dans l'ordre (devant une étape `att.`, on demande d'abord où en est l'attente). Si aucune ne l'est, le workflow est terminé.

**Les étapes confiées à un workflow frère** (4, 8, 9, 10) écrivent leur travail dans le dossier du frère, qui vit dans
le même dépôt : `projet-site/` pour le site, `construction/` pour la construction, `tests/` pour les tests,
`mise-en-ligne/` pour la mise en ligne. Chaque étape déléguée écrit aussi, dans `projet-app/`, une note courte dans son
propre fichier (`04-site-web.md`, `08-construction.md`, `09-tests.md`, `10-mise-en-ligne.md`) : le résultat, la décision
et le dossier du frère où lire son état. L'état du frère se lit dans son dossier, jamais dans celui de l'app.

- Étape 4 : `✓` quand les étapes 1 à 4 et 8 du site sont `✓` ou `s.o.` dans `projet-site/` (la partie hors ligne). La
  partie du site qui se joue en ligne attend l'étape 11.
- Étape 8 : `✓` quand toutes les étapes de `construction/` le sont.
- Étape 9 : `✓` seulement quand `tests/` porte le verdict « on met en ligne ». Avec « on ne met pas en ligne », la note
  garde le verdict, l'étape reste `-` et le workflow s'arrête avant l'étape 10 : la personne choisit de corriger
  (retour à l'étape 8, inscrite `corrigée`, puis l'étape 9 est refaite) ou d'arrêter là (étapes 10 et 11 inscrites
  `sautée`, avec la raison ; le code reste dans le dépôt).
- Étape 10 : `✓` quand toutes les étapes de `mise-en-ligne/` le sont. La note donne l'adresse officielle de l'app, et le
  workflow écrit aussi dans `projet-site/journal.md` la ligne `AAAA-MM-JJ · 00 · fait · en ligne : <adresse officielle>` : sans
  elle, les étapes du site marquées « sur le site en ligne » restent à l'écart.

**Une question n'est pas un ordre.** « Où en est mon app ? » → l'état et la prochaine action, puis on s'arrête. La
commande `/creer-une-app:creer-une-app`, « continue » ou « déroule » → on enchaîne jusqu'à la première étape en attente, puis on s'arrête et on le dit.

### Inscrire une app qui existe déjà

Une app construite avant ce workflow s'inscrit après coup, sans rien refaire. Dans son dépôt, `projet-app/` reçoit,
pour chaque étape déjà faite, un fichier de trois lignes qui dit où vit la preuve, et le journal porte sa ligne `fait`,
datée du jour de l'inscription. Une étape sans objet pour cette version reçoit `sans objet` et sa raison. Quand l'app
tourne déjà, l'ordre des étapes restantes se fixe par une ligne du journal qui ne nomme aucune étape :
`AAAA-MM-JJ · 00 · fait · Ordre : 08, 05, 04, 09, 10, 11 · <raison>`. La dernière de ces lignes l'emporte ; sans elle,
c'est l'ordre du workflow.

### 1. Lancer l'étape suivante

Lire l'étape dans le tableau ci-dessous, appliquer sa **règle de choix**, invoquer la compétence retenue (ou le
workflow frère) **en mode sans dialogue** quand elle en a un, puisque le cadrage est déjà validé. Écrire dans le
fichier de l'étape sa sortie ou, si la compétence écrit ailleurs, une ligne qui dit où elle vit. Inscrire `fait` au
journal (ou `en attente`, voir plus haut), puis passer à la suivante sans redemander.

La fiche de cadrage de l'étape 1 est la seule validation : elle tranche le dépôt, l'étape 6 (agentique ou non),
l'étape 7 (payante ou non) et la conformité à prévoir. Quand elle est validée, le journal reçoit une ligne `sans objet`
pour chaque étape écartée (6 ou 7). Une étape confiée à un workflow frère s'appelle sans second dialogue : ce que ce
workflow demande au cadrage est déjà tranché par la fiche. Tout texte publié au nom de la personne se relit avant
d'être montré (aucune compétence publique pour ça : on le fait à la main, en phrases courtes et en mots simples).

**Si l'app est faite pour un tiers** (un client, un employeur), c'est lui qui décide de l'ouvrir au public : on
prépare, on déploie en brouillon, on vérifie, et on lui remet la main.

<!-- etapes:debut -->
| # | Étape | Compétences | Règle de choix |
|---|---|---|---|
| 1 | Cadrer l'idée | `cadrer-un-chantier` · Cadrer l'idée du produit : `bmad-prfaq` ; `bmad-product-brief` | Par /cadrer-un-chantier:cadrer-un-chantier, arrêté à la fiche produit : il pose le problème, élargit, étudie le marché, attaque le plan. La fiche tranche aussi le dépôt de l'app, si elle est agentique (étape 6) et payante (étape 7) ; c'est la seule validation. |
| 2 | Écrire le produit | `bmad-prd` · `product-management:write-spec` · Écrire ce que le produit doit faire : `agent-skills:spec-driven-development` | bmad-prd, après bmad setup dans le dépôt de l'app (première action de l'étape) ; product-management:write-spec seulement si BMAD ne peut pas s'y installer. |
| 3 | L'architecture et les données | `bmad-architecture` · `engineering:architecture` · Dessiner l'interface d'une API : `agent-skills:api-and-interface-design` | bmad-architecture pour l'ensemble, en mode sans dialogue ; pour une plateforme agentique, elle prévoit d'emblée l'accès aux outils, la mémoire et l'isolation des données de chaque client. engineering:architecture pour une seule décision. |
| 4 | Le site web | `creer-un-site-web` | Par /creer-un-site-web:creer-un-site-web, arrêté à ses étapes hors ligne (1 à 4 et 8) ; pour une app, la carte des pages inclut les écrans et leurs états (bmad-ux). Pas de trace de vitesse sur une maquette : les étapes du site qui mesurent un site en ligne se rejouent après la mise en ligne, au début de l'étape 11. Le code de l'app s'écrit à l'étape 8. |
| 5 | Le back-end : données, connexion, sécurité | `supabase:supabase` · `supabase:supabase-postgres-best-practices` · Ajouter la connexion des utilisateurs : `auth0:auth0` | Le plugin officiel de Supabase ; la connexion par Supabase, sauf exigence d'entreprise. |
| 6 | Les agents IA (seulement pour une plateforme agentique) | `creer-un-agent-ia` · `claude-api:claude-api` | Les agents par /creer-un-agent-ia:creer-un-agent-ia, repris à sa construction : le cadrage et l'architecture sont déjà faits, pas de seconde validation. Le code qui appelle Claude par claude-api:claude-api. |
| 7 | Le paiement (seulement si l'app est payante) | `marketing-skills:pricing` · `stripe:stripe-best-practices` · Écran d'abonnement : `marketing-skills:paywalls` · Brancher les paiements Stripe : `stripe:connect-recommend` ; `stripe:connect-required-verification-information` ; `stripe:metronome` ; `stripe:upgrade-stripe` | Le prix d'abord ; Stripe ensuite, avec les clés de test du propriétaire de l'app, jamais de clé réelle. Passer en réel reste son geste. |
| 8 | Construire | `construire` | Par /construire:construire, sur le document produit et l'architecture ; le site, le back-end, les agents et le paiement se construisent dans cette boucle, lot par lot. |
| 9 | Tester et sécuriser | `tester-et-securiser` | Par /tester-et-securiser:tester-et-securiser ; avant la première mise en ligne, le scan de sécurité en profondeur est obligatoire. Avec le verdict « on ne met pas en ligne », on corrige (retour à l'étape 8) ou on arrête là. |
| 10 | Mettre en ligne | `mettre-en-ligne` | Par /mettre-en-ligne:mettre-en-ligne ; pour l'app d'un client, l'ouverture au public est son geste. Si l'app est faite pour un tiers, c'est lui qui décide de l'ouvrir au public : on s'arrête au brouillon vérifié et on lui remet la main. |
| 11 | Lancer et trouver ses clients | `lancer-un-produit` · `trouver-ses-prochains-clients` | Le lancement par /lancer-un-produit:lancer-un-produit, à partir de son étape 2 ; les prospects par /trouver-ses-prochains-clients:trouver-ses-prochains-clients quand la cible est une entreprise joignable sur LinkedIn, où rien ne part sans validation. Pour un autre public, les canaux du plan de campagne. Le référencement est fait à l'étape 4. Commencer par le site en ligne : relancer /creer-un-site-web:creer-un-site-web, qui propose alors ses étapes marquées « sur le site en ligne » (référencement, vitesse, accessibilité, conversion, amélioration continue) ; la note dit où il en est. |
<!-- etapes:fin -->

### 2. Clore un passage

À la fin de chaque séance, on écrit l'état au journal : ce qui est fait, ce qui reste, la prochaine action. Une
compétence qui a déçu à une étape se signale au journal, pour rouvrir le choix de cette étape.

## Pourquoi ces choix

- Onze étapes, de l'idée à l'acquisition ; les doublons sont tranchés par une règle écrite (le document produit de
  BMAD, avec `product-management:write-spec` en repli quand `bmad-prd` n'est pas installée ; le Supabase officiel plutôt
  que plusieurs compétences tierces).
- **La meilleure compétence pour la tâche**, jamais une plus faible parce qu'elle est déjà installée.
- **Les grosses étapes ont leur propre workflow** (le site, la construction, les tests, la mise en ligne). Leurs
  compétences y vivent, une seule fois ; ce workflow-ci les cite, jamais leurs membres.
- **La critique du design et le référencement ne sont pas des étapes à part** : ils vivent dans le workflow du site. Le
  référencement et les mesures en ligne se jouent au début de l'étape 11, quand le site existe en ligne.
- **Pas d'étape « architecture des écrans »** : pour une app, la carte des pages du site inclut les écrans et leurs
  états (vide, erreur, sans droit).

## Ce qui manque

Trois gestes n'ont pas de compétence publique et se font à la main.

- **Choisir le nom et le domaine.** Chercher trois à cinq noms courts, faciles à épeler à l'oral ; vérifier que le
  domaine voulu est libre chez un bureau d'enregistrement ; chercher le nom dans la base des marques de l'office de
  propriété intellectuelle du pays visé (en France l'INPI, dans l'Union européenne l'EUIPO) et dans les magasins d'apps
  ; vérifier que le même nom est libre sur les réseaux utiles. Acheter le domaine reste un geste de la personne. Le
  choix s'écrit dans `01-cadrage.md`.
- **Vérifier que tout est prêt avant de construire** (début de l'étape 8). Relire le document produit et
  l'architecture ensemble : chaque fonctionnalité a ses critères d'acceptation ; chaque donnée de l'architecture sert
  une fonctionnalité, et inversement ; les mêmes mots désignent les mêmes choses ; les questions encore ouvertes sont
  listées avec qui tranche. Le résultat s'écrit en tête de `08-construction.md`.
- **Relire les textes publiés** : à la main, en phrases courtes et en mots simples.

## Frontières

| Demande | Va à |
|---|---|
| Un agent ou un système seul, sans app | `/creer-un-agent-ia:creer-un-agent-ia` |
| Une stratégie, une offre, un produit non logiciel | `/cadrer-un-chantier:cadrer-un-chantier` |
| Ajouter une fonctionnalité à une app existante, corriger un défaut | `/faire-evoluer-une-app:faire-evoluer-une-app` |
| Un site vitrine seul, sans app autour | `/creer-un-site-web:creer-un-site-web` |
| L'acquisition de clients seule | `/trouver-ses-prochains-clients:trouver-ses-prochains-clients` |
