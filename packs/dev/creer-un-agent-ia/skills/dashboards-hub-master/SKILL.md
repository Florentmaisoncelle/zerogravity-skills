---
name: dashboards-hub-master
description: Crée, publie et tient à jour une page de tableau de bord interne dans un hub de pages (un sujet = une page, rangée sous une catégorie, lisible d'un coup d'œil), puis rend le lien vérifié. À utiliser pour afficher le chiffre du but d'un agent et son point de départ. Déclencheurs : "dashboard", "tableau de bord", "page du hub", "publie la page", "mets-le en ligne", "redéploie".
---

# Publier et tenir une page de tableau de bord

Une page publiée, rangée au bon endroit, lisible en quelques secondes, avec son lien rendu à la fin. Dans le pack « Créer un agent IA », cette compétence sert l'étape Mesurer : la page affiche **le chiffre du but de l'agent** et **son point de départ**, pour que l'écart se voie sans ouvrir autre chose.

Ce qu'il faut avoir : un dossier de projet (idéalement versionné), un compte chez un hébergeur de pages statiques (Vercel, Netlify, Cloudflare Pages ou équivalent), et un hub, c'est-à-dire un dossier avec une page d'accueil qui liste les pages par catégorie. Pas de hub encore : le créer à la première page (voir « Premier hub »).

## 1. Avant d'écrire une ligne

Trois questions, dans cet ordre. Sans réponse à chacune, on ne crée pas la page.

1. **Quel sujet porte cette page ?** Un sujet, une page. Si le sujet a déjà sa page, on l'enrichit, on n'en ouvre pas une deuxième.
2. **Sous quelle catégorie du hub se range-t-il ?** Une page sans catégorie est servie, vivante d'apparence, et introuvable : c'est la page orpheline.
3. **Qu'existe-t-il déjà ?** Chercher dans le hub (titres et descriptions de l'accueil) avant de créer. Le titre ne prouve pas un doublon : lire le contenu des deux pages et chercher qui les relie.

Si la personne qui décide n'a pas validé l'emplacement d'une page neuve, le lui proposer en une ligne (ce qui existe, où la page entrerait) avant de la créer.

## 2. Choisir la forme avant de remplir

Une page se comprend d'un seul coup d'œil, ou elle est à refaire. Choisir la forme qui fait comprendre l'ensemble sans lire :

- un chiffre central pour le but (valeur actuelle, point de départ, cible), avec l'écart en couleur ;
- un enchaînement : une ligne verticale de points, pas des fiches ni une frise de phrases ;
- une comparaison : un tableau court, pas une phrase ;
- un état : une pastille de couleur, pas un mot de plus.

Ce que la page contient, et rien d'autre : tuiles, tableaux, bandeaux, pastilles, liens. Un titre, puis la matière. Le chiffre nu (`12 rendez-vous · 3 semaines`) bat la phrase qui l'explique.

Trois interdits :

- **Le mode d'emploi** ("comment lire cette page"). Une page qui a besoin d'être expliquée est mal structurée : on refait la structure.
- **Le commentaire sur son propre contenu** : décrire ce que la table d'à côté montre, ou d'où viennent les données.
- **Le doublon** : ce qui est déjà porté ailleurs se lie, il ne se réécrit pas.

Contrôle avant publication : un paragraphe de 30 mots ou plus est un pavé, trois par page est un plafond. Test final : *quelqu'un comprend-il l'ensemble en 5 secondes, sur un seul écran ?* Non : changer la forme, pas ajouter du texte.

Lisibilité :

- texte de lecture à 14 px au moins, interligne 1,7, marges larges entre sections ;
- 4 à 5 cartes par section au plus, au-delà un tableau ;
- N éléments = N lignes, jamais une phrase qui les enchaîne avec des points-virgules ;
- le détail long (historique, décisions, journal) ne s'affiche pas : il s'ouvre au clic ou se lie vers sa source ;
- ordre des sections : ce que la page dit d'abord (le chiffre, l'état), la mécanique interne à la fin et repliée.

## 3. Page qui montre le but d'un agent

Structure minimale, du haut vers le bas :

1. **Bandeau** : nom de l'agent, état (en service, en test, en pause), date de la dernière mesure.
2. **Le but en grand** : valeur actuelle, point de départ, cible, écart. Les trois chiffres viennent d'une seule source écrite (la fiche de l'agent ou son journal de résultats), jamais retapés de mémoire.
3. **Évolution** : une courbe ou un tableau court, une ligne par période. Si les mesures sont rares, le tableau.
4. **Pour aller creuser** : liens vers la fiche de l'agent, son journal, le détail des cas.

Règles de données :

- la page est une **vue en lecture seule** d'une source ; elle ne crée aucun suivi parallèle ;
- une valeur absente s'affiche "non mesuré", jamais zéro ni une estimation déguisée ;
- ne jamais additionner des mesures qui peuvent se recouper ;
- un lien non vérifié s'écrit "lien non enregistré", pas un lien deviné.

## 4. Ranger dans la source du hub, pas dans le HTML

Le rangement se fait **dans la source qui génère l'accueil du hub** (un fichier de configuration ou le gabarit), dans la même passe que la page. Si l'accueil est écrit à la main, c'est lui qu'on édite. Ne jamais ranger en retouchant une page générée : la prochaine régénération l'écrase.

Après rangement, **relire l'accueil servi** : la page doit y apparaître sous sa catégorie. Une déclaration qui ne se voit pas est un rangement qui n'a pas eu lieu.

Une page générée se corrige dans son générateur, puis on régénère. Jamais à la main dans le HTML produit.

## 5. Publier

Une page non publiée n'existe pas : on déploie, on ne demande pas la permission de le faire pour un hub interne.

1. **Vérifier ce qu'on publie** : bon dossier, bon projet, branche à jour (`git fetch`, puis comparer avec la branche publiée). Un dossier en retard republie l'ancienne version par-dessus la nouvelle.
2. **Un hub = un projet chez l'hébergeur.** Pas un projet par fichier HTML. Plusieurs dossiers peuvent être liés au même projet : le dernier qui déploie gagne en silence, donc on déploie depuis le dossier propriétaire. Lister les dossiers liés au même identifiant de projet avant le premier déploiement.
3. **Déployer** avec la commande de l'hébergeur, en **journalisant la sortie dans un fichier** et en la lisant. Un refus de permission n'apparaît qu'à la fin du processus et ressemble à une construction en cours (état "inconnu" pendant de longues minutes). Si la forme "production directe" est refusée, publier un déploiement de prévisualisation puis le promouvoir.
4. **Ne jamais retirer des déploiements pour y voir clair** : cela déplace l'adresse de production.
5. **Mesurer les quotas** : les hébergeurs gratuits plafonnent les déploiements par jour. Grouper les retouches, itérer en local, publier une fois à la fin. Un projet relié au dépôt se reconstruit à chaque envoi : désactiver le déploiement automatique si le plafond est atteint par des envois sans changement.
6. **Donnée interne = jamais dans un dossier public.** Une adresse de hub non listée reste accessible à qui la connaît. Un fichier de données interne sort des fichiers servis (exclusion dans la configuration de l'hébergeur) et se lit par une route protégée. Une route seule ne ferme rien : tester les variantes d'adresse (encodée, avec barre finale).

## 6. Vérifier en ligne

Un déploiement vert ne prouve rien sur ce que l'adresse montre. Vérifier le **contenu servi** :

- récupérer la page servie (`curl` ou navigateur) et y chercher le chiffre ou le titre qu'on vient d'ajouter ;
- comparer la taille servie à la taille du fichier local en cas de doute ;
- lire le `<title>` avant de croire une taille : une page de contrôle anti-robot de l'hébergeur peut répondre 200 avec un contenu étranger. Si le titre n'est pas le sien, arrêter de sonder en boucle et mesurer dans un navigateur ;
- ouvrir la page dans un navigateur sur ordinateur et sur téléphone ; vérifier les liens de l'accueil vers la page, et de la page vers ses sources ;
- relire l'accueil : la page y est, sous la bonne catégorie.

## 7. Rendre le lien

Terminer le message par **l'adresse de la page elle-même** (pas celle de la plateforme où la chercher), cliquable, vérifiée à l'étape 6.

- Page neuve : l'ouvrir une fois dans le navigateur de la personne, puis donner le lien.
- Page déjà publiée, republication ou vérification : le lien seul, sans rien ouvrir. Si la page est déjà affichée, dire "rafraîchis l'onglet".
- Déploiement impossible (quota épuisé, projet non lié) : le dire une fois avec la cause exacte, produire un fichier HTML autonome (données incluses) et l'ouvrir en rendu propre, jamais le source ni un fichier texte. Dès que le déploiement redevient possible, revenir au lien.
- Le déploiement qui échoue pour une raison qu'on ne peut pas lever soi-même (permission refusée, identifiants absents) se signale en une ligne avec l'erreur reçue, après avoir lancé la commande.

## Premier hub

Pas de hub encore :

1. créer un dossier `dashboards/` avec une page d'accueil listant les catégories ;
2. une catégorie par grand domaine de l'entreprise (vente, marketing, opérations, agents...), pas une par page ;
3. lier le dossier à un projet chez l'hébergeur, noter l'adresse dans le fichier de notes du projet ;
4. y ranger la première page, puis suivre les étapes 4 à 7.

Style de départ : fond clair (`#fafafa`), cartes blanches, texte foncé, un seul accent (violet ou bleu), statuts en vert (stable), bleu (test), orange (en cours), rose (bloqué). Pas de couleurs arbitraires pour distinguer des éléments de même nature.

## Ce qu'on ne fait jamais

- une page hors du hub, ou sans catégorie ;
- une page de plus sur un sujet qui a déjà la sienne ;
- un projet chez l'hébergeur par fichier HTML ;
- retoucher un HTML généré à la main ;
- publier sans relire ce qui est servi ;
- redéployer après chaque micro-retouche (quota) ;
- laisser un fichier de données interne atteignable par son adresse ;
- recopier dans un second outil ce qu'une page affiche déjà : on met un lien, pas une copie ;
- un tableau de bord qui explique au lieu de montrer ;
- demander la permission de publier un hub interne, ou finir par "à toi de déployer".

## Pour aller plus loin

Le but de l'agent à afficher se fixe à l'étape de cadrage : voir `creer-un-agent-ia:creer-un-agent-ia`. Pour éviter qu'un même fait vive à deux endroits, ranger les leçons durables dans la compétence concernée : `creer-un-agent-ia:router-capitalisation`.
