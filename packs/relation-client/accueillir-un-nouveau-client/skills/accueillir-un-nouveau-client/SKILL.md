---
name: accueillir-un-nouveau-client
description: >-
  Quand on veut accueillir un nouveau client de bout en bout (« un client vient de signer, comment on l'accueille ? »,
  « prépare l'onboarding de ce client », « il a payé, qu'est-ce qu'on lui envoie ? », « il n'a rien fait depuis une
  semaine ») → affiche l'état de l'accueil calculé depuis le dossier `accueil/`, puis déroule quatre étapes dans
  l'ordre : définir la première réussite et la checklist, ouvrir le parcours et préparer les accès, écrire le message de
  bienvenue, contrôler l'activation à sept et à trente jours. Les accès et la mise en service restent à une personne,
  et ce qui manque est dit franchement. Se lance par `/accueillir-un-nouveau-client:accueillir-un-nouveau-client`.
  Déclencheurs : « onboarding client », « accueillir un client », « nouveau client », « message de bienvenue »,
  « première réussite », « activation du client », « mise en route ». Pas pour accueillir un salarié :
  `/recruter:recruter`. Pas pour ses demandes courantes une fois accueilli :
  `/traiter-les-demandes-clients:traiter-les-demandes-clients`. Pas pour l'onboarding des utilisateurs d'un produit en
  ligne (inscription, premières sessions) : `marketing-skills:onboarding` directement.
---

# Accueillir un nouveau client, de la signature à la première réussite

## Ce que ça résout

Un client qui vient de signer attend qu'on le prenne par la main. La plupart des entreprises l'oublient : les accès
arrivent tard, le message de bienvenue s'écrit à la volée, et personne ne regarde si le client a vraiment commencé.
Sans méthode, on recopie la liste d'accueil d'un salarié ou une séquence d'e-mails de logiciel, sans savoir ce que le
client doit réussir en premier.

Ici : l'ordre (la première réussite avant la checklist), l'état, un choix tranché à chaque étape, et les gestes qui
restent à une personne (créer les accès, valider la mise en service).

**Résultat attendu** : pour chaque client, une première réussite écrite en une phrase, un parcours ouvert avec un
responsable par ligne, un message de bienvenue validé, un contrôle à sept et à trente jours. Un dossier
`accueil/` dit à tout moment où en est chaque client, sans un seul nom dedans.

## Stratégie

1. **Une compétence par étape, la meilleure.** La table des étapes (plus bas) dit laquelle et pourquoi ; le détail de
   chaque étape (ce qu'elle rend, sa règle de choix, ce qui manque) est dans `references/workflow.json`.
2. **L'état d'abord, toujours calculé** depuis les fichiers de `accueil/<code-client>/`, jamais recopié.
3. **L'ordre protège le client** : pas de checklist avant la première réussite, pas de message avant que les accès
   existent, pas de relance automatique sur un client qui n'a rien fait.
4. **Une seule validation, à l'étape 1** : la première réussite et la checklist d'accueil, validées par la personne
   avant que quoi que ce soit s'ouvre. Ensuite tout se déroule. Restent à la personne : créer les accès, valider les
   exceptions de droits, envoyer le message, décider de la relance d'un client bloqué.
5. **Aucune donnée personnelle dans le dossier d'état.** Les clients s'y écrivent par un code (`A01`, `A02`…) ;
   noms, adresses et accès restent dans l'outil du dirigeant (CRM, tableur), qui garde aussi la correspondance entre
   le code et le client (`A03` = telle société). Ce workflow ne lit jamais cette correspondance : la personne donne
   le code, le workflow ne le traduit pas.
6. **Les décisions se notent** dans le journal à chaque étape. Au début d'un nouvel accueil, on relit les dernières
   lignes du journal d'un accueil précédent : ce qui a coincé hier se prévoit aujourd'hui.

<!-- prerequis:debut -->
## Prérequis

Ce workflow s'appuie sur des compétences publiques, installées à part. Aucune n'est indispensable : si l'une manque, le workflow le dit et fait l'étape à la main. Faire l'étape à la main veut dire suivre sa règle de choix, écrire ce qu'elle doit rendre (dans le fichier de l'étape, ou dans la réponse quand le workflow n'a pas de dossier) et dire ce qui reste à la charge de la personne.

```text
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin marketplace add coreyhaines31/marketingskills
/plugin install marketing-skills@marketingskills
/plugin install operations@knowledge-work-plugins
```

Les workflows cités ici sont dans le même dépôt (le dépôt s'ajoute une fois : `/plugin marketplace add Gremelinn0/zerogravity-skills`) :

```text
/plugin install ameliorer-le-parcours-client@zerogravity
/plugin install conclure-une-vente@zerogravity
/plugin install recruter@zerogravity
/plugin install traiter-les-demandes-clients@zerogravity
```
<!-- prerequis:fin -->

## Étapes

### 0. Le dossier, puis l'état (lecture seule)

**Le dossier.** Un accueil vit dans le dossier de l'entreprise : `accueil/` à sa racine, un sous-dossier par client,
nommé par son code (`accueil/<code-client>/`, par exemple `accueil/A01/`). Dossier absent ou vide : c'est le premier
client, il n'y a encore rien de fait, l'état est « étape 1 » et le dossier se crée au premier passage. Si le dossier
courant n'est pas celui de l'entreprise, le dire en une ligne et demander où elle vit : rien ne s'écrit avant.

**Quel client ?** Par défaut, le client dont l'accueil est le plus récent et pas terminé ; ou celui que la personne
nomme par son code. Si tous les accueils sont terminés, ou si la personne annonce un nouveau client, on crée le code
suivant (`A01` pour le premier, puis `A02`…) et on repart à l'étape 1. Le code ne dit rien du client : la personne note
elle-même, dans son outil (CRM, tableur), quel client porte quel code.

**L'état**, calculé depuis le journal et les fichiers de `accueil/<code-client>/` (exemple inventé) :

```text
Client             A03 · signé le 2026-03-02
Première réussite  <une phrase, lue en tête de 01-reussite.md> · contrôles prévus le 2026-03-09 et le 2026-04-01
Étapes             01 ✓  02 ✓  03 -  04 -
Dernière décision  2026-03-03 · 02 · fait · accès créés, vérifiés la veille
Étape suivante     03 Écrire le message de bienvenue → marketing-skills:emails
```

- Le journal `accueil/<code-client>/journal.md` a une ligne par décision :
  `AAAA-MM-JJ · NN · fait | en attente | sans objet | sautée | corrigée · <une phrase>`.
- Pour chaque étape, la dernière ligne du journal qui la nomme fait foi. `✓` : cette ligne dit `fait` ou `corrigée` et
  le fichier de l'étape existe. `s.o.` : elle dit `sans objet` ou `sautée` (l'étape n'est plus proposée). `-` : aucune
  ligne, ou le fichier manque.
- `corrigée` : l'étape est refaite après une correction ; elle reste `✓` et la ligne dit ce qui a changé. `sautée` :
  la personne a choisi de passer ; la ligne dit pourquoi.
- `en attente` : l'étape est préparée, mais elle dépend d'un geste ou d'une réponse qui arrive hors de la conversation. La ligne du journal dit ce qu'on attend et de qui. L'état l'affiche `att.` avec ce texte : l'étape n'est pas `✓`, parce que préparé n'est pas fait. Le workflow s'arrête là et le dit ; il n'invente jamais la suite (ni réponse, ni résultat, ni geste qu'on ne lui a pas confirmé). Quand la personne apporte ce qui est arrivé, la ligne `fait` suit. Ici : les accès que le client doit ouvrir ou accepter (étape 2), l'envoi du message de bienvenue par la personne (étape 3), les contrôles à sept et à trente jours (étape 4).
- L'étape suivante est la première étape `-` ou `att.`, dans l'ordre (devant une étape `att.`, on demande d'abord où en est l'attente). Si aucune ne l'est, l'accueil de ce client est terminé et
  on peut ouvrir celui d'un nouveau client.
- L'étape 4 attend sa date : tant que le contrôle à sept jours n'est pas arrivé, elle reste `-` avec la mention « à
  venir le <date> » dans l'étape suivante. La signature, la première réussite et les deux dates de contrôle sont écrites
  en tête de `01-reussite.md` : c'est de là que l'état les lit.

**Une question n'est pas un ordre.** « Où en est l'accueil de ce client ? » : on donne l'état et la prochaine action,
puis on s'arrête. La commande du workflow, « continue » ou « déroule » : on enchaîne jusqu'à la première étape en attente, puis on s'arrête et on le dit.

**Une demande au milieu du chemin** (« envoie-lui un message de bienvenue ») : sans `01-reussite.md`, on définit
d'abord la première réussite en une phrase avec le dirigeant, puis on écrit le message autour d'elle. Jamais de
message de bienvenue sans savoir ce que le client doit réussir.

### 1. Lancer l'étape suivante

Lire l'étape dans `references/workflow.json`, appliquer sa règle de choix, invoquer la compétence retenue, écrire sa
sortie dans le fichier de l'étape (sans nom de client), inscrire `fait` au journal (ou `en attente`, voir plus haut), puis passer à la suivante sans
redemander. Une étape qui a un manque le dit à la personne, avec le geste qui le comble (créer les accès, valider la
mise en service).

L'étape 4 n'a aucune compétence publique : on la fait à la main, en deux contrôles écrits dans `04-activation.md`
(une section « à sept jours », une section « à trente jours »). Pour chacun : la première réussite de l'étape 1
est-elle atteinte (oui, non, en partie) ? Sur quoi s'appuie la réponse (une mesure d'activation définie à l'étape 1,
un fait constaté, pas une impression) ? Si elle ne l'est pas, quelle est la cause (accès manquant, client qui n'a pas
compris, objectif mal choisi, client indisponible) et quelle action, confiée à qui, avant toute relance ? Un client
qui n'a rien fait au bout d'une semaine se signale à son responsable : ce n'est pas un envoi automatique de plus. La
ligne `fait` du journal n'est écrite qu'après le contrôle à trente jours ; entre les deux, la section « à sept jours »
suffit à montrer où on en est. Quand l'accueil est terminé, on note l'état final au journal (fait, reste, prochaine
action) et le client passe au suivi régulier.

Les étapes 2 et 3 s'écrivent aussi quand elles s'arrêtent sur un geste humain : le fichier de l'étape dit alors ce
qui est prêt, ce qui attend la personne (créer un compte, valider un envoi) et qui s'en charge.

<!-- etapes:debut -->
| # | Étape | Compétences | Règle de choix |
|---|---|---|---|
| 1 | Définir la première réussite et la checklist d'accueil | `marketing-skills:onboarding` | Définir la première réussite avant d'ouvrir quoi que ce soit : tout ce qui n'y mène pas attend. Une réussite à la fois, pas dix. Si le parcours du client manipule des données sensibles (santé, données personnelles à protéger), cartographier d'abord ses données et ses consentements par /ameliorer-le-parcours-client:ameliorer-le-parcours-client (étape 5). C'est ici que tombe l'unique validation du workflow : la personne valide la première réussite et la checklist avant l'étape 2. On écrit en tête du fichier le code du client, sa date de signature, la première réussite en une phrase et les dates de contrôle à sept et à trente jours. |
| 2 | Ouvrir le parcours et préparer les accès | `operations:process-doc` | La checklist de l'étape 1 devient une procédure avec un responsable par ligne. Les accès se créent au plus juste et se vérifient la veille du premier contact. Les exceptions d'accès et la mise en service restent à une personne. Manque : créer les comptes, les droits et les espaces partagés dans les outils du dirigeant : aucune compétence publique ne le fait à sa place, et c'est préférable pour des accès. Le fichier de l'étape dit ce qui est prêt et ce qui attend la personne. |
| 3 | Écrire le message de bienvenue | `marketing-skills:emails` | Un seul message à la fois au début ; la séquence seulement si le client en a besoin sur plusieurs semaines. Le message est relu et validé avant l'envoi. Le consentement du client à recevoir des messages se vérifie avant toute séquence automatique. Un message qui sert l'exécution du contrat (accès, premier rendez-vous) n'est pas de la prospection ; une séquence de messages commerciaux suit les règles de l'e-mail de prospection (dans l'UE : consentement préalable d'un particulier, intérêt légitime pour un professionnel si le message touche à sa fonction, identité de l'expéditeur et moyen simple de refuser les envois suivants ; hors UE, à vérifier). |
| 4 | Contrôler l'activation et passer la main | à la main | Les mesures d'activation et la détection de ceux qui calent sont celles de l'étape 1 ; à sept et à trente jours on lit si la première réussite est atteinte, sinon on cherche la cause avant de relancer. Un client qui n'a rien fait au bout d'une semaine se signale à son responsable : ce n'est pas un envoi automatique de plus. L'accueil terminé, le client entre dans le suivi régulier : /traiter-les-demandes-clients:traiter-les-demandes-clients pour ses demandes, /ameliorer-le-parcours-client:ameliorer-le-parcours-client pour sa satisfaction. Deux contrôles écrits dans le fichier de l'étape, à sept et à trente jours : la première réussite de l'étape 1 est-elle atteinte (oui, non, en partie), sur quelle mesure, et sinon quelle est la cause et quelle action est confiée à qui avant toute relance. La ligne « fait » du journal n'est écrite qu'après le contrôle à trente jours. Manque : aucune compétence publique pour ce geste : il se fait à la main, avec la règle de l'étape. |
<!-- etapes:fin -->

### 2. Clore un passage

À la fin de chaque séance, on écrit l'état (fait, reste, prochaine action) au journal. Si une compétence a déçu à une
étape, on le note aussi, pour rouvrir le choix de la compétence de cette étape.

## Ce qui manque

- **Créer les comptes, les droits et les espaces partagés** dans les outils du dirigeant : aucune compétence ne le
  fait à sa place, et c'est préférable pour des accès. L'étape 2 documente la procédure, une personne l'exécute.
- **Le contrôle d'activation** (étape 4) : aucune compétence publique, il se fait à la main avec la règle ci-dessus.
- `marketing-skills:onboarding` est écrite pour l'accueil d'un utilisateur de logiciel. Pour un service rendu à un
  client, la « valeur » devient le premier livrable ou le premier résultat constaté : à vous d'adapter ses exemples.
- **Les messages de la séquence de bienvenue** (étape 3) : un message qui sert l'exécution du contrat (accès, date du
  premier rendez-vous) n'est pas de la prospection. Une séquence de messages commerciaux, elle, suit les règles de
  l'e-mail de prospection : dans l'UE, consentement préalable d'un particulier, intérêt légitime pour un professionnel
  si le message touche à sa fonction, avec l'origine des données, l'identité de l'expéditeur et un moyen simple de
  refuser les envois suivants (CNIL, page du 10/06/2026, vérifiée le 06/11/2026 :
  https://www.cnil.fr/fr/la-prospection-commerciale-par-courrier-electronique-sms-mms-et-automate-dappel). Hors UE, les
  règles sont à vérifier.

## Frontières

| Demande | Va à |
|---|---|
| Accueillir un salarié | `/recruter:recruter` |
| Les demandes courantes d'un client déjà accueilli | `/traiter-les-demandes-clients:traiter-les-demandes-clients` |
| Satisfaction, clients à risque, parcours | `/ameliorer-le-parcours-client:ameliorer-le-parcours-client` |
| Un prospect, un devis | `/conclure-une-vente:conclure-une-vente` |
