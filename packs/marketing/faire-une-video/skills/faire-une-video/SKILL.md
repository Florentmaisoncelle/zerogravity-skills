---
name: faire-une-video
description: >-
  Quand on veut faire une vidéo de bout en bout (« je veux faire une vidéo », « écris le script de ma vidéo »,
  « génère des plans animés », « monte et sous-titre ma prise », « publie-la sur YouTube », « où en est ma vidéo ? »)
  → affiche l'état calculé depuis le dossier `video/`, un sous-dossier par vidéo, puis déroule cinq étapes dans l'ordre :
  choisir comment la fabriquer, écrire le script, tourner ou générer les plans, monter et sous-titrer, publier. Les deux
  grands choix (qui apparaît et qui parle, montage dans un logiciel ou par code) sont posés à la personne, options
  expliquées. Le script est validé avant toute production ; le tournage, les droits de la musique et des images et le
  dernier clic de publication restent à une personne. Le tournage et la publication sur YouTube n'ont pas de compétence
  publique : le workflow donne une méthode courte pour chacun. Se lance par `/faire-une-video:faire-une-video`.
  Déclencheurs : « faire une vidéo », « script vidéo », « avatar », « sous-titres », « montage », « YouTube ». Pas pour
  un post LinkedIn : `/publier-sur-linkedin:publier-sur-linkedin`. Pas pour une pub vidéo :
  `/publicite-payante:publicite-payante`. Pas pour le lancement d'un produit : `/lancer-un-produit:lancer-un-produit`.
---

# Faire une vidéo : choisir la méthode, écrire, tourner, monter, publier

## Ce que ça résout

Une vidéo coûte cher quand la méthode est choisie au hasard ou quand on produit avant d'avoir un script. Ici : les
choix posés avant de produire, le script validé, le tournage ou les plans animés, le montage et les sous-titres, puis
la publication.

**Résultat attendu** : une vidéo montée et sous-titrée, publiée avec son titre et sa description, à partir d'un script
validé.

## Stratégie

1. **Une compétence par étape, la meilleure quand elle existe.** La table des étapes (plus bas) dit laquelle. Les
   règles de choix et les manques sont aussi dans `references/workflow.json`, qui reste la seule source de cette table.
2. **L'état d'abord, toujours calculé** depuis les fichiers du dossier de la vidéo, jamais recopié.
3. **L'ordre protège la décision** : les choix de fabrication d'abord, puis un script validé avant tout tournage ou toute
   génération. Aucun choix n'est imposé : la personne décide, le workflow explique. Sauter une étape reste possible
   sur demande ; le journal dit laquelle et pourquoi.
4. **Deux validations, aux étapes 1 et 2.** À l'étape 1, la personne valide la méthode retenue avec son coût. À
   l'étape 2, elle valide le script. Ensuite le workflow déroule seul, jusqu'aux gestes qui restent à elle : le
   tournage si elle tourne, la vérification des droits de la musique et des images, et le dernier clic de publication.
5. **Les décisions se notent** dans le journal. Après chaque vidéo, deux lignes suffisent pour la suivante : ce qui a
   pris le plus de temps, ce qu'on referait autrement.

<!-- prerequis:debut -->
## Prérequis

Ce workflow s'appuie sur des compétences publiques, installées à part. Aucune n'est indispensable : si l'une manque, le workflow le dit et fait l'étape à la main. Faire l'étape à la main veut dire suivre sa règle de choix, écrire ce qu'elle doit rendre (dans le fichier de l'étape, ou dans la réponse quand le workflow n'a pas de dossier) et dire ce qui reste à la charge de la personne.

```text
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin marketplace add coreyhaines31/marketingskills
/plugin marketplace add heygen-com/hyperframes
/plugin install hyperframes@hyperframes
/plugin install marketing-skills@marketingskills
/plugin install small-business@knowledge-work-plugins
```

Les workflows cités ici sont dans le même dépôt (le dépôt s'ajoute une fois : `/plugin marketplace add Florentmaisoncelle/zerogravity-skills`) :

```text
/plugin install lancer-un-produit@zerogravity
/plugin install publicite-payante@zerogravity
/plugin install publier-sur-linkedin@zerogravity
```
<!-- prerequis:fin -->

Le montage par code et les plans animés passent par Hyperframes, qui demande Node.js 22 ou plus et FFmpeg d'après la
compétence `hyperframes:hyperframes-cli` (version 0.8.154, lue le 06/11/2026). Tourner soi-même et monter dans un
logiciel n'en ont pas besoin.

## Étapes

### 0. Le dossier, puis l'état (lecture seule)

**Le dossier.** Les vidéos vivent dans le dossier de l'entreprise : `video/` à sa racine, avec un sous-dossier par
vidéo, `video/<titre-court>/` (un nom court, par exemple presentation-offre). Chaque sous-dossier a son journal et un
fichier par étape. Dossier `video/` absent ou vide : il n'y a encore rien de fait, l'état est « étape 1 » et le dossier
de la vidéo se crée au premier passage. Si le dossier courant n'est pas celui du projet, le dire en une ligne et
demander où il vit : rien ne s'écrit avant.

**La vidéo par défaut** : la plus récente qui n'est pas terminée, ou celle que la personne nomme. Si toutes sont
terminées, ou si elle demande une nouvelle vidéo, on crée le sous-dossier suivant et on repart à l'étape 1.

**L'état**, calculé depuis le journal et les fichiers de la vidéo :

```text
Vidéo              presentation-offre
Étapes             01 ✓  02 ✓  03 -  04 -  05 -
Dernière décision  2026-11-09 · 02 · fait · script validé par la personne qui le dira
Étape suivante     03 Tourner ou générer les plans → liste de contrôle du tournage
```

- Le journal `video/<titre-court>/journal.md` a une ligne par décision :
  `AAAA-MM-JJ · NN · fait | en attente | sautée | corrigée · <une phrase>`.
- Pour chaque étape, la dernière ligne du journal qui la nomme fait foi. `✓` : cette ligne dit `fait` ou `corrigée` et le
  fichier de l'étape existe. `s.o.` : elle dit `sautée` (l'étape n'est plus proposée). `-` : aucune ligne, ou le
  fichier manque.
- Aucune étape n'est optionnelle ici, donc il n'y a pas de `sans objet` : une personne qui a déjà ses prises saute
  l'étape 3 avec `sautée` et dit pourquoi. `corrigée` : l'étape est refaite après une correction ; elle reste ✓ et la
  ligne dit ce qui a changé.
- `en attente` : l'étape est préparée, mais elle dépend d'un geste ou d'une réponse qui arrive hors de la conversation. La ligne du journal dit ce qu'on attend et de qui. L'état l'affiche `att.` avec ce texte : l'étape n'est pas `✓`, parce que préparé n'est pas fait. Le workflow s'arrête là et le dit ; il n'invente jamais la suite (ni réponse, ni résultat, ni geste qu'on ne lui a pas confirmé). Quand la personne apporte ce qui est arrivé, la ligne `fait` suit. Ici : la validation du script (étape 2), le tournage par la personne ou son accord pour un avatar ou une voix de synthèse (étape 3), et le dernier clic de publication (étape 5).
- L'étape suivante est la première étape `-` ou `att.`, dans l'ordre (devant une étape `att.`, on demande d'abord où en est l'attente). Si aucune ne l'est, la vidéo est terminée, et on peut en
  ouvrir une nouvelle.

**Une question n'est pas un ordre.** « Où en est ma vidéo ? » : on donne l'état et la prochaine action, puis on
s'arrête. La commande du workflow, « continue » ou « déroule » : on enchaîne jusqu'à la première étape en attente, puis on s'arrête et on le dit.

**Une demande au milieu du chemin** (« écris le script de ma vidéo ») : l'étape 2 marche seule ; le script se valide
avant toute production.

### 1. Lancer l'étape suivante

Lire l'étape dans `references/workflow.json`, appliquer sa règle de choix, invoquer la compétence retenue, écrire sa
sortie dans le fichier de l'étape, inscrire `fait` au journal (ou `en attente`, voir plus haut), puis passer à la suivante sans redemander (sauf aux
deux validations). Une étape qui a un manque le dit, avec le geste humain qui le comble ; une étape humaine attend ce
geste.

### 2. Les deux choix à poser (étape 1)

Aucune option n'est un défaut. On pose les deux questions, on explique les options, on note la réponse et le coût dans
`01-choisir.md`. Si la personne hésite, on lui propose une recommandation, qu'elle peut refuser.

**Choix 1 : qui apparaît à l'image et qui parle ?**

| Option | Pour | Contre |
|---|---|---|
| Elle tourne elle-même, face caméra | Authentique, aucun abonnement, le plus crédible pour un témoignage ou une prise de position | Demande du temps, un son et une lumière corrects, souvent plusieurs prises |
| Un avatar IA (une personne de synthèse qui dit le texte) | Aucun tournage ; pratique pour du contenu régulier, en plusieurs langues ou personnalisé | Moins authentique ; service tiers souvent payant (prix à vérifier sur le site de l'outil) ; accord de la personne dont on reproduit le visage ou la voix ; à signaler (voir plus bas) |
| Une voix de synthèse sur des plans animés ou un enregistrement d'écran | Aucun tournage ; on corrige le texte et on régénère | Ton moins vivant ; accord de la personne si la voix est clonée |
| Sans voix : musique et texte à l'écran | Le plus simple, utilisable sans le son | Moins personnel ; plus difficile pour expliquer |

**Choix 2 : comment on monte ?**

| Option | Pour | Contre |
|---|---|---|
| Un logiciel de montage (`marketing-skills:video` cite par exemple Descript, pour couper en éditant le texte, et CapCut, pour les sous-titres et les effets) | Visuel, rapide pour une vidéo isolée, adapté aux coupes d'une prise tournée | Difficile à refaire à l'identique pour une série |
| Le montage par code (Hyperframes : la vidéo est décrite en HTML puis rendue automatiquement) | Reproductible, un modèle sert pour toute une série, un agent peut le modifier | Demande Node.js et FFmpeg ; peu adapté aux coupes fines d'une prise tournée |

**Conseil si la personne hésite** : une seule vidéo tournée, un logiciel de montage ; une série de vidéos animées avec
voix de synthèse, le code.

**Signaler un contenu de synthèse.** Un avatar ou une voix de synthèse qui peuvent passer pour réels se signalent.
En Europe, le règlement (UE) 2024/1689, article 50, demande de signaler les hypertrucages (images, sons ou vidéos de
synthèse qui ressemblent à des personnes ou à des faits réels) et que les contenus de synthèse soient marqués ; il
s'applique depuis le 2 août 2026 (vérifié le 06/11/2026,
https://eur-lex.europa.eu/legal-content/FR/TXT/HTML/?uri=CELEX:32024R1689). Ce qui incombe à l'outil et ce qui vous
incombe dépend de votre cas : à lire dans le texte. YouTube demande de son côté de déclarer à l'import un contenu
réaliste modifié ou généré par IA, par exemple faire dire à une personne réelle ce qu'elle n'a pas dit ; sous-titres et
voix off clonée de sa propre voix n'ont pas à être déclarés (vérifié le 06/11/2026,
https://support.google.com/youtube/answer/14328491).

### 3. Les méthodes courtes quand aucune compétence ne couvre le geste

**Le script (étape 2).** Il est écrit pour être dit à voix haute, pas lu.

1. L'accroche (3 premières secondes) : la promesse ou la situation précise, en une phrase.
2. Le contexte : le problème de la personne qui regarde, en une ou deux phrases.
3. Le contenu : une idée principale, trois points au plus, chacun avec un exemple concret.
4. Un seul appel à l'action : ce que la personne fait ensuite.

À côté de chaque passage, noter ce qu'on voit (plan, texte à l'écran). Phrases courtes, une idée par phrase. La
personne qui parle lit le script à voix haute, le chronomètre et corrige tout ce qu'elle ne dirait pas : c'est la
validation. Critère de réussite : la durée tient dans le format visé et le texte se dit sans buter.

**Le tournage (étape 3).** Liste de contrôle avant d'appuyer sur « enregistrer » :

- Son (le plus important) : micro le plus près possible de la bouche, pièce calme sans écho (rideaux, tapis), appareils
  bruyants éteints. Enregistrer dix secondes et les réécouter au casque.
- Lumière : face à une fenêtre ou à une lampe douce placée devant, jamais de fenêtre dans le dos ; pas de plafonnier
  seul ; une lumière qui ne change pas pendant la prise.
- Cadrage : caméra à hauteur des yeux, regard vers l'objectif, un peu d'air au-dessus de la tête, fond rangé. Format
  vertical pour les formats courts, horizontal pour YouTube ; garder le texte à l'écran loin des bords.
- Prises : tourner deux prises complètes plutôt que des morceaux, nettoyer l'objectif, couper les notifications.

Critère de réussite : on comprend chaque mot au casque, le visage est lisible, et une prise propre existe de bout en
bout.

**La publication (étape 5).** Avant tout : la musique est libre de droits ou sous licence (garder la licence), les
personnes filmées ont donné leur accord, aucune marque n'apparaît sans raison. On prépare ensuite, selon la plateforme :

| Plateforme | Ce qu'on prépare |
|---|---|
| YouTube | Un titre qui dit la promesse avec les mots qu'on chercherait ; une description dont les deux premières lignes servent seules ; des chapitres horodatés si la vidéo est longue ; une miniature lisible en petit ; un fichier de sous-titres ; le réglage obligatoire « destinée aux enfants ou non » (vérifié le 06/11/2026, https://support.google.com/youtube/answer/9527654) ; la déclaration de contenu de synthèse si elle s'applique ; une mise en ligne en « non répertoriée » pour relire avant de passer en public |
| LinkedIn | Le fichier vidéo mis en ligne dans le post plutôt qu'un lien ; des sous-titres ; l'accroche au début du texte ; le lien externe en commentaire. Pour le post lui-même : `/publier-sur-linkedin:publier-sur-linkedin` |
| Instagram, TikTok, YouTube Shorts | Format vertical ; une accroche dans les 3 premières secondes ; des sous-titres ; une légende qui tient seule ; une image de couverture. Durées et rythme conseillés : `marketing-skills:social` |
| Site web | Le fichier ou son intégration ; des sous-titres et une transcription ; pas de lecture automatique avec le son |

Critère de réussite : la vidéo se lit en entier depuis un autre compte ou une fenêtre privée, les sous-titres
s'affichent, et le lien est relevé dans `05-publier.md`. La personne fait le dernier clic.

<!-- etapes:debut -->
| # | Étape | Compétences | Règle de choix |
|---|---|---|---|
| 1 | Choisir comment la fabriquer | Choisir la méthode : `marketing-skills:video` | Aucune option n'est imposée : on pose les deux choix à la personne, avec les deux options expliquées (voir le SKILL.md). Le premier : tourner soi-même, utiliser un avatar IA, ou faire parler une voix de synthèse sur des plans animés. Le second : monter dans un logiciel de montage, ou monter par code. marketing-skills:video compare les approches ; la méthode se choisit ensuite par son coût et son verdict daté, et par l'effet voulu ; par défaut, on tourne soi-même. |
| 2 | Écrire le script | Trouver l'idée du short : `poser-sa-strategie-marketing:video-qui-sortent-du-lot` ; `faire-une-video:video-idee-de-short` · Écrire le script : `marketing-skills:social` ; `marketing-skills:copywriting` ; `hyperframes:hyperframes-creative` | Un script écrit pour l'oral, validé par la personne qui le dira avant tout tournage ou toute génération. Pour une vidéo courte, marketing-skills:social donne les structures et l'accroche ; pour les autres formats, la méthode du SKILL.md. Manque : aucune compétence ne couvre un script long (explicatif de plusieurs minutes, interview) : la méthode du SKILL.md tient lieu de guide. |
| 3 | Tourner ou générer les plans | Générer des plans animés : `hyperframes:hyperframes` ; `hyperframes:motion-graphics` ; `hyperframes:faceless-explainer` · Faire la vidéo de lancement d'un site : `hyperframes:product-launch-video` | Par défaut, on tourne soi-même ; l'avatar seulement quand on le choisit. Le travail suit le choix de l'étape 1 : prises tournées par la personne (liste de contrôle du SKILL.md), plans animés, avatar. Un avatar ou une voix de synthèse ne s'utilisent qu'avec l'accord de la personne dont on reproduit le visage ou la voix, et leur signalement se prépare (voir le SKILL.md). Manque : aucune compétence ne guide le tournage lui-même (son, lumière, cadrage) : la liste de contrôle du SKILL.md tient lieu de méthode. |
| 4 | Monter la vidéo | Monter la vidéo : `hyperframes:talking-head-recut` · Sous-titrer : `hyperframes:embedded-captions` · Tester trois ouvertures : `marketing-skills:ad-creative` ; `faire-une-video:video-tester-trois-ouvertures` | Le montage suit le choix de l'étape 1 : logiciel de montage, ou montage par code avec les compétences Hyperframes (sans logiciel à piloter). Les droits de la musique et des images se vérifient à la main. Manque : aucune compétence ne coupe les silences et les ratés d'une prise : hyperframes:talking-head-recut ajoute des habillages graphiques mais laisse la prise intacte, donc la découpe se fait dans un logiciel de montage ou à la main. |
| 5 | Publier la vidéo | Faire le titre et la miniature : `marketing-skills:image` ; `faire-une-video:video-titre-et-miniature` · Inventorier les moments : `small-business:social-content-engine` ; `faire-une-video:video-declinaison-des-moments` · Publier en format court (LinkedIn, Instagram, TikTok, Shorts) : `marketing-skills:social` | Rien ne part sans le dernier clic. On prépare ce que chaque plateforme demande (voir le tableau du SKILL.md), on vérifie les droits de la musique et des images, puis la personne fait le dernier clic. Rien ne part sans lui. Manque : aucune compétence ne guide la publication sur YouTube : la méthode du SKILL.md tient lieu de guide ; pour un post LinkedIn qui présente la vidéo, voir /publier-sur-linkedin:publier-sur-linkedin. |
<!-- etapes:fin -->

### 4. Clore un passage

À la fin de chaque séance, on écrit l'état (fait, reste, prochaine action) au journal. Si une compétence a déçu à une
étape, on le note aussi, pour rouvrir le choix de la compétence de cette étape.

## Ce qui manque

- **Le tournage** (étape 3) et **la publication sur YouTube** (étape 5) : aucune compétence publique, la liste de
  contrôle et le tableau ci-dessus tiennent lieu de méthode.
- **Un script long** (étape 2) : `marketing-skills:social` couvre la vidéo courte ; pour un explicatif de plusieurs
  minutes ou une interview, la méthode ci-dessus sert de guide.
- **La découpe d'une prise** (étape 4) : `hyperframes:talking-head-recut` habille une prise sans la couper ; couper les
  silences et les ratés se fait dans un logiciel de montage.
- **Les droits de la musique et des images** se vérifient à la main.

## Frontières

| Demande | Va à |
|---|---|
| Un post LinkedIn | `/publier-sur-linkedin:publier-sur-linkedin` |
| Une pub vidéo, les campagnes payantes | `/publicite-payante:publicite-payante` |
| Le lancement d'un produit | `/lancer-un-produit:lancer-un-produit` |
