---
name: conclure-une-vente
description: >-
  Quand on veut conclure une vente de bout en bout, de la demande jusqu'à la signature (accueillir une demande entrante, préparer un rendez-vous, écrire le compte rendu d'un appel, chiffrer une proposition, répondre à une objection, mener jusqu'à la signature) → affiche l'état de l'affaire calculé depuis le dossier `affaires/<affaire>/`, puis déroule neuf étapes dans l'ordre : la demande entrante, la préparation, le compte rendu et le CRM, la recommandation, l'offre, la proposition chiffrée, les objections, la signature, la commande. Ce qui manque est dit franchement (recommander un produit dans un catalogue, monter la proposition complète, transformer une demande en commande). Se lance par `/conclure-une-vente:conclure-une-vente`. Déclencheurs : « conclure une vente », « préparer un rendez-vous client », « compte rendu d'appel », « devis », « proposition commerciale », « il hésite sur le prix », « comment faire signer cette affaire », « où en est cette affaire », « demande entrante ». Pas pour trouver des prospects : `/trouver-ses-prochains-clients:trouver-ses-prochains-clients`. Pas pour la revue du pipeline : `/piloter-le-pipeline:piloter-le-pipeline`.
---

# Conclure une vente, de la demande à la signature

## Ce que ce workflow résout

Une affaire se perd souvent par manque de suite : un compte rendu jamais écrit, un CRM (le logiciel ou le tableur où l'on note ses contacts et ses affaires) qui ne dit plus rien, un devis improvisé, une objection laissée sans réponse, une date de signature qui glisse. Des compétences existent pour chaque geste, mais elles ne disent ni l'ordre ni laquelle prendre. Ici : l'ordre, l'état de l'affaire, un choix tranché à chaque étape, et les trous dits franchement.

**Résultat attendu** : une affaire suivie de la demande à la signature. Une fiche par rendez-vous, un compte rendu sourcé et le CRM à jour, une offre et une proposition chiffrées sans tarif inventé, les objections traitées, un plan daté jusqu'au oui. Un dossier `affaires/<affaire>/` par affaire, qui dit à tout moment où on en est.

## Stratégie

1. **L'état d'abord**, toujours calculé depuis les fichiers de `affaires/<affaire>/`, jamais recopié.
2. **Un choix par étape.** Chaque étape a sa compétence par défaut et sa règle de choix, dans la table plus bas, qui vient de `references/workflow.json`.
3. **L'ordre protège la décision** : pas de devis sans offre, pas d'offre sans compte rendu, pas d'écriture du CRM sans accord. Sauter une étape reste possible sur demande ; le journal dit laquelle et pourquoi.
4. **Une validation de fond, à l'étape 5.** Le dirigeant valide l'offre (promesses, conditions et prix) avant tout chiffrage. Ce n'est pas la première étape : les étapes 1 à 4 ne produisent que des notes et des brouillons. Ensuite le travail se déroule. Restent toujours à la personne qui vend : mener le rendez-vous, accepter chaque écriture dans le CRM, envoyer chaque message et chaque proposition, signer.
5. **Tout texte qui sort au nom de l'entreprise** est relu avant d'être montré, et rien ne part sans validation.
6. **Chaque passage se clôt au journal** : ce qui est fait, ce qui reste, la prochaine action.

<!-- prerequis:debut -->
## Prérequis

Ce workflow s'appuie sur des compétences publiques, installées à part. Aucune n'est indispensable : si l'une manque, le workflow le dit et fait l'étape à la main. Faire l'étape à la main veut dire suivre sa règle de choix, écrire ce qu'elle doit rendre (dans le fichier de l'étape, ou dans la réponse quand le workflow n'a pas de dossier) et dire ce qui reste à la charge de la personne.

```text
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin marketplace add coreyhaines31/marketingskills
/plugin install legal@knowledge-work-plugins
/plugin install marketing-skills@marketingskills
/plugin install operations@knowledge-work-plugins
/plugin install sales@knowledge-work-plugins
/plugin install small-business@knowledge-work-plugins
```

Les workflows cités ici sont dans le même dépôt (le dépôt s'ajoute une fois : `/plugin marketplace add Florentmaisoncelle/zerogravity-skills`) :

```text
/plugin install organiser-sa-force-de-vente@zerogravity
/plugin install piloter-le-pipeline@zerogravity
/plugin install trouver-ses-prochains-clients@zerogravity
```
<!-- prerequis:fin -->

## Étapes

### 0. Le dossier, puis l'état (lecture seule)

**Le dossier.** Une affaire, un dossier : `affaires/<affaire>/`, nommé d'après l'entreprise cliente et le mois (par exemple `affaires/boulangerie-2026-11/`), avec son propre journal. Il porte l'entreprise cliente, les rôles et les décisions ; les noms et coordonnées des personnes restent dans le CRM : le dossier n'en garde aucun, mais les compétences appelées peuvent lire le CRM et y écrire (`sales:call-prep`, `sales:log-activity` à l'étape 3, après accord). Dossier absent ou vide : il n'y a encore rien de fait, l'état est « étape 1 » et le dossier se crée au premier passage. Plusieurs affaires : on travaille sur la plus récente qui n'est pas terminée, ou sur celle que la personne nomme ; si toutes sont terminées, ou si elle demande une nouvelle affaire, on crée le dossier suivant et on repart à l'étape 1. Si le dossier courant n'est pas celui de l'entreprise qui vend, le dire en une ligne et demander où il vit : rien ne s'écrit avant.

**L'état**, calculé depuis le journal et les fichiers de l'affaire :

```text
Affaire            <entreprise cliente> · <montant visé>
Étapes             01 s.o.  02 ✓  03 ✓  04 s.o.  05 -  06 -  07 -  08 -  09 -
Dernière décision  <date> · 04 · sans objet · un seul produit possible
Étape suivante     05 Construire l'offre → marketing-skills:offers
```

- Le journal `affaires/<affaire>/journal.md` a une ligne par décision : `AAAA-MM-JJ · NN · fait | en attente | sans objet | sautée | corrigée · <une phrase>`.
- Pour chaque étape, la dernière ligne du journal qui la nomme fait foi. `✓` : cette ligne dit `fait` ou `corrigée` et le fichier de l'étape existe. `s.o.` : elle dit `sans objet` ou `sautée` (l'étape n'est plus proposée). `-` : aucune ligne, ou le fichier manque.
- `corrigée` : l'étape est refaite après une correction ; elle reste ✓ et la ligne dit ce qui a changé. `sautée` : la personne a choisi de passer ; la ligne dit pourquoi.
- `en attente` : l'étape est préparée, mais elle dépend d'un geste ou d'une réponse qui arrive hors de la conversation. La ligne du journal dit ce qu'on attend et de qui. L'état l'affiche `att.` avec ce texte : l'étape n'est pas `✓`, parce que préparé n'est pas fait. Le workflow s'arrête là et le dit ; il n'invente jamais la suite (ni réponse, ni résultat, ni geste qu'on ne lui a pas confirmé). Quand la personne apporte ce qui est arrivé, la ligne `fait` suit. Ici : la demande du prospect (étape 1), le rendez-vous lui-même (étapes 2 et 3), la réponse du client à la proposition et à ses objections (étapes 6 et 7), la signature (étape 8) et la confirmation écrite du client (étape 9).
- L'étape suivante est la première étape `-` ou `att.`, dans l'ordre (devant une étape `att.`, on demande d'abord où en est l'attente). Si aucune ne l'est, l'affaire est terminée, et on peut en ouvrir une autre.
- Les étapes 1, 4 et 9 sont optionnelles : quand elles ne s'appliquent pas, on les marque `sans objet` au journal et on écrit une note d'une ligne dans leur fichier.

**Une question n'est pas un ordre.** « Où en est cette affaire ? » : on affiche l'état et la prochaine action, puis on s'arrête. « Conclure cette vente », « continue » ou « déroule » : on enchaîne jusqu'à la première étape en attente, puis on s'arrête et on le dit.

**Une demande au milieu du chemin** (« fais-moi le devis »). L'étape 6 exige l'offre de l'étape 5. Sans offre validée dans `05-offre.md`, on écrit d'abord l'offre courte (périmètre, livrables, conditions), on la fait valider, puis on chiffre. Jamais un devis sans offre validée.

### 1. Lancer l'étape suivante

Lire l'étape dans la table, appliquer sa règle de choix, invoquer la compétence retenue, écrire sa sortie dans le fichier de l'étape, inscrire « fait » au journal (ou `en attente`, voir plus haut), puis passer à la suivante sans redemander. Une étape qui porte un « Manque » le dit franchement, avec le geste humain qui le comble ; une étape qui demande une décision attend cette décision.

<!-- etapes:debut -->
| # | Étape | Compétences | Règle de choix |
|---|---|---|---|
| 1 | Accueillir une demande entrante (quand le prospect vient de lui-même (formulaire, email, appel)) | Répartir les leads : `sales:route-lead` · Accueillir une demande entrante : `small-business:speed-to-lead` ; `sales:lead-triage` ; `sales:schedule-meeting` | speed-to-lead tient la demande de bout en bout ; la priorité se lit dans la grille de lead-triage ; route-lead seulement quand plusieurs personnes vendent. Le consentement de la personne qui écrit se vérifie avant toute relance. |
| 2 | Préparer le rendez-vous | `sales:call-prep` | Une fiche par rendez-vous, depuis le CRM et les échanges passés ; un fait sans source s'écrit « non vérifié ». Pour la semaine entière, on refait la fiche pour chaque rendez-vous, dans l'ordre de l'agenda. |
| 3 | Tirer du rendez-vous les décisions et les actions | `sales:call-summary` · `sales:log-activity` · Mettre à jour l'opportunité dans le CRM : `sales:update-opportunity` ; `sales:deal-advance-gap` · Relever les mots et les objections du client : `sales:customer-voice` | Le compte rendu d'abord, puis l'écriture du CRM après accord. Aucun engagement inventé : ce qui n'a pas été dit ne s'écrit pas. Enregistrer un appel suppose l'accord des participants : on informe chaque interlocuteur dès le début de l'appel (France, voir « Les règles à connaître » du SKILL.md). Le transcript se récupère là où il vit (Granola, Google Meet, Notion, un enregistrement transcrit sur le poste) ; la collecte du pack propale-auto le range pour la proposition de l'étape 6. |
| 4 | Recommander la bonne solution (quand plusieurs produits ou formules peuvent répondre) | Comparer les formules aux critères du prospect : `operations:vendor-review` | Les critères viennent du compte rendu ; un produit sensible ou un engagement commercial se fait valider avant d'être proposé. Manque : aucune compétence publique ne confronte les critères d'un prospect à un catalogue de formules pour justifier un choix ; la tâche ci-dessous emprunte une trame de comparaison d'options. Le choix se justifie depuis le compte rendu de l'étape 3. |
| 5 | Construire l'offre | `marketing-skills:offers` · `marketing-skills:pricing` · Poser son offre : `marketing-skills:product-marketing` | offers pour la structure de l'offre ; pricing seulement si le prix ou les paliers sont à décider. Le dirigeant valide les promesses, les conditions et le prix avant la proposition : c'est la validation de fond du workflow. |
| 6 | Écrire la proposition ou le devis | `small-business:proposal-builder` · `sales:create-an-asset` · Rédiger la proposition depuis l'enregistrement du rendez-vous : `marketing-skills:customer-research` | proposal-builder monte la proposition chiffrée depuis ce qui est sorti du rendez-vous, d'après les prix réellement pratiqués, un blanc plutôt qu'un tarif inventé ; propale-redaction quand l'entreprise a son modèle à remplir, avec une source par champ ; create-an-asset seulement quand le client attend un support à faire circuler. Sans transcript, pas de proposition : la fiche et les questions pour l'appel. Les mentions légales françaises (SIRET, TVA, pénalités de retard) vivent dans le gabarit de l'entreprise. Envoyer reste le geste de la personne qui vend. La proposition se monte à la main depuis le compte rendu de l'étape 3 et le modèle de l'entreprise : contexte du client, besoin exprimé, solution, ce qui est inclus et ce qui ne l'est pas, délais, conditions, prix. Les mentions à prévoir (délai de paiement, pénalités de retard, indemnité de recouvrement de 40 € pour un client professionnel, mention de franchise de TVA le cas échéant) sont listées dans « Les règles à connaître » du SKILL.md. Manque : aucune compétence publique ne monte le document complet à partir du rendez-vous et du modèle de l'entreprise : on l'assemble à la main, avec la règle ci-dessus. |
| 7 | Répondre aux objections | Répondre aux objections : `sales:handle-objection` ; `sales:competitive-intelligence` ; `marketing-skills:sales-enablement` | handle-objection pour l'objection d'aujourd'hui ; sales:competitive-intelligence quand l'objection cite un concurrent ; sales-enablement pour construire ou compléter la bibliothèque d'une vente complexe, une fois. Une allégation juridique ou chiffrée se fait valider avant de servir. |
| 8 | Mener jusqu'à la signature | `sales:close-plan` · `small-business:inbox-manager` · `small-business:contract-review` · Relire un contrat avant de signer : `legal:review-contract` ; `legal:triage-nda` · Faire signer : `legal:signature-request` | close-plan dès qu'une date de décision existe ; inbox-manager pour chaque message, relu avant envoi ; contract-review sur tout contrat reçu. Signer reste le geste du dirigeant. Manque : aucune compétence publique ne rédige le contrat ou l'accord de confidentialité de l'entreprise : on le prépare à la main, avec un juriste. |
| 9 | Confirmer la commande (quand la vente se conclut par une commande (références, quantités)) | Facturer la commande : `small-business:invoice-chase` | Rien n'est engagé avant la confirmation écrite du client. Manque : aucune compétence publique ne transforme une demande en récapitulatif à confirmer avec sa référence de commande : à fabriquer. |
<!-- etapes:fin -->

### 2. Clore un passage

À la fin de chaque séance, on note au journal l'état (fait, reste, prochaine action) et les décisions prises. Une compétence qui a déçu à une étape se note aussi : on rouvre alors le choix de cette étape.

## Les règles à connaître (France)

Ces règles valent pour une entreprise et des clients en France. Ailleurs, elles sont à vérifier.

- **Enregistrer un appel.** Chaque interlocuteur est informé dès le début de l'appel de la finalité de l'enregistrement, de ses destinataires et de ses droits ; un message d'accueil suffit pour cette première information (CNIL, https://www.cnil.fr/fr/cnil-direct/question/enregistrement-ou-ecoute-des-conversations-telephoniques-faut-il-informer-ses, vérifié le 06/11/2026).
- **Les mentions d'une facture.** La liste officielle (https://entreprendre.service-public.gouv.fr/vosdroits/F31808, vérifiée le 06/11/2026) comprend : un numéro unique, la date d'émission, la date de la vente ou de la prestation ; l'identité du vendeur (SIREN, forme juridique, capital pour une société) et celle de l'acheteur ; le numéro de TVA du vendeur (non exigé si le total hors taxes est de 150 € ou moins) ; la désignation, la quantité, le prix unitaire hors taxes et le taux de TVA ; les totaux hors taxes et toutes taxes comprises ; la date d'échéance de paiement, les conditions d'escompte et le taux des pénalités de retard ; l'indemnité forfaitaire de recouvrement de 40 €, qui ne se réclame qu'à un client professionnel ; et, pour une entreprise en franchise en base de TVA, la mention « TVA non applicable, art. 293 B du CGI ». La facturation électronique ajoute des mentions par étapes : le calendrier et les nouvelles mentions sont à vérifier sur cette même page.
- **Devis et facture.** Cette liste concerne la facture, qui vient après la signature. Les règles propres au devis sont à vérifier selon le métier ; il est prudent d'y annoncer déjà le délai de paiement, les pénalités de retard et, pour un client professionnel, l'indemnité de 40 €, que la facture reprendra.
- **Le droit de rétractation.** Pour un contrat conclu à distance avec un consommateur, 14 jours pour se rétracter (Code de la consommation, article L221-18, https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000032226842/, vérifié le 06/11/2026), sauf exceptions, par exemple un service pleinement exécuté avant la fin du délai à la demande du consommateur (article L221-28). Entre professionnels, il n'existe pas en principe.

## Ce qui manque

- **Recommander un produit dans un catalogue** (étape 4) : aucune compétence publique ne confronte les critères du prospect à une liste de produits ou de formules. On compare à la main, depuis le compte rendu.
- **Monter la proposition complète** (étape 6) : l'assemblage du document à partir de la transcription du rendez-vous et du modèle de l'entreprise se fait à la main, avec la règle de l'étape. Les mentions légales à prévoir sont dans « Les règles à connaître » ci-dessus ; sans modèle d'entreprise, on part de cette liste.
- **Rédiger le contrat ou l'accord de confidentialité** (étape 8) : à préparer avec un juriste.
- **Transformer une demande en commande** (étape 9) : le récapitulatif à confirmer et sa référence se font à la main.

## Frontières

Les workflows cités ici se trouvent dans le même dépôt de plugins que celui-ci.

| Demande | Va à |
|---|---|
| Trouver des prospects, jusqu'au rendez-vous | `/trouver-ses-prochains-clients:trouver-ses-prochains-clients` |
| La revue du pipeline, la prévision, les extensions chez les clients | `/piloter-le-pipeline:piloter-le-pipeline` |
| L'objectif commercial, les rôles, l'incitation, les partenaires | `/organiser-sa-force-de-vente:organiser-sa-force-de-vente` |
| Écrire la règle de notation et de répartition des demandes entrantes | hors de ce workflow : ici on applique la règle, on ne l'écrit pas |
