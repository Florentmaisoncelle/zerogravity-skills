---
name: envoyer-des-e-mails
description: >-
  Quand on veut envoyer des e-mails à ses inscrits (« une séquence de bienvenue », « des relances pour mes inscrits »,
  « écris ma newsletter », « mes e-mails arrivent en spam », « SPF DKIM DMARC », « des SMS de relance », « où en sont
  mes e-mails ? ») → affiche l'état calculé depuis le dossier `emails/<parcours>/`, puis déroule quatre étapes dans
  l'ordre : les parcours automatiques (avec le consentement et la désinscription), la newsletter, la délivrabilité,
  les SMS. Personne n'entre dans une liste sans une base légale écrite, et la fréquence se fixe avant le premier
  envoi. Le consentement, la newsletter et la délivrabilité n'ont pas de compétence publique : la méthode est dans ce
  workflow. Se lance par `/envoyer-des-e-mails:envoyer-des-e-mails`.
  Déclencheurs : « séquence d'e-mails », « nurturing », « newsletter », « consentement », « désinscription »,
  « délivrabilité », « SMS ».
  Pas pour la prospection directe : `/trouver-ses-prochains-clients:trouver-ses-prochains-clients`. Pas pour le
  lancement d'un produit : `/lancer-un-produit:lancer-un-produit`. Pas pour les clients qui partent ou qui recommandent :
  `/fideliser-et-faire-recommander:fideliser-et-faire-recommander`.
---

# Envoyer des e-mails : les parcours, la newsletter, la délivrabilité, les SMS

## Ce que ça résout

Les e-mails qui accompagnent les inscrits se perdent quand les parcours, la newsletter et les envois sont tenus à
part, sans consentement clair, sans désinscription simple et sans domaine authentifié. Ici : le consentement et la
désinscription, les parcours automatiques (accueil, relances, résiliation), la newsletter, la délivrabilité (SPF,
DKIM, DMARC, montée en volume) et les SMS.

**Résultat attendu** : une base légale écrite pour chaque liste, des parcours automatiques avec leurs délais, leurs
sorties et leur mesure, une newsletter tenue à rythme fixe, des e-mails qui arrivent, et des SMS de relance quand ils
se justifient.

## Stratégie

1. **Une compétence par étape quand il en existe une.** La table des étapes (plus bas) dit laquelle. Pour le
   consentement, la newsletter et la délivrabilité, aucune compétence publique n'existe : la méthode est écrite ici
   et dans `references/delivrabilite.md`. Les règles de choix sont aussi dans `references/workflow.json`.
2. **L'état d'abord, toujours calculé** depuis les fichiers de `emails/<parcours>/`, jamais recopié.
3. **L'ordre protège les destinataires.** Une base légale écrite avant tout message, la fréquence fixée avant le
   premier envoi, un domaine authentifié avant tout gros envoi. Sauter une étape reste possible sur demande ; le
   journal dit laquelle et pourquoi.
4. **Une seule validation, à l'étape 1** : le programme des parcours (messages, délais, fréquence), une fois la base
   légale posée. Ce n'est pas la première chose faite : le consentement vient avant. Ensuite tout se déroule. Restent
   à une personne : le recueil du consentement lui-même (il se fait dans le formulaire et l'outil d'envoi, pas ici),
   les réglages DNS (chez l'hébergeur du domaine) et la relecture avant chaque envoi.
5. **Tout texte qui sort au nom de l'entreprise** est relu et montré avant diffusion ; rien ne part sans validation.
6. **Les décisions se notent** dans le journal, avec ce qu'on a appris d'un envoi à l'autre : quelques lignes
   suffisent.

<!-- prerequis:debut -->
## Prérequis

Ce workflow s'appuie sur des compétences publiques, installées à part. Aucune n'est indispensable : si l'une manque, le workflow le dit et fait l'étape à la main. Faire l'étape à la main veut dire suivre sa règle de choix, écrire ce qu'elle doit rendre (dans le fichier de l'étape, ou dans la réponse quand le workflow n'a pas de dossier) et dire ce qui reste à la charge de la personne.

```text
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin marketplace add coreyhaines31/marketingskills
/plugin install marketing-skills@marketingskills
/plugin install marketing@knowledge-work-plugins
```

Les workflows cités ici sont dans le même dépôt (le dépôt s'ajoute une fois : `/plugin marketplace add Florentmaisoncelle/zerogravity-skills`) :

```text
/plugin install fideliser-et-faire-recommander@zerogravity
/plugin install lancer-un-produit@zerogravity
/plugin install publicite-payante@zerogravity
/plugin install trouver-ses-prochains-clients@zerogravity
```
<!-- prerequis:fin -->

## Étapes

### 0. Le dossier, puis l'état (lecture seule)

**Le dossier.** Un sous-dossier par parcours d'e-mails (une liste, ou une série : `emails/bienvenue/`,
`emails/newsletter/`), à la racine du dossier de l'entreprise. Dossier absent ou vide : il n'y a encore rien de
fait, l'état est « étape 1 » et le dossier se crée au premier passage. Si le dossier courant n'est pas celui de
l'entreprise, le dire en une ligne et demander où il vit : rien ne s'écrit avant. Les adresses et les noms des
inscrits restent dans l'outil d'envoi : le dossier ne contient que des règles, des textes et des chiffres.

**L'état**, calculé depuis le journal et les fichiers :

```text
Parcours           bienvenue
Étapes             01 ✓  02 s.o.  03 -  04 -
Dernière décision  2026-11-06 · 02 · sans objet · pas de newsletter dans ce parcours
Étape suivante     03 Soigner la délivrabilité
```

- Le journal `emails/<parcours>/journal.md` a une ligne par décision :
  `AAAA-MM-JJ · NN · fait | en attente | sans objet | sautée | corrigée · <une phrase>`.
- Pour chaque étape, la dernière ligne du journal qui la nomme fait foi. `✓` : cette ligne dit `fait` ou `corrigée`
  et le fichier de l'étape existe. `s.o.` : elle dit `sans objet` ou `sautée` (l'étape n'est plus proposée). `-` :
  aucune ligne, ou le fichier manque.
- `corrigée` : l'étape est refaite après une correction ; elle reste ✓ et la ligne dit ce qui a changé. `sautée` :
  la personne a choisi de passer ; la ligne dit pourquoi.
- `en attente` : l'étape est préparée, mais elle dépend d'un geste ou d'une réponse qui arrive hors de la conversation. La ligne du journal dit ce qu'on attend et de qui. L'état l'affiche `att.` avec ce texte : l'étape n'est pas `✓`, parce que préparé n'est pas fait. Le workflow s'arrête là et le dit ; il n'invente jamais la suite (ni réponse, ni résultat, ni geste qu'on ne lui a pas confirmé). Quand la personne apporte ce qui est arrivé, la ligne `fait` suit. Ici : la publication des réglages du domaine chez l'hébergeur (étape 3), l'envoi des premiers messages par la personne (étapes 1 et 2), les quatre numéros qu'il faut mesurer avant de changer le rythme (étape 2) et l'accord des inscrits pour les SMS (étape 4).
- L'étape suivante est la première étape `-` ou `att.`, dans l'ordre (devant une étape `att.`, on demande d'abord où en est l'attente). Si aucune ne l'est, le parcours est terminé, et on peut
  ouvrir un nouveau parcours (nouveau sous-dossier, retour à l'étape 1).
- **Plusieurs parcours.** Le parcours par défaut est le plus récent qui n'est pas terminé, ou celui que la personne
  nomme. Le domaine d'envoi est le même pour tous : au deuxième parcours, l'étape 3 écrit une note courte (« domaine
  déjà authentifié le ..., dans `emails/<premier parcours>/03-delivrabilite.md` ; nouveau test fait ») et refait
  seulement le test d'envoi à soi-même.

**Une question n'est pas un ordre.** « Où en sont mes e-mails ? » : on donne l'état et la prochaine action, puis on
s'arrête. La commande du workflow, « continue » ou « déroule » : on enchaîne jusqu'à la première étape en attente, puis on s'arrête et on le dit.

**Une demande au milieu du chemin** (« écris ma séquence de bienvenue ») : l'étape 1 marche seule, mais la base
légale de la liste d'abord ; personne n'y entre sans elle.

### 1. Lancer l'étape suivante

Lire l'étape dans `references/workflow.json`, appliquer sa règle de choix, invoquer la compétence retenue (ou suivre
la méthode ci-dessous quand il n'y en a pas), écrire la sortie dans le fichier de l'étape, inscrire la ligne au
journal (`fait` ou `en attente`, voir plus haut), puis passer à la suivante sans redemander.

<!-- etapes:debut -->
| # | Étape | Compétences | Règle de choix |
|---|---|---|---|
| 1 | Écrire les parcours automatiques | Écrire les parcours automatiques : `marketing:email-sequence` ; `marketing-skills:emails` | emails pour le programme, les textes et les sorties de chaque séquence. Le consentement et la désinscription se posent avant le premier message : personne n'entre dans une séquence sans une base légale écrite pour sa liste (consentement pour un particulier, intérêt légitime avec information et opposition pour un professionnel, selon la CNIL en France ; hors de France, à vérifier). La fréquence se fixe avant le premier envoi. |
| 2 | Tenir la newsletter | Écrire la newsletter : à la main · Recueillir le consentement : à la main | Personne ne reçoit la newsletter sans consentement, et la fréquence se fixe avant le premier envoi. Une newsletter n'est envoyée qu'aux personnes de la liste posée à l'étape 1, avec le lien de désinscription dans chaque numéro. Le rythme se fixe avant le premier envoi et ne change qu'après quatre numéros mesurés. Sans newsletter dans ce parcours, l'étape est sans objet. |
| 3 | Soigner la délivrabilité | Tester les objets et nettoyer la liste : à la main | On teste l'objet et on nettoie la liste avant un gros envoi. Aucun gros envoi tant que SPF, DKIM et DMARC ne répondent pas « pass » sur un message de test. Un domaine neuf monte en volume par paliers. La liste de suppression (désinscrits, plaintes, adresses en échec définitif) ne se réimporte jamais. |
| 4 | Envoyer des SMS (quand les inscrits ont donné leur numéro et leur accord) | Écrire les SMS : `marketing-skills:sms` | Le SMS se réserve aux messages urgents, avec consentement. Un accord distinct de celui de l'e-mail, l'expéditeur nommé et la mention pour refuser (« STOP ») dans chaque message, des heures de jour (pas de nuit, de dimanche ni de jour férié, plages exactes à vérifier auprès de la plateforme d'envoi). Les messages urgents ou utiles d'abord ; la compétence est écrite surtout pour les États-Unis, donc ses règles de droit ne s'appliquent pas telles quelles en France. |
<!-- etapes:fin -->

### 2. La méthode, étape par étape

#### Étape 1 : le consentement, la désinscription, puis les parcours

**D'abord la base légale de chaque liste**, écrite dans `01-parcours.md` (une ligne par liste). Elle dépend de qui est
la personne. Ce qui suit vient de la CNIL et vaut pour la France ; hors de France, y compris dans le reste de l'Union européenne, les
règles sont à vérifier pour le pays des destinataires.

| Qui reçoit | Ce qu'il faut | Comment le garder |
|---|---|---|
| Un particulier | Son accord avant le premier message : libre, précis, éclairé, explicite. Case non pré-cochée ; des conditions générales acceptées ne suffisent pas. Exception : un client existant, pour des produits ou services similaires à ceux qu'il a achetés, à condition qu'il ait pu refuser dès la collecte et à chaque envoi. Un simple compte sans achat ne suffit pas. | Date, source (quel formulaire, quelle page) et texte exact affiché au moment de l'accord, dans l'outil d'envoi ou un tableur |
| Un professionnel | Un message en rapport avec sa fonction (intérêt légitime), une information sur l'origine de ses coordonnées et sur son droit de s'opposer, un moyen simple et gratuit de refuser | La source de l'adresse et la date du premier contact |
| Dans tous les cas | L'émetteur identifiable dans le message et un moyen simple de refuser les envois suivants | Le lien de désinscription dans chaque message |

Source : CNIL, https://www.cnil.fr/fr/la-prospection-commerciale-par-courrier-electronique-sms-mms-et-automate-dappel
(vérifié le 06/11/2026). Les adresses génériques d'une entreprise (contact@, info@) ne suivent pas ces règles de la
même façon : la page ci-dessus précise le cas. Ceci n'est pas un avis juridique : en cas de doute (liste achetée,
fichier ancien, activité réglementée), demander à un juriste.

**Ensuite la désinscription**, avant d'écrire le moindre message : un lien visible dans chaque message, un clic, aucune
connexion ni question ; les entêtes d'un clic ajoutés par l'outil d'envoi ; une liste de suppression (désinscrits,
plaintes, adresses en échec définitif) qui ne se réimporte jamais ; un traitement immédiat, sous 48 heures au plus.
Le détail et le test sont dans `references/delivrabilite.md`. Écrire dans `01-parcours.md` où se trouve la liste de
suppression.

**Enfin les parcours**, avec `marketing-skills:emails`. Pour chaque séquence, le fichier note : l'événement qui fait
entrer (inscription, achat, abandon), le nombre de messages, le délai entre chacun, ce qui fait sortir (achat, réponse,
désinscription), la fréquence maximale par personne et par semaine, et la mesure (clics, réponses, désinscriptions
par message). Critère de réussite : une personne ne reçoit jamais deux séquences en même temps, et chaque séquence a
une sortie. Après le premier mois, une séquence dont les désinscriptions dépassent celles des autres séquences se
raccourcit ou s'espace.

#### Étape 2 : la newsletter

Faire écrire dans `02-newsletter.md` :

1. **La promesse** en une phrase : pour qui, quoi, à quel rythme (« chaque jeudi, un conseil pour ... »).
2. **Le rythme**, fixé avant le premier envoi : hebdomadaire, tous les quinze jours ou mensuel. Un rythme tenu vaut
   mieux qu'un rythme ambitieux.
3. **Un format fixe** : un sujet principal, trois liens ou idées au plus, un seul appel à l'action. La personne doit
   savoir ce qu'elle trouve avant d'ouvrir.
4. **Les quatre prochains numéros** en une ligne chacun, pour ne jamais partir d'une page blanche. Les idées
   viennent des questions réellement posées par les clients.
5. **La mesure**, relue après quatre numéros : clics, réponses reçues, désinscriptions par numéro. Décision : si les
   désinscriptions montent d'un numéro à l'autre, réduire la fréquence ou resserrer le sujet ; si les clics sont
   faibles, changer le sujet principal avant de changer le format.

Pas de newsletter dans ce parcours : l'étape est « sans objet » au journal. Chaque numéro est relu et validé avant
l'envoi.

#### Étape 3 : la délivrabilité

Suivre `references/delivrabilite.md`, dans l'ordre : domaine d'envoi, publication de SPF et DKIM, DMARC en
observation (`p=none`), test d'envoi à soi-même, puis durcissement quand tout passe. Écrire dans `03-delivrabilite.md` :
le domaine d'envoi, la date de chaque enregistrement publié, le résultat du test (`PASS` ou `FAIL` pour SPF, DKIM,
DMARC), le plan de montée en volume avec ses paliers, et la date du prochain nettoyage de liste. Ensuite le test
d'objet : deux objets, deux moitiés tirées au hasard, décision sur les clics seulement si l'écart se répète sur deux
envois. Critère de réussite : trois « pass » sur un message réel, et aucun gros envoi avant.

#### Étape 4 : les SMS (optionnelle)

À faire seulement si les inscrits ont donné leur numéro **et** un accord propre au SMS (un accord pour l'e-mail ne
couvre pas le SMS). Mêmes principes qu'en France pour l'e-mail (CNIL, page ci-dessus, vérifiée le 06/11/2026) :
accord préalable d'un particulier, intérêt légitime pour un professionnel avec information et refus possible,
expéditeur identifiable. Pour chaque SMS :

- le nom de l'entreprise au début du message ;
- un moyen gratuit de refuser dans le message, en pratique la mention « STOP » suivie du mot ou du numéro à utiliser ;
- des heures de jour : pas de nuit, ni de dimanche, ni de jour férié. Les plages exactes imposées en France
  (opérateurs, charte professionnelle) ne sont pas fixées par la CNIL et les sources consultées divergent : à
  vérifier auprès de la plateforme d'envoi choisie ;
- un message court (environ 160 caractères, moins avec certains accents et émojis), un seul appel à l'action.

La compétence `marketing-skills:sms` aide à écrire les messages et à choisir entre SMS et e-mail. Elle est écrite
surtout pour les États-Unis (règles TCPA, enregistrement des numéros 10DLC) : ne pas appliquer ses règles de droit et
d'heures en France. Le SMS n'est pas réservé aux urgences : il sert quand l'immédiateté compte (rappel de rendez-vous,
suivi de livraison, relance d'un panier). Critère de réussite : le taux de désinscription par SMS reste bas ; une
hausse, c'est un envoi trop fréquent ou mal ciblé.

### 3. Clore un passage

À la fin de chaque séance, on écrit l'état (fait, reste, prochaine action) au journal. Si une compétence a déçu à une
étape, on le note aussi, pour rouvrir le choix de la compétence de cette étape.

## Ce qui se fait à la main

Aucune compétence publique ne couvre le consentement, la newsletter ni la délivrabilité : ces trois gestes suivent la
méthode ci-dessus. Les réglages DNS et le recueil du consentement dans les formulaires se font chez l'hébergeur du
domaine et dans l'outil d'envoi.

## Frontières

| Demande | Va à |
|---|---|
| Les messages de prospection | à la main, ou `/trouver-ses-prochains-clients:trouver-ses-prochains-clients` pour la prospection directe jusqu'au rendez-vous |
| Le lancement d'un produit | `/lancer-un-produit:lancer-un-produit` |
| Quand un contact entre et sort d'un parcours dans le CRM, le score, la règle de passage à la vente | à la main, dans l'outil de CRM : ce workflow écrit les messages, pas ces règles |
| La publicité payante | `/publicite-payante:publicite-payante` |
| Les clients qui partent ou qui recommandent | `/fideliser-et-faire-recommander:fideliser-et-faire-recommander` |
