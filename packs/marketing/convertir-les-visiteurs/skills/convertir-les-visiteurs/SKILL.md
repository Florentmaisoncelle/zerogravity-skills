---
name: convertir-les-visiteurs
description: >-
  Quand on veut transformer les visiteurs d'un site existant en inscrits (« mon site ne convertit pas », « teste une
  autre version de ma page », « pose une fenêtre pour récolter des adresses », « une ressource gratuite pour récolter
  des contacts », « où en est ma conversion ? ») → affiche l'état calculé depuis le dossier `conversion/<page>/`, puis déroule
  quatre étapes dans l'ordre : diagnostic de la page, test d'une variante, capture de l'adresse, ressource gratuite.
  Chaque étape a une compétence publique et une méthode courte (ce qu'on mesure, ce qu'on décide, quand on s'arrête) ; les biais et la confidentialité se relisent par une personne. Se lance par
  `/convertir-les-visiteurs:convertir-les-visiteurs`. Déclencheurs : « taux de conversion », « CRO », « test A/B »,
  « popup », « lead magnet », « ressource gratuite », « outil gratuit ». Pas pour le référencement et la visibilité :
  `/referencer-son-site:referencer-son-site`. Pas pour les annuaires et les stores :
  `/lancer-un-produit:lancer-un-produit`. Pas pour construire le site : `/creer-un-site-web:creer-un-site-web`.
---

# Convertir les visiteurs : la page, le test, la capture, la ressource gratuite

## Ce que ça résout

Du trafic qui ne s'inscrit pas : une page qui freine, des changements faits à l'impression, une adresse jamais captée.
Ici : le diagnostic de la page, le test d'une variante, la capture d'adresse et une ressource gratuite, dans cet ordre.

**Résultat attendu** : la liste des freins de la page classés par impact, un test décidé sur une règle écrite avant, une
capture qui ne gêne pas, une ressource gratuite livrée tout de suite.

## Stratégie

1. **Une compétence par étape, la meilleure.** La table des étapes (plus bas) dit laquelle et pourquoi. Les règles de
   choix et les manques sont aussi dans `references/workflow.json`.
2. **L'état d'abord, toujours calculé** depuis les fichiers de `conversion/<page>/`, jamais recopié.
3. **L'ordre protège la décision** : une hypothèse à la fois, mesurée avant d'être généralisée ; une seule variable par
   test. Sauter une étape reste possible sur demande ; le journal dit laquelle et pourquoi.
4. **Une seule validation, à la fin de l'étape 1** : le diagnostic et l'hypothèse à tester. Ce n'est pas un cadrage
   fait avant de regarder la page : on valide ce que le diagnostic a trouvé. Ensuite tout se déroule. Restent à la
   personne : le contrôle du consentement avant de servir une variante, la relecture des biais et de la
   confidentialité.
5. **Tout texte qui sort au nom de l'entreprise** se relit avant d'être montré (ton naturel, aucun chiffre inventé), et
   rien ne part sans validation.
6. **Aucun gain n'est promis** : une décision se prend sur la règle écrite avant le test.
7. **Les décisions se notent** dans le journal à chaque étape, avec ce qu'on a appris : quelques lignes suffisent.

<!-- prerequis:debut -->
## Prérequis

Ce workflow s'appuie sur des compétences publiques, installées à part. Aucune n'est indispensable : si l'une manque, le workflow le dit et fait l'étape à la main. Faire l'étape à la main veut dire suivre sa règle de choix, écrire ce qu'elle doit rendre (dans le fichier de l'étape, ou dans la réponse quand le workflow n'a pas de dossier) et dire ce qui reste à la charge de la personne.

```text
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin marketplace add coreyhaines31/marketingskills
/plugin install design@knowledge-work-plugins
/plugin install marketing-skills@marketingskills
```

Les workflows cités ici sont dans le même dépôt (le dépôt s'ajoute une fois : `/plugin marketplace add Gremelinn0/zerogravity-skills`) :

```text
/plugin install creer-un-site-web@zerogravity
/plugin install envoyer-des-e-mails@zerogravity
/plugin install lancer-un-produit@zerogravity
/plugin install referencer-son-site@zerogravity
```
<!-- prerequis:fin -->

## Étapes

### 0. Le dossier, puis l'état (lecture seule)

**Le dossier.** Un sous-dossier par page travaillée : `conversion/<page>/`, à la racine du dossier de l'entreprise,
avec un nom court (`accueil`, `tarifs`, `inscription`). Une page, un test à la fois. Un deuxième test sur la même page,
une fois le premier terminé, ouvre un nouveau sous-dossier (`accueil_2`). Dossier absent ou vide : il n'y a encore
rien de fait, l'état est « étape 1 » et le dossier se crée au premier passage. Si le dossier courant n'est pas celui
de l'entreprise, le dire en une ligne et demander où il vit : rien ne s'écrit avant. Les adresses des inscrits ne
sont jamais dans le dossier : elles restent dans l'outil d'envoi.

**L'état**, calculé depuis le journal et les fichiers :

```text
Page               accueil
Étapes             01 ✓  02 ✓  03 -  04 -
Dernière décision  2026-11-06 · 02 · fait · variante B gardée
Étape suivante     03 Capter l'adresse du visiteur
```

- Le journal `conversion/<page>/journal.md` a une ligne par décision :
  `AAAA-MM-JJ · NN · fait | en attente | sans objet | sautée | corrigée · <une phrase>`.
- Pour chaque étape, la dernière ligne du journal qui la nomme fait foi. `✓` : cette ligne dit `fait` ou `corrigée`
  et le fichier de l'étape existe. `s.o.` : elle dit `sans objet` ou `sautée` (l'étape n'est plus proposée). `-` :
  aucune ligne, ou le fichier manque.
- `corrigée` : l'étape est refaite après une correction ; elle reste ✓ et la ligne dit ce qui a changé. `sautée` :
  la personne a choisi de passer ; la ligne dit pourquoi.
- `en attente` : l'étape est préparée, mais elle dépend d'un geste ou d'une réponse qui arrive hors de la conversation. La ligne du journal dit ce qu'on attend et de qui. L'état l'affiche `att.` avec ce texte : l'étape n'est pas `✓`, parce que préparé n'est pas fait. Le workflow s'arrête là et le dit ; il n'invente jamais la suite (ni réponse, ni résultat, ni geste qu'on ne lui a pas confirmé). Quand la personne apporte ce qui est arrivé, la ligne `fait` suit. Ici : les visiteurs, qui doivent venir assez nombreux pour conclure un test (étape 2), la mise en ligne d'une variante ou d'une fenêtre par la personne (étapes 2 à 4) et la décision à trente jours (étape 4).
- L'étape suivante est la première étape `-` ou `att.`, dans l'ordre (devant une étape `att.`, on demande d'abord où en est l'attente). Si aucune ne l'est, la page est terminée, et on peut ouvrir
  une nouvelle page.
- Page par défaut : la plus récente qui n'est pas terminée, ou celle que la personne nomme.

**Une question n'est pas un ordre.** « Où en est ma conversion ? » : on donne l'état et la prochaine action, puis on
s'arrête. La commande du workflow, « continue » ou « déroule » : on enchaîne jusqu'à la première étape en attente, puis on s'arrête et on le dit.

**Une demande au milieu du chemin** (« fais-moi une ressource gratuite ») : l'étape 4 marche seule ; l'inscription aux
e-mails reste un choix à part.

### 1. Lancer l'étape suivante

Lire l'étape dans `references/workflow.json`, appliquer sa règle de choix, invoquer la compétence retenue, écrire sa
sortie dans le fichier de l'étape, inscrire `fait` au journal (ou `en attente`, voir plus haut), puis passer à la suivante sans redemander.

<!-- etapes:debut -->
| # | Étape | Compétences | Règle de choix |
|---|---|---|---|
| 1 | Diagnostiquer la page qui convertit mal | Diagnostiquer la page : `marketing-skills:cro` ; `marketing-skills:marketing-psychology` | Une hypothèse à la fois, mesurée avant d'être généralisée. Le consentement se contrôle avant de servir une variante ; les biais et la confidentialité se relisent par une personne. Une page à la fois, regardée d'abord sur téléphone. On note le taux de départ (visiteurs, actions, taux sur les quatre dernières semaines) avant de changer quoi que ce soit. Les freins se classent par impact et par effort ; une seule hypothèse sort du classement. |
| 2 | Tester une variante | Tester une variante : `marketing-skills:ab-testing` · Mesurer un test avec peu de volume : `convertir-les-visiteurs:marketing-mesurer-un-test` | Une seule variable par test ; on décide sur la règle écrite avant, pas sur l'impression. La taille d'échantillon et la règle de décision s'écrivent avant le lancement ; on ne s'arrête pas avant de l'avoir atteinte, et on ne l'allonge pas pour un résultat qui déplaît. Trop peu de visiteurs pour tester : changer la page puis comparer quatre semaines avant et après, en le disant. Résultat peu net : on garde la version actuelle. |
| 3 | Capter l'adresse du visiteur | Poser une fenêtre de capture : `marketing-skills:popups` · Simplifier l'inscription : `marketing-skills:signup` · Identifier les entreprises qui visitent le site : à la main | Une seule action par écran ; la fenêtre ne bloque jamais la lecture sur téléphone et n'apparaît pas dès l'arrivée. Case de consentement non pré-cochée. Mesure : adresses captées par visiteur exposé, et effet sur l'action principale de la page. Si l'action principale baisse, on retire la fenêtre. |
| 4 | Offrir une ressource contre une adresse | Créer une ressource contre une adresse : `marketing-skills:lead-magnets` · Construire un outil gratuit : `marketing-skills:free-tools` | La ressource se débloque tout de suite ; l'inscription aux emails est un choix à part. lead-magnets par défaut, free-tools pour un outil. Décision à trente jours, fixée avant la mise en ligne : on garde la ressource si elle capte plus d'adresses que le formulaire d'avant, sinon on change la promesse avant le format. |
<!-- etapes:fin -->

### 2. La méthode, étape par étape

#### Étape 1 : diagnostiquer la page

1. **Choisir une page** : celle qui reçoit le plus de visiteurs et en perd le plus avant l'action voulue (inscription, demande de devis, achat).
2. **Écrire le point de départ** dans `01-diagnostic.md` : l'action voulue, le nombre de visiteurs et d'actions sur les quatre dernières semaines, le taux obtenu (actions divisées par visiteurs). Sans ce chiffre, aucun test ne se juge. Pas d'outil de mesure sur le site : le poser d'abord, et le dire.
3. **Regarder la page comme un visiteur, d'abord sur téléphone** : que promet le titre, que fait-on ensuite, qu'est-ce qui rassure, qu'est-ce qui freine (trop de champs, bouton caché, texte vague). Les compétences `marketing-skills:cro` et `marketing-skills:marketing-psychology` listent les freins à chercher.
4. **Classer les freins** par impact attendu et par effort, dix au plus. Garder le meilleur rapport impact sur effort.
5. **Formuler l'hypothèse** : « Parce que [ce qu'on a vu], si on change [une chose], alors [l'action] augmentera, ce qu'on verra à [la mesure]. »

*Ce qu'on décide* : l'hypothèse retenue ; c'est la validation de la personne. *Critère d'arrêt* : le diagnostic s'arrête à une page et dix freins ; vouloir tout corriger d'un coup est le piège.

#### Étape 2 : tester une variante

1. **Calculer ce que la page peut tester.** La compétence `marketing-skills:ab-testing` donne des tailles d'échantillon : à 3 % de conversion, repérer une hausse relative de 20 % demande de l'ordre de 14 000 visiteurs par version. Un site qui en reçoit beaucoup moins ne peut pas tester de petites différences.
2. **Si le trafic suffit** : une seule variable change entre A et B (le titre, ou le bouton, pas les deux). Écrire avant le lancement : la mesure principale, la taille d'échantillon, la durée (des semaines entières, au moins deux, pour couvrir tous les jours), la règle (« on garde B si son taux dépasse celui de A avec la confiance prévue »).
3. **Si le trafic est trop faible** : faire un seul gros changement, puis comparer les quatre semaines d'avant et d'après. C'est moins fiable (une saison ou une promotion peut tout expliquer) : le journal le dit.
4. **Pendant le test** : ne rien modifier, et ne pas s'arrêter dès que B semble gagner (le piège du coup d'œil, que la compétence décrit).
5. **À la fin** : écrire le résultat, la décision et ce qu'on en retient dans `02-tester.md`.

*Ce qu'on décide* : garder B, garder A, ou refaire un test plus audacieux. *Critère d'arrêt* : l'échantillon prévu est atteint, ou la durée maximale (six semaines) est écoulée. Résultat peu net : on garde la version actuelle, la plus simple, et on passe à l'hypothèse suivante.

#### Étape 3 : capter l'adresse

1. **Un seul endroit, une seule offre** : une fenêtre, une bannière ou un formulaire en bas d'article, pas les trois. La compétence `marketing-skills:popups` décrit les déclencheurs (temps, défilement, intention de sortie) ; choisir celui qui laisse lire d'abord.
2. **Sur téléphone**, pas de fenêtre plein écran à l'arrivée, et une croix de fermeture facile à toucher.
3. **Le formulaire demande l'adresse, rien de plus** (`marketing-skills:signup` passe champ par champ). Le consentement : case non pré-cochée, avec ce qu'on enverra et comment se désinscrire (voir `/envoyer-des-e-mails:envoyer-des-e-mails`).
4. **Mesurer** deux choses dans `03-capter.md` : les adresses captées par visiteur qui a vu la fenêtre, et l'action principale de la page, avant et après.

*Ce qu'on décide* : garder, déplacer ou retirer la fenêtre. *Critère d'arrêt* : si l'action principale de la page baisse alors que les adresses augmentent, on retire la fenêtre ; une adresse captée n'est pas un client.

#### Étape 4 : offrir une ressource contre une adresse

1. **Un problème précis**, résolu en moins de cinq minutes de lecture ou d'usage (modèle, liste de contrôle, calculateur). `marketing-skills:lead-magnets` aide à choisir le type selon le moment où en est le visiteur ; `marketing-skills:free-tools` quand c'est un outil.
2. **La page de présentation** : la promesse en une phrase, ce que contient la ressource, le formulaire. La ressource est livrée tout de suite, sur la page de remerciement et par e-mail.
3. **L'inscription aux e-mails est un choix à part** : une case non pré-cochée, distincte du téléchargement.
4. **Fixer la décision avant la mise en ligne**, dans `04-ressource-gratuite.md` : à trente jours, on garde la ressource si elle capte plus d'adresses que le formulaire d'avant.

*Ce qu'on décide* : garder, changer la promesse ou arrêter. *Critère d'arrêt* : à trente jours, la décision écrite s'applique, sans attendre « un peu plus de données » ; si la ressource ne capte pas, on change la promesse avant de changer le format.

### 3. Clore un passage

À la fin de chaque séance, on écrit l'état (fait, reste, prochaine action) au journal. Si une compétence a déçu à une
étape, on le note aussi, pour rouvrir le choix de la compétence de cette étape.

## Ce qui reste à la personne

Aucun trou de compétence pour l'instant. Deux gestes restent humains : relire les biais et la confidentialité, et
contrôler le consentement avant de servir une variante.

## Frontières

| Demande | Va à |
|---|---|
| Le référencement, la visibilité dans Google et les IA | `/referencer-son-site:referencer-son-site` |
| Les annuaires, les stores | `/lancer-un-produit:lancer-un-produit` |
| Construire ou refaire le site | `/creer-un-site-web:creer-un-site-web` |
| Les e-mails qui suivent l'inscription | `/envoyer-des-e-mails:envoyer-des-e-mails` |
