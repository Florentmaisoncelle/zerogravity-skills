---
name: fideliser-et-faire-recommander
description: >-
  Quand on veut faire travailler ses clients satisfaits (« un programme de parrainage », « récupérer des témoignages
  clients », « répondre aux avis », « des clients partent, comment les retenir ? », « un programme de fidélité », « où
  en est ma fidélisation ? ») → affiche l'état calculé depuis le dossier `fidelisation/AAAA-MM/`, puis déroule quatre
  étapes dans l'ordre : le programme de recommandation, les avis et témoignages autorisés, la rétention, le programme
  de fidélité quand il se justifie. Les règles du programme s'écrivent avant la première invitation, aucun témoignage
  ne se publie sans autorisation. Le programme de fidélité n'a pas de compétence publique : la méthode est dans ce
  workflow. Se lance par `/fideliser-et-faire-recommander:fideliser-et-faire-recommander`. Déclencheurs :
  « parrainage », « programme de recommandation », « affiliation », « témoignage client », « avis clients »,
  « rétention », « churn », « fidélité ». Pas pour développer le chiffre chez un client :
  `/piloter-le-pipeline:piloter-le-pipeline`. Pas pour des apporteurs d'affaires :
  `/organiser-sa-force-de-vente:organiser-sa-force-de-vente`.
---

# Fidéliser et faire recommander : parrainage, témoignages, rétention

## Ce que ça résout

Les clients satisfaits peuvent faire venir de nouveaux clients, et on les exploite mal : pas de programme de
recommandation, des témoignages réutilisés sans autorisation, des départs qu'on découvre trop tard. Ici : un programme
écrit avant la première invitation, des avis et des témoignages autorisés et tracés, la rétention, et un programme de
fidélité seulement s'il rapporte. Pour savoir si c'est un bon canal chez soi, on compare le coût d'un client
recommandé à celui d'un client venu autrement ; ce workflow demande ce chiffre.

**Résultat attendu** : un programme de recommandation avec ses règles et sa mesure, des témoignages autorisés dont la
preuve est conservée, des départs retenus honnêtement, et la décision d'un programme de fidélité.

## Stratégie

1. **Une compétence par étape, la meilleure quand elle existe.** La table des étapes (plus bas) dit laquelle. Les
   règles de choix et les manques sont aussi dans `references/workflow.json`.
2. **L'état d'abord, toujours calculé** depuis les fichiers de `fidelisation/AAAA-MM/`, jamais recopié.
3. **L'ordre protège les clients** : pas d'invitation sans règles d'attribution, pas de témoignage publié sans
   autorisation. Sauter une étape reste possible sur demande ; le journal dit laquelle et pourquoi.
4. **Une seule validation, à l'étape 1** : les règles du programme, une fois écrites et avant la première
   invitation. Ce n'est pas un cadrage préalable. Ensuite tout se déroule. Restent à une personne : obtenir et
   conserver l'accord du client, et valider la récompense (avec son comptable ou un conseil juridique quand elle a une
   valeur notable).
5. **Aucune donnée personnelle dans le dossier d'état.** Les citations et les accords des clients restent dans l'outil
   de l'entreprise (CRM ou tableur) ; le dossier d'état ne porte que des codes (C01, C02...). La table de
   correspondance code, client vit dans cet outil et le workflow ne la lit jamais.
6. **Tout texte qui sort au nom de l'entreprise** est relu et montré avant diffusion ; rien ne part sans validation.
7. **Les décisions se notent** dans le journal, avec ce qu'on a appris d'un cycle à l'autre : quelques lignes suffisent.

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
/plugin install ameliorer-le-parcours-client@zerogravity
/plugin install organiser-sa-force-de-vente@zerogravity
/plugin install piloter-le-pipeline@zerogravity
/plugin install traiter-les-demandes-clients@zerogravity
```
<!-- prerequis:fin -->

## Étapes

### 0. Le dossier, puis l'état (lecture seule)

**Le dossier.** Un sous-dossier par mois de travail : `fidelisation/AAAA-MM/`, à la racine du dossier de l'entreprise.
Dossier absent ou vide : il n'y a encore rien de fait, l'état est « étape 1 » et le dossier se crée au premier
passage. Si le dossier courant n'est pas celui de l'entreprise, le dire en une ligne et demander où il vit : rien ne
s'écrit avant. Les règles du programme (étape 1) valent d'un mois à l'autre : au cycle suivant, l'étape 1 s'inscrit
`sans objet` (« règles inchangées, voir `fidelisation/<premier mois>/01-recommandations.md` ») ou `corrigée` si elles
changent.

**L'état**, calculé depuis le journal et les fichiers :

```text
Cycle              2026-11
Étapes             01 ✓  02 ✓  03 -  04 -
Dernière décision  2026-11-06 · 02 · fait · demande d'avis validée, 3 autorisations obtenues
Étape suivante     03 Retenir les clients qui partent
```

- Le journal `fidelisation/AAAA-MM/journal.md` a une ligne par décision :
  `AAAA-MM-JJ · NN · fait | en attente | sans objet | sautée | corrigée · <une phrase>`.
- Pour chaque étape, la dernière ligne du journal qui la nomme fait foi. `✓` : cette ligne dit `fait` ou `corrigée`
  et le fichier de l'étape existe. `s.o.` : elle dit `sans objet` ou `sautée` (l'étape n'est plus proposée). `-` :
  aucune ligne, ou le fichier manque.
- `corrigée` : l'étape est refaite après une correction ; elle reste ✓ et la ligne dit ce qui a changé. `sautée` :
  la personne a choisi de passer ; la ligne dit pourquoi.
- `en attente` : l'étape est préparée, mais elle dépend d'un geste ou d'une réponse qui arrive hors de la conversation. La ligne du journal dit ce qu'on attend et de qui. L'état l'affiche `att.` avec ce texte : l'étape n'est pas `✓`, parce que préparé n'est pas fait. Le workflow s'arrête là et le dit ; il n'invente jamais la suite (ni réponse, ni résultat, ni geste qu'on ne lui a pas confirmé). Quand la personne apporte ce qui est arrivé, la ligne `fait` suit. Ici : l'envoi des demandes de recommandation et d'avis par la personne (étapes 1 et 2), la permission de chaque témoin (étape 2), les réponses des clients (étape 3) et les décisions à trois mois (étapes 1 et 4).
- L'étape suivante est la première étape `-` ou `att.`, dans l'ordre (devant une étape `att.`, on demande d'abord où en est l'attente). Si aucune ne l'est, le cycle est terminé, et on peut
  ouvrir le mois suivant.
- Cycle par défaut : le plus récent qui n'est pas terminé, ou celui que la personne nomme.

**Une question n'est pas un ordre.** « Où en est ma fidélisation ? » : on donne l'état et la prochaine action, puis on
s'arrête. La commande du workflow, « continue » ou « déroule » : on enchaîne jusqu'à la première étape en attente, puis on s'arrête et on le dit.

**Une demande au milieu du chemin** (« récupère des témoignages ») : l'étape 2 marche seule ; l'autorisation pour
chaque usage se demande avant toute publication.

### 1. Lancer l'étape suivante

Lire l'étape dans `references/workflow.json`, appliquer sa règle de choix, invoquer la compétence retenue (ou suivre
la méthode ci-dessous), écrire sa sortie dans le fichier de l'étape (sans nom de client), inscrire la ligne au
journal (`fait` ou `en attente`, voir plus haut), puis passer à la suivante sans redemander.

<!-- etapes:debut -->
| # | Étape | Compétences | Règle de choix |
|---|---|---|---|
| 1 | Lancer un programme de recommandation | Lancer le programme de recommandation : `marketing-skills:referrals` | Les règles d'attribution et la récompense s'écrivent avant la première invitation ; la récompense ne dépasse pas ce que coûte un client acquis autrement. Le droit à la récompense et le consentement se valident par une personne. Décision à trois mois : on garde le programme s'il a amené des clients à un coût inférieur à celui des autres canaux. |
| 2 | Recueillir des témoignages autorisés | Recueillir les témoignages : `small-business:review-reputation` | La citation exacte et sa source gardées, la permission obtenue, jamais deux personnes fusionnées en une phrase, les coupures marquées. marketing-skills:referrals pour demander des avis et des témoignages et les réutiliser avec permission ; small-business:review-reputation pour répondre aux avis publics. Une demande d'avis est la même pour tous les clients concernés, satisfaits ou non, et ne promet rien en échange. |
| 3 | Retenir les clients qui partent | Retenir les clients qui partent : `marketing-skills:churn-prevention` | Une offre de rétention reste honnête : partir doit rester simple. marketing-skills:churn-prevention vise surtout les abonnements (parcours d'annulation, paiements échoués) ; pour une activité sans abonnement, small-business:review-reputation repère les clients dont le rythme d'achat s'est arrêté. Un message de reprise de contact s'appuie sur quelque chose de réel dans l'histoire du client. |
| 4 | Opérer un programme de fidélité (quand un programme de fidélité se justifie) | Opérer le programme de fidélité : à la main | Avant de lancer, vérifier que le programme rapporte plus qu'il ne coûte : il n'a de sens que si les clients achètent plusieurs fois. Les règles se valident avant la première émission, avec le comptable pour les effets de TVA et de comptabilité (à vérifier selon le pays). Décision à trois mois : on arrête si les clients inscrits ne rachètent pas plus que les autres. |
<!-- etapes:fin -->

### 2. La méthode, étape par étape

#### Étape 1 : le programme de recommandation (`marketing-skills:referrals`)

Écrire dans `01-recommandations.md` :

1. **Le coût d'un client acquis autrement** (publicité, prospection) : c'est le plafond de la récompense.
2. **Le moment de la demande** : juste après un résultat que le client apprécie (livraison réussie, objectif atteint,
   renouvellement), jamais au hasard.
3. **Le mécanisme le plus simple** : un message personnel qui demande « connaissez-vous quelqu'un à qui ça servirait ? »
   avec une présentation préparée, avant tout lien ou code.
4. **La récompense**, ou l'absence de récompense : un remerciement, un avantage réciproque, une remise. Pas de
   récompense est un choix valable pour des clients professionnels.
5. **Les règles d'attribution** : comment savoir qui a recommandé qui (question « comment nous avez-vous connus ? »,
   code personnel), à quel moment la récompense est due, plafond, qui ne peut pas être récompensé (soi-même, un proche
   qui s'inscrit deux fois).
6. **La mesure** : invitations envoyées, recommandations reçues, clients signés, coût total.

*Ce qu'on décide* : lancer ou non, avec quelle récompense. *Critère d'arrêt* : à trois mois, on garde le programme
s'il a amené des clients à un coût inférieur à celui des autres canaux ; sinon on l'arrête ou on change le moment ou la
récompense, un seul des deux à la fois.

#### Étape 2 : les avis et les témoignages (`marketing-skills:referrals`, puis `small-business:review-reputation`)

La partie « avis » de `marketing-skills:referrals` couvre la demande d'avis, la réutilisation d'un témoignage avec
permission et les règles de chaque plateforme. La compétence `small-business:review-reputation` sert à répondre aux
avis déjà publiés. Chacune a sa tâche :

1. **Demander** : un message neutre, identique pour tous les clients concernés (satisfaits ou non), avec le lien vers
   le profil réel de la plateforme, sans « donnez cinq étoiles », sans texte prérédigé, sans contrepartie. Une relance
   au plus.
2. **Garder la preuve** de chaque témoignage réutilisé : la citation exacte, la source et la date, l'autorisation de la
   personne pour chaque usage (site, publicité, propositions), le nom sous lequel on la cite, la date de fin éventuelle.
   Ces éléments restent dans l'outil de l'entreprise ; le dossier d'état n'en garde que le nombre.
3. **Ne jamais fusionner deux personnes** en une phrase, ne pas changer le sens d'une citation, marquer les coupures.
4. **Répondre à chaque avis** avec `small-business:review-reputation` : un brouillon dans la voix du dirigeant, validé
   avant publication, qui nomme le problème et propose une suite privée. Les détails de la commande ne se disent
   jamais en public.

*Ce qu'on décide* : quels témoignages sont publiés, où. *Critère d'arrêt* : un témoignage sans autorisation
enregistrée reste inutilisé.

#### Étape 3 : retenir les clients qui partent (`marketing-skills:churn-prevention`)

Deux cas, selon l'activité :

- **Abonnement ou contrat récurrent** : la compétence `marketing-skills:churn-prevention` couvre le parcours
  d'annulation, la question « pourquoi partez-vous ? », les offres de maintien et la relance des paiements échoués.
- **Pas d'abonnement** : un client est « parti » quand son rythme d'achat s'arrête. Pour chaque client, comparer le
  temps écoulé depuis la dernière commande à son propre rythme habituel (pas à une moyenne), classer par valeur du
  client et ne garder qu'une courte liste de ceux qu'on contactera vraiment. `small-business:review-reputation`
  décrit cette méthode.

Dans les deux cas, un message de reprise de contact s'appuie sur un élément réel (la dernière réalisation, une
question restée sans réponse), jamais un « vous nous manquez » générique. L'offre de maintien reste honnête : partir
doit rester simple. *Ce qu'on mesure* : clients partis ce mois-ci, clients récupérés. *Critère d'arrêt* : une offre
qui ne retient personne après deux envois est retirée.

#### Étape 4 : le programme de fidélité (optionnelle)

À faire seulement si les clients rachètent plusieurs fois par an. Si l'achat est annuel ou rare, la rétention (étape
3) rapporte davantage et l'étape est « sans objet ». Écrire dans `04-fidelite.md` :

1. **Le test d'utilité** : combien d'achats en plus faut-il pour payer le coût des récompenses ? Si ce nombre paraît
   hors de portée, on s'arrête là.
2. **La forme la plus simple** : un avantage après N achats ou un niveau, sans points compliqués.
3. **Les règles** : qui gagne quoi, quand ça expire, comment on l'utilise, ce qui l'annule, le plafond par client.
4. **Les contrôles** : une récompense par achat réel, pas de cumul abusif entre comptes. Les effets de TVA et de
   comptabilité d'un avantage se vérifient avec son comptable (à vérifier selon le pays).
5. **Le suivi** : coût total des récompenses, achats des membres comparés à ceux des autres clients.

*Ce qu'on décide* : continuer, ajuster ou arrêter. *Critère d'arrêt* : à trois mois, si les membres ne rachètent pas
plus que les autres clients, le programme s'arrête.

### 3. Clore un passage

À la fin de chaque séance, on écrit l'état (fait, reste, prochaine action) au journal. Si une compétence a déçu à une
étape, on le note aussi, pour rouvrir le choix de la compétence de cette étape.

## Ce qui se fait à la main

- **Le programme de fidélité** (étape 4) : aucune compétence publique n'en opère un, il suit la méthode ci-dessus.
- **Le droit de réutiliser un avis ou un témoignage** : l'autorisation se demande à chaque client et se conserve ;
  aucune compétence ne la recueille à la place de la personne.

## Frontières

| Demande | Va à |
|---|---|
| Développer le chiffre chez un client existant | `/piloter-le-pipeline:piloter-le-pipeline` |
| Repérer les clients à risque, exploiter une enquête de satisfaction ou des avis, cartographier le parcours | `/ameliorer-le-parcours-client:ameliorer-le-parcours-client` |
| Répondre à un client (commande, facture, abonnement, demande technique) | `/traiter-les-demandes-clients:traiter-les-demandes-clients` |
| Des partenaires qui apportent des affaires | `/organiser-sa-force-de-vente:organiser-sa-force-de-vente` |
