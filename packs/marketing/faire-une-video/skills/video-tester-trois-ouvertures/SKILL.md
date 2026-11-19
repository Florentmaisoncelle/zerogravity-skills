---
name: video-tester-trois-ouvertures
description: >-
  Quand un short a un bon extrait mais que son ouverture n'est pas tranchée (« l'ouverture de mon short est molle »,
  « teste trois accroches », « quelle entrée pour cette vidéo courte », « mon short est prêt à relire avant sortie »)
  → écrit trois cartes d'ouverture (problème, preuve, mécanisme) pour un même extrait en ne changeant qu'une chose à la
  fois, fait fabriquer des aperçus de quatre secondes, aide le créateur à choisir l'entrée la plus claire, puis passe la
  liste des défauts à corriger avant la sortie. Triggers : « ouverture du short », « hook test », « trois ouvertures »,
  « relecture avant de sortir le short ».
metadata:
  scope: l'ouverture et la relecture éditoriale d'un short vertical déjà écrit, avant sa mise en ligne
  owns: le laboratoire de trois cartes d'ouverture, les trois formats de short, la liste de défauts avant sortie, la règle du compteur animé
  consumes: /video-edit-auto (fabriquer les aperçus et le montage), /router-motion-design (un schéma d'ouverture), /script-short (la phrase d'ouverture), /youtube-publish (la mise en ligne)
---

# /video-tester-trois-ouvertures : choisir l'entrée d'un short avant de monter tout le reste

<!-- capitaliser:squelette-v1 -->
<!-- dev-qa-link -->
**Dev / Test / QA** : AUCUNE QA jumelle (compétence de méthode, aucun script). La candidate est la proposition de trois
cartes ; la preuve est le visionnage des aperçus à 360 px avec et sans le son ; le choix de l'entrée revient au créateur.

## Ce que la compétence résout

Les premières secondes décident si un short est regardé, et on les règle souvent au hasard après avoir tout monté.
Résultat attendu : trois ouvertures comparables d'un même extrait, une qui est choisie sur des critères écrits, et un
short relu sur une liste de défauts connus avant sa sortie. Une ouverture est une hypothèse, jamais un gain prouvé.

## Stratégie

1. Une seule chose change entre les cartes : la promesse d'entrée. Corps, appel à l'action, palette et sous-titres restent fixes.
2. Trois cartes d'abord, rendu coûteux ensuite : on ne monte que l'ouverture gagnante.
3. Une seule ouverture est publiée par défaut ; trois quasi-doublons ne se publient pas.
4. Aucune affirmation parlée nouvelle : les mots viennent de l'enregistrement, sinon le créateur tourne une reprise.
5. Une relecture est un visionnage réel, pas un score inventé.
6. Un agent prépare, le créateur choisit et valide.

> 🧱 **Une seule maison.** Le montage lui-même est celui de la compétence de montage. Ici : quoi essayer à l'ouverture et quoi
> corriger avant sortie.

## Étapes

1. **Choisir l'extrait** : un argument complet, une preuve utilisable, un vrai résultat, pas déjà publié.
2. **Choisir le format** parmi preuve, flux de travail, récit d'opérateur, d'après la matière réelle disponible
   ([`references/cartes-et-formats.md`](references/cartes-et-formats.md)).
3. **Écrire les trois cartes** (problème, preuve, mécanisme) : phrase exacte avec temps source, promesse à l'écran,
   image de départ, tenue sur 0 à 4 secondes, passage au corps, hypothèse.
4. **Faire fabriquer les aperçus** de quatre secondes si les médias existent ; les regarder à 360 px avec le son, puis
   sans le son.
5. **Choisir** l'entrée la plus claire, la plus curieuse et la plus honnête. Dire pourquoi, en une phrase.
6. **Monter le short complet** avec l'entrée choisie (la compétence de montage), puis passer la liste de défauts avant sortie.
7. **Rendre** : les trois cartes, l'entrée choisie et son pourquoi, les défauts trouvés, ce qui reste à faire.

## Frontières

- Le montage, les sous-titres, le format vertical : la compétence de montage.
- Un schéma ou un plan animé pour l'ouverture : la compétence d'animation.
- Le script parlé et ses phrases : la compétence de script. Trouver l'idée avant : `/video-idee-de-short`.
- Vérifier des coupes sur transcription : `/video-declinaison-des-moments`. La miniature d'une vidéo longue :
  `/video-titre-et-miniature`.
- Mettre en ligne ou programmer : la compétence de mise en ligne (avec l'accord du créateur). Aucun service de planification
  externe n'est repris ici.
- Ni voix de synthèse, ni avatar, ni visage généré : une reprise est tournée par le créateur.

## Décisions et rejets

- **Trois cartes, une seule variable.** Rejeté : changer ouverture, preuve et explication ensemble en appelant cela un test.
- **Prévisualiser trois, publier une.** Rejeté : publier des quasi-doublons ; des publications organiques ne font pas un test contrôlé.
- **Pas de grille chiffrée de relecture** : celle de la source renvoyait à une évaluation non fournie ; la liste de défauts
  connus la remplace, sans note inventée pour faire passer un candidat.
- **Pas de style graphique imposé** (palette et typographie propres à l'auteur de la source), pas d'outil de
  planification payant d'un tiers, pas de suivi automatique à 24 h ou 72 h.
- **Aucun script** : tout ici est un jugement ou un visionnage, pas un calcul.

## Preuves restantes

- Gate : relecture de la liste de défauts sur un short réel, avec écoute continue.
- Témoin négatif attendu : un chiffre pris au milieu d'un compteur animé est refusé comme preuve.
- NON MESURÉ : aucune ouverture réelle n'a encore été testée avec cette méthode ; l'effet d'une entrée sur la
  rétention n'est ni mesuré ni promis ; les aperçus de quatre secondes dépendent de la compétence de montage, non testé de
  bout en bout pour cet usage.

## Crédit

Retravaillé depuis shortform-production d'AI Marketing Skills (Single Grain, MIT),
https://github.com/ericosiu/ai-marketing-skills ; ce qu'on a changé : seule la partie sur l'ouverture, les formats et
la relecture est gardée, réécrite en français ; service de planification d'un tiers, style graphique de l'auteur,
grille chiffrée non fournie, suivi automatique et préambule de suivi retirés ; exemple remplacé par un cas fictif.
Licence d'origine : `LICENSE-single-grain.txt`.
