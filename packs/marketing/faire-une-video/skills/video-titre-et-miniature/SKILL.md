---
name: video-titre-et-miniature
description: >-
  Quand une vidéo YouTube est prête ou presque et qu'il faut son titre et sa miniature (« titre de ma vidéo »,
  « miniature YouTube », « trouve-moi trois titres », « mon titre et ma miniature se répètent », « révise cette
  miniature sans tout casser ») → fabrique trois paquets titre plus miniature à promesses différentes (verdict, preuve,
  utilité), les note sur une grille, contrôle la lisibilité et les marges de sécurité par script, recommande un paquet
  et le soumet au créateur. Triggers : « miniature », « thumbnail », « titre YouTube », « packaging de la vidéo »,
  « A/B de miniature », « retouche ciblée de la miniature ».
metadata:
  scope: le titre et la miniature d'une vidéo YouTube longue, de la matière du script jusqu'au paquet validé
  owns: les trois pistes de promesse, les portes de simplicité et de clarté, la grille de notes, le contrat titre et miniature, le contrôle des marges et des retouches (scripts/thumbnail_guard.py)
  consumes: /router-faire-une-video (le script validé), /youtube-publish (la mise en ligne), /video-qui-sortent-du-lot (les formules qui marchent chez les voisins)
---

# /video-titre-et-miniature : un titre et une miniature qui promettent la même chose, chacun à sa façon

<!-- capitaliser:squelette-v1 -->
<!-- dev-qa-link -->
**Dev / Test / QA** : AUCUNE QA jumelle (compétence de méthode, sans boucle de vérification continue). La candidate est
la proposition de trois paquets ; la preuve est `scripts/thumbnail_guard.py` (marges, retouche hors zone) et ses tests ;
le jugement (quel paquet, quelle promesse) reste au créateur.

## Ce que la compétence résout

Une vidéo bien faite se perd quand son titre et sa miniature disent deux fois la même chose, promettent plus que la vidéo
ne tient, ou ne se lisent pas sur un téléphone. Résultat attendu : trois paquets dont les promesses diffèrent vraiment,
chacun noté, un recommandé, des images contrôlées, et le créateur qui choisit. Rien n'est changé sur YouTube sans lui.

## Stratégie

1. Partir de la vidéo réelle (script validé, notes), jamais d'un titre rêvé : la promesse doit être tenue dans les
   30 premières secondes.
2. Trois questions de spectateur différentes (verdict, preuve, utilité), pas trois habillages.
3. Deux portes avant toute note : simplicité (trois groupes visuels au plus) et clarté (texte caché, la miniature ne
   raconte pas l'inverse).
4. Le titre porte les mots cherchés, la miniature l'émotion : jamais la même phrase deux fois.
5. Le décidable est confié au script (marges, zone du chronomètre, changement hors zone) ; le jugement reste visible.
6. La fiche de chaîne tient sur un écran, validée une fois par le créateur, au lieu d'un audit de vingt miniatures.

> 🧱 **Une seule maison.** Le texte du titre vient du script déjà validé (le workflow Faire une vidéo, la compétence de script) ;
> l'image se fabrique dans ChatGPT par Chrome ; la mise en ligne appartient à la compétence de mise en ligne. Ici : le paquet.

## Étapes

1. **Fiche de chaîne.** Si elle n'existe pas, l'écrire en un écran ([`references/fiche-chaine.md`](references/fiche-chaine.md))
   et la faire valider. Sinon la relire, sans réauditer la chaîne.
2. **Lire la matière.** Spectateur, thèse, verdict, preuve, tension, réserves ; compter ce qui est vraiment expliqué
   avant d'écrire un chiffre ; repérer l'objet qui prouve la promesse (détail dans
   [`references/grille-de-notes.md`](references/grille-de-notes.md), § 1).
3. **Écrire les paquets.** Autant que demandé, trois par défaut : un verdict, une preuve, une utilité. Pour chacun :
   titre exact, texte de miniature (zéro à quatre mots), composition, inventaire des composants, logique de l'accroche,
   risque.
4. **Passer les portes**, puis **noter** (grille pondérée, seuil 8,0 sans dimension sous 7) et recommander un paquet.
5. **Traduire la promesse en géométrie** : qui gagne, qui est écarté, quelle direction (grille, § 8). Test texte caché.
6. **Fabriquer les images** dans ChatGPT par Chrome, une demande par variante, versionnées
   ([`references/contrat-image.md`](references/contrat-image.md)). Vérifier les marques officielles à la source.
7. **Contrôler** : taille de flux à l'œil, puis `python scripts/thumbnail_guard.py final --image … --safe-box …`.
   Un échec bloque la promotion.
8. **Réviser** sans casser : tableau de retours, variantes approuvées gardées, retouche limitée à une zone déclarée
   et contrôlée par `thumbnail_guard.py edit`.
9. **Remettre au créateur** : chaque titre avec ses images A et B affichées, une ligne de retour (`A / B / aucune /
   combiner`). Il choisit ; la mise en ligne passe à la compétence de mise en ligne.

## Frontières

- Le script et le tournage : le workflow Faire une vidéo, la compétence de script. Ici, jamais de visage ni de voix générés ;
  le créateur se montre lui-même.
- Le montage des plans et les premières secondes : la compétence de montage, `/video-tester-trois-ouvertures`.
- Une animation ou un schéma animé pour la vidéo : la compétence d'animation.
- Mettre en ligne, régler la miniature sur YouTube : la compétence de mise en ligne (avec l'accord du créateur).
- Un visuel pour LinkedIn : la compétence de visuel LinkedIn. Des variantes de titre en langage de vente : `/marketing-skills:copywriting`.
- Les formules qui marchent chez les voisins : `/video-qui-sortent-du-lot`.

## Décisions et rejets

- **Fiche d'un écran à la place de l'audit de vingt miniatures.** Rejeté : l'audit complet, trop lourd avant d'avoir
  une seule miniature publiée. Réouverture : si le créateur veut comparer sa chaîne à d'autres.
- **Pas de registre de performance** (suivi à 24 h, 72 h, 7 jours). Rejeté pour le début : « construire d'abord,
  mesurer plus tard ». Si le créateur saisit à la main ses chiffres de YouTube Studio, ce sont des pistes, pas des règles.
- **Pas de paquet de passation pour une équipe d'éditeurs**, pas de génération d'image automatique intégrée à l'agent.
- **Pas de contrôle de fiche de chaîne par script** : la fiche est un jugement à faire valider, pas un fichier à
  conformer.
- **Aucun visage généré.** Seule une photo fournie par le créateur peut servir de référence.

## Preuves restantes

- `python -I -m unittest discover -s tests` dans ce dossier : 11 tests, sans réseau (Pillow requis).
- Témoin négatif : les tests refusent une marque trop près du bord, une marque dans le coin du chronomètre et un
  changement hors zone, y compris de transparence seule.
- NON MESURÉ : aucune miniature réelle n'a encore été fabriquée avec cette méthode ; les seuils de notes (8,0 et 7)
  viennent de la source et ne sont pas calibrés sur nos chaînes ; le rendu dans ChatGPT n'a pas été testé de bout en bout.

## Crédit

Retravaillé depuis packaging-youtube-thumbnails d'AI Marketing Skills (Single Grain, MIT),
https://github.com/ericosiu/ai-marketing-skills ; ce qu'on a changé : texte réécrit en français et resserré autour de
trois pistes, deux portes et une grille ; audit de chaîne remplacé par une fiche d'un écran ; registre de performance,
passation en archive et préambule de suivi retirés ; génération d'image confiée à ChatGPT par Chrome, sans visage
généré ; script de contrôle réduit aux commandes `final` et `edit`, messages en français. Licence d'origine :
`LICENSE-single-grain.txt`.
