---
name: referencer-son-site
description: >-
  Quand on veut que son site soit trouvé dans Google et cité par les IA, de façon suivie (« fais tourner notre SEO »,
  « l'audit SEO de la semaine », « écris un article qui se classe », « une page perd des clics », « est-ce que ChatGPT
  nous cite ? », « où en est notre référencement ? ») → affiche l'état calculé depuis le dossier `seo/AAAA-Sww/`, puis
  déroule neuf étapes dans l'ordre : audit et priorités, requêtes, technique, pages, articles, maillage, liens,
  citations par les IA, suivi. Trois gestes n'ont pas de compétence publique (optimiser une page, rédiger un article,
  trouver les liens internes) et se font à la main. Se lance par `/referencer-son-site:referencer-son-site`.
  Déclencheurs : « référencement suivi », « SEO en continu », « audit SEO », « citations des IA ». Pas pour un
  diagnostic de conversion, une ressource gratuite ou l'inscription : `/convertir-les-visiteurs:convertir-les-visiteurs`.
  Pas pour les annuaires ou la presse : `/lancer-un-produit:lancer-un-produit`. Pas pour créer ou refaire le site :
  `/creer-un-site-web:creer-un-site-web`.
---

# Référencer son site : être trouvé dans Google et cité par les IA, chaque semaine

## Ce que ça résout

Le référencement ne se fait pas en une fois : il se mesure, se corrige et s'écrit chaque semaine, et il se joue
désormais aussi dans les réponses des IA. Sans ordre, on écrit des articles sans demande, on touche aux pages qui
marchent et on diagnostique des baisses imaginaires. Ici : une liste de contrôle en neuf étapes, tenue par des
compétences installables, avec des outils gratuits (console de recherche du moteur, crawl local) et sans abonnement.

**Résultat attendu** : à chaque passage (une semaine), un audit daté dans son propre dossier, un backlog trié, une action
utile faite, et les chiffres qui disent si ça marche. Le référencement ne se lance qu'une fois le site en ligne.

## Stratégie

1. **Une compétence par étape, la meilleure.** La table des étapes (plus bas) dit laquelle et pourquoi. Les règles de
   choix et les manques sont aussi dans `references/workflow.json`.
2. **L'état d'abord, toujours calculé** depuis les fichiers du passage en cours, `seo/AAAA-Sww/`, jamais recopié.
3. **Les étapes sans compétence publique le disent** et suivent la méthode écrite plus bas.
4. **Une seule validation par passage, à l'étape 1** : la personne choisit, dans le backlog trié, l'action de la
   semaine. Ce n'est pas un cadrage préalable. Restent à la personne : la prise de contact pour obtenir un lien, la
   publication d'une page.
5. **Tout texte qui sort au nom de l'entreprise** se relit pour sonner humain avant d'être montré.
6. **Les décisions se notent** dans le journal à chaque étape, avec ce qu'on a appris d'une semaine à l'autre : quelques lignes suffisent.

<!-- prerequis:debut -->
## Prérequis

Ce workflow s'appuie sur des compétences publiques, installées à part. Aucune n'est indispensable : si l'une manque, le workflow le dit et fait l'étape à la main. Faire l'étape à la main veut dire suivre sa règle de choix, écrire ce qu'elle doit rendre (dans le fichier de l'étape, ou dans la réponse quand le workflow n'a pas de dossier) et dire ce qui reste à la charge de la personne.

```text
/plugin marketplace add addyosmani/web-quality-skills
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin marketplace add coreyhaines31/marketingskills
/plugin install marketing-skills@marketingskills
/plugin install marketing@knowledge-work-plugins
/plugin install small-business@knowledge-work-plugins
/plugin install web-quality-skills@addy-web-quality-skills
```

Les workflows cités ici sont dans le même dépôt (le dépôt s'ajoute une fois : `/plugin marketplace add Florentmaisoncelle/zerogravity-skills`) :

```text
/plugin install convertir-les-visiteurs@zerogravity
/plugin install creer-un-site-web@zerogravity
/plugin install lancer-un-produit@zerogravity
```
<!-- prerequis:fin -->

## Étapes

### 0. Le dossier, puis l'état (lecture seule)

**Le dossier.** Un sous-dossier par passage, nommé par l'année et la semaine : `seo/2026-S45/`, à la racine du dossier
de l'entreprise. Chaque passage a son journal et ses fichiers. Dossier absent ou vide : il n'y a encore rien de fait,
l'état est « étape 1 » et le dossier se crée au premier passage. Si le dossier courant n'est pas celui de
l'entreprise, le dire en une ligne et demander où il vit : rien ne s'écrit avant. Passage par défaut : le plus récent
qui n'est pas terminé ; s'ils sont tous terminés ou si la personne demande un nouveau passage, on crée le dossier de la
semaine en cours et on repart à l'étape 1.

**L'état**, calculé depuis le journal et les fichiers :

```text
Site               <domaine>
Étapes             01 ✓  02 s.o.  03 -  04 -  05 -  06 -  07 -  08 -  09 -
Dernière décision  2026-11-06 · 02 · sans objet · requêtes inchangées depuis 2026-S41
Étape suivante     03 Rendre le site indexable, rapide et ouvert aux robots des IA
```

- Le journal `seo/AAAA-Sww/journal.md` a une ligne par décision :
  `AAAA-MM-JJ · NN · fait | en attente | sans objet | sautée | corrigée · <une phrase>`.
- Pour chaque étape, la dernière ligne du journal qui la nomme fait foi. `✓` : cette ligne dit `fait` ou `corrigée`
  et le fichier de l'étape existe. `s.o.` : elle dit `sans objet` ou `sautée` (l'étape n'est plus proposée). `-` :
  aucune ligne, ou le fichier manque.
- `corrigée` : l'étape est refaite après une correction ; elle reste ✓ et la ligne dit ce qui a changé. `sautée` :
  la personne a choisi de passer ; la ligne dit pourquoi.
- `en attente` : l'étape est préparée, mais elle dépend d'un geste ou d'une réponse qui arrive hors de la conversation. La ligne du journal dit ce qu'on attend et de qui. L'état l'affiche `att.` avec ce texte : l'étape n'est pas `✓`, parce que préparé n'est pas fait. Le workflow s'arrête là et le dit ; il n'invente jamais la suite (ni réponse, ni résultat, ni geste qu'on ne lui a pas confirmé). Quand la personne apporte ce qui est arrivé, la ligne `fait` suit. Ici : la mise en ligne des corrections (étapes 3 et 4), les liens que d'autres sites acceptent ou non (étape 7), les citations par les IA (étape 8) et les résultats, qui ne bougent qu'après des semaines (étape 9).
- L'étape suivante est la première étape `-` ou `att.`, dans l'ordre (devant une étape `att.`, on demande d'abord où en est l'attente). Si aucune ne l'est, le passage est terminé, et on peut
  ouvrir la semaine suivante.
- **Un passage n'est pas les neuf étapes.** L'étape 1 (audit et backlog) et l'étape 9 (suivi) se font à chaque
  passage. Parmi les autres, la personne choisit l'action de la semaine dans le backlog ; chaque étape qui ne sert pas
  cette semaine s'inscrit `sans objet`, en une ligne (« requêtes inchangées depuis 2026-S41 »). Au premier passage,
  toutes les étapes sont proposées dans l'ordre.
- **L'audit compare au passage précédent.** Il lit `01-audit-et-priorites.md` du dossier de la semaine précédente,
  écrit par la même étape. Si ce fichier est absent (premier passage), l'audit part de zéro et le dit.

**Une question n'est pas un ordre.** « Où en est notre référencement ? » : on donne l'état et la prochaine action, puis
on s'arrête. La commande du workflow, « continue » ou « déroule » : on enchaîne jusqu'à la première étape en attente, puis on s'arrête et on le dit.

### 1. Lancer l'étape suivante

Lire l'étape dans `references/workflow.json`, appliquer sa règle de choix, invoquer la compétence retenue, écrire sa
sortie dans le fichier de l'étape, inscrire `fait` au journal (ou `en attente`, voir plus haut), puis passer à la suivante sans redemander. Une étape qui
a un manque le dit franchement, avec le geste qui le comble.

Trois gestes n'ont pas de compétence publique et se font à la main :

- **Optimiser une page presque en tête (étape 4).** Pour chaque page en positions 4 à 15, on écrit un titre et une
  description qui font cliquer, on vérifie que la structure des titres répond aux questions, on ajoute les données
  structurées qui manquent, on soigne les images et le chemin vers la conversion. On commence par les gains rapides ; on
  ne réécrit jamais une page déjà en tête sans raison mesurée.
- **Rédiger un article original (étape 5).** Brief d'abord (plan, angle, questions), page écrite à partir de sources
  primaires, relecture d'expert (faits, sources, expérience). Pas de page sans demande vérifiée ; chaque chiffre porte
  son auteur, son année et son lien.
- **Trouver les liens internes à poser (étape 6).** On relève les pages orphelines et les pages qui se disputent la même
  requête, on arbitre (fusionner, différencier, rediriger) et on dresse la liste exacte des liens à poser.

<!-- etapes:debut -->
| # | Étape | Compétences | Règle de choix |
|---|---|---|---|
| 1 | Faire l'état des lieux et trier les priorités | Auditer le référencement du site : `marketing:seo-audit` ; `marketing-skills:seo-audit` · Mesurer la visibilité dans Google et dans les IA : `small-business:seo-ai-visibility` | Un audit par passage, daté, dans le dossier de la semaine, comparé à celui du passage précédent quand il existe : on ne reporte que le neuf dans le backlog. Un passage par semaine au plus. Les concurrents se prennent dans les résultats réels de la requête, jamais de mémoire. |
| 2 | Trouver les requêtes qui achètent et les ranger en sujets | Ranger les requêtes en sujets : `marketing-skills:content-strategy` | Une requête ne vaut que par l'intention de qui la tape : on commence par celles des gens prêts à acheter, jamais par le volume seul. |
| 3 | Rendre le site indexable, rapide et ouvert aux robots des IA | Rendre le site indexable : `web-quality-skills:seo` · Rendre le site rapide : `web-quality-skills:core-web-vitals` | On mesure ce que le moteur voit sans exécuter de JavaScript, sur la surface réellement servie ; un chiffre se croit après le témoin positif et le témoin négatif de l'outil. |
| 4 | Optimiser les pages qui sont presque en tête | Optimiser une page en page 2 : `marketing-skills:copywriting` ; `marketing-skills:cro` · Poser les données structurées : `marketing-skills:schema` | On commence par les gains rapides : les pages déjà vues mais peu cliquées. Aucune page en tête ne se réécrit sans raison mesurée. |
| 5 | Écrire et tenir à jour les pages qui se classent | Produire des pages en série : `marketing-skills:programmatic-seo` · Écrire une page comparatif : `marketing-skills:competitors` · Écrire un article original et vérifiable : `marketing-skills:copy-editing` | Pas de page sans demande vérifiée ni sans source primaire ; chaque chiffre porte son auteur, son année et son lien. Une page produite en série doit apporter une valeur propre à chaque page : Google traite comme du spam les pages produites en masse pour manipuler le classement, qu'elles viennent d'une IA ou d'une personne. Un texte qui sort au nom de l'entreprise passe par la relecture anti-IA : il se relit pour sonner humain avant d'être montré. Manque : Aucune compétence publique pour rédiger un article original et vérifiable : on l'écrit à la main, brief d'abord, à partir de sources primaires, puis relecture d'expert. |
| 6 | Relier les pages entre elles | Relier les pages entre elles : `marketing-skills:site-architecture` | Chaque page satellite pointe vers sa page pilier ; deux pages sur la même requête ne restent pas toutes les deux. |
| 7 | Obtenir des liens d'autres sites | Obtenir des liens d'autres sites : `marketing-skills:link-building` | Un lien se gagne par une raison d'être cité (une donnée, une page utile), jamais par un achat. link-building choisit les tactiques ; les annuaires et la presse se font dans « Lancer un produit ». |
| 8 | Être cité dans les réponses des IA | Se faire citer par les IA : `marketing-skills:ai-seo` | On mesure les réponses réelles des IA sur des questions d'achat fixées à l'avance, avant et après chaque changement ; aucune promesse de citation. |
| 9 | Suivre les résultats et réagir à une baisse | Suivre les positions et le trafic : `marketing-skills:analytics` · Trouver les mots-clés proches et les pages en baisse : `referencer-son-site:seo-search-console` | Une baisse ne se diagnostique qu'au-dessus d'un plancher de volume et sur deux périodes comparables ; sans alerte, aucun diagnostic inventé. |
<!-- etapes:fin -->

### 2. Clore un passage

À la fin de chaque séance, on écrit l'état (fait, reste, prochaine action) au journal. Si une compétence a déçu à une
étape, on le note aussi, pour rouvrir le choix de la compétence de cette étape.

## Ce qui se fait à la main

- **Optimiser une page presque en tête** (étape 4), **rédiger un article** (étape 5) et **trouver les liens internes à poser**
  (étape 6) : aucune compétence publique, on les fait à la main.
- **La lecture des positions** (étape 9) se fait à la main, à partir des chiffres de la console de recherche du moteur.
- **Aucune promesse de classement ni de citation** : on mesure, on ne garantit pas.

## Frontières

| Demande | Va à |
|---|---|
| Diagnostiquer une page qui convertit mal, une ressource gratuite, la capture d'adresse | `/convertir-les-visiteurs:convertir-les-visiteurs` |
| Les annuaires, la presse, un lancement | `/lancer-un-produit:lancer-un-produit` |
| Créer ou refaire le site | `/creer-un-site-web:creer-un-site-web` |
