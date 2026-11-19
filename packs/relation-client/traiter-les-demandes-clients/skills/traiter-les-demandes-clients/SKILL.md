---
name: traiter-les-demandes-clients
description: >-
  Quand on veut traiter les demandes de ses clients de bout en bout (« réponds à ce client », « trie mes e-mails
  clients », « un client demande un remboursement », « il me pose une question sur sa facture », « il veut résilier son
  abonnement », « il n'arrive plus à se connecter, escalade ») → affiche l'état calculé depuis le dossier
  `demandes/`, puis déroule six étapes dans l'ordre : trier et affecter, répondre sur une commande, répondre sur
  une facture ou un abonnement, résoudre ou escalader une demande technique, écrire la réponse et la faire valider,
  écrire l'article d'aide. Ce qui manque est dit franchement. Se lance par
  `/traiter-les-demandes-clients:traiter-les-demandes-clients`. Déclencheurs : « support client », « service client »,
  « ticket client », « SAV », « répondre à un client », « demande de remboursement », « question de facturation »,
  « résiliation d'abonnement », « escalade », « article d'aide ». Pas pour un prospect, un devis ou un rendez-vous :
  `/conclure-une-vente:conclure-une-vente`. Pas pour retenir un client qui part, ni pour un parrainage ou un
  témoignage : `/fideliser-et-faire-recommander:fideliser-et-faire-recommander`. Pas pour relancer les factures que des
  clients doivent : c'est de la comptabilité, à faire à la main ou avec un outil de facturation.
---

# Traiter les demandes clients, du premier message à la réponse validée

## Ce que ça résout

Une demande de client traverse six gestes. Sans méthode, on répond avant d'avoir lu la politique de retour, on promet un
remboursement que personne n'a approuvé, on transfère un bug à l'équipe technique sans contexte, ou on confond un
prospect avec un client.

Ici : l'ordre, l'état, un choix tranché à chaque étape, et les trous dits franchement, étape par étape.

**Résultat attendu** : chaque demande est classée et affectée, la réponse est validée et appuyée sur l'état réel de la
commande, de la facture ou de l'abonnement, l'escalade est qualifiée quand il le faut. Un dossier `demandes/`
dit à tout moment où on en est, sans un seul nom de client dedans.

## Stratégie

1. **Une compétence par étape, la meilleure.** La table des étapes (plus bas) dit laquelle et pourquoi ; le détail de
   chaque étape (ce qu'elle rend, sa règle de choix, ce qui manque) est dans `references/workflow.json`.
2. **L'état d'abord, toujours calculé** depuis le journal et les fichiers de la semaine en cours
   (`demandes/<AAAA-Sww>/`), jamais recopié.
3. **L'ordre protège le client** : pas de réponse avant la politique de retour, pas de remboursement sans un oui, pas
   d'escalade sans contexte, pas de promesse de date que l'équipe technique n'a pas donnée.
4. **Une seule validation, à l'étape 1 de la première semaine** : les règles de tri et la politique (retours,
   remboursements, délais promis), écrites dans `demandes/regles.md`. Ce fichier sert à toutes les semaines suivantes ;
   on ne le refait que si la politique change. Ensuite tout se déroule. Restent à la personne : approuver un
   remboursement, traiter une exception, décider d'une escalade critique, envoyer chaque message.
5. **Aucune donnée personnelle dans le dossier d'état.** Les demandes s'y écrivent par un code (`D01`, `D02`…, numéroté
   dans la semaine) ; noms, adresses, numéros de commande complets et cartes bancaires restent dans l'outil du
   dirigeant (boîte mail, boutique, outil de facturation), où la personne note le code sur la demande (étiquette,
   objet du fil) : c'est elle qui garde la correspondance, et ce workflow ne la lit jamais. Dans l'UE, le RGPD
   s'applique (il vise les traitements d'un établissement dans l'UE et les acteurs hors UE qui visent des personnes dans
   l'UE, CNIL, https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre1#Article3, vérifié le
   06/11/2026) : la base légale et la durée de conservation d'une demande se décident avec le dirigeant, pas avec la
   compétence. Ailleurs, les règles locales sont à vérifier.
6. **Les décisions se notent** dans le journal de la semaine à chaque étape. Au début d'une nouvelle semaine, on relit
   les dernières lignes du journal précédent : une réponse qui a coincé hier se prévoit aujourd'hui.

<!-- prerequis:debut -->
## Prérequis

Ce workflow s'appuie sur des compétences publiques, installées à part. Aucune n'est indispensable : si l'une manque, le workflow le dit et fait l'étape à la main. Faire l'étape à la main veut dire suivre sa règle de choix, écrire ce qu'elle doit rendre (dans le fichier de l'étape, ou dans la réponse quand le workflow n'a pas de dossier) et dire ce qui reste à la charge de la personne.

```text
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin install customer-support@knowledge-work-plugins
/plugin install sales@knowledge-work-plugins
/plugin install small-business@knowledge-work-plugins
```

Les workflows cités ici sont dans le même dépôt (le dépôt s'ajoute une fois : `/plugin marketplace add Gremelinn0/zerogravity-skills`) :

```text
/plugin install accueillir-un-nouveau-client@zerogravity
/plugin install ameliorer-le-parcours-client@zerogravity
/plugin install conclure-une-vente@zerogravity
/plugin install envoyer-des-e-mails@zerogravity
/plugin install fideliser-et-faire-recommander@zerogravity
```
<!-- prerequis:fin -->

## Étapes

### 0. Le dossier, puis l'état (lecture seule)

**Le dossier.** Les demandes d'une entreprise vivent dans le dossier de cette entreprise : `demandes/` à sa racine,
un sous-dossier par semaine de traitement, nommé par son numéro de semaine (`demandes/AAAA-Sww/`, par exemple
`demandes/2026-S45/`), avec son propre journal et ses propres fichiers. Un fichier commun, `demandes/regles.md`,
porte la politique de tri et de réponse pour toutes les semaines. Dossier absent ou vide : il n'y a encore rien de
fait, l'état est « étape 1 » et le dossier se crée au premier passage (l'étape 1 écrit alors d'abord `regles.md`).
Si le dossier courant n'est pas celui de l'entreprise, le dire en une ligne et demander où elle vit : rien ne
s'écrit avant.

**Quelle semaine ?** Par défaut, la plus récente qui n'est pas terminée ; ou celle que la personne nomme. Si toutes sont
terminées, ou si elle demande une nouvelle série de demandes, on crée la suivante (un second passage dans la même
semaine prend le suffixe `-2`) et on repart à l'étape 1. Une semaine est terminée quand chaque étape est `✓` ou `s.o.`.

**L'état**, calculé depuis le journal et les fichiers de `demandes/<AAAA-Sww>/` (exemple inventé) :

```text
Semaine            2026-S45
Règles             demandes/regles.md ✓ (validées le 2026-10-26)
Étapes             01 ✓  02 ✓  03 -  04 -  05 -  06 s.o.
Demandes           14 reçues · 9 répondues · 3 escaladées · 2 en attente de validation
Dernière décision  2026-11-04 · 02 · fait · demandes de commande traitées
Étape suivante     03 Répondre sur une facture ou un abonnement → à la main (voir small-business:ticket-deflector)
```

- Les compteurs « Demandes » viennent du tableau écrit en tête de `01-tri.md` (une ligne par demande : code,
  catégorie, priorité, personne ou file, statut). Chaque étape met à jour le statut des demandes qu'elle traite ; le
  journal ne le contredit pas. La ligne « Règles » vient de la première ligne de `regles.md` (« validées le <date> »).
- Le journal `demandes/<AAAA-Sww>/journal.md` a une ligne par décision :
  `AAAA-MM-JJ · NN · fait | en attente | sans objet | sautée | corrigée · <une phrase>`.
- Pour chaque étape, la dernière ligne du journal qui la nomme fait foi. `✓` : cette ligne dit `fait` ou `corrigée` et
  le fichier de l'étape existe. `s.o.` : elle dit `sans objet` ou `sautée` (l'étape n'est plus proposée : aucune
  demande de ce type cette semaine, ou l'étape 6 optionnelle). `-` : aucune ligne, ou le fichier manque.
- `corrigée` : l'étape est refaite après une correction ; elle reste `✓` et la ligne dit ce qui a changé. `sautée` :
  la personne a choisi de passer ; la ligne dit pourquoi.
- `en attente` : l'étape est préparée, mais elle dépend d'un geste ou d'une réponse qui arrive hors de la conversation. La ligne du journal dit ce qu'on attend et de qui. L'état l'affiche `att.` avec ce texte : l'étape n'est pas `✓`, parce que préparé n'est pas fait. Le workflow s'arrête là et le dit ; il n'invente jamais la suite (ni réponse, ni résultat, ni geste qu'on ne lui a pas confirmé). Quand la personne apporte ce qui est arrivé, la ligne `fait` suit. Ici : les demandes, qui arrivent hors de la conversation (étape 1), la validation de chaque réponse et son envoi par la personne (étape 5), la réponse du client (étapes 2 à 4) et la décision d'escalade (étape 4).
- L'étape suivante est la première étape `-` ou `att.`, dans l'ordre (devant une étape `att.`, on demande d'abord où en est l'attente). Si aucune ne l'est, la semaine est terminée et on peut en
  ouvrir une nouvelle.

**Une question n'est pas un ordre.** « Où en sont mes demandes clients ? » : on donne l'état et la prochaine action,
puis on s'arrête. La commande du workflow, « continue » ou « déroule » : on enchaîne jusqu'à la première étape en attente, puis on s'arrête et on le dit.

**Une demande au milieu du chemin** (« réponds à ce client, il veut un remboursement ») : sans `demandes/regles.md`, on
écrit d'abord la politique de retour et de remboursement avec le dirigeant, on la fait valider, puis on répond. Jamais
de réponse sans politique.

### 1. Lancer l'étape suivante

Lire l'étape dans `references/workflow.json`, appliquer sa règle de choix, invoquer la compétence retenue, écrire sa
sortie dans le fichier de l'étape (sans nom de client), inscrire `fait` au journal (ou `en attente`, voir plus haut), puis passer à la suivante sans
redemander. Une étape qui a un manque le dit à la personne, avec le geste qui le comble.

Trois étapes se font en partie à la main (elles écrivent quand même leur fichier, avec ce qui a été décidé et ce qui
attend la personne) :

- **Étape 3 (facture ou abonnement).** `small-business:ticket-deflector` lit la facture et les paiements, mais pas
  l'abonnement lui-même. On lit l'état de l'abonnement (échéance, pause, renouvellement, résiliation, paiement échoué)
  dans l'outil de facturation et on le colle dans la demande. On vérifie l'identité et le droit du demandeur avant de
  lire ou de changer quoi que ce soit, et le contrat avant toute résiliation.
- **Étape 4 (technique).** Seule l'escalade est outillée. Le diagnostic et la recherche de la procédure écrite se font
  à la main : résoudre quand une procédure et une action autorisée existent, escalader sinon.
- **Étape 5 (réponse).** Aucune compétence dédiée aux situations délicates (retard, refus, panne, silence, client
  mécontent). Le brouillon se fait avec les compétences des étapes 1 et 2, d'après les faits des étapes précédentes, et
  la personne le relit avant l'envoi.

<!-- etapes:debut -->
| # | Étape | Compétences | Règle de choix |
|---|---|---|---|
| 1 | Trier et affecter chaque demande | `small-business:inbox-manager` · `sales:account-context` · Trier une demande : `customer-support:ticket-triage` | small-business:inbox-manager trie la boîte ; sales:account-context attache le contexte du client avant toute réponse ; customer-support:ticket-triage donne la catégorie et la priorité de P1 à P4. Le résultat s'écrit dans un tableau en tête du fichier de l'étape (code, catégorie, priorité, personne ou file, statut). Un litige, un client en colère, une demande de remboursement hors règle, un sujet de sécurité ou de données personnelles se signale à une personne et ne reçoit aucune réponse automatique. Une demande qui est en réalité un prospect (devis, rendez-vous) part vers /conclure-une-vente:conclure-une-vente. Le dossier d'état ne porte aucun nom, aucune adresse ni aucun numéro de carte de client : des codes (D01, D02, etc.) ; la personne garde la correspondance dans sa boîte mail ou son outil de tickets. Si `demandes/regles.md` n'existe pas, on commence par l'écrire avec le dirigeant (politique de retour et de remboursement, délais promis, règles de tri) et on la fait valider : c'est l'unique validation du workflow, elle tombe ici, à l'étape 1 de la première semaine. Manque : le classement par catégorie (bug, comment faire, facturation, demande de fonctionnalité, sécurité), la priorité de P1 à P4, les règles d'aiguillage par équipe et la détection des doublons et des incidents connus : la compétence ticket-triage du plugin customer-support d'Anthropic (dépôt anthropics/knowledge-work-plugins) le fait, mais elle n'est pas installée. Commande : claude plugin install customer-support@knowledge-work-plugins. Une fois installée, elle se loge ici pour le classement, et inbox-manager garde le tri de la boîte. |
| 2 | Répondre sur une commande, un suivi ou un retour | `small-business:ticket-deflector` | ticket-deflector répond à toute demande qui touche une commande ou un paiement. La politique de retour s'écrit avant : aucune connexion ne la lit, la compétence la demande et refuse d'accorder ce qu'elle n'offre pas. En France, le droit de rétractation de 14 jours pour une vente à distance (Code de la consommation, L221-18) et la garantie légale de conformité s'ajoutent à la politique du dirigeant. Un remboursement, une contestation de paiement, un soupçon de fraude et une exception commerciale restent à une personne : la compétence les prépare, elle ne les exécute jamais seule. Pour un consommateur qui achète à distance en France ou dans l'UE, le droit de rétractation est de 14 jours (Code de la consommation, article L221-18, https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000032226842/ ; page grand public : https://www.service-public.gouv.fr/particuliers/vosdroits/F10485 ; vérifié le 06/11/2026). Il ne vaut pas, en principe, entre professionnels (l'article L221-3 l'étend à certains contrats conclus hors établissement avec un professionnel de moins de cinq salariés, hors de son activité principale). Il a des exceptions (article L221-28, https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000032226820, vérifié le 06/11/2026) : par exemple un service pleinement exécuté avant la fin du délai quand le consommateur l'a demandé et a reconnu perdre ce droit, un bien fabriqué sur mesure ou nettement personnalisé, un bien périssable, un contenu numérique sans support dont l'exécution a commencé avec son accord exprès ; lire la liste complète dans l'article. La garantie légale de conformité s'ajoute pour un bien vendu par un professionnel à un consommateur (défaut apparu dans les deux ans suivant la délivrance, https://www.service-public.gouv.fr/particuliers/vosdroits/F11094, vérifié le 06/11/2026). Depuis le 19/06/2026, la directive (UE) 2023/2673 impose aux vendeurs qui concluent des contrats à distance par une interface en ligne une fonction de rétractation « renoncer au contrat ici » (https://eur-lex.europa.eu/legal-content/FR/TXT/HTML/?uri=CELEX:32023L2673) : sa transposition en droit français et son périmètre exact sont à vérifier. Hors France et UE, ces règles ne s'appliquent pas telles quelles : à vérifier. |
| 3 | Répondre sur une facture ou un abonnement | à la main | ticket-deflector (étape 2) lit la facture, le paiement et ce qui a déjà été remboursé, et rédige la réponse. L'identité et le droit du demandeur à agir sur le compte se vérifient avant de lire ou de changer quoi que ce soit. Une règle tarifaire ne s'invente pas dans la conversation. Aucun débit, aucun remboursement et aucune modification comptable sans l'accord d'une personne. Un désaccord sur une facture remonte au dirigeant avec la pièce. Manque : L'état d'un abonnement (échéance, pause, renouvellement, résiliation, paiement échoué) : ticket-deflector lit les paiements et les remboursements, pas l'abonnement lui-même. La compétence customer-billing-ops du dépôt ECC (affaan-m/ECC, auteur reconnu) le fait avec Stripe : abonnements, remboursements limités aux prélèvements concernés, relance d'un paiement échoué, rétablissement du portail de facturation, vérification du contrat avant toute résiliation. Elle n'est pas dans la bibliothèque : à rapatrier dans ~/.claude/skills/customer-billing-ops (copie du dossier skills/customer-billing-ops du dépôt), puis à loger ici. En attendant, aucune compétence publique ne le lit : l'état de l'abonnement se lit dans l'outil de facturation et se colle dans la demande, un remboursement se limite aux prélèvements concernés, et le contrat se vérifie avant toute résiliation. |
| 4 | Résoudre ou escalader une demande technique | Escalader une demande : `customer-support:customer-escalation` | Résoudre quand une procédure écrite et une action autorisée existent ; escalader dès qu'il n'y en a pas, qu'un autre client signale la même chose, que le délai promis est dépassé ou que la sécurité est en jeu. Une escalade porte toujours le contexte du compte (étape 1) et ce qui a déjà été essayé. Ne jamais promettre une date de correction que l'équipe technique n'a pas donnée. customer-support:customer-escalation prépare l'escalade. Manque : diagnostiquer, retrouver la procédure ou l'incident connu, puis empaqueter l'escalade : trois compétences du plugin customer-support d'Anthropic le font. customer-research cherche dans toutes les sources avec un niveau de confiance par réponse ; customer-escalation fixe les niveaux d'escalade, rédige les étapes pour reproduire, chiffre l'impact et règle la cadence de suivi ; ticket-triage repère les doublons et les incidents connus. Le plugin n'est pas installé. Commande : claude plugin install customer-support@knowledge-work-plugins. Aucune compétence publique chargée aujourd'hui ne diagnostique une demande ni ne retrouve la procédure écrite : la recherche se fait à la main, le contexte du compte vient de sales:account-context (étape 1). Seule l'escalade est outillée. |
| 5 | Écrire la réponse et la faire valider | à la main | inbox-manager (étape 1) écrit les brouillons dans la voix du dirigeant ; ticket-deflector (étape 2) écrit ceux qui touchent une commande ou un paiement. Les faits viennent du dossier des étapes qui précèdent. Jamais un prix, une date ni un engagement que le dirigeant n'a pas pris. Rien ne part sans validation : l'envoi reste un clic de la personne. L'emailing marketing en volume n'est pas ici : /envoyer-des-e-mails:envoyer-des-e-mails. Manque : les situations délicates (annoncer un retard ou un refus, répondre à une panne, relancer après un silence, calmer un client mécontent) ont des modèles et une grille de ton dans draft-response, du plugin customer-support d'Anthropic ; le plugin n'est pas installé (commande à l'étape 1). Aucune autre compétence chargée ne les couvre : on écrit le brouillon à la main avec les deux compétences de la règle, et la personne le relit avant l'envoi. |
| 6 | Transformer les demandes résolues en articles d'aide (quand la même question revient) | Écrire un article d'aide : `customer-support:kb-article` | Un article par question qui revient, écrit d'après la solution qui a vraiment résolu la demande et non d'après la solution espérée. Aucune donnée d'un client précis dans l'article. Manque : la compétence kb-article du plugin customer-support d'Anthropic écrit l'article d'aide à partir d'une demande résolue (comment faire, dépannage, questions fréquentes, incident connu) et le structure pour la recherche ; le plugin n'est pas installé (commande à l'étape 1). Aucune autre compétence chargée ne le fait. Aucun cas d'usage n'est encore rédigé pour cette étape. |
<!-- etapes:fin -->

### 2. Clore un passage

À la fin de chaque séance, on écrit l'état (fait, reste, prochaine action) au journal. Si une compétence a déçu à une
étape, on le note aussi, pour rouvrir le choix de la compétence de cette étape.

## Ce qui manque

- **L'état d'un abonnement** (étape 3) : aucune compétence publique ne le lit, on le fait à la main avec l'outil de
  facturation.
- **Le diagnostic d'une demande technique** (étape 4) : aucune compétence publique ne diagnostique une demande de
  client. Le contexte du compte vient de `sales:account-context`, les doublons et incidents connus de
  `customer-support:ticket-triage`.
- **Les situations délicates** (étape 5) : aucune compétence publique dédiée, on rédige à la main et la personne valide.
- `small-business:ticket-deflector` n'est pas faite pour le droit d'un pays précis : la règle de l'étape 2 ajoute celui
  de la France et de l'UE pour les consommateurs.

## Frontières

| Demande | Va à |
|---|---|
| Un prospect, un devis, un rendez-vous commercial | `/conclure-une-vente:conclure-une-vente` |
| Retenir un client qui part, parrainage, témoignage, fidélité | `/fideliser-et-faire-recommander:fideliser-et-faire-recommander` |
| Accueillir un client qui vient de signer | `/accueillir-un-nouveau-client:accueillir-un-nouveau-client` |
| Améliorer la satisfaction, les retours et le parcours des clients | `/ameliorer-le-parcours-client:ameliorer-le-parcours-client` |
| Un emailing marketing en volume | `/envoyer-des-e-mails:envoyer-des-e-mails` |
