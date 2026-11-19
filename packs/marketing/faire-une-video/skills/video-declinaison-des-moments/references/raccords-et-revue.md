# Vérifier les raccords : script, relecture, preuve visible

## 1. Le contrôle par script (avant le rendu)

```bash
python scripts/audit_edit_boundaries.py \
  --transcript <transcription-exacte.json> \
  --clips <clips-retenus.json> \
  --output <audit-raccords.json>
```

Transcription :

```json
{"granularity": "sentence",
 "segments": [{"start": 0.35, "end": 2.45, "text": "Phrase complète."}]}
```

Clips retenus (les temps en secondes) :

```json
{"retained_clips": [{"id": "c1", "source_start": 0.0, "content_start": 0.35,
                     "content_end": 5.15, "source_end": 5.4}]}
```

- `content_start` et `content_end` : la pensée entière gardée. `source_start` et `source_end` : les marges d'air autour (souffle, respiration) conservées pour ne pas hacher le rythme.
- Tolérance : 0,12 s par défaut, réglable avec `--tolerance`.
- Granularité `word` : les mots sont regroupés en phrases à la ponctuation finale. Si la transcription ne porte pas de ponctuation, passer en `sentence`.
- Code de sortie : 0 si tout est bon, 1 si une coupe est mauvaise, 2 si un fichier ne se lit pas.
- Ce que le script ne dit pas : si des idées réordonnées forment un raisonnement cohérent. Cela reste une relecture humaine ou d'agent.

## 2. La relecture après le rendu

Un décodage propre, un son synchronisé et un volume correct prouvent que le fichier est lisible, pas que le montage est bon. Regarder et écouter la vidéo entière, avec le son. Pour chaque raccord, noter dans un tableau : la fin de ce qui précède, le début de ce qui suit, la transition, le verdict, la réparation. Contrôler aussi les changements de mise en page, les références à l'écran, les sous-titres, les réserves sur une affirmation et la dernière phrase (un montage qui s'arrête parce que la durée est atteinte n'a pas de fin).

Si une relecture complète n'est pas possible, la porte reste « en attente » et le fichier est appelé « brouillon technique ». Une version ratée se garde avec ses retours ; on répare, puis on relit la séquence modifiée et l'ensemble.

## 3. Avant de choisir les coupes : toutes les pistes

Lister séparément chaque piste d'origine : caméra, partage d'écran, diaporama, micro, son de l'ordinateur. Un montage "caméra" peut ne pas contenir l'écran que la personne commente. Caler les pistes sur des événements visibles et audibles et vérifier la dérive aux deux bouts. Ne pas supposer que les pistes démarrent ensemble.

Faire une carte de la preuve visible : phrase prononcée, temps source, écran ou objet requis, placement, recadrage lisible, traitement de confidentialité, élément manquant. Quand l'auteur dit « regardez ça », le spectateur voit la chose elle-même ; l'écran en image principale et le visage en incrustation quand la démonstration porte l'argument. Garder le curseur et le contexte d'interface utiles. Étiqueter toute reconstruction ; ne jamais inventer un résultat manquant. Une preuve d'écran absente ou une ouverture faible bloque la qualité éditoriale.

## 4. Concevoir l'ouverture avant le rendu

Écrire les trente premières secondes en temps : phrase exacte, repère source, preuve visible, promesse, passage vers le corps. Ouvrir sur un résultat concret, un problème, un enjeu, un désaccord ou une observation surprenante tirée de la source. Un conseil générique ou un titre décoratif n'est pas une accroche. Garder les réserves quand un résultat monte dans l'ouverture. Pour chaque short : ouverture exacte, contexte utile à un nouveau spectateur, résultat, dernière phrase.

Rôles de l'agent : il inventorie, propose, contrôle ; le créateur décide des coupes qu'il garde et tourne ce qui manque lui-même. Ni voix de synthèse ni avatar pour combler un trou.
