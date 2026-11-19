---
name: systeme-ia
description: >-
  Poser l'architecture d'un système IA : des agents, des routines, une mémoire et un tableau de
  suivi qui produisent un résultat continu. Dit ce qu'un système doit avoir (son dossier, sa carte,
  sa compétence qui l'opère, ses routines, son interface de validation), l'ordre pour le bâtir, et
  fournit le gabarit d'un registre des systèmes.
  Déclencheurs : « système IA », « architecture de mon système », « un système = une compétence »,
  « la carte du système », « quels sont mes systèmes », « ce système n'a pas de compétence ».
---

# Système IA : bâtir, opérer, recenser

## Le principe

**Un système = une compétence qui l'opère.** Avant de travailler sur un système, on charge sa
compétence. Un système qui n'en a pas reçoit la sienne, rangée dans sa propre maison.

Un système, ce n'est pas un agent isolé. C'est un ensemble qui produit un résultat dans la durée :
un but écrit, une mesure, une mémoire unique, des routines, et un dernier clic humain nommé.
Exemples : une prospection qui tourne chaque jour, une production de contenu, une veille du matin,
un suivi de candidatures.

## Ce que cette compétence résout

Quand on monte des systèmes les uns après les autres, chacun finit éparpillé : des routines sans
propriétaire, des cartes dans des pages que personne n'ouvre, des règles rangées au mauvais endroit,
et aucune liste de ce qui tourne. Résultat typique : une veille arrêtée depuis cinq jours sans que
personne le voie, un calendrier rempli par un ancien planning automatique, trois copies divergentes
de la même compétence d'écriture. Cette compétence donne le gabarit d'un système, l'ordre pour en
bâtir un, et la seule liste des systèmes.

## Les six règles d'architecture

1. **Un système est un produit** : un but écrit, une mesure, une mémoire unique, un dernier clic
   humain nommé.
2. **Une maison par système** : son propre dossier de projet (ou dépôt) quand il doit être partagé
   ou installé ailleurs ; sinon un sous-dossier du projet de l'entreprise.
3. **Chaque pièce chez son propriétaire** : la carte et les priorités dans le fichier d'instructions
   du système (celui que l'assistant lit à chaque session), la méthode dans sa compétence, le
   contrat de chaque routine à un seul endroit, le tableau de suivi dans l'outil de suivi.
4. **Une brique à la fois**, chacune prouvée par un passage réel avant la suivante.
5. **Le consommateur garde ses sources en vie** : une routine dont personne ne lit la sortie meurt
   en silence. Chaque sortie a un lecteur nommé.
6. **L'agent prépare, l'humain valide dans une interface, puis l'agent agit.** Tout ce qui sort au
   nom de la personne (message, post, candidature, envoi) passe par une file où elle valide, modifie,
   commente ou écarte, avec un verrou (rien ne sort sans validation) et un retour (ses corrections
   reviennent à l'agent et nourrissent une banque d'exemples).

## Le kit d'un système

| Pièce | Où elle vit | Comment on la fait |
|---|---|---|
| Le but, la mesure, le dernier clic humain | en tête du fichier d'instructions du système | cadrage du chantier avec la personne, validé une fois |
| La carte : sources, chaîne de traitement, sorties ; chaque routine reliée à son contrat | même fichier (un schéma Mermaid suffit) | la session qui bâtit |
| Les priorités, brique par brique, avec leur état | un fichier `PLAN.md`, auquel le fichier d'instructions renvoie | idem |
| La compétence qui opère le système : étapes, quelle compétence pour quelle demande, frontières, preuves restantes | un dossier `skills/<système>/SKILL.md` dans la maison du système | méthode de création de compétence (structure, déclencheurs, preuves) |
| Les routines : le contrat d'abord, l'armement ensuite | un fichier de contrat par routine, un planificateur pour l'armer | une routine = un contrat écrit + un planificateur |
| La mémoire unique | nommée dans le fichier d'instructions (base de données, tableur, fichiers d'état) | choisie au cadrage, jamais deux |
| Le tableau de suivi : la carte, l'état, ce qui attend l'humain | une page d'un outil de suivi (voir `creer-un-agent-ia:dashboards-hub-master`) | la session qui bâtit |
| L'interface de validation : ce que l'agent a préparé, que l'humain valide avant tout envoi | une page privée (jamais publique quand elle montre des personnes) | la session qui bâtit |
| Le partage, si le système doit tourner ailleurs | un `README.md` (installation, aucun secret) | à la fin, une fois le système éprouvé |

## Bâtir un système

1. **Cadrer** : le problème, le but, la mesure, le dernier clic humain. La personne valide une
   fois ; la suite se déroule sans revalidation par étape. Pour le cadrage et la suite de la
   création, la porte d'entrée est `creer-un-agent-ia:creer-un-agent-ia`.
2. **Poser la maison** : le dossier ou le dépôt, son fichier d'instructions (but, carte, règles,
   vérité lue à ses sources) et son `PLAN.md` (les briques).
3. **Écrire la compétence qui opère le système**, avec son gabarit : quand la charger, les étapes,
   quelle compétence appeler pour quelle demande, les frontières, les preuves restantes. La rendre
   visible de l'assistant (dossier de compétences du projet ou lien vers lui).
4. **Armer les routines**, une par une : contrat écrit, planificateur, première exécution
   observée. Voir `creer-un-agent-ia:construire-solution` pour la construction des pièces.
5. **Monter le tableau de suivi** : la carte, l'état, ce qui attend l'humain.
6. **Inscrire le système au registre** (gabarit plus bas).
7. **Premier passage réel de bout en bout**, avec `creer-un-agent-ia:tester-solution`, puis
   `creer-un-agent-ia:piloter-mise-en-service` pour la mise en service. Ensuite, ranger ce qu'on a
   appris dans la compétence concernée (`creer-un-agent-ia:router-capitalisation`).

## Bâtir pour tous, puis déployer chez chacun

Quand le même système sert plusieurs entreprises ou plusieurs clients, on le bâtit **une fois**
dans sa maison, puis on le **met en place** dans chaque entreprise. Une demande qui change le
système partagé (un nouveau signal, une brique, un mode) remonte d'abord à celui qui le construit.
Il la bâtit pour tous, puis la renvoie à chaque entreprise, qui l'installe chez elle. Celui qui
déploie ne rebâtit pas le système de son côté : il envoie la demande avec son plan et sa preuve, puis
met en place ce qui revient.

**Contrôle** : ce que je m'apprête à faire, est-ce bâtir le système (alors chez son constructeur)
ou le mettre en place dans une entreprise (alors ici) ?

## Opérer un système

- Charger sa compétence ; lire son `PLAN.md` ; lire les reçus de ses routines.
- Une routine muette se diagnostique à un seul endroit (moteur, contrat, mode, outillage), jamais
  en créant un doublon.
- Un défaut se répare chez son propriétaire, dans la même passe.

## Auditer ses systèmes

Pour chaque ligne du registre : la maison existe, la compétence se charge, les routines sont
vivantes dans leur planificateur, le tableau de suivi répond. L'état vivant des routines se lit
dans le planificateur, jamais dans le registre.

## Le registre des systèmes (gabarit)

Une ligne par système. Le registre est une liste, pas une documentation : il ne recopie ni la carte
ni les contrats.

| Système | Pour qui | Maison | Compétence qui l'opère | Routines | Tableau de suivi |
|---|---|---|---|---|---|
| Nom du système | l'entreprise ou le client servi | dossier ou dépôt | `/nom-de-la-competence` | noms des routines | adresse de la page ou « aucun » |

Règles de tenue :
- Un système sans compétence qui l'opère est une ligne en défaut : on la crée avant d'aller plus loin.
- Une case « aucun » est honnête ; une case inventée ne l'est pas.
- On date le relevé et on le revérifie ligne à ligne à chaque audit.

## Décisions et rejets

- **Une compétence par système, plutôt qu'un seul grand aiguillage.** Rejeté : tout faire passer par
  une compétence unique. Un système se charge par son nom ; cette compétence ne garde que le gabarit
  et la liste.
- **La carte dans le fichier d'instructions, pas seulement dans le tableau de suivi** : le tableau se
  lit quand on y pense, le fichier d'instructions est chargé à chaque session.
- **Les routines restent à un seul endroit** : un seul propriétaire des contrats et de l'armement ;
  le système les cite, il ne les recopie pas.

## Frontières

- Créer un agent ou un système de bout en bout : `creer-un-agent-ia:creer-un-agent-ia`, qui appelle
  ce kit pour l'architecture.
- Choisir entre un agent et une simple automatisation : `creer-un-agent-ia:choisir-agent-ou-automatisation`.
- Faire tourner un agent hors de son poste : `creer-un-agent-ia:agents-cloud`.
- Le tableau de suivi : `creer-un-agent-ia:dashboards-hub-master`.

## Preuves restantes

- Un système neuf bâti de bout en bout avec ce gabarit : à mesurer au premier passage réel.
- Les cases « aucun » du registre signalent un tableau de suivi encore à construire.
