---
name: publicite-payante
description: >-
  Quand on veut faire de la publicité payante de bout en bout (« fais-moi une pub », « écris et dessine mes annonces »,
  « une pub vidéo », « lance mes campagnes Meta et Google », « dois-je couper cette campagne ? », « où en est ma
  publicité ? ») → affiche l'état calculé depuis le dossier `publicite/`, un sous-dossier par campagne, puis déroule
  trois étapes dans l'ordre : la créa, la pub vidéo (si la campagne en a une), les campagnes. Chaque dépense et chaque
  paramètre se valident avant le lancement. Chaque étape a une compétence publique ; l'étape vidéo s'appuie sur deux
  d'entre elles et sur le workflow `/faire-une-video:faire-une-video` pour la fabrication. Se lance par
  `/publicite-payante:publicite-payante`. Déclencheurs : « publicité », « ads », « pub Meta », « pub Google »,
  « créa publicitaire », « pub vidéo », « campagne payante ». Pas pour le lancement d'un produit :
  `/lancer-un-produit:lancer-un-produit`. Pas pour une vidéo qui n'est pas une pub :
  `/faire-une-video:faire-une-video`. Pas pour les e-mails : `/envoyer-des-e-mails:envoyer-des-e-mails`.
---

# Faire de la publicité payante : la créa, la pub vidéo, les campagnes

## Ce que ça résout

Une publicité qui coûte sans qu'on sache pourquoi : des visuels et des textes écrits sans méthode, des campagnes
lancées sans validation de la dépense. Ici : les visuels et les textes de la pub, la pub vidéo si la campagne en a une,
puis les campagnes lancées et pilotées sur Meta et Google.

**Résultat attendu** : des visuels et des textes de pub, une pub vidéo prête à diffuser si la campagne en a une, et des
campagnes en ligne dont les réglages sont suivis.

## Stratégie

1. **Une compétence par étape, la meilleure quand elle existe.** La table des étapes (plus bas) dit laquelle. Les
   règles de choix et les manques sont aussi dans `references/workflow.json`, qui reste la seule source de cette table.
2. **L'état d'abord, toujours calculé** depuis les fichiers du dossier de la campagne, jamais recopié.
3. **L'ordre protège la dépense** : rien ne dépense avant que la créa soit validée et qu'une conversion test arrive.
   Sauter une étape reste possible sur demande ; le journal dit laquelle et pourquoi.
4. **Trois validations, car la dépense est le risque.** À l'étape 1, la personne valide chaque visuel et chaque
   promesse. À l'étape 2, elle valide le script de la pub vidéo avant toute fabrication. À l'étape 3, elle valide le
   budget et les paramètres de chaque campagne avant son lancement : c'est la plus importante, et elle n'est pas
   la première. Entre ces points, le workflow déroule seul.
5. **Tout texte qui sort au nom de l'entreprise** est relu et montré avant diffusion ; rien ne part sans validation.
6. **Les décisions se notent** dans le journal. Après chaque campagne, deux lignes suffisent pour la suivante : ce qui a
   marché, ce qu'on arrête.

<!-- prerequis:debut -->
## Prérequis

Ce workflow s'appuie sur des compétences publiques, installées à part. Aucune n'est indispensable : si l'une manque, le workflow le dit et fait l'étape à la main. Faire l'étape à la main veut dire suivre sa règle de choix, écrire ce qu'elle doit rendre (dans le fichier de l'étape, ou dans la réponse quand le workflow n'a pas de dossier) et dire ce qui reste à la charge de la personne.

```text
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin marketplace add coreyhaines31/marketingskills
/plugin install marketing-skills@marketingskills
/plugin install small-business@knowledge-work-plugins
```

Les workflows cités ici sont dans le même dépôt (le dépôt s'ajoute une fois : `/plugin marketplace add Florentmaisoncelle/zerogravity-skills`) :

```text
/plugin install envoyer-des-e-mails@zerogravity
/plugin install faire-une-video@zerogravity
/plugin install lancer-un-produit@zerogravity
/plugin install poser-sa-strategie-marketing@zerogravity
/plugin install trouver-ses-prochains-clients@zerogravity
```
<!-- prerequis:fin -->

## Étapes

### 0. Le dossier, puis l'état (lecture seule)

**Le dossier.** La publicité vit dans le dossier de l'entreprise : `publicite/` à sa racine, avec un sous-dossier par
campagne, `publicite/<campagne>/` (un nom court, par exemple lancement-automne). Chaque sous-dossier a son journal et
un fichier par étape. Dossier `publicite/` absent ou vide : il n'y a encore rien de fait, l'état est « étape 1 » et le
dossier de la campagne se crée au premier passage. Si le dossier courant n'est pas celui du projet, le dire en une ligne
et demander où il vit : rien ne s'écrit avant.

**La campagne par défaut** : la plus récente qui n'est pas terminée, ou celle que la personne nomme. Si toutes sont
terminées, ou si elle demande une nouvelle campagne, on crée le sous-dossier suivant et on repart à l'étape 1.

**L'état**, calculé depuis le journal et les fichiers de la campagne :

```text
Campagne           lancement-automne
Étapes             01 ✓  02 -  03 -
Dernière décision  2026-11-09 · 01 · fait · trois angles, douze titres validés
Étape suivante     02 Faire une pub vidéo → marketing-skills:ad-creative
```

- Le journal `publicite/<campagne>/journal.md` a une ligne par décision :
  `AAAA-MM-JJ · NN · fait | en attente | sans objet | sautée | corrigée · <une phrase>`.
- Pour chaque étape, la dernière ligne du journal qui la nomme fait foi. `✓` : cette ligne dit `fait` ou `corrigée` et le
  fichier de l'étape existe. `s.o.` : elle dit `sans objet` ou `sautée` (l'étape n'est plus proposée). `-` : aucune
  ligne, ou le fichier manque.
- `sans objet` ne s'applique qu'à l'étape optionnelle (la pub vidéo, quand la campagne n'en a pas). `corrigée` : l'étape
  est refaite après une correction ; elle reste ✓ et la ligne dit ce qui a changé. `sautée` : la personne a choisi de
  passer ; la ligne dit pourquoi.
- `en attente` : l'étape est préparée, mais elle dépend d'un geste ou d'une réponse qui arrive hors de la conversation. La ligne du journal dit ce qu'on attend et de qui. L'état l'affiche `att.` avec ce texte : l'étape n'est pas `✓`, parce que préparé n'est pas fait. Le workflow s'arrête là et le dit ; il n'invente jamais la suite (ni réponse, ni résultat, ni geste qu'on ne lui a pas confirmé). Quand la personne apporte ce qui est arrivé, la ligne `fait` suit. Ici : la validation de la créa (étape 1), le lancement de la campagne dans la régie par la personne et les résultats, qui n'arrivent qu'après des jours de diffusion (étape 3).
- L'étape suivante est la première étape `-` ou `att.`, dans l'ordre (devant une étape `att.`, on demande d'abord où en est l'attente). Si aucune ne l'est, la campagne est terminée, et on peut en
  ouvrir une nouvelle.

**Une question n'est pas un ordre.** « Où en est ma publicité ? » : on donne l'état et la prochaine action, puis on
s'arrête. La commande du workflow, « continue » ou « déroule » : on enchaîne jusqu'à la première étape en attente, puis on s'arrête et on le dit.

**Une demande au milieu du chemin** (« lance une campagne de pub LinkedIn ») : la créa de l'étape 1 passe d'abord ;
chaque dépense attend la validation.

### 1. Lancer l'étape suivante

Lire l'étape dans `references/workflow.json`, appliquer sa règle de choix, invoquer la compétence retenue, écrire sa
sortie dans le fichier de l'étape, inscrire `fait` au journal (ou `en attente`, voir plus haut), puis passer à la suivante sans redemander (sauf aux
validations). Une étape qui a un manque le dit, avec le geste humain qui le comble.

**Étape 2, la pub vidéo.** Deux compétences publiques la couvrent : `marketing-skills:ad-creative` pour le format, le
script et l'accroche, `marketing-skills:video` pour choisir comment fabriquer la vidéo (programmée, générée par IA,
avec un avatar, ou montée à partir de prises). Le workflow `/faire-une-video:faire-une-video` prend ensuite la suite
pour le tournage, le montage et les sous-titres. On écrit le script dans `02-pub-video.md`, on le fait valider, puis on
fabrique. Méthode courte pour le script d'une pub de 15 à 30 secondes :

| Temps | Contenu |
|---|---|
| 0 à 3 secondes | L'accroche : une question, un chiffre ou une situation précise qui arrête le défilement. Une accroche générique (« Stop, regarde ça ») ne compte pas. |
| 3 à 8 secondes | Le problème, tel que le client le dit lui-même. |
| 8 à 20 secondes | La solution montrée en action, pas décrite. |
| 20 à 30 secondes | Un seul appel à l'action : ce qu'on fait ensuite et ce qu'on obtient. |

Critères de réussite : l'idée se comprend sans le son (sous-titres toujours), le format correspond à l'emplacement
(vertical pour les stories et les formats courts, carré ou horizontal pour le fil), aucune promesse n'est inventée, et
les droits de la musique et des images sont réglés. Avec un avatar ou une voix de synthèse, relire les règles de la
plateforme publicitaire sur les contenus générés par IA (à vérifier avant le lancement).

**Étape 3, avant la première dépense.** On vérifie qu'une conversion test arrive pour de bon, avec la compétence de
suivi des conversions. Ensuite seulement, après la validation du budget et des paramètres, on lance et on pilote.

<!-- etapes:debut -->
| # | Étape | Compétences | Règle de choix |
|---|---|---|---|
| 1 | Faire la créa | Écrire et dessiner la pub : `marketing-skills:ad-creative` | Les variantes se font avec ad-creative, par angle (une raison différente de cliquer) et dans les limites de caractères de la plateforme ; chaque visuel et chaque promesse se valident avant le lancement. |
| 2 | Faire une pub vidéo | Choisir comment fabriquer la vidéo : `marketing-skills:video` | La pub vidéo part d'un script validé ; chaque dépense et chaque paramètre se valident avant le lancement. marketing-skills:ad-creative choisit le format et écrit le script et l'accroche ; marketing-skills:video choisit comment la fabriquer (code, génération, avatar, montage) ; le tournage, le montage et la publication se déroulent dans /faire-une-video:faire-une-video. |
| 3 | Lancer et piloter les campagnes | Vérifier le suivi des conversions : `marketing-skills:conversion-tracking` · Lancer et piloter les campagnes : `marketing-skills:ads` ; `small-business:ad-manager` | ads pour piloter, ad-creative pour les variantes ; ad-manager quand le dirigeant demande « dois-je couper cette campagne ? ». Avant la première dépense, conversion-tracking vérifie qu'une conversion test arrive bien. Chaque dépense et chaque paramètre se valident avant le lancement : rien ne dépense avant ce oui. |
<!-- etapes:fin -->

### 2. Clore un passage

À la fin de chaque séance, on écrit l'état (fait, reste, prochaine action) au journal. Si une compétence a déçu à une
étape, on le note aussi, pour rouvrir le choix de la compétence de cette étape.

## Ce qui manque

- **Rien de bloquant côté compétences.** Le tournage, le montage et la publication de la vidéo passent par
  `/faire-une-video:faire-une-video` ; la validation du budget et des paramètres reste un geste humain.

## Frontières

| Demande | Va à |
|---|---|
| Le lancement d'un produit | `/lancer-un-produit:lancer-un-produit` |
| Une vidéo qui n'est pas une pub | `/faire-une-video:faire-une-video` |
| Les e-mails et les SMS | `/envoyer-des-e-mails:envoyer-des-e-mails` |
| La stratégie et la mesure | `/poser-sa-strategie-marketing:poser-sa-strategie-marketing` |
| La prospection directe | `/trouver-ses-prochains-clients:trouver-ses-prochains-clients` |
