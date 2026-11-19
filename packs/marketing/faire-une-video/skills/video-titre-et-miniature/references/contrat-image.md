# Contrat d'image : fabrication, contrôle, retouche

`<racine>` désigne le dossier de la compétence installée ; ne jamais supposer que le dossier courant est le sien.

## Où l'image se fabrique

L'image se génère dans ChatGPT, piloté par Chrome (jamais un générateur d'image intégré à l'agent). Aucun visage, aucune ressemblance générés : si la miniature montre le créateur, la photo vient de lui et se fournit en entrée comme image de référence ; l'agent ne la produit pas. Un agent prépare, le créateur valide : rien ne change sur YouTube sans son accord.

## Rangement

```text
<dossier-de-sortie>/<slug-video>/
  manifeste.md
  variante-01/variante-01-v001.png
  variante-02/variante-02-v001.png
  variante-03/variante-03-v001.png
```

Les révisions s'appellent `v002`, `v003`, avec un suffixe parlant (`-logo-seul`). Ne jamais écraser une version acceptée ou déjà montrée. Une génération par variante, enregistrée tout de suite sous son chemin versionné.

## Gabarit de demande à ChatGPT

```text
Type : miniature YouTube finie, 16:9, composée pour 1280x720
Demande principale : <la promesse du paquet>
Images fournies : étiqueter chacune par son rôle (sujet, style de la chaîne, marque vérifiée)
Décor : <décor cohérent avec la chaîne>
Sujet : <un sujet central et une relation dominante>
Budget : trois groupes visuels majeurs au plus plus un bloc de texte court
Inventaire : <groupe 1> ; <groupe 2> ; <groupe 3> ; <bloc de texte>
Style : miniature YouTube soignée, lisible sur téléphone
Cadrage : <placement, échelle, vide, coin du chronomètre libre>
Palette : <palette de la chaîne>
Texte (mot pour mot) : "<texte exact>"
Marges : chaque marque critique entière à 64 px au moins des bords gauche et droit et à 36 px au moins du haut et du bas à 1280x720 ; le coin bas droit de 154x72 reste libre
Contraintes : le texte une seule fois ; marques officielles entières ; aucun texte en plus ; aucun filigrane ; retirer ou regrouper plutôt que rétrécir
À éviter : interface minuscule, accessoires redondants, logos sans rapport, affirmations non soutenues
```

Si la miniature est sans texte : « Aucun texte, lettre, chiffre, ponctuation ni étiquette nulle part. »

## Contrôle de simplicité

À 320x180, repérer la relation centrale en une seconde. Échec au-delà de trois groupes, sans hiérarchie nette, ou avec une interface minuscule ou plusieurs accessoires secondaires. Noter l'inventaire des composants dans le manifeste. Si l'inventaire ne tient pas en trois groupes plus un texte, on ne note ni ne fabrique la proposition. Une marque complexe qui se lit comme une seule silhouette compte pour un groupe.

## Contrôle de géométrie (script)

À 1280x720 : chaque marque critique entière à 64 px au moins des bords latéraux, 36 px au moins du haut et du bas, et rien d'important dans le coin bas droit de 154x72 (chronomètre YouTube). Mesurer la marque entière, traînées, particules et halo compris.

Noter chaque boîte `nom:x1,y1,x2,y2` dans le manifeste, puis :

```bash
python <racine>/scripts/thumbnail_guard.py final \
  --image <miniature.png> \
  --safe-box 'marque-a:x1,y1,x2,y2' \
  --safe-box 'marque-b:x1,y1,x2,y2'
```

Un échec bloque la promotion : déplacer ou redimensionner, puis recontrôler. Jamais d'exception parce que la marque « se voit à peu près ».

## Marques visibles

Avant de fabriquer, retrouver la marque exacte à sa source officielle (page de lancement, page du modèle, kit de marque ou ressource du créateur) : orthographe, adresse du fichier, et ce que la marque identifie (société, application, famille, modèle précis). Une marque de société n'est pas celle d'un modèle ; une image de campagne n'est pas un logo. Passer le fichier vérifié comme image d'entrée étiquetée, interdire dans la demande les substitutions connues, les robots génériques et les mots ajoutés. À taille d'origine, comparer le rendu au fichier : géométrie, mot, proportions, silhouette entière. Garder les fichiers de marque avec la vidéo, jamais dans la compétence. Une correction du créateur sur une marque est une contrainte absolue : recontrôler toutes les variantes concernées.

## Relation : l'écrire avant de fabriquer

Écrire la relation voulue en une phrase littérale, puis la coder par l'échelle et la position. Le héros se lit en premier à 320x180 ; un barré se pose sur l'objet rejeté sans toucher le héros ; une poursuite ou un remplacement montre une direction claire par la pose ou le déplacement ; retirer flèches, points d'interrogation et connecteurs quand la taille et la position suffisent. Test texte caché : échec si le visuel restant peut raconter l'inverse.

## Retouche ciblée

```text
Cas : retouche d'un seul objet
Images : 1 la miniature à retoucher ; 2 le fichier de remplacement de référence
Demande : remplacer uniquement <cible> par <remplacement> aux mêmes dimensions approximatives
Zone modifiable : <nom:x1,y1,x2,y2>
À conserver : visage, pose, cadrage, fond, lumière, typographie, texte exact et tout objet non concerné
Contraintes : ne changer que la zone ; aucun recadrage ; aucun texte en plus ; aucun filigrane
```

Toute retouche générée est provisoire. La regarder à taille d'origine, puis :

```bash
python <racine>/scripts/thumbnail_guard.py edit \
  --before <version-acceptee.png> \
  --after <version-provisoire.png> \
  --allowed-box 'zone:x1,y1,x2,y2'
```

Si le contrôle signale un changement hors zone, rejeter, réessayer une fois depuis la dernière version acceptée avec moins d'images de référence et une consigne de protection plus serrée. Si cela échoue encore, ne pas appeler cela une retouche ciblée : enregistrer sous un suffixe `-refait`, dire la dérive, garder la dernière version acceptée comme version courante.

## Révision à partir des retours

Avant de réviser, traduire les retours en tableau : paquet, variante visée, variante témoin à ne pas toucher, changements demandés, éléments fixes, texte exact, implications refusées. Garder les variantes approuvées ou non visées. Pour chaque paquet révisé, vérifier à taille de flux : le héros demandé se lit en premier, le visuel ne peut pas être lu à l'envers, tout chiffre du texte est soutenu par la vidéo. Quand la vidéo couvre plus d'éléments que le petit sous-ensemble montré, préférer un texte sans chiffre (« les outils qui valent le coup ») à un total non soutenu.

## Remise au créateur

Grouper par titre. Sous chaque titre, montrer A et B en image, avec leur texte de miniature et une ligne de retour : `A / B / aucune / combiner` plus `Changements`. Après une révision, remontrer l'ensemble courant, témoins inchangés compris. Chaque image se montre avec son chemin absolu ; le créateur n'a pas à ouvrir un dossier pour la voir. Noter dans le manifeste : chemin source, chemin courant, inventaire, boîtes critiques, boîtes modifiables, sortie du contrôle, provenance des marques.
