---
name: recruter
description: >-
  Quand on veut recruter un collaborateur de bout en bout (embaucher un commercial ou un développeur, ouvrir un poste, trier les candidatures d'une annonce, préparer l'arrivée d'une recrue) → affiche l'état du recrutement calculé depuis le dossier `projet-recrutement/`, puis déroule cinq étapes dans l'ordre : décider d'embaucher, écrire le paquet de recrutement, trier et répondre à tous, faire l'offre, préparer l'arrivée. Ce qui manque est dit franchement (diffusion de l'annonce, relance par délai, contrat de travail français, déclaration préalable à l'embauche et paie). Se lance par `/recruter:recruter`. Déclencheurs : « recruter », « embaucher », « ouvrir un poste », « fiche de poste », « trier des candidatures », « grille d'entretien », « lettre d'offre », « intégrer une recrue », « où en est mon recrutement ». Pas pour chercher un emploi soi-même (le côté candidat). Pas pour clarifier les rôles d'une équipe sans embauche : `operations:process-doc`.
---

# Recruter, de la décision d'embaucher au premier mois

## Ce que ce workflow résout

Recruter demande cinq gestes dans l'ordre, et aucune compétence publique ne les couvre tous. Sans méthode, on écrit une annonce avant que le besoin soit chiffré, on note des CV sans grille, on oublie de répondre aux candidats écartés, ou on prend une compétence de recherche d'emploi (le côté candidat) pour une compétence de recrutement. Ici : l'ordre, l'état, le choix tranché, et les trous dits franchement.

**Résultat attendu** : un poste chiffré, une annonce et une grille, chaque candidat trié et répondu, une offre en brouillon de signature, une arrivée préparée. Un dossier `projet-recrutement/<poste>/` qui dit à tout moment où on en est, sans un seul nom de candidat dedans.

**Pays.** Les repères de droit du travail de ce workflow valent pour la France. Dans un autre pays, ils sont à vérifier avec un spécialiste local.

## Stratégie

1. **L'état d'abord**, toujours calculé depuis le journal et les fichiers de `projet-recrutement/<poste>/`, jamais recopié.
2. **Un choix par étape.** Chaque étape a sa compétence par défaut et sa règle de choix, dans la table plus bas, qui vient de `references/workflow.json`. Une compétence qui écrit plusieurs documents (le paquet de l'étape 2 contient aussi le modèle de lettre d'offre et le guide d'entretien) les fournit aux étapes suivantes : elles en reprennent la partie nommée dans leur règle.
3. **L'ordre protège la décision** : pas d'annonce sans besoin chiffré, pas de note sans grille, pas de refus décidé par un score. Sauter une étape reste possible sur demande (si le besoin est déjà tranché, l'étape 1 est sans objet) ; le journal dit laquelle et pourquoi.
4. **Une seule validation, à l'étape 2** : le paquet de recrutement (annonce, guide d'entretien, grille). Si l'étape 1 est faite, ce n'est donc pas la première étape qui est validée. Ensuite tout se déroule. Restent à la personne qui recrute : publier l'annonce, mener les entretiens, décider de l'embauche, envoyer chaque message, signer. La validation s'écrit en tête de `02-paquet.md` (« Validé le AAAA-MM-JJ par <fonction> ») et au journal : sans elle, l'étape 2 reste `en attente`.
5. **Aucune donnée personnelle dans le dossier d'état.** Les candidats s'y écrivent par un code (`C01`, `C02`…) ; noms, CV et coordonnées restent dans l'outil de la personne qui recrute (boîte mail, logiciel de suivi), qui garde aussi la correspondance entre le code et le candidat. Le workflow donne le code suivant à chaque CV qu'on lui montre et le dit à la personne, qui le note dans son outil à côté du candidat ; un code n'est jamais réutilisé. Ce workflow ne lit jamais la correspondance : il ne traduit pas un code en nom.
6. **Le droit, en France, en quelques repères** (à faire valider par un juriste ou le cabinet comptable avant d'agir) :
   - l'article L1132-1 du Code du travail interdit d'écarter une personne d'une procédure de recrutement pour un des critères qu'il liste (notamment l'origine, le sexe, l'âge, la situation de famille ou la grossesse, l'orientation sexuelle, l'identité de genre, l'état de santé, le handicap, les opinions politiques, les activités syndicales, les convictions religieuses, l'apparence physique, le lieu de résidence) ; la liste complète est dans l'article (https://code.travail.gouv.fr/code-du-travail/l1132-1, ouvert le 06/11/2026, page mise à jour le 01/09/2022) ;
   - le RGPD s'applique aux candidatures traitées par un établissement dans l'UE (CNIL, https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre1#Article3, vérifié le 06/11/2026) : informer les candidats de l'usage de leurs données et ne pas garder leurs CV sans limite. La durée de conservation à retenir est à vérifier.
7. **Chaque passage se clôt au journal** : ce qui est fait, ce qui reste, la prochaine action.
8. **Sans accès au web**, le workflow ne peut pas relire les pages de droit citées plus haut ni plus bas : il le dit, laisse ces repères marqués « à vérifier » (avec le cabinet comptable ou un juriste) et n'en complète aucun de mémoire.

<!-- prerequis:debut -->
## Prérequis

Ce workflow s'appuie sur des compétences publiques, installées à part. Aucune n'est indispensable : si l'une manque, le workflow le dit et fait l'étape à la main. Faire l'étape à la main veut dire suivre sa règle de choix, écrire ce qu'elle doit rendre (dans le fichier de l'étape, ou dans la réponse quand le workflow n'a pas de dossier) et dire ce qui reste à la charge de la personne.

```text
/plugin marketplace add addyosmani/agent-skills
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin install agent-skills@addy-agent-skills
/plugin install human-resources@knowledge-work-plugins
/plugin install operations@knowledge-work-plugins
/plugin install sales@knowledge-work-plugins
/plugin install small-business@knowledge-work-plugins
```

Les workflows cités ici sont dans le même dépôt (le dépôt s'ajoute une fois : `/plugin marketplace add Florentmaisoncelle/zerogravity-skills`) :

```text
/plugin install cadrer-un-chantier@zerogravity
/plugin install creer-une-app@zerogravity
/plugin install organiser-sa-force-de-vente@zerogravity
```
<!-- prerequis:fin -->

## Étapes

### 0. Le dossier, puis l'état (lecture seule)

**Le dossier.** Un recrutement vit dans le dossier de l'entreprise qui recrute : `projet-recrutement/` à sa racine, un sous-dossier par poste, nommé par un mot court (`projet-recrutement/<poste>/`, par exemple `projet-recrutement/commercial/`), même s'il n'y a qu'un poste. Chaque poste a son propre journal et ses propres fichiers. Dossier absent ou vide : il n'y a encore rien de fait, l'état est « étape 1 » et le dossier se crée au premier passage. Si le dossier courant n'est pas celui de l'entreprise qui recrute, le dire en une ligne et demander où elle vit : rien ne s'écrit avant.

**Quel poste ?** Par défaut, le poste le plus récent dont le recrutement n'est pas terminé ; ou celui que la personne nomme. Si tous sont terminés, ou si elle ouvre un nouveau poste, on demande d'abord son nom (un mot court, fixé une fois et jamais changé), on crée le suivant et on repart à l'étape 1. Au premier passage d'un poste, une fois le nom fixé, on demande si le besoin est déjà tranché : si oui, le journal reçoit tout de suite `AAAA-MM-JJ · 01 · sans objet · besoin déjà tranché`.

**L'état**, calculé depuis le journal et les fichiers de `projet-recrutement/<poste>/` (exemple inventé) :

```text
Poste              Commercial terrain
Étapes             01 s.o.  02 ✓  03 att.  04 -  05 -
Candidats          12 reçus · 4 convoqués · 3 à clarifier · 2 refus rédigés · 3 refus envoyés
Dernière décision  2026-03-18 · 03 · en attente · 2 refus à envoyer, 3 réponses de candidats
Étape suivante     03 Trier, répondre, convoquer (en attente : 2 refus à envoyer, 3 réponses de candidats)
```

- Les compteurs « Candidats » viennent du tableau de suivi écrit en tête de `03-tri.md` : une ligne par candidat, avec son code, la date de réception (« Reçu le »), la note par critère de la grille et son statut. Les statuts sont : à trier, à clarifier, convoqué, refus rédigé (écrit, pas encore envoyé), refus envoyé, retenu. « Reçus » est le nombre de lignes ; chaque autre nombre est celui des lignes de ce statut, et leur somme égale « reçus ». Le journal ne contredit pas ce tableau.
- Les fichiers sont dans `projet-recrutement/<poste>/` : `01-besoin.md`, `02-paquet.md`, `03-tri.md`, `04-offre.md`, `05-arrivee.md`.
- Le journal `projet-recrutement/<poste>/journal.md` a une ligne par décision : `AAAA-MM-JJ · NN · fait | en attente | sans objet | sautée | corrigée · <une phrase>`.
- Pour chaque étape, la dernière ligne du journal qui la nomme fait foi. `✓` : cette ligne dit `fait` ou `corrigée` et le fichier de l'étape existe. `s.o.` : elle dit `sans objet` ou `sautée` (l'étape n'est plus proposée). `-` : aucune ligne, ou le fichier manque.
- `corrigée` : l'étape est refaite après une correction ; elle reste `✓` et la ligne dit ce qui a changé. `sautée` : la personne a choisi de passer ; la ligne dit pourquoi.
- `en attente` : l'étape est préparée, mais elle dépend d'un geste ou d'une réponse qui arrive hors de la conversation. La ligne du journal dit ce qu'on attend et de qui. L'état l'affiche `att.` avec ce texte : l'étape n'est pas `✓`, parce que préparé n'est pas fait. Le workflow s'arrête là et le dit ; il n'invente jamais la suite (ni réponse, ni résultat, ni geste qu'on ne lui a pas confirmé). Quand la personne apporte ce qui est arrivé, la ligne `fait` suit. Ici : la validation du paquet (étape 2) ; la publication de l'annonce par la personne, puis l'arrivée des candidatures, qui ne viennent qu'après (étape 3) ; l'envoi des réponses et la réponse des candidats (étape 3) ; les entretiens, la réponse du candidat à l'offre et la signature (étape 4) ; le premier jour (étape 5).
- L'étape suivante est la première étape `-` ou `att.`, dans l'ordre (devant une étape `att.`, on demande d'abord où en est l'attente). Si aucune ne l'est, le recrutement de ce poste est terminé et on peut ouvrir un nouveau poste. Avant de clore un poste, aucun candidat ne reste « à clarifier » : la personne le convoque ou le refuse, ou on note « dossier clos, sans réponse » avec la date.

**Une question n'est pas un ordre.** « Où en est mon recrutement ? » : on affiche l'état et la prochaine action, puis on s'arrête. « Recruter un commercial », « continue » ou « déroule » : on enchaîne jusqu'à la première étape en attente, puis on s'arrête et on le dit.

**Une demande au milieu du chemin** (« trie ces 40 CV »). L'étape 3 exige la grille de l'étape 2. Sans `02-paquet.md`, on fait d'abord la grille de tri (la partie « grille » de `small-business:job-post-builder`, courte), on la fait valider, puis on trie. Jamais une note sans grille.

### 1. Lancer l'étape suivante

Lire l'étape dans la table, appliquer sa règle de choix, invoquer la compétence retenue, écrire dans le fichier de l'étape sa sortie (sans nom de candidat), inscrire « fait » au journal (ou `en attente`, voir plus haut), puis passer à la suivante sans redemander. Une étape qui porte un « Manque » le dit à la personne qui recrute, avec le geste humain qui le comble : le cabinet comptable pour la déclaration préalable à l'embauche et la paie, un juriste pour le contrat de travail. Une étape faite à la main ou arrêtée sur un geste humain écrit quand même son fichier : ce qui est prêt, ce qui attend la personne, qui s'en charge.

<!-- etapes:debut -->
| # | Étape | Compétences | Règle de choix |
|---|---|---|---|
| 1 | Décider d'embaucher (seulement si le besoin n'est pas déjà tranché) | Chiffrer la charge et décider d'embaucher : `operations:capacity-plan` · Clarifier le besoin avec le dirigeant : `agent-skills:interview-me` · Prévoir les effectifs et la place du poste : `human-resources:org-planning` | Les chiffres d'abord : on ne rédige pas d'annonce pour un besoin qui n'a passé ni la charge, ni le budget, ni la date d'arrivée voulue. La place du poste dans l'équipe (qui décide, qui est prévenu, qui remplace) s'écrit en quelques lignes dans le fichier de l'étape ; le tableau détaillé des responsabilités se fait à l'étape 5 avec operations:process-doc. Si le besoin est déjà tranché, le journal note l'étape comme sans objet dès le premier passage. |
| 2 | Écrire le paquet de recrutement | Écrire l'annonce de poste : `small-business:job-post-builder` · Diffuser l'annonce : à la main | Une seule compétence pour tout le paquet, y compris le modèle de lettre d'offre et le brouillon de signature, qui servent à l'étape 4. Publier l'annonce reste le geste du recruteur. Le modèle de lettre est écrit pour le droit américain : ses clauses se remplacent par celles du droit français. C'est ici que tombe l'unique validation du workflow : la personne valide le paquet (annonce, guide d'entretien, grille) avant que quoi que ce soit se publie, et sa validation s'écrit en tête du fichier de l'étape ; tant qu'elle manque, l'étape est en attente. |
| 3 | Trier, répondre, convoquer | Trier les CV sur la grille : `small-business:hiring-screener` · Suivre le pipeline des candidats : à la main · Convoquer et placer les entretiens au calendrier : `sales:schedule-meeting` | Rien ne se note hors de la grille de l'étape 2. Un fait manquant place le candidat dans « à clarifier », il ne l'écarte pas. Aucun refus n'est décidé par un score. À lire avec les critères interdits du droit français (Code du travail, article L1132-1, https://code.travail.gouv.fr/code-du-travail/l1132-1, vérifié le 06/11/2026). Les noms des candidats restent hors du dossier d'état : le tri s'écrit avec des codes (C01, C02, etc.) dans un tableau en tête du fichier de l'étape (code, reçu le, note par critère, statut parmi : à trier, à clarifier, convoqué, refus rédigé, refus envoyé, retenu) ; le workflow donne le code suivant à chaque CV qu'on lui montre, la personne le note dans son outil et garde la correspondance, que ce workflow ne lit jamais. Les candidatures n'arrivent qu'après la publication de l'annonce : sans candidature reçue, l'étape est en attente et le workflow n'invente aucun candidat ; elle l'est aussi tant que des refus rédigés ne sont pas envoyés ou que des candidats restent à clarifier. |
| 4 | Faire l'offre et signer | Fixer la rémunération : `human-resources:comp-analysis` · Chiffrer et écrire la lettre d'offre : `human-resources:draft-offer` · Relire avant la signature : `small-business:contract-review` · Écrire le contrat de travail français : à la main | draft-offer chiffre le paquet, écrit la lettre et prépare la négociation ; le modèle de lettre de l'étape 2, s'il est déjà rempli, en donne la forme ; contract-review relit le texte final. Les entretiens se mènent avec le guide de l'étape 2 ; la décision revient au recruteur ; la lettre part en brouillon de signature et l'envoi reste un clic du dirigeant. Le fichier de l'étape s'ouvre sur la décision du recruteur : code du candidat retenu et raisons tirées de la grille, sans nom. Les entretiens se mènent avec le guide de l'étape 2 ; les notes d'entretien se prennent sur la grille et se rangent par code, sans nom, dans une section « Entretiens » du fichier de l'étape : avec la grille, elles sont la source de la décision, qui revient au recruteur ; avant de chiffrer, le fichier note la fourchette de rémunération retenue et la convention collective de l'entreprise (ou « aucune »), qui peut imposer des minimums : à vérifier avec le cabinet comptable ; la lettre part en brouillon de signature et l'envoi reste un clic du dirigeant. |
| 5 | Préparer l'arrivée et les trente premiers jours | Préparer l'arrivée et les trente premiers jours : `human-resources:onboarding` · Écrire les procédures et le tableau des responsabilités : `operations:process-doc` · Faire les formalités françaises d'embauche : à la main | human-resources:onboarding fait le plan d'arrivée, avec sa liste d'avant le premier jour (comptes, matériel, parrain) ; la checklist d'arrivée de l'étape 3 (papiers, paie, accès, matériel) le complète. On y ajoute les points français : papiers, déclaration préalable à l'embauche (obligatoire avant toute embauche, envoyée à l'Urssaf au plus tôt 8 jours avant et avant la mise au travail effective, https://www.service-public.gouv.fr/entreprendre/vosdroits/R57098, vérifié le 06/11/2026), mutuelle (à vérifier), paie. operations:process-doc écrit les procédures qui manquent. On vérifie la veille que les accès marchent. Les accès sensibles et la validation du manager restent des gestes humains. |
<!-- etapes:fin -->

### 2. Clore un passage

À la fin de chaque séance, on note au journal l'état (fait, en attente et de quoi, prochaine action) et les décisions prises. Une compétence qui a déçu à une étape se note aussi : on rouvre alors le choix de cette étape.

## Ce qui manque

- **Diffuser l'annonce** (étape 2) : France Travail, Welcome to the Jungle, Indeed, LinkedIn. Aucune compétence ne publie, c'est le geste du recruteur.
- **Relancer par délai** (étape 3) : rien ne repère un candidat resté trop longtemps à une étape, et il n'y a pas d'import depuis un outil de suivi des candidatures. On tient le suivi à la main : au début de chaque passage, on relit le tableau de `03-tri.md` et on signale tout candidat sans réponse depuis plus d'une semaine.
- **Le contrat de travail français** (étape 4) : CDI, CDD, période d'essai, convention collective. À faire avec le cabinet comptable ou un juriste.
- **La partie française de l'embauche** (étape 5) : la déclaration préalable à l'embauche est obligatoire avant toute embauche ; elle s'envoie à l'Urssaf au plus tôt 8 jours avant l'embauche et avant la mise au travail effective, et elle sert aussi à demander la visite d'information et de prévention (https://www.service-public.gouv.fr/entreprendre/vosdroits/R57098, ouvert le 06/11/2026, page vérifiée par ses auteurs le 17/03/2026 ; certains dispositifs simplifiés pour petites entreprises la remplacent). La mutuelle et la paie sont à vérifier avec le cabinet comptable ou l'outil de paie ; les compétences américaines de paie ne conviennent pas.

## Frontières

Les workflows cités ici se trouvent dans le même dépôt de plugins que celui-ci.

| Demande | Va à |
|---|---|
| Chercher un emploi, postuler, préparer un entretien comme candidat | hors de ce workflow : c'est le côté candidat |
| Clarifier les rôles d'une équipe sans embauche | `operations:process-doc` |
| Organiser une équipe commerciale (objectif, rôles, incitation) | `/organiser-sa-force-de-vente:organiser-sa-force-de-vente` |
| Cadrer un projet ou un chantier, qui n'est pas un recrutement | `/cadrer-un-chantier:cadrer-un-chantier` |
| Créer une application ou un SaaS | `/creer-une-app:creer-une-app` |
