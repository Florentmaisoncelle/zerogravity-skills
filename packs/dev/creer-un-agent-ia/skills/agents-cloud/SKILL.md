---
name: agents-cloud
description: "Méthode pour bâtir et exploiter un agent qui tourne dans le cloud : choisir son type (assistant, planifié, déclenché par un événement, n8n ou Make), poser le modèle commun (modèles, budget, traces, clé, information IA), puis le configurer, le déployer, l'essayer pour de vrai et le faire évoluer. Rend un agent hébergé, borné en coût, observable et coupable à tout moment. Déclencheurs : « agent cloud », « agent hébergé », « agent déclenché », « webhook », « agent planifié », « agent n8n », « agent Make », « déploie l'agent », « essaie l'agent »."
---

# Agents cloud : une seule méthode pour les agents hébergés

Un agent cloud tourne sans ton ordinateur : un visiteur lui parle, un événement le réveille, une horloge le lance. Le risque n'est pas de le faire marcher une fois, c'est de le laisser tourner sans plafond, sans trace et sans moyen de l'arrêter. Cette méthode pose les mêmes règles pour tous les agents hébergés, quel que soit leur type.

## Ce qu'il faut avoir

- Un dossier de projet versionné (le code de l'agent et ses tests).
- Un hébergement pour les fonctions serveur (Supabase Edge Functions, Cloudflare Workers, Vercel Functions ou équivalent) et une base pour les traces.
- Une clé d'API du modèle, rangée côté serveur.
- Pour le type no-code : un compte n8n ou Make.

## 1. Choisir le type d'agent

Le choix local ou cloud, et celui entre no-code et code, se fait avant (`creer-un-agent-ia:creer-un-agent-ia`, étape de choix du type ; `creer-un-agent-ia:choisir-agent-ou-automatisation`). Une fois le cloud retenu :

| Type | Comment on le bâtit |
|---|---|
| Assistant ou agent d'entretien | une fonction serveur appelle le modèle ; la personne dialogue sur une page web |
| Déclenché par un événement | une fonction reçoit l'événement (rendez-vous, paiement, formulaire), **vérifie sa signature**, répond vite, puis lance le travail en tâche de fond |
| Planifié | une tâche planifiée de la base (pg_cron par exemple) appelle une fonction ; ou une routine cloud du fournisseur quand l'agent n'a pas besoin de ta base |
| Sur n8n ou Make | le flux vit sur l'outil ; l'agent et le flux se parlent par un MCP ou un webhook (`creer-un-agent-ia:n8n-workflow-builder` pour n8n) |

Écrire pour chaque agent **ce qu'il ne fait pas, et qui le fait**. Ouvrir un agent en ligne ne supprime pas forcément une routine existante : un agent qui prépare une analyse mais n'écrit ni le message ni la proposition laisse en place la routine qui les écrit. Contrôle : quelle routine ce nouvel agent remplace-t-il vraiment ?

## 2. Le modèle commun

Tout agent d'entretien suit ces six règles. Un agent qui en manque une ne part pas en ligne.

1. **Un grand modèle mène la conversation.** Il pose les relances, fait le diagnostic, le plan d'action. Pas de modèle conseiller en plus si le grand modèle mène déjà : il n'apporte rien et coûte. Effort par défaut ; réflexion étendue seulement pour un livrable long.
2. **Un petit modèle lit les documents.** Un agent à part, aux outils de lecture seuls (lire, lister, chercher), que l'agent principal appelle. Il ne peut rien modifier ni rien faire sortir.
3. **Un plafond de budget par conversation**, vérifié côté serveur. À 80 % du plafond, l'agent conclut au lieu de continuer. Ajouter un plafond par jour pour toutes les conversations ensemble. Mesure ta consommation sur un essai complet avant de fixer les chiffres.
4. **Des traces lisibles** : chaque message, chaque étape et chaque coût sont enregistrés en base et se relisent dans la conversation elle-même, avec ses boutons pour l'arrêter.
5. **La clé reste côté serveur.** La fonction lit la clé ; les outils du poste passent par un relais de la fonction, jamais par une clé copiée sur une machine. Une clé ne s'affiche jamais et ne se colle jamais dans un chat.
6. **L'information IA dès le premier message.** Toute personne qui échange avec l'agent apprend, clairement et au début, qu'elle parle à une IA (obligation d'information du règlement européen sur l'IA, applicable depuis août 2026 : à vérifier dans la documentation officielle pour ton cas).

Et un moyen de le couper : un interrupteur par agent, testé.

## 3. Les règles de conception

- **Le web se fait côté serveur, pas dans l'agent.** Un agent qui lit des pages ne doit jamais pouvoir faire sortir une donnée. Garde son environnement d'exécution fermé (réseau limité) ; la fonction fait la recherche web, range le résultat dans une note, et la montre à l'agent. Autoriser des hôtes pour la recherche ouvre aussi le bac à sable : à vérifier dans la documentation du fournisseur.
- **Un long document ne se fait pas réécrire en entier par le modèle.** Le modèle rend les textes de chaque emplacement en JSON, le code remplit le gabarit. Un document HTML complet dépasse vite la limite de sortie ; une liste de textes aussi si elle est longue : prévoir une limite de sortie large et mesurer.
- **Les calculs se font dans le code, jamais par le modèle** (un gain, une somme, un taux). Le modèle relit, le code calcule.
- **Un modèle peut refuser certains réglages** (choix d'outil forcé, par exemple). Ne pas l'imposer ; laisser le choix libre et nommer l'outil dans la consigne. À vérifier dans la documentation du modèle retenu.
- **Un événement se reçoit vite.** Vérifier la signature, enregistrer, répondre, puis travailler en tâche de fond ; sinon l'émetteur relance et l'on traite deux fois. Rendre le traitement idempotent (même événement, même résultat).
- **Le secret d'un webhook ne se tape jamais.** Génère-le, pose-le côté serveur, copie-le dans le presse-papiers sans l'afficher, colle-le dans l'outil émetteur.

## 4. Les gestes, dans l'ordre

1. **Changer un modèle ou la consigne** : ces réglages vivent dans un seul fichier de la fonction (constantes des modèles, texte de la consigne). Lancer les tests de la fonction avant tout déploiement.
2. **Préparer l'agent** chez le fournisseur : environnement, agent de lecture, agent principal. Créer ou mettre à jour par nom : une consigne changée donne une nouvelle version du même agent, jamais un second agent. Écrire l'identifiant et la version dans un manifeste qui reste hors du dépôt.
3. **Poser les secrets** (identifiants de l'agent, version, clé) côté serveur, par l'interface ou l'API de l'hébergeur.
4. **Déployer** : tests verts d'abord, jamais une commande chaînée qui déploie après un test rouge. Vérifier que ton dossier n'est pas en retard sur la branche principale : un déploiement depuis un dossier en retard efface le travail des autres.
5. **Essayer pour de vrai** (voir ci-dessous).
6. **Montrer un changement** sur une copie de test de la page avant de publier ; ne publier qu'après relecture.
7. **Clore un essai** : un parcours d'essai arrêté en route se ferme (état « perdu » avec la raison), sinon le tableau de bord le montre « en cours » et la fonction le relit sans fin. Un essai joué sur le vrai site se marque « essai » tout de suite.

## 5. L'essai réel

Des tests verts ne suffisent pas : sur un agent de ce type, un essai réel a trouvé cinq défauts malgré plus de 270 tests verts, et un autre en a trouvé deux malgré 200 tests à faux modèle. Les tests à faux modèle ne voient pas ce qu'un vrai appel révèle.

- Joue un parcours complet avec un faux prospect écrit une fois et rejouable ; mesure le coût réel.
- Une fonction déclenchée s'essaie par son vrai appel, avec son vrai secret lu au coffre du serveur, jamais affiché.
- Les sorties d'outil disent la raison d'un échec ; aucun mode dangereux ne s'active par omission d'une option ; les commandes exactes sont écrites dans le fichier de consigne d'un petit modèle.
- Contrôle de fin : l'agent dit-il qu'il est une IA ? Le plafond coupe-t-il ? L'interrupteur coupe-t-il ? La trace montre-t-elle chaque coût ?

## 6. Une carte de tes agents

Tiens un tableau unique de tes agents hébergés : nom, où il tourne, modèles, qui y a accès, état réel (en essai, en service, coupé). Un agent neuf y entre le jour de sa création et en sort quand on l'archive. Un agent absent du tableau est un agent que personne ne surveille.

## Pour aller plus loin

- Concevoir les outils de l'agent : `creer-un-agent-ia:creer-un-agent-ia`, puis `creer-un-agent-ia:construire-solution`.
- Tester et mettre en service : `creer-un-agent-ia:tester-solution`, `creer-un-agent-ia:piloter-mise-en-service`.
- L'API, le SDK et les agents gérés du fournisseur : la compétence `claude-api:claude-api` (modèles, outils, mise en cache).
- Ranger ce que l'essai t'a appris : `creer-un-agent-ia:router-capitalisation`.
