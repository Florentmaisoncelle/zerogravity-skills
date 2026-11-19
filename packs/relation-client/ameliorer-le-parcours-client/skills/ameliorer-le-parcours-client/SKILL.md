---
name: ameliorer-le-parcours-client
description: >-
  Quand on veut améliorer l'expérience de ses clients de bout en bout (« exploite mes réponses NPS », « que disent mes
  avis ? », « quels clients vont partir ? », « transforme ces retours en priorités produit », « cartographie le parcours
  client », « où nos clients bloquent-ils ? ») → affiche l'état du cycle calculé depuis le dossier `parcours/`,
  puis déroule cinq étapes dans l'ordre : transformer la satisfaction en actions suivies, repérer les clients à risque,
  transformer les retours en priorités produit, cartographier le parcours et ses frictions, et, si les données sont
  sensibles, cadrer les autorisations avant toute automatisation. Ce qui manque est dit franchement. Se lance par
  `/ameliorer-le-parcours-client:ameliorer-le-parcours-client`. Déclencheurs : « NPS », « CSAT », « satisfaction
  client », « avis clients », « clients à risque », « voix du client », « retours clients », « parcours client »,
  « points de friction », « parcours sensible ». Pas pour le parrainage, le témoignage, le parcours d'annulation, l'offre
  de rétention ou la fidélité : `/fideliser-et-faire-recommander:fideliser-et-faire-recommander`. Pas pour répondre à un
  client : `/traiter-les-demandes-clients:traiter-les-demandes-clients`. Pas pour développer le chiffre chez un client en
  place : `/piloter-le-pipeline:piloter-le-pipeline`.
---

# Améliorer le parcours client, du retour du client à l'action suivie

## Ce que ça résout

Les entreprises collectent des retours (enquêtes, avis, tickets) et n'en font presque rien. Personne n'en est
responsable, les clients qui se taisent ne sont pas vus, les demandes de fonctionnalités s'empilent sans preuve. Sans
méthode, on résume les avis sans nommer de responsable, on confond un client qui se tait avec un client qui part, ou on
trace un parcours sans aucun retour de client.

Ici : l'ordre (le client parle d'abord, la carte du parcours vient des preuves), l'état, un choix tranché à chaque
étape, et les trous dits franchement.

**Résultat attendu** : chaque retour a un responsable, une action et une date ; la liste des clients à risque a son plan
de contact ; les priorités produit s'appuient sur des citations exactes ; une carte du parcours classe ses frictions.
Un dossier `parcours/` dit à tout moment où on en est, sans un seul nom de client dedans.

## Stratégie

1. **Une compétence par étape, la meilleure.** La table des étapes (plus bas) dit laquelle et pourquoi ; le détail de
   chaque étape (ce qu'elle rend, sa règle de choix, ce qui manque) est dans `references/workflow.json`.
2. **L'état d'abord, toujours calculé** depuis le journal et les fichiers du cycle en cours (`parcours/<AAAA-MM>/`),
   jamais recopié.
3. **L'ordre protège le client** : pas de priorité produit sans preuve vérifiée, pas de message de reprise qui vend,
   pas d'automatisation d'un parcours sensible avant la validation d'un spécialiste.
4. **Une seule validation, au début de l'étape 1** : le périmètre du cycle (quels retours, quelle période, quels
   clients, et si le parcours manipule des données sensibles). Ensuite tout se déroule. Restent à la personne : toute décision commerciale (remise, geste), tout arbitrage produit, toute
   publication de réponse à un avis, la validation du spécialiste d'un parcours sensible.
5. **Aucune donnée personnelle dans le dossier d'état.** Les clients s'y écrivent par un code (`K01`, `K02`…), les
   citations sans nom ; noms, adresses et dossiers sensibles (santé par exemple) restent dans l'outil du dirigeant
   (CRM, tableur), qui garde aussi la correspondance entre le code et le client. Ce workflow ne lit jamais cette
   correspondance. Pour un parcours sensible, le dossier ne reçoit que la structure du parcours (catégories de données,
   base légale, consentements, escalades), jamais le cas d'une personne.
   Le RGPD s'applique aux traitements d'un établissement dans l'UE et aux acteurs hors UE qui visent des personnes dans
   l'UE (CNIL, https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre1#Article3, vérifié le
   06/11/2026) ; ailleurs, les règles locales sont à vérifier.
6. **Les décisions se notent** dans le journal du cycle à chaque étape. Au début d'un nouveau cycle, on relit les
   dernières lignes du journal du cycle précédent : ce qui a coincé le mois dernier se prévoit ce mois-ci.

<!-- prerequis:debut -->
## Prérequis

Ce workflow s'appuie sur des compétences publiques, installées à part. Aucune n'est indispensable : si l'une manque, le workflow le dit et fait l'étape à la main. Faire l'étape à la main veut dire suivre sa règle de choix, écrire ce qu'elle doit rendre (dans le fichier de l'étape, ou dans la réponse quand le workflow n'a pas de dossier) et dire ce qui reste à la charge de la personne.

```text
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin install operations@knowledge-work-plugins
/plugin install product-management@knowledge-work-plugins
/plugin install sales@knowledge-work-plugins
/plugin install small-business@knowledge-work-plugins
```

Les workflows cités ici sont dans le même dépôt (le dépôt s'ajoute une fois : `/plugin marketplace add Florentmaisoncelle/zerogravity-skills`) :

```text
/plugin install accueillir-un-nouveau-client@zerogravity
/plugin install fideliser-et-faire-recommander@zerogravity
/plugin install piloter-le-pipeline@zerogravity
/plugin install traiter-les-demandes-clients@zerogravity
```
<!-- prerequis:fin -->

## Étapes

### 0. Le dossier, puis l'état (lecture seule)

**Le dossier.** Un cycle d'amélioration vit dans le dossier de l'entreprise : `parcours/` à sa racine, un sous-dossier
par cycle, nommé par son mois (`parcours/AAAA-MM/`), avec son propre journal et ses propres fichiers. Un second cycle
dans le même mois prend le suffixe `-2`. Dossier absent ou vide : il n'y a encore rien de fait, l'état est « étape 1 »
et le dossier se crée au premier passage. Si le dossier courant n'est pas celui de l'entreprise, le dire en une ligne
et demander où elle vit : rien ne s'écrit avant.

**Quel cycle ?** Par défaut, le plus récent qui n'est pas terminé ; ou celui que la personne nomme. Si tous sont
terminés, ou si elle demande un nouveau cycle, on crée le suivant et on repart à l'étape 1. Un cycle est terminé
quand les étapes 1 à 4 sont `✓` et l'étape 5 est `✓` ou `s.o.`.

**L'état**, calculé depuis le journal et les fichiers de `parcours/<AAAA-MM>/` (exemple inventé) :

```text
Cycle              2026-03 · retours de février
Étapes             01 ✓  02 ✓  03 -  04 -  05 s.o.
Retours            40 reçus · 5 thèmes · 40 affectés · 7 clos
Dernière décision  2026-03-12 · 02 · fait · liste des clients à risque et plan de contact
Étape suivante     03 Transformer les retours en priorités produit → product-management:synthesize-research
```

- Les compteurs « Retours » viennent du tableau de suivi écrit en tête de `01-satisfaction.md` (une ligne par retour :
  code, thème, responsable, action, date de clôture, statut ouvert ou clos). « Reçus » est le nombre de lignes,
  « affectés » celui des lignes qui ont un responsable, une action et une date, « clos » celui des lignes au statut
  clos. Le workflow met le statut à jour quand la personne lui dit qu'une action est close ; le journal ne le
  contredit pas.
- Le journal `parcours/<AAAA-MM>/journal.md` a une ligne par décision :
  `AAAA-MM-JJ · NN · fait | en attente | sans objet | sautée | corrigée · <une phrase>`.
- Pour chaque étape, la dernière ligne du journal qui la nomme fait foi. `✓` : cette ligne dit `fait` ou `corrigée` et
  le fichier de l'étape existe. `s.o.` : elle dit `sans objet` ou `sautée` (l'étape n'est plus proposée). `-` : aucune
  ligne, ou le fichier manque.
- `corrigée` : l'étape est refaite après une correction ; elle reste `✓` et la ligne dit ce qui a changé. `sautée` :
  la personne a choisi de passer ; la ligne dit pourquoi.
- L'étape 5 est optionnelle. À la validation du périmètre, la personne dit si le parcours manipule des données
  sensibles. Sinon, le journal reçoit tout de suite `AAAA-MM-JJ · 05 · sans objet · parcours sans donnée sensible`.
- `en attente` : l'étape est préparée, mais elle dépend d'un geste ou d'une réponse qui arrive hors de la conversation. La ligne du journal dit ce qu'on attend et de qui. L'état l'affiche `att.` avec ce texte : l'étape n'est pas `✓`, parce que préparé n'est pas fait. Le workflow s'arrête là et le dit ; il n'invente jamais la suite (ni réponse, ni résultat, ni geste qu'on ne lui a pas confirmé). Quand la personne apporte ce qui est arrivé, la ligne `fait` suit. Ici : les retours et les avis que la personne apporte (étapes 1 et 3), les validations du service client, du marketing et du produit (étape 4), l'avis du spécialiste pour un parcours sensible (étape 5).
- L'étape suivante est la première étape `-` ou `att.`, dans l'ordre (devant une étape `att.`, on demande d'abord où en est l'attente). Si aucune ne l'est, le cycle est terminé et on peut ouvrir
  le suivant.

**Une question n'est pas un ordre.** « Où en est l'amélioration de notre service ? » : on donne l'état et la prochaine
action, puis on s'arrête. La commande du workflow, « continue » ou « déroule » : on enchaîne jusqu'à la première étape en attente, puis on s'arrête et on le dit.

**Une demande au milieu du chemin** (« cartographie le parcours de nos clients ») : sans retours dans
`01-satisfaction.md` ni `03-retours.md`, on le dit. Une carte sans retour de client est une carte de l'organisation,
pas du parcours. On propose d'abord les retours disponibles, puis la carte.

### 1. Lancer l'étape suivante

Lire l'étape dans `references/workflow.json`, appliquer sa règle de choix, invoquer la compétence retenue, écrire sa
sortie dans le fichier de l'étape (sans nom de client), inscrire `fait` au journal (ou `en attente`, voir plus haut), puis passer à la suivante sans
redemander. Une étape qui a un manque le dit à la personne, avec le geste qui le comble (tenir le suivi de clôture dans
son outil, faire valider un parcours sensible).

L'étape 5 n'a aucune compétence publique : on la fait à la main, avec la même méthode que l'étape 4. On liste d'abord,
pour chaque point de contact, les catégories de données utilisées, leur base légale et le consentement requis, puis les
escalades et les conditions d'arrêt. On dresse enfin la liste des points qu'un spécialiste (juriste, délégué à la
protection des données, professionnel du métier concerné) doit valider avant toute automatisation. Le fichier
`05-sensible.md` décrit la structure du parcours, jamais le cas d'une personne.

<!-- etapes:debut -->
| # | Étape | Compétences | Règle de choix |
|---|---|---|---|
| 1 | Transformer la satisfaction en actions suivies | `small-business:review-reputation` | review-reputation lit et classe (thèmes, citations, réponses prêtes). Un retour sans responsable ni date n'est pas traité : l'étape finit quand chaque ligne a un nom, une action et une date de clôture. Une réclamation sensible et toute décision de rétention restent à une personne ; les réponses aux avis publics se valident avant publication. Avant tout, la personne valide le périmètre du cycle : quels retours, quelle période, quels clients, et si le parcours manipule des données sensibles (c'est l'unique validation du workflow). Le tableau de suivi (code, thème, responsable, action, date de clôture, statut ouvert ou clos) est écrit en tête du fichier de l'étape. Manque : L'affectation d'un responsable à chaque retour et le contrôle de clôture : aucune compétence publique ne tient ce suivi ; il se tient dans l'outil du dirigeant (CRM, tableau de tâches). |
| 2 | Repérer les clients à risque et préparer leur rétention | `sales:customer-health` · `sales:renewal-radar` · `small-business:reactivate` | customer-health pour un compte nommé sous contrat, reactivate pour une base de clients qui achètent à leur rythme (boutique, service récurrent) ; renewal-radar dit quand. Le premier contact reconnaît l'écart sans rien vendre. Les décisions commerciales (remise, geste, renégociation) restent au dirigeant. Le parcours d'annulation, les offres de rétention et la relance des paiements échoués sont dans /fideliser-et-faire-recommander:fideliser-et-faire-recommander (étape 3). |
| 3 | Transformer les retours des clients en priorités produit | `product-management:synthesize-research` · `sales:customer-voice` · `product-management:roadmap-update` | synthesize-research fait la synthèse ; customer-voice donne la parole exacte des clients quand les appels ou les e-mails sont lisibles ; roadmap-update seulement pour ce qui entre dans la feuille de route. Une demande sans preuve vérifiée n'entre pas. L'arbitrage produit reste humain. |
| 4 | Cartographier le parcours et corriger ses frictions | `operations:process-optimization` · `operations:process-doc` | Les retours viennent des étapes 1 et 3, les frictions chiffrées de la mesure (site, support) ; process-optimization cherche les pertes et propose l'état cible, process-doc dessine la carte. Le service client, le marketing et le produit valident la carte et sa mesure avant toute automatisation. Manque : aucune compétence publique ne cartographie un parcours client de bout en bout (moments, canaux, émotions, mesures, propriétaires) : la carte se dessine avec process-doc, les retours viennent des étapes 1 et 3. Même trou déclaré à l'étape « Cartographier le parcours client » de « Poser sa stratégie marketing ». |
| 5 | Cartographier un parcours sensible et ses autorisations (quand le parcours manipule des données sensibles (santé, données personnelles à protéger)) | à la main | Même méthode que l'étape 4, mais les catégories de données, la base légale et les consentements passent avant les points de contact, et rien ne s'automatise avant la validation du spécialiste (juriste, délégué à la protection des données, professionnel du métier concerné). Le fichier décrit la structure du parcours, jamais le cas d'une personne : aucune donnée personnelle dans le dossier d'état. Manque : aucune compétence publique ne fixe la base légale d'un traitement de données ni ne contrôle un parcours qui traite des données sensibles (de santé par exemple, comme un parcours de patient) : on le fait à la main, avec la règle de l'étape, et un spécialiste valide. |
<!-- etapes:fin -->

### 2. Clore un passage

À la fin de chaque séance, on écrit l'état (fait, reste, prochaine action) au journal. Si une compétence a déçu à une
étape, on le note aussi, pour rouvrir le choix de la compétence de cette étape.

## Ce qui manque

- **Le suivi de clôture des retours** : aucune compétence ne tient l'affectation d'un responsable à chaque retour ni le
  contrôle de clôture. Il se tient dans l'outil du dirigeant (CRM, tableau de tâches).
- **La cartographie d'un parcours client de bout en bout** (moments, canaux, émotions, mesures, propriétaires) : aucune
  compétence publique ne la couvre. `operations:process-optimization` cherche les pertes d'un processus et
  `operations:process-doc` dessine la carte, mais aucune ne recueille le vécu du client : les retours des étapes 1 et 3
  y suppléent.
- **La base légale d'un traitement de données** : aucune compétence publique ne la fixe ni ne contrôle un parcours qui
  traite des données sensibles (de santé par exemple). L'étape 5 se fait à la main, avec un spécialiste.

## Frontières

| Demande | Va à |
|---|---|
| Parrainage, témoignage, parcours d'annulation, offre de rétention, fidélité | `/fideliser-et-faire-recommander:fideliser-et-faire-recommander` |
| Répondre à un client, trier ses demandes | `/traiter-les-demandes-clients:traiter-les-demandes-clients` |
| Accueillir un client qui vient de signer | `/accueillir-un-nouveau-client:accueillir-un-nouveau-client` |
| Développer le chiffre chez un client en place | `/piloter-le-pipeline:piloter-le-pipeline` |
