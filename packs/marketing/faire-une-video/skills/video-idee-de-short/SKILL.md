---
name: video-idee-de-short
description: >-
  Quand il faut trouver quoi filmer en vidéo courte (Reels, TikTok, Shorts, vidéo LinkedIn) et que le créateur n'a pas
  d'idée solide (« quoi tourner cette semaine », « idées de shorts », « trouve-moi des sujets de vidéo courte »,
  « interroge-moi pour trouver mes idées ») → interroge le créateur une question à la fois, mine son travail réel,
  classe les idées par niveau de preuve puis par deux notes, et rend un tableau : accroche de cinq secondes, trois puces
  à dire, réponse complète, vidéo de référence, suite. Triggers : « idée de short », « sujets de vidéos courtes »,
  « file d'attente de tournage », « accroche », « quoi filmer ».
metadata:
  scope: trouver et classer des idées de vidéos courtes tirées du travail réel d'un créateur, avant l'écriture du script
  owns: l'entretien d'idées, les huit pistes, l'échelle de preuve, les deux notes, la colonne vidéo de référence, le classement (scripts/score_ideas.py)
  consumes: /script-short (écrire le script de l'idée retenue), /video-declinaison-des-moments (quand l'idée sort d'une vidéo existante), /router-faire-une-video (le workflow complet)
---

# /video-idee-de-short : des idées de shorts qui s'appuient sur du vrai travail

<!-- capitaliser:squelette-v1 -->
<!-- dev-qa-link -->
**Dev / Test / QA** : AUCUNE QA jumelle (compétence de méthode). La candidate est le tableau proposé par l'agent ; la
preuve est `scripts/score_ideas.py` (validation et classement) et ses tests ; la décision de tourner reste au créateur.

## Ce que la compétence résout

Sans méthode, un short part d'une inspiration du moment : accroche floue, preuve absente, promesse non tenue au bout.
Résultat attendu : un tableau classé d'idées nouvelles, chacune avec une accroche lisible sans le son, trois puces à dire,
une preuve qu'on peut montrer, une vidéo de référence pour le format, et la suite proposée. Le créateur choisit ; il
tourne lui-même.

## Stratégie

1. Lire d'abord ce qui existe (notes, chiffres, contenus déjà sortis) ; n'interroger que sur ce qui manque.
2. Une question à la fois, dans l'ordre : résultat voulu, spectateur, preuves, travaux en cours, limites, suite,
   contraintes de tournage.
3. Miner le travail de la semaine plutôt que recycler d'anciennes vidéos.
4. La preuve classe avant le charme : une idée prête a un niveau de preuve 1 ou 2.
5. Succès d'abord : un échec crée la tension, la vidéo finit sur un mécanisme ou une décision.
6. Le classement mécanique (notes, niveaux) est un script ; le jugement des notes reste visible et discutable.

> 🧱 **Une seule maison.** Cette compétence s'arrête à l'idée choisie. Le script parlé : la compétence de script. Le tournage :
> le créateur, sans avatar ni voix de synthèse.

## Étapes

1. **Lire le contexte** fourni, puis **mener l'entretien** une question à la fois
   ([`references/entretien-et-pistes.md`](references/entretien-et-pistes.md)). Si l'essentiel manque : rendre « à
   compléter », la question suivante et la réponse recommandée.
2. **Générer des candidates** sur au moins cinq des huit pistes appuyées sur des preuves ; écarter celles sans spectateur
   précis, sans preuve crédible, sans résultat utile ou sans traitement filmable.
3. **Écrire l'accroche de cinq secondes** et les **trois puces** de chaque idée.
4. **Poser le niveau de preuve** (1 à 5) et le statut de l'affirmation
   ([`references/preuve-et-reference.md`](references/preuve-et-reference.md)).
5. **Choisir la vidéo de référence** (lien direct, ce qu'on emprunte) ou écrire « à trouver ».
6. **Noter** : potentiel et accroche des trois premières secondes, de 1 à 10.
7. **Classer** : enregistrer les idées en JSON puis `python scripts/score_ideas.py idees.json --sortie classees.json`
   (et `--valider-seulement` pour contrôler seul). Les prêtes passent d'abord.
8. **Rendre le tableau** exact du fichier de références, puis une ligne d'ordre de tournage. Le créateur retient celles
   qu'il tournera.

Contrôle final : chaque idée est nouvelle ou marquée « angle repris » ; chaque accroche a sa réponse complète ; trois
puces par ligne ; chaque chiffre a son pointeur de preuve ; chaque lien de source pointe la vraie base, pas une
recherche ; le tableau est trié par priorité de tournage.

## Frontières

- Écrire le script parlé de l'idée retenue : la compétence de script. Dérouler tout le workflow : le workflow Faire une vidéo.
- Idées qui sortent d'une vidéo déjà tournée : `/video-declinaison-des-moments`.
- Monter, sous-titrer, mettre en vertical : la compétence de montage. Animations et schémas : la compétence d'animation.
- Tester l'ouverture d'un short déjà écrit : `/video-tester-trois-ouvertures`. Mettre en ligne : la compétence de mise en ligne.
- Texte d'accroche pour LinkedIn : la compétence d'accroche LinkedIn. Jamais d'avatar, de voix de synthèse ni de visage généré.

## Décisions et rejets

- **Priorité = moyenne de deux notes, classement d'abord par statut de preuve.** Rejeté : la note interne de confiance
  dans la résolution de l'accroche, jamais affichée et redondante avec le niveau de preuve.
- **Colonne « vidéo de référence » reprise, la mécanique de commentaire contre ressource non reprise** : la suite est
  écrite en toutes lettres, sans mot-clé ni outil de livraison.
- **La piste « argent créé » reste fermée sans relevé chiffré.** Rejeté : l'estimer pour boucher le trou.
- **Un niveau de preuve 1 ou 2 exige une source** dans le fichier d'idées (règle ajoutée ici, absente de la version d'origine).
- **Table fixe, sans prévision de vues** : repris tel quel.

## Preuves restantes

- `python -I -m unittest discover -s tests` dans ce dossier : 8 tests, Python standard seulement, sans réseau.
- Témoins négatifs : deux puces au lieu de trois, note hors bornes, source absente pour un niveau 1, référence sans
  emprunt sont refusés ; une idée prête passe avant une idée fragile mieux notée.
- NON MESURÉ : aucune session d'entretien réelle n'a encore été menée ; les pondérations des deux notes viennent de la
  source et ne sont pas calibrées sur nos contenus ; rien ne prouve qu'un classement prédise les vues.

## Crédit

Retravaillé depuis shortform-idea-grill (avec l'échelle de preuve de show-and-tell-video-slate et la colonne vidéo de
référence de shortform-format-library) d'AI Marketing Skills (Single Grain, MIT),
https://github.com/ericosiu/ai-marketing-skills ; ce qu'on a changé : texte réécrit en français ; mécanique de mot-clé
d'appel à l'action et note interne de confiance retirées ; échelle de preuve intégrée au classement ; colonne
« suite » écrite en toutes lettres ; script réécrit avec champs, messages et règles en français, lecture en UTF-8.
Licence d'origine : `LICENSE-single-grain.txt`.
