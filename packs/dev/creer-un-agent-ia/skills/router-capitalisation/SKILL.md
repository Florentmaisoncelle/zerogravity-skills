---
name: router-capitalisation
description: >-
  Étape Capitaliser : quand quelque chose vient d'être tranché (un comportement, un prix, un nom, une méthode, une valeur par défaut, une interdiction), cette porte d'entrée dit ce qui devient faux ailleurs, corrige la ligne qui ment, puis aiguille chaque leçon vers son propriétaire : règle toujours chargée, compétence, référence, contrôle automatique, ou rien. À lancer à chaud, pas en fin de session. Déclencheurs : « on fait comme ça », « c'est tranché », « on renomme », « désormais », « ne fais plus jamais ça », « la doc dit encore », « capitalise », « grave ça », « mets à jour ce qu'il faut ».
---

# Capitaliser : fermer la porte derrière une décision

Après un travail, une décision ou une erreur, la leçon se perd si personne ne se demande où elle doit vivre. Pire : la documentation garde l'ancienne version, parfois en tête de fichier, et on lit la fausse information avant la vraie. Cette compétence est ce réflexe. Elle ne rédige rien elle-même : elle cherche ce qui ment, le corrige, puis envoie chaque leçon chez celui qui la possède.

## Ce qui la distingue des autres passes de rangement

Toutes finissent par rendre une vérité durable. Seul le moment change.

| Passe | Quand | Sur quoi | Poids |
|---|---|---|---|
| Optimisation du système (`entretenir-son-systeme:optimise-systeme`) | à froid, en grande passe | tout le système, mesuré et chiffré | lourde, volontairement |
| Clôture de session | une fois, à la fin | le travail de la session, avec ses preuves | lourde |
| Entretien d'une compétence (`entretenir-son-systeme:capitaliser`) | à la fin d'une tâche | une compétence : entrée, références, scripts, contrôles | ciblée |
| Cette porte d'entrée | à chaud, à la seconde où c'est tranché | toutes les surfaces, mais aucune n'est traitée ici | la plus légère |

On peut l'ouvrir dix fois dans un après-midi. Si elle devient lourde, elle ne part plus jamais : elle reste donc volontairement fine.

## Les 3 gestes, dans cet ordre

### 1. Nommer ce qui vient d'être tranché

Écrire la décision en une phrase, avec la valeur exacte : le libellé, le nombre, le nom de fichier, la commande. Une décision notée en approximatif sera à rechercher entièrement dans six mois. Si la phrase ne vient pas, il n'y a pas eu de décision : sortir de la compétence, ne rien mettre à jour.

### 2. Chercher ce qui devient faux, avant d'écrire quoi que ce soit

Le mauvais réflexe est « où j'écris ça ? ». Le bon est « qu'est-ce qui ment maintenant ? ».

- Chercher dans tout le dossier de projet les anciens termes (recherche de texte, `grep` ou équivalent), un terme à la fois puis ensemble.
- Regarder en premier les occurrences situées en tête de fichier : c'est la zone la plus lue, donc la plus dangereuse.
- Un résultat à zéro sur tous les termes veut presque toujours dire qu'on a cherché le mauvais mot. Tester avec un terme dont on sait qu'il existe avant de conclure que rien n'en parle.

Trois issues, toutes légitimes, aucune silencieuse :
- une ligne contredit : la corriger d'abord, ajouter ensuite ;
- une ligne dit déjà la même chose ailleurs : ne pas dupliquer, garder la source et pointer vers elle ;
- rien ne contredit : l'écrire dans le reçu (« rien ne contredisait »). C'est une information.

### 3. Aiguiller vers le propriétaire, jamais rédiger à sa place

Balayer les quatre lecteurs ci-dessous, puis ouvrir la table des surfaces. Toute surface écartée l'est explicitement, en un mot : un silence ne se distingue pas d'un oubli.

## Le balayage des 4 lecteurs

Une table de surfaces est toujours incomplète. Ces quatre questions partent de qui lit, pas de comment c'est rangé.

1. **L'utilisateur** voit-il une différence ? Un libellé, un prix, une promesse, un e-mail, une page du site, un parcours d'accueil, une mention légale.
2. **Toi (ou ton équipe)** doit-elle le savoir ou pouvoir le retrouver ? Outil de suivi des tâches, document partagé, page de projet.
3. **L'assistant dans trois semaines** : qu'est-ce qui le lui rappellera ? Une règle toujours chargée, une compétence, une carte, une mémoire. Si la réponse est « rien », l'information est déjà perdue : elle a juste l'air d'exister.
4. **La machine** encode-t-elle encore l'ancien monde ? Une valeur par défaut, une constante, un schéma, un test qui vérifie l'ancien comportement, un contrôle qui vérifie une règle morte.

## Table des surfaces et de leur propriétaire

Chaque propriétaire fait le travail. Cette porte d'entrée ne fait que l'appeler. Si le projet a déjà un propriétaire pour une surface, le sien gagne.

| Surface | Ce qui la rend fausse | Qui la traite |
|---|---|---|
| Règles de comportement (fichier d'instructions du projet, `CLAUDE.md`) | on décide comment l'assistant doit travailler | `entretenir-son-systeme:clean-rules-cleanup` : créer, corriger, supprimer, réorganiser |
| Compétence (entrée, références, scripts, contrôles) | un geste, un ordre, un nom ou un savoir durable changent | `entretenir-son-systeme:capitaliser` pour le maintien et la non-perte ; `entretenir-son-systeme:skill-quality-guard` avant de la dire prête |
| Doc produit d'une fonctionnalité | le comportement du produit change | le fichier de la fonctionnalité, mis à jour dans le même commit que le code |
| Côté utilisateur | ce que l'utilisateur voit, lit ou entend change | la personne ou la compétence qui tient les textes publics (site, e-mails, interface) |
| Doc système (cartes, onboarding, tableau de bord) | une règle, une compétence ou l'architecture bougent | passe de mise en cohérence sur les trois couches : règles, tableau de bord, documentation partagée |
| Suivi (tâches, priorités, décisions produit) | un statut ou une priorité changent | l'outil de suivi de l'équipe |
| Réglages, valeurs par défaut, constantes | une valeur par défaut change | le code et la doc de la fonctionnalité, dans le même commit |
| Légal (conditions, confidentialité, mentions) | on collecte, traite ou facture autrement | souvent sans propriétaire : le dire au lieu de faire semblant |
| Fiches par cible (plateforme, client, environnement) | une décision touche un produit présent sur plusieurs cibles | la compétence de portage du projet, qui déroule un vrai cycle par cible |
| Chantier partagé entre plusieurs sessions | le constat touche un mécanisme commun | le registre des chantiers du projet, puis un message à la session propriétaire avec le pointeur du document |
| Cartes et index | une des lignes ci-dessus a bougé | la compétence qui possède la carte |
| Comptes, accès, identifiants | un compte ou une adresse change | le coffre ou le document d'accès de l'équipe |

Pour une décision sur l'entreprise (offre, prix, cible, objectif, façon de travailler), la première étape est la mémoire de l'entreprise : une ligne datée, avec le lien de sa maison, dans la liste des dernières décisions lue par chaque session. Puis le routage ordinaire.

## La loi d'échelle : une décision vaut partout, sauf différence écrite

Un produit présent sur plusieurs cibles rend le balayage faux par défaut : on décide en pensant à une cible, on documente une cible, et les autres héritent d'une doc qui ne les décrit plus. La question est donc : quelles surfaces, fois combien de cibles ?

- Par défaut, la décision vaut partout. Une différence par cible n'existe que si elle est écrite dans la fiche de cette cible. Une différence non écrite est un oubli.
- Contrôle : si ce que tu écris nomme une cible précise, c'est soit une mesure datée (légitime), soit une règle mal écrite, à reporter sur le mécanisme plutôt que sur une liste de cibles.
- Une cible qu'on portera le mois prochain hérite-t-elle de ce fait ? Si non, ce n'est pas capitalisé, c'est archivé : un fait qui ne vit que dans des fiches de cibles existantes est invisible pour les cibles à venir.

## Les 5 règles anti-bordel : corriger avant d'ajouter

1. **Chercher avant d'écrire.** Aucune ligne nouvelle avant d'avoir cherché celle qui la contredit. Une passe qui n'a rien cherché n'a rien capitalisé, elle a grossi.
2. **La tête du fichier d'abord.** L'information lue en premier doit être la vraie. Une info périmée en haut est pire qu'absente : elle est crue et elle masque la bonne.
3. **Corriger, pas empiler.** Une décision qui en annule une autre réécrit l'ancienne ligne. Pas de « mis à jour le… » collé dessous, pas de deuxième section qui dit le contraire de la première.
4. **Pas de nouveau fichier** quand un fichier existant couvre le sujet. Trop gros ? Une annexe sous le même propriétaire, jamais un deuxième propriétaire.
5. **Une ligne fausse se réécrit, elle ne s'archive pas.** Archiver vaut pour des fichiers qu'on retire, pas pour laisser un mensonge dans un fichier vivant sous prétexte de ne rien perdre.

## Corriger ici, ne déléguer que si c'est impossible

Un constat juste, posé au bon endroit, ne vaut rien si personne ne le reprend. Le mode d'échec propre à cette porte : produire de la lucidité et zéro correction.

- Par défaut, corriger dans la foulée : même dépôt, fichiers accessibles, session pas saturée. Ouvrir une session ou une tâche pour cela fabrique de la gestion au lieu d'une correction.
- « Hors de portée » veut dire : impossible d'ici (autre dépôt, autre machine, besoin de parallélisme réel). Là seulement, envoyer le travail à une session dédiée, dans la même passe, pas « plus tard ».
- Le destinataire doit être réel : le titre exact d'une session vivante ou le chemin exact d'un dossier. Un nom inventé ne route vers personne et fait croire que le poste est pourvu. Avant d'écrire la ligne, vérifier que le nom se retrouve.
- Un défaut envoyé vers un dossier que personne ne lit n'est routé nulle part : l'écrire dans le fichier d'instructions de ce dossier et ouvrir la tâche qui ira le corriger.
- Seule décision qui reste en attente : un choix de produit qui appartient au responsable du projet. Elle se pose, se nomme dans le reçu, jamais enterrée dans un fichier.
- Écrire « à trancher par le propriétaire » sans ouvrir la porte vers lui, c'est classer sans suite.

## Le reçu : cinq lignes

```text
Tranché       : <la décision, une phrase, valeur exacte>
Devenait faux : <fichier:ligne> corrigé   (ou : rien ne contredisait)
Mis à jour    : <surface, propriétaire invoqué>
Écarté        : <surface, un mot de raison>
Reste         : <ce qui ne peut pas se faire ici, et pourquoi>
```

La ligne « Reste » est obligatoire quand elle n'est pas vide. Annoncer une mise à jour qui n'a pas eu lieu est exactement le mal que cette compétence combat : un résultat non prouvé se dit « posé, à confirmer ».

## Ce que cette compétence ne fait jamais

- Rédiger le contenu d'une surface. Si tu te retrouves à écrire une doc produit, une règle ou un parcours utilisateur, le geste 3 est raté : le propriétaire existe, appelle-le.
- Remplacer la clôture de session : elle tourne en plein milieu du travail, autant de fois que nécessaire.
- Se déclencher sur une simple conversation. Une hypothèse, une exploration, une question ne sont pas des décisions. Une compétence qui part à chaque phrase finit désactivée.
- Laisser un inventaire derrière soi : un ticket que personne ne reprendra.
- Ouvrir une session pour un travail que la session courante pouvait faire.
- Poser une question dont la réponse est déjà tranchée : décider où ça va, l'annoncer, laisser corriger en un mot.

## Quand ne pas l'invoquer

Rien n'a été tranché ; la décision ne survit pas à la session (un choix d'implémentation local, un nom de variable) ; on est déjà dans le propriétaire, invoqué pour cette raison précise. Dans ces cas, ne pas ouvrir la passe : l'inflation de passes vides tue les réflexes.

## Auto-amélioration

Quelqu'un dit « tu n'as pas mis à jour X » : ajouter la surface manquante à la table, dans la même passe. Une surface découverte sans propriétaire se déclare dans la table (comme le légal) plutôt que d'être routée au hasard.
