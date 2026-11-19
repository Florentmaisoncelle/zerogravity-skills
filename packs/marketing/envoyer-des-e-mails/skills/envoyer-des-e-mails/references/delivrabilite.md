# Délivrabilité : authentifier son domaine et monter en volume

La délivrabilité, c'est la part de vos e-mails qui arrive dans la boîte de réception et non dans les courriers indésirables. Elle dépend de trois choses : prouver que vous êtes bien l'expéditeur (SPF, DKIM, DMARC), donner à chacun une sortie simple (désinscription), et ne pas déclencher de plaintes (liste propre, envois attendus, volume progressif).

Sources : les exigences de Google pour les expéditeurs (https://support.google.com/a/answer/81126 et https://support.google.com/a/answer/14229414, vérifiées le 06/11/2026) et celles de Yahoo (https://senders.yahooinc.com/best-practices/). Elles visent les gros expéditeurs (plus de 5 000 messages par jour vers Gmail) mais les bonnes pratiques valent pour tous. Les chiffres marqués « repère » sont des usages courants, pas des règles publiées par un fournisseur.

## Ce que prouve chaque sigle

| Sigle | Ce qu'il prouve | Où il se publie |
|---|---|---|
| SPF | Le serveur qui envoie est autorisé à envoyer pour ce domaine | Un enregistrement DNS de type TXT à la racine du domaine, qui commence par `v=spf1` |
| DKIM | Le message a été signé par le domaine et n'a pas été modifié en route | Une clé publique dans le DNS, à l'adresse `<sélecteur>._domainkey.<votre domaine>`, donnée par l'outil d'envoi |
| DMARC | Dit au destinataire quoi faire quand SPF et DKIM ne correspondent pas au domaine de l'adresse d'expéditeur, et où envoyer les rapports | Un enregistrement TXT à l'adresse `_dmarc.<votre domaine>` |

Deux précisions qui évitent les pannes :

- **L'alignement.** Pour DMARC, il ne suffit pas que SPF ou DKIM passe : le domaine qui a passé doit être le même que celui de l'adresse d'expéditeur (le « De : »). Un outil d'envoi qui signe avec son propre domaine, sans votre clé, fait échouer DMARC.
- **Un seul SPF par domaine.** Deux enregistrements SPF rendent les deux invalides. Si vous utilisez une messagerie (par exemple Google Workspace) et un outil de newsletter, fusionnez-les en un seul enregistrement avec plusieurs `include:`. SPF accepte au plus 10 interrogations DNS imbriquées : au-delà, il échoue.

## Ordre de mise en place

1. **Choisir le domaine d'envoi.** Pour les envois en nombre, un sous-domaine dédié (par exemple `news.votredomaine.fr`) protège la réputation du domaine principal, celui des e-mails du quotidien.
2. **Lire la page « authentification du domaine » de l'outil d'envoi.** Elle donne les enregistrements exacts à publier (SPF, DKIM, souvent aussi un enregistrement de retour). Ne pas les inventer.
3. **Les publier** dans l'espace DNS du domaine, chez le registrar ou l'hébergeur : ajouter un enregistrement, choisir le type (TXT ou CNAME comme indiqué), recopier le nom et la valeur. Beaucoup d'interfaces ajoutent le domaine elles-mêmes : on saisit alors `_dmarc` et non `_dmarc.votredomaine.fr`. La propagation prend de quelques minutes à quelques heures, parfois jusqu'à 48 heures.
4. **Publier DMARC en observation** : `v=DMARC1; p=none; rua=mailto:ADRESSE@votredomaine.fr`. La politique `none` ne bloque rien : elle demande seulement des rapports. Google l'accepte.
5. **Tester** (voir plus bas). Ne passer à la suite que si SPF, DKIM et DMARC répondent « pass ».
6. **Observer deux à quatre semaines** les rapports ou les résultats de test : les rapports DMARC sont des fichiers techniques ; la plupart des outils d'envoi et plusieurs services gratuits les rendent lisibles. Chercher toute source légitime qui échoue (outil de facturation, formulaire du site, CRM) et la corriger.
7. **Durcir** quand toutes les sources légitimes passent : d'abord `p=quarantine` (les messages douteux vont en indésirables), éventuellement en commençant par une part des messages avec `pct=10`, puis `p=reject` (les messages douteux sont refusés). Reculer à `none` au moindre message légitime perdu.

## Tester avec un envoi à soi-même

1. Envoyer un message réel depuis l'outil, avec son lien de désinscription, vers une adresse Gmail personnelle.
2. Dans Gmail, ouvrir le message, le menu à trois points, « Afficher l'original ».
3. Lire l'entête : SPF, DKIM et DMARC doivent dire `PASS`. Vérifier aussi que les entêtes `List-Unsubscribe` et `List-Unsubscribe-Post` sont présents (ils permettent à Gmail d'afficher un bouton « Se désabonner »).
4. Un `FAIL` ou un `NEUTRAL` : revenir à l'étape 2 ou 3 de l'ordre ci-dessus. La cause la plus fréquente est un enregistrement mal copié ou un deuxième SPF.
5. Pour des tests plus larges (spam, liens, poids), l'outil d'envoi ou un service de test gratuit donne une note ; elle guide, elle ne remplace pas le test réel.

## Désinscription

- **Un lien visible** dans chaque message, en bas, qui désinscrit en un clic, sans connexion ni question.
- **Les entêtes d'un clic** `List-Unsubscribe` et `List-Unsubscribe-Post: List-Unsubscribe=One-Click` (norme RFC 8058) : la plupart des outils d'envoi sérieux les ajoutent seuls, il suffit de le vérifier dans l'entête du message de test. Google les exige des messages marketing de ses gros expéditeurs.
- **Un traitement rapide.** Google recommande de traiter les demandes sous 48 heures. En pratique, le faire tout de suite : l'outil le fait seul, sauf pour une demande reçue par réponse ou par un autre canal, qu'il faut saisir à la main.
- **La liste de suppression** : toutes les personnes désinscrites, celles qui ont signalé un message comme indésirable et les adresses en échec définitif. Elle vit dans l'outil d'envoi. Avant toute importation de contacts (fichier, CRM, salon), on la compare : réimporter une personne désinscrite est la faute la plus courante et la plus coûteuse.

## Monter en volume avec un domaine neuf

Un domaine ou une adresse d'envoi sans historique n'a aucune réputation : il faut la construire. Un plan type sur trois à quatre semaines (repères usuels, à adapter) :

| Période | Envoi par jour | À qui |
|---|---|---|
| Jours 1 à 3 | 20 à 50 | Les personnes les plus engagées : clients, inscrits récents qui ont ouvert ou cliqué |
| Jours 4 à 10 | Doubler tous les deux à trois jours | Les mêmes, puis les inscrits actifs |
| Semaines 2 à 4 | Doubler tant que les signaux restent bons | Le reste de la liste, par tranches |

À chaque palier, regarder avant de monter : plaintes pour spam (Google demande de rester sous 0,30 % et recommande moins de 0,10 %, mesurés dans Google Postmaster Tools), échecs définitifs (repère : moins de 2 %), désinscriptions. Si un seuil est dépassé, on ne monte plus et on revient au palier précédent jusqu'à ce que les chiffres redescendent.

## Nettoyer la liste

- Retirer à l'instant toute adresse en échec définitif (adresse inexistante).
- Une personne qui n'a rien ouvert ni cliqué depuis six mois (repère) reçoit une série de deux ou trois messages de réveil (voir `marketing-skills:emails`), puis est retirée si elle ne réagit pas. Les ouvertures sont un indicateur imparfait (certains lecteurs de messagerie les déclenchent seuls), les clics et les réponses comptent davantage.
- Ne jamais acheter ni louer une liste pour une newsletter.
- Les adresses de rôle (contact@, info@) des entreprises ne s'importent qu'après vérification qu'une personne les lit.

## Tester l'objet

Découper la liste au hasard en deux parts égales, envoyer deux objets différents (une seule différence à la fois), à la même heure. Le résultat n'a de sens qu'avec quelques centaines de destinataires par part ; en dessous, on tire plutôt un objet clair et précis. Juger sur les clics et les réponses plutôt que sur les ouvertures. Critère d'arrêt : retenir un objet seulement si l'écart se répète sur deux envois ; sinon, c'est du hasard et on garde le plus simple.
