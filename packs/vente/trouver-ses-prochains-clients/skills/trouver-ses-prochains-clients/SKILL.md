---
name: trouver-ses-prochains-clients
description: >-
  Quand on veut trouver ses prochains clients en B2B, c'est-à-dire en vendant à des entreprises (décider qui viser, repérer les entreprises qui montrent un besoin, choisir les comptes de la semaine, trouver la bonne personne, écrire un message tiré du signal, l'envoyer, tenir la conversation jusqu'au rendez-vous, mesurer) → affiche l'état de la prospection calculé depuis le dossier `prospection/<cible>/`, puis déroule neuf étapes dans l'ordre. Chaque étape a une méthode écrite et un critère de réussite ; une compétence publique s'y ajoute quand il en existe une. Se lance par `/trouver-ses-prochains-clients:trouver-ses-prochains-clients`. Déclencheurs : « trouve-moi des clients », « prospecter », « qui viser », « liste de prospects », « écris le message de prospection », « où en est ma prospection ». Pas pour préparer le rendez-vous obtenu et conclure la vente (`/conclure-une-vente:conclure-une-vente`), ni pour suivre un pipeline déjà rempli (`/piloter-le-pipeline:piloter-le-pipeline`).
---

# Trouver ses prochains clients, du signal au rendez-vous

## Ce que ça résout

Prospecter sans ordre produit de longues listes de contacts froids, des messages qui se ressemblent tous et personne pour dire ce qui marche. Ici, neuf étapes dans l'ordre : la cible, les signaux, les comptes de la semaine, la bonne personne, le message, l'envoi, les réponses, le suivi, la mesure. Un « compte » est une entreprise visée ; un « signal d'achat » est un fait observable et daté qui rend un besoin probable maintenant (un recrutement, un nouveau dirigeant, un site à refaire).

**Résultat attendu** : chaque semaine, une sélection courte de comptes avec leur raison, un message relu pour chaque contact, des réponses traitées, des chiffres qui disent quoi continuer. Un dossier `prospection/<cible>/` qui dit à tout moment où on en est.

## Stratégie

1. **La cible avant la liste.** On sait qui on vise, et qui on exclut, avant de chercher un seul nom.
2. **Un signal, une preuve datée.** Une entreprise entre dans la sélection parce qu'elle montre quelque chose de précis, pas parce qu'elle est dans un fichier.
3. **Un message par contact, tiré de son signal.** Aucun texte générique envoyé en masse.
4. **Rien ne part sans validation de la personne qui vend.** Deux points de contrôle, jamais plus : à l'étape 5, elle valide le lot de messages (premier message, relances et règle d'arrêt), ce qui vaut feu vert d'envoi pour ce lot ; à l'étape 7, elle relit chaque réponse écrite à un prospect, parce qu'une réponse ne se prévoit pas. L'étape 6 n'ajoute aucune validation : elle envoie seulement ce qui est validé, depuis le compte de la personne.
5. **Les limites de chaque canal se respectent** : plafonds du compte, règles de la plateforme, droit de refuser et information des personnes contactées.
6. **Aucune donnée personnelle dans le dossier d'état.** Le dossier ne contient ni nom de personne, ni e-mail, ni téléphone, ni lien de profil. Les contacts s'y écrivent par code (`P01`, `P02`…).

<!-- prerequis:debut -->
## Prérequis

Ce workflow s'appuie sur des compétences publiques, installées à part. Aucune n'est indispensable : si l'une manque, le workflow le dit et fait l'étape à la main. Faire l'étape à la main veut dire suivre sa règle de choix, écrire ce qu'elle doit rendre (dans le fichier de l'étape, ou dans la réponse quand le workflow n'a pas de dossier) et dire ce qui reste à la charge de la personne.

```text
/plugin marketplace add Florentmaisoncelle/zerogravity-skills
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin marketplace add coreyhaines31/marketingskills
/plugin install leadlint@zerogravity
/plugin install marketing-skills@marketingskills
/plugin install marketing@knowledge-work-plugins
/plugin install sales@knowledge-work-plugins
/plugin install small-business@knowledge-work-plugins
```

Les workflows cités ici sont dans le même dépôt (le dépôt s'ajoute une fois : `/plugin marketplace add Florentmaisoncelle/zerogravity-skills`) :

```text
/plugin install conclure-une-vente@zerogravity
/plugin install envoyer-des-e-mails@zerogravity
/plugin install organiser-sa-force-de-vente@zerogravity
/plugin install piloter-le-pipeline@zerogravity
/plugin install publier-sur-linkedin@zerogravity
```
<!-- prerequis:fin -->

## Étapes

### 0. Le dossier, puis l'état (lecture seule)

**Le dossier.** Une cible, un dossier : `prospection/<cible>/` (par exemple `prospection/cabinets-comptables/`), avec son journal. Dossier absent ou vide : il n'y a encore rien de fait, l'état est « étape 1 » et le dossier se crée au premier passage. Si la personne vise plusieurs types de clients, chacun a son dossier ; la cible par défaut est le dossier le plus récent dont une étape reste à faire, ou celle que la personne nomme. Si le dossier courant n'est pas celui de l'entreprise, le dire en une ligne et demander où il vit : rien ne s'écrit avant.

**Les codes et le registre.** Chaque entreprise listée à l'étape 2 reçoit un code (`P01`, `P02`…) que tous les fichiers reprennent. Le code se donne une seule fois, dans `prospection/<cible>/registre.md`, qui reste à la racine du dossier et ne s'archive jamais : un code n'est jamais réutilisé ni renuméroté, et une entreprise déjà codée garde son code d'une semaine à l'autre (on cherche dans le registre avant d'en donner un). Le registre a deux tableaux. *Codes* : le code, l'entreprise, la semaine d'entrée, le statut (en séquence, en conversation, rendez-vous, client, refus) et la prochaine relance (date et numéro). *Exclusions* : l'entreprise ou le code, la date, la raison (déjà client, concurrent, refus, demande de désinscription) ; les exclusions écrites à l'étape 1 y entrent aussi, et rien ne s'y efface. L'étape 6 le consulte avant chaque envoi. La correspondance entre un code et la personne (nom, profil, coordonnées) est tenue par la personne qui vend, dans son outil (un tableur ou son CRM, le logiciel où elle note ses contacts et ses affaires), dans une colonne « code » qu'elle remplit à l'étape 4 ; le workflow ne la lit jamais. Le nom d'une entreprise peut s'écrire dans le dossier, sauf si elle porte le nom d'une personne : le code suffit alors.

**L'état**, calculé depuis le journal et les fichiers de `prospection/<cible>/` :

```text
Cible              <type de client visé>
Étapes             01 ✓  02 ✓  03 ✓  04 -  05 -  06 -  07 -  08 -  09 -
Comptes            12 listés · 5 retenus · 0 contacts trouvés · 0 messages validés
Dernière décision  <date> · 03 · fait
Étape suivante     04 Trouver le bon contact (à la main, voir la méthode)
```

- Les compteurs viennent des fichiers du dossier : « listés » = les lignes du tableau principal de `02-signaux.md` (sans la section « à surveiller »), « retenus » = les lignes de la section « Retenus » de `03-selection.md`, « contacts trouvés » = les lignes de `04-bon-contact.md` qui ont un rôle, une source et une date de vérification, « messages validés » = les messages marqués « validé » dans `05-message.md`. À partir de l'étape 6, deux compteurs s'ajoutent : « envoyés » = les lignes de `06-sequence.md`, « réponses » = les lignes de `07-reponses.md`.
- Le journal `prospection/<cible>/journal.md` a une ligne par décision : `AAAA-MM-JJ · NN · fait | en attente | sans objet | sautée | corrigée · <une phrase>`. Deux lignes spéciales : la clôture d'un passage, `AAAA-MM-JJ · 09 · fait · <la décision de la semaine>`, puis l'archivage, `AAAA-MM-JJ · 00 · fait · passage archivé : passages/AAAA-Sww/` (00 désigne le dossier, pas une étape).
- Pour chaque étape, la dernière ligne du journal qui la nomme fait foi. `✓` : cette ligne dit `fait` ou `corrigée` et le fichier de l'étape existe. `s.o.` : elle dit `sans objet` ou `sautée` (l'étape n'est plus proposée). `-` : aucune ligne, ou le fichier manque.
- `corrigée` : l'étape est refaite après une correction ; elle reste ✓ et la ligne dit ce qui a changé. `sautée` : la personne a choisi de passer ; la ligne dit pourquoi.
- `en attente` : l'étape est préparée, mais elle dépend d'un geste ou d'une réponse qui arrive hors de la conversation. La ligne du journal dit ce qu'on attend et de qui. L'état l'affiche `att.` avec ce texte : l'étape n'est pas `✓`, parce que préparé n'est pas fait. Le workflow s'arrête là et le dit ; il n'invente jamais la suite (ni réponse, ni résultat, ni geste qu'on ne lui a pas confirmé). Quand la personne apporte ce qui est arrivé, la ligne `fait` suit. Ici : les envois faits par la personne (étape 6), les réponses des prospects (étape 7), le temps qu'il faut avant de mesurer (étape 9), et tout ce que la personne doit encore valider ou apporter.
- L'étape suivante est la première étape `-` ou `att.`, dans l'ordre (devant une étape `att.`, on demande d'abord où en est l'attente).
- **La semaine suivante.** Quand l'étape 9 est faite, on clôt le passage. Les fichiers 02 à 09 partent dans `passages/AAAA-Sww/` du même dossier, où `AAAA-Sww` est la semaine (numérotation ISO) du jour où l'étape 2 a été inscrite pour la première fois dans ce passage, par exemple `passages/2026-S45/`, même si l'étape 9 finit la semaine suivante. Le journal et le registre restent en place. Pour l'état des étapes 2 à 9, seules comptent les lignes du journal qui suivent la dernière ligne `00 · passage archivé` : le nouveau passage repart donc à l'étape 2, même si l'ancien journal dit `fait` pour la même étape. L'étape 1 garde sa dernière ligne, avant ou après l'archivage : elle reste valable tant que la cible ne change pas. Une nouvelle cible est un nouveau dossier, qui repart à l'étape 1.
- **Ce qui continue d'une semaine à l'autre ne s'archive pas.** Les relances à venir et les exclusions vivent dans le registre, et le texte validé de chaque relance dans `prospection/<cible>/relances.md` (le code, le numéro de relance, le canal, le texte sans nom). Ces deux fichiers ne partent jamais dans `passages/`. L'étape 6 de la semaine suivante envoie donc aussi les relances échues, et l'étape 7 traite les réponses reçues plus tard aux envois d'un passage archivé.

Une question (« où en est ma prospection ? ») : on affiche l'état et la prochaine action, puis on s'arrête. « Continue » ou « déroule » : on enchaîne jusqu'à la première étape en attente, puis on s'arrête et on le dit.

### 1. Lancer l'étape suivante

Lire l'étape dans la table, appliquer sa règle, invoquer la compétence retenue si elle existe, sinon suivre la méthode écrite plus bas. Écrire la sortie dans le fichier de l'étape (sans nom ni coordonnée de personne), inscrire « fait » au journal (ou « en attente » quand l'étape dépend d'un geste ou d'une réponse qui arrive plus tard), puis passer à la suivante si elle n'est pas en attente. Une étape qui demande une information à la personne le dit avant de commencer.

**Sans recherche sur le web.** Si aucun outil de recherche n'est disponible, le workflow le dit en tête des étapes 2, 3 et 4 et l'écrit au journal. Il n'invente aucune entreprise, aucun signal ni aucun contact : la personne apporte les entreprises et les liens de preuve, ou l'étape reste `att.` en l'attendant.

<!-- etapes:debut -->
| # | Étape | Compétences | Règle de choix |
|---|---|---|---|
| 1 | Définir la cible | Remplir les réglages et écrire les cibles : `marketing-skills:product-marketing` · Nettoyer exclusions et doublons : `leadlint:leadlint` · Construire sa base de prospects : `small-business:lead-finder` | La préparation d'abord, une fois par installation ; elle appelle la cible stricte pour chaque type de client. Les réglages se montrent au dirigeant, qui les corrige : c'est la validation du cadrage. La cible avant la liste : un type de client à la fois, avec ses exclusions écrites. Une liste de contacts se nettoie avant d'être utilisée. |
| 2 | Repérer les signaux et lister les entreprises | Croiser les signaux : `sales:account-tiering` · Lister les entreprises : `marketing-skills:prospecting` | Les capteurs publics du système d'abord, sans abonnement : registre des entreprises, annonces légales, marchés publics, offres d'emploi, actualités, site et pages LinkedIn publiques. GojiBerry seulement pour ce que seul un compte connecté voit. Un signal sans preuve datée ne compte pas. Deux signaux concordants valent mieux qu'un seul fort. |
| 3 | Choisir les comptes de la semaine | Classer les comptes de la semaine : `sales:lead-triage` · Préparer la fiche d'un compte : `sales:account-research` | La semaine de chaque cible par agent-icp ; avant tout premier envoi, vingt lignes contrôlées par ciblage-b2b-qa. Les cas douteux partent en « à juger », jamais dans la séquence. Peu de comptes, bien choisis : la sélection de la semaine tient sur une page, chaque exclu a sa raison. |
| 4 | Trouver le bon contact | à la main | Le rôle du comité d'achat que la cible désigne : le rôle de la personne qui décide, pas le premier nom venu. L'enrichissement (e-mail, téléphone) ne se fait que pour la personne retenue. Manque : aucune compétence publique pour ce geste : il se fait à la main, avec la règle de l'étape. |
| 5 | Écrire le message | Écrire le message : `sales:draft-outreach` ; `small-business:outreach-composer` · Écrire le message : `sales:draft-outreach` | Un message par contact, tiré de son signal ; aucun texte libre ne part, seul le texte contrôlé et validé. Un message par contact, tiré de son signal. Aucun texte libre ne part : seul le texte relu et marqué « validé » par la personne qui vend. Tant que la personne n'a pas validé le lot, l'étape est en attente. |
| 6 | Envoyer la séquence | Appeler : `small-business:call-list` | L'envoi se fait depuis le compte du client, à la main avec la liste du jour, ou par son outil d'envoi sur un feu vert écrit. L'email et l'appel suivent les mêmes plafonds. Une réponse ou une opposition arrête la séquence du contact. Le workflow prépare la liste, la personne envoie : l'étape reste en attente tant que les envois ne sont pas confirmés, et une liste préparée n'est pas une liste envoyée. Seuls partent les messages validés à l'étape 5, depuis le compte de la personne qui vend. Les plafonds et les règles de chaque canal se respectent, et la liste d'exclusion du registre se consulte avant chaque envoi. |
| 7 | Tenir la conversation jusqu'au rendez-vous | Tenir jusqu'au rendez-vous : `sales:handle-objection` · Prendre le rendez-vous : `sales:schedule-meeting` · Tenir la bibliothèque de ressources : `marketing-skills:sales-enablement` ; `sales:create-an-asset` | Rien ne part sans le feu vert de la personne qui vend. Chaque semaine, la mesure par signal, angle et canal décide : continuer, corriger ou arrêter. Chaque réponse écrite à un prospect est relue par la personne qui vend avant d'être envoyée. Une réponse arrête la séquence de ce contact. Le workflow n'invente aucune réponse : sans réponse apportée par la personne, l'étape reste en attente. |
| 8 | Tenir le fichier maître et le CRM | Tenir le fichier maître : `small-business:crm-autopilot` · Écrire dans le CRM : `sales:log-activity` | La compétence par défaut de chaque tâche d'abord ; les autres selon le cas qu'elles disent. Une seule fiche par contact. Le CRM s'écrit sans doublon et sans effacer ce qui y est déjà. |
| 9 | Mesurer et ajuster | Mesurer : `marketing:performance-report` · Revue hebdomadaire des leviers : `sales:weekly-wrap` · Mémoire d'un client à l'autre : `sales:win-loss-review` | La compétence par défaut de chaque tâche d'abord ; les autres selon le cas qu'elles disent. Chaque semaine, les chiffres par canal et par signal décident : continuer, corriger ou arrêter. |
<!-- etapes:fin -->

### La méthode, étape par étape

Chaque étape dit ce qu'elle rend (le fichier) et à quoi on reconnaît qu'elle est réussie.

#### Étape 1. Définir la cible (`01-cible.md`)

1. Partir des trois à cinq meilleurs clients actuels : ceux qui paient bien, restent et recommandent. Noter ce qu'ils ont en commun (secteur, taille en nombre de personnes, zone, façon dont le besoin est apparu chez eux). Sans client, partir de l'offre : qui a le problème qu'elle résout, et qui paie pour le résoudre.
2. Écrire la cible en une phrase : des entreprises de tel type, de telle taille, dans telle zone, où telle fonction a tel problème.
3. Écrire trois à cinq critères d'inclusion et la liste des exclusions. Un critère se vérifie en deux minutes sur un site ou un profil, sinon on le retire. Exclusions fréquentes : déjà client, concurrent, trop petit ou trop grand pour l'offre, secteur qu'on ne sert pas, entreprise dont un contact a déjà refusé ou demandé à ne plus être contacté.
4. Écrire un ou deux angles : le problème par lequel on ouvre la conversation.
5. Noter ce que les messages pourront dire de vous : l'offre en une phrase, le problème qu'elle résout pour la cible, et les preuves réelles (un client semblable, un résultat vrai, avec sa source). Sans preuve réelle, aucun message n'en cite. Si la personne ne donne pas ces trois éléments, l'étape 1 les lui demande avant d'être faite.
6. Si une liste de contacts existe déjà, la nettoyer avant usage avec `leadlint:leadlint` si la compétence est installée. À la main : retirer les doublons (même entreprise ou même site), les lignes sans entreprise identifiable, les entreprises exclues et toute personne qui a demandé à ne plus être contactée.

**Réussite.** Une personne qui ne connaît pas l'entreprise décide en deux minutes, avec la seule fiche, si une entreprise est dans la cible ou non. La fiche porte aussi l'offre, le problème résolu et les preuves réelles, dont l'étape 5 a besoin.

#### Étape 2. Repérer les signaux et lister les entreprises (`02-signaux.md`)

1. Choisir deux ou trois signaux d'achat, pas plus. Exemples : une offre d'emploi sur le sujet que l'on traite, un nouveau dirigeant, une levée de fonds, l'ouverture d'un site ou d'un point de vente, un site refait ou à l'abandon, une publication de la personne sur le sujet, le départ d'un prestataire. Pour chacun, écrire pourquoi il précède un achat, où le voir (site de l'entreprise, offres d'emploi, actualité, réseau professionnel, annonces légales) et son âge maximum (par exemple 60 jours, à ajuster : plus il est ancien, moins il vaut).
2. Chercher à la main : une recherche par signal, ou une vérification des entreprises de la liste de l'étape 1 une à une. `marketing-skills:prospecting` aide à découvrir des entreprises et à recouper plusieurs sources. Des alertes (par mots-clés, par entreprise) peuvent faire le guet, mais elles ne remplacent pas la vérification du fait.
3. Pour chaque entreprise qui montre un signal, écrire une ligne, une seule par entreprise : code (cherché d'abord dans le registre, sinon donné et inscrit au registre), entreprise, signal, lien de la preuve, date, force (forte : précis, récent et lié directement à l'offre ; moyenne ; faible). Une entreprise qui montre deux signaux garde une seule ligne, avec les deux signaux, chacun avec son lien et sa date. Sans preuve datée, l'entreprise n'entre pas : elle va dans une section « à surveiller ».
4. Deux signaux concordants valent mieux qu'un seul fort. `sales:account-tiering` note à part l'ajustement à la cible et l'intérêt montré, ce qui aide à prioriser.
5. Viser une vingtaine d'entreprises listées pour en retenir cinq à dix. Si la liste est plus courte, élargir la cible ou les signaux, jamais baisser l'exigence de preuve.
6. N'utiliser que des informations publiques et professionnelles.

**Réussite.** Chaque ligne a un lien et une date, aucun signal n'est plus vieux que son âge maximum, aucune entreprise n'est hors cible.

#### Étape 3. Choisir les comptes de la semaine (`03-selection.md`)

1. Fixer le nombre de comptes d'après ce que la personne peut suivre : chaque réponse reçue doit avoir une suite sous un jour ouvré. Au départ, cinq à dix ; on monte quand les réponses sont traitées à temps.
2. Noter chaque entreprise listée de 0 à 2 sur deux points. L'ajustement à la cible : 2 si tous les critères d'inclusion de l'étape 1 sont vérifiés, 1 si l'un d'eux reste à vérifier, 0 si l'un d'eux n'est pas rempli (l'entreprise est alors écartée). La force du signal, reprise de l'étape 2 : forte = 2, moyenne = 1, faible = 0. Garder les totaux les plus hauts ; à égalité, le signal le plus récent gagne.
3. Pour chaque compte retenu, écrire l'angle choisi parmi ceux de l'étape 1 et une phrase de preuve (le signal et sa date). `sales:account-research` prépare une fiche plus complète pour les comptes à enjeu.
4. Pour chaque compte écarté, écrire la raison en quelques mots. Les cas que seule la personne peut trancher vont dans une section « à juger » : la personne décide de les retenir ou de les écarter, et l'étape reste `att.` tant qu'il en reste.

**Réussite.** La sélection tient sur une page, chaque compte retenu a un angle et un signal daté, chaque compte écarté a sa raison.

#### Étape 4. Trouver le bon contact (`04-bon-contact.md`)

1. Choisir le rôle, pas le premier nom venu : la personne qui ressent le problème et qui décide ou pèse sur la décision. Dans une très petite entreprise, c'est le dirigeant ; plus grande, c'est la fonction concernée par le signal (un recrutement ouvert mène vers la personne qui recrute).
2. Chercher où la personne se trouve réellement : page « équipe » ou mentions légales du site, registre officiel des entreprises (les dirigeants y sont publics en France), réseau professionnel. Vérifier qu'elle est toujours en poste, le jour même.
3. Une seule personne par compte et par semaine. Si deux personnes comptent, on les contacte l'une après l'autre, jamais ensemble.
4. Choisir un canal par contact : le réseau professionnel si la personne y est active et que le signal s'y voit, l'e-mail si l'adresse professionnelle est vérifiée, le téléphone pour un rappel après un premier échange.
5. Chercher l'adresse e-mail professionnelle et le téléphone seulement pour les comptes retenus. Un outil d'enrichissement (service payant qui retrouve des coordonnées) peut aider ; vérifier ensuite l'adresse avec un outil de vérification avant d'écrire, car un lot d'adresses fausses abîme la réputation de la boîte d'envoi. Noter la source de chaque coordonnée, pour pouvoir répondre à qui la demande.
6. Écrire dans le dossier, par code : le rôle, la source, la date de vérification, la confiance (haute, moyenne, basse), le canal. Le nom et les coordonnées ne s'écrivent dans aucun fichier du dossier : le workflow les donne à la personne dans la conversation, et elle les note dans son outil avec le code (colonne « code »).

**Réussite.** Chaque compte retenu a un contact dont le rôle correspond au problème, vérifié le jour même, avec un canal et une source.

#### Étape 5. Écrire le message (`05-message.md`)

1. Écrire pour chaque contact un premier message en quatre temps, court : le fait observé (le signal, précis et daté, que la personne reconnaît), pourquoi ce fait mène souvent à tel problème et ce que vous faites à ce sujet (une phrase), une preuve seulement si elle est réelle (un client semblable, un résultat vrai), puis une question simple, par exemple « est-ce un sujet pour vous en ce moment ? ».
2. Gabarit : « Bonjour [prénom], j'ai vu que [entreprise] [fait observé, avec sa date]. [Une phrase : le problème que ce fait annonce, et ce que vous faites.] [Une preuve réelle, si elle existe.] Est-ce un sujet pour vous en ce moment ? » Le prénom se met au moment de l'envoi, pas dans le dossier.
3. À éviter : la flatterie générique, la fausse familiarité, une promesse chiffrée sans preuve, une urgence inventée, un objet d'e-mail trompeur, une pièce jointe dans le premier message, plus d'une demande.
4. Écrire la séquence (la suite des messages à une même personne) : le premier message, puis au plus deux relances espacées de trois à sept jours. Chaque relance apporte quelque chose de nouveau (un autre fait, une ressource utile, une question plus simple), jamais « je me permets de relancer » seul.
5. Écrire la règle d'arrêt dans le même fichier : toute réponse, même négative, arrête la séquence de cette personne sur tous les canaux. Un refus ou une demande de désinscription met la personne sur une liste d'exclusion définitive, consultée avant chaque envoi futur.
6. Par e-mail, le message identifie l'expéditeur et propose un moyen simple de refuser les envois suivants (CNIL, page du 10/06/2026, vérifiée le 06/11/2026 : https://www.cnil.fr/fr/la-prospection-commerciale-par-courrier-electronique-sms-mms-et-automate-dappel ; en France, entre professionnels, l'intérêt légitime peut fonder le message s'il concerne la fonction de la personne).
7. Pour rédiger, `sales:draft-outreach` ou `small-business:outreach-composer`.
8. **Validation.** La personne relit tout le lot : chaque fait est exact et vérifiable, le ton est le sien, la demande est unique. Chaque message approuvé est marqué « validé » ; un message non marqué ne part pas. Les relances validées sont recopiées dans `relances.md`. C'est la validation qui vaut feu vert pour l'étape 6. Tant que la personne n'a pas validé, l'étape est `en attente` (« validation du lot »).

**Réussite.** Chaque message cite un fait daté exact, tient en quelques phrases, ne fait qu'une demande et porte la mention « validé » ; la séquence et la règle d'arrêt sont écrites.

#### Étape 6. Envoyer la séquence (`06-sequence.md`)

1. Établir la liste du jour par canal : d'abord les relances échues (celles dont la date de prochaine relance, dans le registre, est atteinte et dont le statut est encore « en séquence » ; leur texte est dans `relances.md`), puis les premiers messages, les meilleurs comptes d'abord. Avant chaque envoi, contrôler trois choses : le message est marqué « validé », la personne n'est pas sur la liste d'exclusion du registre, aucune conversation n'est déjà en cours avec elle.
2. Envoyer depuis le compte de la personne qui vend, à la main ou avec son outil d'envoi sur son feu vert écrit. Ne pas écrire un message libre à ce moment : seul part le texte validé. **Le workflow prépare la liste, il n'envoie rien lui-même** : l'étape est `en attente` (« envois à faire par la personne ») jusqu'à ce que la personne dise ce qui est parti. Une liste préparée n'est pas une liste envoyée.
3. Réseau professionnel. LinkedIn interdit les logiciels tiers qui automatisent l'activité du compte (page d'aide « Prohibited software and extensions », consultée le 06/11/2026 : https://www.linkedin.com/help/linkedin/answer/a1341387) ; un compte qui en utilise risque des restrictions. Envoyer donc à la main, à un rythme humain. Le plafond d'invitations dépend du compte et peut changer : commencer bas (par exemple cinq à dix par jour), ne monter que si le compte ne reçoit aucun avertissement, et s'arrêter au premier avertissement.
4. E-mail. Écrire depuis une vraie boîte professionnelle du nom de domaine de l'entreprise, avec les trois réglages qui prouvent que le message vient bien de ce domaine (SPF, DKIM et DMARC, à configurer chez l'hébergeur du nom de domaine). Monter le volume progressivement. Ajouter une façon simple de se désinscrire et traiter chaque désinscription tout de suite. Google exige de ses gros expéditeurs (plus de 5 000 messages par jour vers Gmail) ces réglages, une désinscription en un clic et un taux de plaintes pour spam sous 0,30 % (https://support.google.com/a/answer/81126, vérifié le 06/11/2026) : ces bonnes pratiques valent aussi pour de petits volumes.
5. Téléphone. Préparer la liste des appels du jour avec `small-business:call-list`. Les règles du démarchage téléphonique varient selon le pays : à vérifier avant d'appeler. Pas de SMS pour un premier contact.
6. Pour chaque envoi que la personne confirme, noter dans `06-sequence.md` : le code, le canal, la date, l'étape de la séquence (premier message, relance 1, relance 2) et la date de la prochaine relance, puis reporter cette date dans le registre. L'étape est `fait` quand tout ce qui était prévu est parti ; si une partie seulement est partie, la ligne `en attente` dit combien restent.

**Réussite.** Chaque envoi du jour correspond à un message validé, aucun plafond n'est dépassé, aucune personne de la liste d'exclusion n'a été contactée, chaque relance a une date.

#### Étape 7. Tenir la conversation jusqu'au rendez-vous (`07-reponses.md`)

Les réponses arrivent dans la boîte de la personne, pas dans le dossier. Le workflow n'en devine aucune : la personne colle ou résume ce qu'elle a reçu, et il les range par code. Sans réponse reçue, l'étape reste `en attente` (« réponses des prospects ») et les étapes 8 et 9 ne démarrent pas. Elle est `fait` quand chaque réponse reçue a sa catégorie, son brouillon relu et sa suite datée, et que la personne n'en attend plus avant la clôture du passage.

1. Classer chaque réponse dans une catégorie : intéressé, question ou objection, pas maintenant (à relancer à une date), mauvais contact (demander qui est la bonne personne), refus ou désinscription. Une réponse automatique d'absence ne compte pas comme réponse : la relance est décalée.
2. Répondre sous un jour ouvré. Une réponse arrête la séquence de la personne (règle de l'étape 5) : dans le registre, sa prochaine relance s'efface et son statut passe à « en conversation ». Un « pas maintenant » garde son statut et note sa date de reprise dans `07-reponses.md`, sans relance automatique. Un refus va sur la liste d'exclusion avec un mot de remerciement, rien d'autre, et son statut passe à « refus ».
3. Face à une objection, répondre avec un fait ou une preuve, sans insister. `sales:handle-objection` aide à construire la réponse.
4. Pour un intérêt, proposer deux ou trois créneaux réels de l'agenda, puis confirmer par écrit : date, durée, moyen. Un rappel la veille.
5. **Validation.** Le workflow écrit un brouillon de réponse pour chaque réponse reçue, dans `07-reponses.md`, sans nom (le prénom se met au moment de l'envoi). La personne relit chaque brouillon, le marque « validé », puis l'envoie elle-même : tant que ce n'est pas fait, l'étape reste `en attente`.
6. Dans `07-reponses.md`, noter par code : la catégorie, la décision prise, la date du prochain geste. Une fois le rendez-vous posé, le statut du registre passe à « rendez-vous » et l'affaire passe à `/conclure-une-vente:conclure-une-vente`.

**Réussite.** Aucune réponse n'attend plus d'un jour ouvré, chaque personne qui a répondu a une catégorie et une suite, chaque rendez-vous est dans l'agenda.

#### Étape 8. Tenir le fichier maître et le CRM (`08-suivi.md`)

1. Choisir un seul endroit pour les contacts (un CRM ou un tableur) et s'y tenir : une ligne par personne, avec statut (à contacter, contacté, en conversation, rendez-vous, refus, client), canal, date du dernier contact, prochaine action, source de la coordonnée, code `P` et signal à l'origine.
2. Avant d'ajouter une personne, chercher un doublon (même adresse e-mail, même profil, ou même entreprise et même nom). S'il existe, fusionner en gardant l'historique des deux fiches. Ne rien effacer : une fiche obsolète s'archive.
3. Mettre à jour la fiche après chaque envoi ou réponse, au plus tard à la fin de la journée.
4. Dans `08-suivi.md`, noter seulement l'outil utilisé et, pour la semaine, le nombre de fiches ajoutées, mises à jour et fusionnées. Le fichier ne contient aucune coordonnée.

**Réussite.** Chaque personne contactée a une fiche avec un statut et une prochaine date, il n'y a aucun doublon, et les codes `P` se retrouvent dans l'outil.

#### Étape 9. Mesurer et ajuster (`09-mesure.md`)

1. Compter, par canal et par signal : messages envoyés, réponses, réponses positives, rendez-vous obtenus, à partir de `06-sequence.md` et de `07-reponses.md`. Mesurer les réponses, pas les ouvertures d'e-mails, qui sont peu fiables. Sans envoi confirmé, il n'y a rien à mesurer : on écrit « non mesuré » et l'étape reste `en attente`.
2. Calculer deux taux : réponses sur envois, rendez-vous sur envois. Sous une trentaine d'envois par ligne, ne pas conclure : on note une tendance.
3. Décider pour chaque signal et chaque canal : continuer, corriger ou arrêter. Arrêter seulement après assez d'envois (au moins une trentaine, à ajuster) sans résultat.
4. Changer une seule chose par semaine (l'angle, le message, le signal ou le canal), sinon on ne sait pas ce qui a joué. Les affaires gagnées et perdues s'analysent dans `/piloter-le-pipeline:piloter-le-pipeline`.
5. Écrire trois lignes pour la semaine suivante : ce qui a marché, le changement choisi, la question qui reste.

**Réussite.** Un tableau chiffré par signal et par canal, une décision écrite pour chacun, un seul changement choisi pour la semaine suivante.

### 2. Clore un passage

À la fin de chaque séance, on note au journal l'état (fait, en attente et de quoi, prochaine action) et les décisions prises.

## Ce qui manque

Aucune compétence publique de la liste ne couvre le choix de la cible, le repérage des signaux, la recherche du bon contact, l'envoi, le tri des réponses, le suivi ni la mesure : la méthode ci-dessus les remplace, avec ses critères de réussite. Restent hors de ce workflow : l'envoi lui-même (la personne envoie), les réglages du nom de domaine pour l'e-mail (chez son hébergeur), et le choix d'un outil d'enrichissement ou de vérification d'adresses (service payant, au choix de la personne).

## Frontières

| Demande | Va à |
|---|---|
| Préparer le rendez-vous obtenu et conclure la vente | `/conclure-une-vente:conclure-une-vente` |
| Suivre un pipeline déjà rempli et développer ses clients | `/piloter-le-pipeline:piloter-le-pipeline` |
| Écrire et envoyer des e-mails automatiques ou une newsletter | `/envoyer-des-e-mails:envoyer-des-e-mails` |
| Se faire connaître sur LinkedIn par ses publications | `/publier-sur-linkedin:publier-sur-linkedin` |
| Organiser l'équipe commerciale (objectif, rôles, incitation) | `/organiser-sa-force-de-vente:organiser-sa-force-de-vente` |

Les workflows cités ici se trouvent dans le même dépôt de plugins que celui-ci.

Pour faire monter le système complet, de la cible aux réponses, voir https://zerogravity.builders.
