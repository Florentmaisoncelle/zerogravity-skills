---
name: video-declinaison-des-moments
description: >-
  Quand une vidéo ou un enregistrement est tourné et qu'on veut savoir quoi en tirer (« quels moments garder »,
  « décline cette vidéo en shorts et en posts », « inventorie les temps forts », « que faire de cet enregistrement »),
  ou qu'un montage est fait et qu'il faut vérifier ses coupes (« vérifie les raccords », « mes coupes tombent
  bien ? ») → inventorie les moments par type, les note, tranche (produire, réparer, reporter, rejeter), les dédoublonne
  et les route vers le bon format ; et contrôle chaque coupe par script puis par relecture. Triggers : « décliner la
  vidéo », « atomes », « moments forts », « audit des coupes », « raccords », « repurposing ».
metadata:
  scope: tirer d'une source vidéo ou audio déjà tournée un portefeuille de contenus justifiés, et contrôler les raccords d'un montage
  owns: l'inventaire des moments (sept types d'atomes), le verdict et le routage par format, le dédoublonnage, le contrôle des raccords (scripts/audit_edit_boundaries.py)
  consumes: /video-edit-auto (le montage et les sous-titres), /script-short (écrire un short retenu), /router-linkedin (le post issu d'un moment), /video-titre-et-miniature (l'emballage d'une pièce)
---

# /video-declinaison-des-moments : trouver ce que la vidéo contient, et vérifier ce qu'on en coupe

<!-- capitaliser:squelette-v1 -->
<!-- dev-qa-link -->
**Dev / Test / QA** : AUCUNE QA jumelle (compétence de méthode). La candidate est l'inventaire proposé par l'agent ; la
preuve est `scripts/audit_edit_boundaries.py` et ses tests pour les raccords ; le choix des pièces à produire reste au
créateur.

## Ce que la compétence résout

Une vidéo contient souvent plus de matière qu'on n'en exploite, et un montage pressé coupe au milieu d'une idée. Deux
usages, une seule source de vérité :

1. **Inventorier les moments** : quoi tirer de la source, sous quelle forme, dans quel ordre, sans fabriquer un quota.
2. **Vérifier les raccords** : chaque coupe commence et finit sur une pensée complète, puis le montage rendu se relit.

Résultat attendu : un tableau de moments avec verdict et raison, une première vague bornée, et des coupes contrôlées.

## Stratégie

1. Par défaut, **diagnostiquer et recommander**, ne pas produire d'office. Produire attend l'accord du créateur.
2. Le nombre de pièces est un résultat de l'inventaire, jamais un objectif.
3. Une source ancrée : un fichier ou une transcription fournis par le créateur, ses droits à lui. Jamais le
   téléchargement d'une vidéo tierce, jamais un substitut (miroir, autre épisode, autre compte).
4. Le moins lourd qui règle le défaut : polir avant resserrer, resserrer avant refaire.
5. Le décidable va au script (coupes), le jugement reste à la relecture.

> 🧱 **Une seule maison.** Le montage lui-même (nettoyage, coupes, sous-titres) appartient à la compétence de montage. Ici :
> le choix des moments et le contrôle des raccords.

## Étapes

### Usage A : inventorier les moments

1. **Poser le contrat** : source exacte, destination, pièces voulues, ce qui est livré ce tour-ci, condition d'arrêt.
2. **Obtenir une transcription** avec locuteurs et horodatage, corriger noms, produits et chiffres d'après la source.
   Pour un enregistrement à plusieurs pistes (caméra, écran, diaporama), les lister séparément
   ([`references/raccords-et-revue.md`](references/raccords-et-revue.md), § 3).
3. **Écrire la phrase pivot** : « [Spectateur] doit croire [verdict] parce que [preuve], puis utiliser [méthode] pour
   [résultat]. »
4. **Extraire les atomes** selon les sept types, avec le registre des affirmations (atteint, estimation, anecdote,
   prévision, objectif) et la ligne des droits ([`references/atomes-et-routage.md`](references/atomes-et-routage.md)).
5. **Noter, trancher** : Produire, Réparer, Reporter, Rejeter, chacun avec sa raison ; router vers un format.
6. **Dédoublonner** dans le lot et contre les sorties des 30 derniers jours (recouvrement de sens au-delà de 70 %).
7. **Rendre** : le tableau, la première vague bornée, les réparations et dépendances, ce qui attend l'accord du créateur.

### Usage B : vérifier les raccords

1. Résoudre chaque coupe sur la transcription exacte (mot ou phrase), jamais sur les repères d'un mémo.
2. Lancer `python scripts/audit_edit_boundaries.py --transcript … --clips …` : un clip dont le début ou la fin ne tombe
   pas sur une phrase est refusé.
3. Après rendu, regarder et écouter l'ensemble, noter chaque raccord (fin avant, début après, transition, verdict,
   réparation). Un décodage propre ne prouve pas un bon montage.
4. Garder les versions précédentes ; réparer, puis relire la séquence changée et l'ensemble.

## Frontières

- Nettoyer, couper, sous-titrer, mettre au format vertical : la compétence de montage. On lui passe la liste des moments
  retenus et leurs temps.
- Écrire le script d'un short retenu : la compétence de script. Trouver une idée de short qui n'existe pas encore :
  `/video-idee-de-short`.
- Transformer un moment en post : la compétence de post LinkedIn (le texte du créateur reste intact).
- Titre et miniature d'une pièce longue : `/video-titre-et-miniature`. Les trois premières secondes d'un short :
  `/video-tester-trois-ouvertures`.
- Schémas animés, graphiques de reprise : la compétence d'animation. Mise en ligne : la compétence de mise en ligne.
- Voix de synthèse, avatar, visage généré : exclus. Un moment manquant est une prise à tourner par le créateur.

## Décisions et rejets

- **Sept types d'atomes plutôt qu'un seul « bon moment »** (repris du tri de la source). Rejeté : la note « virale »
  pondérée (nouveauté, controverse, utilité) ; arbitraire.
- **Défaut = diagnostic.** Rejeté : produire d'office un lot de dérivés.
- **Pas de manifeste de livraison avec empreintes**, pas d'espace de travail partagé (il décrit un éditeur hébergé qui
  n'existe pas chez nous), pas de plan de mesure par défaut (« construire d'abord, mesurer plus tard »).
- **Granularité « mot » : regroupement en phrases par la ponctuation.** La version d'origine acceptait n'importe quel
  début de mot comme coupe propre, donc ne refusait rien. Réouverture : si les transcriptions arrivent sans ponctuation.
- **Seuil de 70 % de recouvrement** : repère de jugement, jamais mesuré par programme.

## Preuves restantes

- `python -I -m unittest discover -s tests` dans ce dossier : 7 tests, sans réseau, Python standard seulement.
- Témoins négatifs : une coupe au milieu d'une phrase, des temps dans le désordre, une granularité inconnue et un clip
  incomplet sont refusés sans trace d'erreur.
- NON MESURÉ : aucun inventaire réel n'a encore été mené avec cette méthode ; aucune vidéo réelle n'a passé le contrôle
  des raccords ; la relecture sémantique d'un montage reste un travail d'agent ou de personne, pas du script.

## Crédit

Retravaillé depuis video-content-engine (avec la liste des types d'atomes et le dédoublonnage de podcast-ops) d'AI
Marketing Skills (Single Grain, MIT), https://github.com/ericosiu/ai-marketing-skills ; ce qu'on a changé : texte
réécrit en français autour de deux usages ; manifeste de livraison, espace de travail partagé, plan de mesure et
préambule de suivi retirés ; scoring viral de podcast-ops et appels à des services tiers non repris ; script de contrôle
des coupes corrigé pour la granularité par mot, messages et rapport en français, lecture en UTF-8. Licence d'origine :
`LICENSE-single-grain.txt`.
