---
name: publier-sur-linkedin
description: >-
  Quand on veut publier sur LinkedIn de bout en bout (« choisis mes posts de la semaine », « écris-moi un post avec une
  bonne accroche », « il me faut le visuel du post », « programme mon post », « décline mon post sur les autres réseaux »,
  « où en est mon LinkedIn ? ») → affiche l'état calculé depuis le dossier `contenu/`, un sous-dossier par semaine, puis
  déroule huit étapes dans l'ordre : choisir, écrire, illustrer, programmer, poster, décliner, commenter, soigner le
  profil. Presque toutes les étapes ont une compétence publique ; seuls le sondage, le texte du profil et le dernier
  clic de publication se font à la main, et c'est dit. Se lance par `/publier-sur-linkedin:publier-sur-linkedin`.
  Déclencheurs : « post LinkedIn », « accroche », « programmer un post », « décliner un post », « commentaires
  LinkedIn », « profil LinkedIn ». Pas pour une vidéo : `/faire-une-video:faire-une-video`. Pas pour un lancement, la
  presse, les annuaires ou la traduction : `/lancer-un-produit:lancer-un-produit`. Pas pour le référencement :
  `/referencer-son-site:referencer-son-site`.
---

# Publier sur LinkedIn : choisir, écrire, illustrer, programmer, poster, commenter

## Ce que ça résout

Publier de façon régulière demande de la matière, un texte et une accroche (la première ligne, celle qui donne envie de
cliquer sur « voir plus ») relus, un visuel, une programmation, puis des commentaires et un profil à jour. Ici : la
chaîne complète dans l'ordre réel du travail, de l'idée choisie dans une banque d'idées notées jusqu'au profil, avec un
seul état lisible, semaine par semaine.

**Résultat attendu** : les posts de la semaine choisis, écrits, illustrés, programmés et postés, déclinés sur les autres
réseaux si besoin, les commentaires posés et, quand l'offre change, le profil soigné.

**À savoir avant de commencer** : la compétence `marketing-skills:social` porte l'essentiel du travail (matière,
écriture, programmation, commentaires). Ce workflow apporte l'ordre, l'état et les points de validation. Trois gestes
restent à la main : rédiger un sondage, écrire le texte du profil et faire le dernier clic de publication ; la section
« Ce que les compétences ne font pas » donne une méthode courte pour chacun.

## Stratégie

1. **Une compétence par étape quand il y en a une.** La table des étapes (plus bas) dit laquelle et pourquoi. Les
   règles de choix et les manques sont aussi dans `references/workflow.json`, qui reste la seule source de cette table.
2. **L'état d'abord, toujours calculé** depuis les fichiers du dossier de la semaine, jamais recopié.
3. **L'ordre protège la décision** : on choisit les meilleures idées plutôt que d'en inventer, une idée par post, court
   par défaut. Sauter une étape reste possible sur demande ; le journal dit laquelle et pourquoi.
4. **Deux validations, aux étapes 1 et 2.** À l'étape 1, la personne valide les posts retenus pour la semaine. À
   l'étape 2, elle valide le texte de chaque post avant toute programmation. Entre les deux et après, le workflow
   déroule seul. Restent à la personne : le dernier clic de publication, et les droits à l'image et les marques
   déposées, qu'aucune compétence ne vérifie.
5. **Tout texte qui sort au nom de l'entreprise** se relit avant d'être montré (ton naturel, aucun chiffre inventé), et
   rien ne part sans validation.
6. **Les décisions se notent** dans le journal à chaque étape. En fin de semaine, deux lignes suffisent pour le
   prochain passage : le post qui a le plus réagi et ce qu'on en retient.

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
/plugin install faire-une-video@zerogravity
/plugin install lancer-un-produit@zerogravity
/plugin install referencer-son-site@zerogravity
```
<!-- prerequis:fin -->

## Étapes

### 0. Le dossier, puis l'état (lecture seule)

**Le dossier.** Le contenu LinkedIn vit dans le dossier de l'entreprise : `contenu/` à sa racine, avec un
sous-dossier par semaine, `contenu/AAAA-Sww/` (année, puis `S` et le numéro de semaine, par exemple `2026-S46`). Dans
chaque sous-dossier : un fichier par étape, un journal, et pour les étapes qui touchent plusieurs posts, une section par
post (`## Post 1`, `## Post 2`, et ainsi de suite). Dossier `contenu/` absent ou vide : il n'y a encore rien de fait, l'état est
« étape 1 » et le dossier de la semaine se crée au premier passage. Si le dossier courant n'est pas celui du projet, le
dire en une ligne et demander où il vit : rien ne s'écrit avant.

**La semaine par défaut** : la plus récente qui n'est pas terminée, ou celle que la personne nomme. Si toutes sont
terminées, ou si elle demande une nouvelle semaine, on crée le sous-dossier suivant et on repart à l'étape 1.

**L'état**, calculé depuis le journal et les fichiers de la semaine :

```text
Réseau             LinkedIn
Semaine            2026-S46
Étapes             01 ✓  02 ✓  03 -  04 -  05 -  06 -  07 -  08 -
Dernière décision  2026-11-09 · 02 · fait · trois posts écrits et validés
Étape suivante     03 Illustrer le post → marketing-skills:image
```

- Le journal `contenu/AAAA-Sww/journal.md` a une ligne par décision :
  `AAAA-MM-JJ · NN · fait | en attente | sans objet | sautée | corrigée · <une phrase>`.
- Pour chaque étape, la dernière ligne du journal qui la nomme fait foi. `✓` : cette ligne dit `fait` ou `corrigée` et le
  fichier de l'étape existe. `s.o.` : elle dit `sans objet` ou `sautée` (l'étape n'est plus proposée). `-` : aucune
  ligne, ou le fichier manque.
- `sans objet` ne s'applique qu'aux étapes optionnelles (6 et 8). `corrigée` : l'étape est refaite après une
  correction ; elle reste ✓ et la ligne dit ce qui a changé. `sautée` : la personne a choisi de passer ; la ligne dit
  pourquoi.
- Une étape est faite pour tous les posts de la semaine à la fois : son fichier a une section par post, et la ligne
  `fait` n'est écrite qu'une fois tous les posts traités.
- `en attente` : l'étape est préparée, mais elle dépend d'un geste ou d'une réponse qui arrive hors de la conversation. La ligne du journal dit ce qu'on attend et de qui. L'état l'affiche `att.` avec ce texte : l'étape n'est pas `✓`, parce que préparé n'est pas fait. Le workflow s'arrête là et le dit ; il n'invente jamais la suite (ni réponse, ni résultat, ni geste qu'on ne lui a pas confirmé). Quand la personne apporte ce qui est arrivé, la ligne `fait` suit. Ici : la validation des idées et des textes (étapes 1 et 2), la publication ou la programmation par la personne (étapes 4 et 5), les réactions et les commentaires à traiter (étape 7).
- L'étape suivante est la première étape `-` ou `att.`, dans l'ordre (devant une étape `att.`, on demande d'abord où en est l'attente). Si aucune ne l'est, la semaine est terminée, et on peut
  ouvrir la suivante.

**Une question n'est pas un ordre.** « Où en est mon LinkedIn ? » : on donne l'état et la prochaine action, puis on
s'arrête. La commande du workflow, « continue » ou « déroule » : on enchaîne jusqu'à la première étape en attente, puis on s'arrête et on le dit.

**Une demande au milieu du chemin** (« écris-moi une accroche ») : l'étape 2 marche seule ; le texte se relit avant
toute publication.

### 1. Lancer l'étape suivante

Lire l'étape dans `references/workflow.json`, appliquer sa règle de choix, invoquer la compétence retenue, écrire sa
sortie dans le fichier de l'étape, inscrire `fait` au journal (ou `en attente`, voir plus haut), puis passer à la suivante sans redemander (sauf aux deux
validations). Une étape qui a un manque le dit franchement, avec le geste qui le comble.

Ce que chaque fichier d'étape contient :

- **01-choisir.md** : la banque d'idées (une ligne par idée : l'idée, sa source, sa note) et les posts retenus pour la
  semaine, avec le jour prévu pour chacun.
- **02-ecrire.md** : une section par post, avec l'accroche, le texte final et la date de validation une fois que la
  personne a dit oui.
- **03-illustrer.md** : par post, le visuel (ou « sans visuel »), sa source et le droit de l'utiliser, le sondage s'il y
  en a un.
- **04-programmer.md** : par post, le créneau et l'outil utilisé (programmation de LinkedIn ou outil tiers) ; ou
  « brouillon » si rien n'est encore programmé.
- **05-poster.md** : par post, le lien du post en ligne.
- **06-decliner.md**, **07-commenter.md**, **08-profil.md** : ce qui a été préparé ou fait, en quelques lignes.

<!-- etapes:debut -->
| # | Étape | Compétences | Règle de choix |
|---|---|---|---|
| 1 | Choisir quoi publier | Choisir les posts de la semaine : `small-business:content-strategy` · Trouver la matière du post : `marketing-skills:content-strategy` | On note chaque idée de la banque, puis on prend les meilleures plutôt que d'en inventer : une idée par post, court par défaut. Sans ligne éditoriale, small-business:content-strategy en pose une. La personne valide les posts retenus : c'est la première des deux validations du workflow. Seul un texte validé par un humain part : sa validation déclenche la publication programmée. |
| 2 | Écrire le post | Écrire l'accroche : à la main | Une idée par post, court par défaut, une section par post dans le fichier ; seul un texte validé par un humain part, et sa validation déclenche la publication programmée. marketing-skills:social écrit le post : accroches, modèles de post, carrousels (posts en plusieurs pages à faire défiler) et liste des tics d'écriture qui font « texte généré ». La personne valide le texte de chaque post avant toute programmation : c'est la deuxième validation du workflow. |
| 3 | Illustrer le post | Faire le visuel du post : `marketing-skills:image` · Fixer la charte graphique : `small-business:brand-style` · Ajouter un sondage : à la main | La charte se fixe une fois avec small-business:brand-style, puis marketing-skills:image produit les visuels ; les visuels d'annonce se font avec la campagne, dans /lancer-un-produit:lancer-un-produit. Les droits à l'image et les marques déposées se vérifient à la main : aucune compétence ne le fait. |
| 4 | Programmer le post | Préparer et programmer la publication : `small-business:social-content-engine` | Une idée par post, court par défaut ; seul un texte validé par un humain est programmé, et sa validation déclenche la publication programmée. small-business:social-content-engine tient le calendrier et la file de une à deux semaines et crée les posts en brouillon d'abord ; elle ne publie jamais sans accord. Manque : aucune compétence ne programme seule : il faut un outil de programmation (celui de LinkedIn, à vérifier sur votre compte, ou un outil tiers avec une API ou un serveur MCP). Le workflow prépare le texte, le visuel et le créneau. |
| 5 | Poster | Poster le post : à la main | Une idée par post, court par défaut ; seul un texte validé par un humain part, et sa validation déclenche la publication programmée. Le post part par la programmation de l'étape d'avant, ou à la main. Le lien du post publié se relève dans le fichier de l'étape et le journal. Manque : le dernier clic de publication reste à la personne : aucune compétence ne publie à sa place. |
| 6 | Décliner sur les autres réseaux (quand l'entreprise publie ailleurs que sur LinkedIn) | Décliner le post sur les autres réseaux : `marketing-skills:social` | marketing-skills:social décline vers les autres réseaux ; le calendrier et la file passent par small-business:social-content-engine à l'étape précédente. La source d'origine se cite ; la publication reste validée. Instagram, TikTok, X et Reddit n'ont pas encore de méthode propre. marketing-skills:social par défaut : elle détaille LinkedIn, X, Instagram, TikTok, Facebook et Telegram (format, rythme, ce qui marche) ; pour Reddit elle ne couvre que le repérage de conversations. |
| 7 | Commenter et animer | Animer la communauté : `marketing-skills:community-marketing` | marketing-skills:social pour commenter : une routine quotidienne courte, des commentaires qui apportent quelque chose, et un tri des posts à commenter (une liste de dix notée). marketing-skills:community-marketing pour le plan et l'animation, seulement si l'entreprise anime sa propre communauté (groupe, forum, Slack, Discord). Les créateurs se travaillent dans le workflow « Lancer un produit » (/lancer-un-produit:lancer-un-produit). Les règles de modération et d'escalade s'écrivent avant l'ouverture d'une communauté : la compétence n'en dit que deux lignes. |
| 8 | Soigner son profil (quand l'offre ou le positionnement change) | Écrire et auditer son profil : à la main · Faire la bannière du profil : `small-business:canva-creator` | Le profil se refait quand l'offre change, pas à chaque post. marketing-skills:image fait la bannière aux bonnes dimensions ; le texte du profil s'écrit à la main avec la méthode du SKILL.md. Manque : aucune compétence ne rédige le titre et le résumé d'un profil LinkedIn : on les écrit à la main, d'après l'offre et le positionnement du moment. |
<!-- etapes:fin -->

### 2. Ce que les compétences ne font pas

Trois gestes restent à la main. Voici une méthode courte pour chacun.

**Rédiger un sondage (étape 3).** `marketing-skills:social` dit seulement que les sondages font réagir sans bâtir
d'autorité : à doser, un de temps en temps. Pour en écrire un : une question à laquelle on répond en cinq secondes, deux
à quatre réponses courtes qui ne se recoupent pas, et une ligne dans le post qui dit pourquoi on pose la question.
Prévoir un post de suite qui donne le résultat et ce qu'on en fait. Critère de réussite : quelqu'un qui ne connaît pas
l'entreprise comprend la question sans lire le reste.

**Écrire le texte du profil (étape 8).** Aucune compétence ne le fait. Le titre dit qui on aide et pour quel résultat,
pas seulement un intitulé de poste. Le résumé tient en quatre temps : le problème du client en une phrase, ce qu'on
fait et comment, une preuve vraie (un résultat chiffré ou un client qu'on a le droit de citer), puis comment nous
joindre. On vérifie que la photo et la bannière disent la même chose que le texte. Critère de réussite : un inconnu
comprend en dix secondes qui l'entreprise aide et à quoi, et ce qu'il peut faire ensuite.

**Le dernier clic (étape 5).** Avant de publier : relire le texte final dans l'aperçu, vérifier que le visuel est le
bon, mettre les liens externes en commentaire plutôt que dans le corps du post (`marketing-skills:social` explique que
les liens dans le corps réduisent la portée), puis publier. Relever aussitôt le lien du post dans `05-poster.md`.
LinkedIn propose une programmation intégrée dans la fenêtre de rédaction (une icône d'horloge) ; à vérifier sur votre
compte, selon son type (profil ou page entreprise).

### 3. Clore un passage

À la fin de chaque séance, on écrit l'état (fait, reste, prochaine action) au journal. Si une compétence a déçu à une
étape, on le note aussi, pour rouvrir le choix de la compétence de cette étape.

## Choix de méthode

- Ce workflow ne couvre que LinkedIn, dans l'ordre réel du travail. La vidéo, le lancement, la presse, les annuaires, la
  traduction et le référencement ont chacun leur workflow.
- Pour les autres réseaux, `marketing-skills:social` par défaut ; `small-business:social-content-engine` quand
  l'entreprise travaille déjà dans Canva et HubSpot.

## Ce qui manque

- **Le texte d'un sondage** (étape 3) et **le titre et le résumé du profil** (étape 8) : aucune compétence ne les écrit,
  tout se fait à la main avec la méthode ci-dessus.
- **La programmation** (étape 4) : la compétence prépare le plan mais ne programme pas seule ; il faut un outil de
  programmation.
- **Le dernier clic de publication** (étape 5) reste à la personne.
- **Reddit** (étape 6) : `marketing-skills:social` n'aide qu'à repérer des conversations, pas à y publier.
- **Les droits à l'image et les marques déposées** se vérifient à la main (étape 3).

## Frontières

| Demande | Va à |
|---|---|
| Une vidéo | `/faire-une-video:faire-une-video` |
| Un lancement, la presse, les annuaires, la traduction | `/lancer-un-produit:lancer-un-produit` |
| Le référencement, le SEO | `/referencer-son-site:referencer-son-site` |
