---
name: poser-sa-strategie-marketing
description: >-
  Quand on veut poser sa stratégie marketing de bout en bout (« étudie mon marché », « qui sont mes concurrents et
  qu'ont-ils changé ? », « aide-moi à me positionner », « quels messages pour quelle cible ? », « fais-moi un plan
  marketing », « où en est ma stratégie marketing ? ») → affiche l'état calculé depuis le dossier
  `strategie-marketing/`, puis déroule sept étapes dans l'ordre : marché et publics, concurrents, positionnement, offre
  et prix, parcours client, plan, mesure. Le chiffrage du marché et la carte du parcours client se font à la main,
  et c'est dit. Se lance par `/poser-sa-strategie-marketing:poser-sa-strategie-marketing`. Déclencheurs : « stratégie
  marketing », « étude de marché », « personas », « veille concurrentielle », « positionnement », « messages clés »,
  « plan marketing », « parcours client ». Pas pour produire du contenu :
  `/publier-sur-linkedin:publier-sur-linkedin`. Pas pour lancer un produit ou une campagne :
  `/lancer-un-produit:lancer-un-produit`. Pas pour une décision d'affaires difficile :
  `/decider-une-strategie:decider-une-strategie`. Pas pour cadrer un chantier flou :
  `/cadrer-un-chantier:cadrer-un-chantier`.
---

# Poser sa stratégie marketing : le marché, les concurrents, le positionnement et le plan

## Ce que ça résout

Une entreprise produit souvent avant de savoir à qui elle parle : des posts sans positionnement, une campagne sans
étude, un plan sans concurrent. Chaque geste existe déjà dans une compétence, mais aucune ne dit l'ordre. Ici : le
marché et les publics d'abord, une veille concurrentielle qui ne signale jamais deux fois la même chose, un
positionnement que toutes les autres compétences relisent, puis le plan qui mène à une décision, et la mesure qui dit
si ça marche.

**Résultat attendu** : une étude citée et datée, un dossier par concurrent et sa veille, un positionnement et des
messages prouvés dans un fichier de contexte partagé, l'offre et le prix chiffrés, la carte du parcours client, un plan
présenté pour décision, puis un rapport de résultats.

## Stratégie

1. **Une compétence par étape, la meilleure.** La table des étapes (plus bas) dit laquelle et pourquoi. Les règles de
   choix et les manques sont aussi dans `references/workflow.json`.
2. **L'état d'abord, toujours calculé** depuis les fichiers de `strategie-marketing/`, jamais recopié.
3. **L'ordre protège la décision** : pas de positionnement sans publics étudiés, pas de plan sans positionnement.
   Sauter une étape reste possible sur demande ; le journal dit laquelle et pourquoi.
4. **Une seule validation, à l'étape 3** : le positionnement et les messages. Ce n'est pas la première étape : le
   marché, les publics et les concurrents (étapes 1 et 2) se déroulent d'abord sans validation, parce que le
   positionnement s'appuie sur eux. Ensuite tout se déroule. Restent à la personne : valider les allégations,
   décider du prix, arbitrer le plan.
5. **Tout texte qui sort au nom de l'entreprise** se relit avant d'être montré (ton naturel, aucun chiffre inventé), et
   rien ne part sans validation.
6. **Les décisions se notent** dans le journal à chaque étape, avec ce qu'on a appris : quelques lignes suffisent.

<!-- prerequis:debut -->
## Prérequis

Ce workflow s'appuie sur des compétences publiques, installées à part. Aucune n'est indispensable : si l'une manque, le workflow le dit et fait l'étape à la main. Faire l'étape à la main veut dire suivre sa règle de choix, écrire ce qu'elle doit rendre (dans le fichier de l'étape, ou dans la réponse quand le workflow n'a pas de dossier) et dire ce qui reste à la charge de la personne.

```text
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin marketplace add anthropics/skills
/plugin marketplace add coreyhaines31/marketingskills
/plugin install document-skills@anthropic-agent-skills
/plugin install marketing-skills@marketingskills
/plugin install marketing@knowledge-work-plugins
/plugin install operations@knowledge-work-plugins
/plugin install product-management@knowledge-work-plugins
/plugin install small-business@knowledge-work-plugins
```

Les workflows cités ici sont dans le même dépôt (le dépôt s'ajoute une fois : `/plugin marketplace add Gremelinn0/zerogravity-skills`) :

```text
/plugin install cadrer-un-chantier@zerogravity
/plugin install creer-un-site-web@zerogravity
/plugin install decider-une-strategie@zerogravity
/plugin install lancer-un-produit@zerogravity
/plugin install publier-sur-linkedin@zerogravity
```
<!-- prerequis:fin -->

## Étapes

### 0. Le dossier, puis l'état (lecture seule)

**Le dossier.** Un seul dossier : `strategie-marketing/`, à la racine du dossier de l'entreprise. Il n'y a qu'une
stratégie à la fois ; chaque passage de révision se date dans le journal. Dossier absent ou vide : il n'y a encore
rien de fait, l'état est « étape 1 » et le dossier se crée au premier passage. Si le dossier courant n'est pas celui
de l'entreprise, le dire en une ligne et demander où il vit : rien ne s'écrit avant.

**L'état**, calculé depuis le journal et les fichiers :

```text
Étapes             01 ✓  02 ✓  03 -  04 -  05 -  06 -  07 -
Dernière décision  2026-11-06 · 02 · fait · trois concurrents suivis
Étape suivante     03 Se positionner et écrire ses messages
```

- Le journal `strategie-marketing/journal.md` a une ligne par décision :
  `AAAA-MM-JJ · NN · fait | en attente | sans objet | sautée | corrigée · <une phrase>`.
- Pour chaque étape, la dernière ligne du journal qui la nomme fait foi. `✓` : cette ligne dit `fait` ou `corrigée`
  et le fichier de l'étape existe. `s.o.` : elle dit `sans objet` ou `sautée` (l'étape n'est plus proposée, comme
  l'offre et le prix quand ils ne sont pas à revoir). `-` : aucune ligne, ou le fichier manque.
- `corrigée` : l'étape est refaite après une correction ; elle reste ✓ et la ligne dit ce qui a changé. `sautée` :
  la personne a choisi de passer ; la ligne dit pourquoi.
- `en attente` : l'étape est préparée, mais elle dépend d'un geste ou d'une réponse qui arrive hors de la conversation. La ligne du journal dit ce qu'on attend et de qui. L'état l'affiche `att.` avec ce texte : l'étape n'est pas `✓`, parce que préparé n'est pas fait. Le workflow s'arrête là et le dit ; il n'invente jamais la suite (ni réponse, ni résultat, ni geste qu'on ne lui a pas confirmé). Quand la personne apporte ce qui est arrivé, la ligne `fait` suit. Ici : les retours d'entretiens ou d'enquêtes (étape 1), la surveillance des concurrents, qui se joue dans la durée (étape 2), les validations de la personne (étapes 3 à 6) et les résultats, qui n'existent qu'après des semaines (étape 7).
- L'étape suivante est la première étape `-` ou `att.`, dans l'ordre (devant une étape `att.`, on demande d'abord où en est l'attente). Si aucune ne l'est, la stratégie est posée ; pour la
  revoir, on ajoute au journal une ligne `corrigée` pour chaque étape refaite.

**Une question n'est pas un ordre.** « Où en est ma stratégie marketing ? » : on donne l'état et la prochaine action,
puis on s'arrête. La commande du workflow, « continue » ou « déroule » : on enchaîne jusqu'à la première étape en attente, puis on s'arrête et on le dit.

**Une demande au milieu du chemin** (« écris mes messages ») : l'étape 3 exige les publics de l'étape 1. Sans
`01-marche-et-publics.md`, on fait d'abord un recueil court (documents existants, avis, entretiens), puis on positionne.

### 1. Lancer l'étape suivante

Lire l'étape dans `references/workflow.json`, appliquer sa règle de choix, invoquer la compétence retenue, écrire sa
sortie dans le fichier de l'étape, inscrire `fait` au journal (ou `en attente`, voir plus haut), puis passer à la suivante sans redemander. Une étape qui
a un manque le dit franchement, avec le geste qui le comble.

Le positionnement (étape 3) passe par `marketing-skills:marketing-council`, qui réunit des conseillers simulés dont
une spécialiste du positionnement : la simulation est déclarée et aucune citation n'est inventée. La veille concurrentielle (étape 2)
compare chaque semaine au relevé précédent et ne reporte que ce qui est neuf.

Deux étapes n'ont pas de compétence publique et se font à la main :

- **Le chiffrage du marché (étape 1).** On croise plusieurs sources indépendantes, on note pour chaque chiffre sa source
  et sa date, et on signale une source ancienne ou biaisée. Ce qui reste incertain s'écrit tel quel.
- **La carte du parcours client (étape 5).** On part des retours recueillis à l'étape 1 (entretiens, avis, forums) et de
  la mesure du site. On dessine les points de contact du premier signe à la fidélité, les frictions et leurs causes, et
  les améliorations classées. `operations:process-doc` aide à dessiner les étapes et les responsabilités, mais ne
  connaît pas le parcours client.

<!-- etapes:debut -->
| # | Étape | Compétences | Règle de choix |
|---|---|---|---|
| 1 | Étudier le marché et les publics | Valider le marché et parler aux utilisateurs : `marketing-skills:customer-research` | Les publics par marketing-skills:customer-research ; le marché par bmad-market-research, ou à la main ; deep-research quand l'étude demande beaucoup de sources croisées. Chaque chiffre a sa source et sa date ; une source ancienne ou biaisée se signale. |
| 2 | Surveiller les concurrents | Faire le dossier d'un concurrent : `marketing-skills:competitor-profiling` ; `marketing-skills:reverse-engineer-marketing` · Tenir la veille de la semaine : `marketing-skills:marketing-loops` ; `small-business:marketing-monday` ; `marketing-skills:ads` · Repérer les vidéos qui sortent du lot : `poser-sa-strategie-marketing:video-qui-sortent-du-lot` | Le premier relevé par competitor-profiling, puis la veille hebdomadaire par marketing-loops, diffusée au dirigeant par marketing-monday. Les publicités des concurrents passent par la veille de ads. Chaque changement se vérifie à sa source avant d'être diffusé. |
| 3 | Se positionner et écrire ses messages | Tenir le dossier de contexte marketing : `marketing-skills:product-marketing` · Formuler et contester le positionnement : `marketing-skills:marketing-council` | product-marketing recueille et tient les faits ; marketing-council formule le positionnement et le conteste. Faits et allégations se séparent ; la personne qui vend valide chaque allégation avant qu'elle serve. |
| 4 | Choisir l'offre et le prix (quand l'offre ou le prix est à revoir) | Construire l'offre et ses prix : `marketing-skills:pricing` ; `marketing-skills:offers` · Chiffrer l'offre dans un tableur : `document-skills:xlsx` | pricing pour un produit, offers pour un service ; chaque scénario chiffré dans un tableur. Aucune décision de prix ici : elle revient au dirigeant, avec la finance. |
| 5 | Cartographier le parcours client | Cartographier le parcours client : `operations:process-doc` | Les retours viennent du recueil de l'étape 1 (entretiens, avis, forums) ; les frictions chiffrées viennent de la mesure du site. La personne qui reçoit les clients valide la carte et sa mesure, avec le marketing et le produit. |
| 6 | Écrire le plan marketing et le faire décider | Écrire le plan marketing : `marketing-skills:marketing-plan` · Présenter le plan et faire trancher : `decider-une-strategie` ; `document-skills:pptx` | Le plan par marketing-plan ; la présentation dit la décision attendue en premier ; un arbitrage difficile passe par le workflow de décision. Le porteur du sujet valide chiffres, citations et diffusion. |
| 7 | Mesurer les résultats et décider la suite | Vérifier le suivi : `marketing-skills:analytics` · Relier les campagnes aux revenus : `marketing-skills:attribution` ; `poser-sa-strategie-marketing:marketing-relier-le-contenu-aux-contrats` · Faire le rapport : `marketing:performance-report` ; `small-business:growth-pulse` · Relire le résultat d'un changement : `poser-sa-strategie-marketing:marketing-relire-un-changement` | Le suivi d'abord (analytics), puis attribution ; performance-report pour l'équipe, growth-pulse pour le dirigeant. Un modèle d'attribution reste imparfait : le rapport le dit. |
<!-- etapes:fin -->

### 2. Clore un passage

À la fin de chaque séance, on écrit l'état (fait, reste, prochaine action) au journal. Si une compétence a déçu à une
étape, on le note aussi, pour rouvrir le choix de la compétence de cette étape.

## Ce qui se fait à la main

- **Le chiffrage du marché** (étape 1) : aucune compétence publique, il se fait à la main avec la règle de l'étape.
- **La cartographie du parcours client** (étape 5) : aucune compétence publique, elle se dessine à la main.
- **La décision finale** reste humaine : valider les allégations, trancher le prix, arbitrer le plan.

## Frontières

| Demande | Va à |
|---|---|
| Produire et diffuser du contenu sur LinkedIn | `/publier-sur-linkedin:publier-sur-linkedin` |
| Lancer une campagne ou un produit | `/lancer-un-produit:lancer-un-produit` |
| Une décision d'affaires difficile | `/decider-une-strategie:decider-une-strategie` |
| Cadrer un chantier encore flou | `/cadrer-un-chantier:cadrer-un-chantier` |
