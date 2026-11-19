---
name: video-qui-sortent-du-lot
description: >-
  Quand il faut voir ce qui marche chez des chaînes YouTube voisines pour nourrir un titre, un sujet ou une analyse de
  concurrents (« quelles vidéos de mes concurrents explosent », « analyse YouTube de ces chaînes », « inspire-moi pour
  mes titres », « quelles formules de titres reviennent ») → interroge l'API officielle YouTube pour une liste de
  chaînes, repère les vidéos qui font plus de deux fois la moyenne de leur chaîne (longues et shorts séparés), donne la
  cadence de publication et les mots qui reviennent, puis en tire la promesse commune sans copier les titres. Triggers :
  « vidéos virales des concurrents », « outliers YouTube », « benchmark YouTube », « packaging des autres chaînes ».
metadata:
  scope: repérer, sur des chaînes YouTube choisies, les vidéos nettement au-dessus de leur moyenne et en tirer des enseignements de promesse
  owns: la lecture des vidéos hors du lot par l'API officielle (scripts/analyze.py), la règle du seuil et de l'échantillon minimal
  consumes: /marketing-skills:competitor-profiling (le profil global d'un concurrent), /video-titre-et-miniature (qui reçoit les enseignements)
---

# /video-qui-sortent-du-lot : ce que les chaînes voisines font mieux que leur moyenne

<!-- capitaliser:squelette-v1 -->
<!-- dev-qa-link -->
**Dev / Test / QA** : AUCUNE QA jumelle (compétence de méthode avec un script de lecture). La candidate est la liste
proposée par le script et lue par l'agent ; la preuve hors ligne est la suite `tests/test_analyze.py` (calcul du multiple,
seuil, échantillon minimal) ; la lecture des enseignements reste un jugement.

## Ce que la compétence résout

Choisir un titre ou un sujet à l'aveugle, sans savoir ce qui a réellement surpassé la normale chez des chaînes qui parlent
au même public. Résultat attendu : pour 5 à 10 chaînes voisines, la liste des vidéos qui dépassent nettement leur
moyenne, la cadence de chacune, et une note courte sur la promesse qu'elles ont en commun, qui nourrit
`/video-titre-et-miniature`.

## Stratégie

1. Données officielles seulement : l'API YouTube Data v3 avec une clé gratuite ; pas de collecte de pages, pas de
   téléchargement de vidéos.
2. Comparer une vidéo à **sa propre chaîne** (multiple de la moyenne), pas à des chaînes de taille différente.
3. Séparer longues et shorts, et ne désigner personne sous cinq vidéos dans un groupe : trop peu pour une moyenne.
4. On emprunte une structure de promesse, jamais un titre mot pour mot ni une miniature.
5. Après publication, confronter à ses propres chiffres, à la main, avant de dire qu'un titre « marche ».

## Étapes

1. **Choisir les chaînes** : 5 à 10 chaînes voisines (même public, même sujet), dont les identifiants `@…` viennent du
   créateur ou de `/marketing-skills:competitor-profiling`. Aucune liste prédéfinie.
2. **Préparer la clé** : créer une clé API YouTube Data v3 dans la console Google Cloud, la mettre dans la variable
   d'environnement `YOUTUBE_API_KEY`. Jamais dans un fichier du dépôt ni dans une commande.
3. **Lancer** : `python scripts/analyze.py --chaines @a,@b,@c --jours 30` (option `--sortie json` pour garder la donnée).
4. **Lire** : par chaîne, le nombre de longues et de shorts et la cadence ; par groupe, les vidéos hors du lot avec leur
   multiple de la moyenne et de la médiane ; les mots qui reviennent dans leurs titres (un indice, pas une formule).
5. **Interpréter** : regarder trois à cinq vidéos hors du lot et écrire en quelques lignes la promesse commune, le
   format, l'objet montré. Distinguer un sujet qui plaît d'un titre qui plaît.
6. **Passer** la note à `/video-titre-et-miniature` pour le prochain paquet.
7. **Après publication (à la main)** : relever les chiffres de YouTube Studio du créateur à une date convenue et les
   comparer à ce que la note prédisait. Sans ce relevé, le titre reste une hypothèse.

## Frontières

- Le profil global d'un concurrent (offre, positionnement, prix) : `/marketing-skills:competitor-profiling` et
  `/marketing-skills:competitors`. Ici : seulement les vidéos YouTube.
- Fabriquer le titre et la miniature : `/video-titre-et-miniature`. Écrire le script : la compétence de script,
  le workflow Faire une vidéo. Mettre en ligne et lire les chiffres propres à la chaîne : la compétence de mise en ligne.
- Montage et sous-titres : la compétence de montage. Animations : la compétence d'animation.
- Ne jamais télécharger une vidéo tierce ni en reproduire le contenu.

## Décisions et rejets

- **Aucune liste de créateurs prédéfinie** (celle de la source n'avait aucun lien avec nos cibles). Rejeté aussi : les
  « squelettes de titres éprouvés », liste maigre sans preuve ; les formules viennent des vidéos réellement relevées.
- **Résolution des chaînes par identifiant exact** (`forHandle`) plutôt que par recherche : moins de quota, pas de chaîne
  voisine prise pour une autre.
- **Seuil de deux fois la moyenne, échantillon minimal de cinq par groupe.** La moyenne inclut la vidéo testée ; la
  médiane est donnée à côté. Rejeté : un seuil absolu de vues, sans sens entre chaînes de tailles différentes.
- **La clé se lit dans l'environnement seulement.** Rejeté : la passer en argument, où elle reste dans l'historique.

## Preuves restantes

- `python -I -m unittest discover -s tests` dans ce dossier : 6 tests hors ligne (durée, multiple, seuil, échantillon
  minimal, ordre, mots qui reviennent).
- Témoin négatif : trois vidéos dont une très haute ne désignent personne (échantillon trop petit).
- NON EXÉCUTÉ contre l'API : aucune clé `YOUTUBE_API_KEY` n'est disponible ici, donc la résolution par `forHandle`, la
  pagination et les messages d'erreur réseau ne sont pas éprouvés en vrai. Les vidéos récentes ont moins de vues que les
  anciennes : les plus fraîches sous-estiment. Un short peut durer plus de 60 secondes (option `--seuil-short`).

## Crédit

Retravaillé depuis yt-competitive-analysis d'AI Marketing Skills (Single Grain, MIT),
https://github.com/ericosiu/ai-marketing-skills ; ce qu'on a changé : texte réécrit en français ; listes de créateurs
et squelettes de titres retirés ; script réécrit (clé lue dans l'environnement, résolution par identifiant exact,
échantillon minimal, médiane en plus de la moyenne, séparation des durées réglable, séparation fonctions pures et appels
réseau pour les tests, messages en français) ; boucle de retour gardée comme geste manuel. Licence d'origine :
`LICENSE-single-grain.txt`.
