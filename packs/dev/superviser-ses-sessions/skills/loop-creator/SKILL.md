---
name: loop-creator
description: >-
  Concevoir, lancer, relancer ou réparer une BOUCLE Claude Code (`/loop`) pour qu'elle avance
  jusqu'à un objectif mesurable, s'arrête au bon moment et ne tourne jamais dans le vide.
  Déclencher sur : « crée / lance / relance la boucle », « fais tourner ça toutes les N minutes »,
  « mode nuit », « boucle autonome », « elle s'arrête pour rien », « elle tourne dans le vide »,
  « elle ne finit jamais », « quand est-ce qu'une boucle doit s'arrêter », « loop ou routine ? »,
  « ma boucle a disparu », « prends tout en charge et va jusqu'au bout », « le plan est fini, et
  après ? » — ou le symptôme sans le nom : une tâche récurrente qui consomme des jetons sans
  produire de résultat. PAS pour un simple rappel ponctuel, ni pour une tâche qui tient en un seul
  tour.
---

# loop-creator — une boucle qui avance, s'arrête, et se relance proprement

## §0 Ce qu'est une boucle, et ce qu'elle n'est pas

Une boucle Claude Code, c'est `/loop <intervalle> <compétence ou prompt>` : toutes les N minutes
(ou heures, ou jours), Claude se réveille dans **la même session** et rejoue le même prompt.
Chaque réveil doit faire **un pas utile** : un lot terminé, une preuve produite, un état mis à jour.

Trois choses qu'une boucle n'est pas :

- **Pas un moniteur.** Un réveil qui écrit « rien de neuf » est un réveil perdu : il a payé un tour
  complet pour constater une absence. Le livrable d'un réveil est un fait qui a bougé.
- **Pas une mémoire.** Ce que la boucle sait entre deux réveils tient dans ce qu'elle a **écrit** :
  un fichier d'état. Le contexte de la session, lui, grossit et finit par coûter cher ou par être
  compacté.
- **Pas une garantie de survie.** Elle vit dans une session ouverte (voir §5).

La question qui gouverne tout le reste : **est-ce qu'un prochain réveil peut changer quelque chose ?**
Oui → la boucle a une raison d'exister. Non → elle doit s'arrêter, pas ralentir.

## §1 Avant d'armer : objectif, état, premier travail

Une boucle sans objectif écrit tourne jusqu'à ce qu'on la coupe. Avant `/loop`, poser quatre choses.

1. **Un objectif mesurable.** Pas « améliorer X » : « les 40 pages migrées, les tests au vert, la file
   vide ». Si on ne peut pas dire en une phrase *à quoi on reconnaît que c'est fini*, on n'est pas
   prêt à armer.
2. **Un fichier d'état**, écrit à un endroit que le prochain réveil relit : objectif, ce qui est
   fait, ce qui reste, ce qu'on attend et de qui, date du dernier pas. C'est la mémoire de la boucle,
   pas la conversation (modèle dans `references/modeles.md`).
3. **Le premier travail réel du prochain réveil**, nommé. Si on ne sait pas quoi faire au premier
   réveil, la boucle est vide avant d'avoir commencé.
4. **Un pré-mortem de cinq lignes**, une réponse par risque :
   - le réveil tombe sur *rien à faire* : qu'est-ce qu'il fait ? (réponse : il s'arrête ou espace ;
     il ne tourne pas à vide)
   - le réveil dépend de **moi** (une décision, un clic, un test à jouer) : comment le sait-il ?
   - un blocage local (permission, outil absent) : continue-t-il sur le reste ?
   - l'état est périmé (quelqu'un a avancé entre-temps) : le relit-il avant d'agir ?
   - l'outil dont il dépend est indisponible : se dégrade-t-il sans inventer ?

Armer seulement quand les quatre existent. Le coût d'écrire ça : dix minutes. Le coût de s'en passer :
une nuit de réveils vides.

## §2 Le prompt de réveil : court, stable, qui pointe

Le prompt rejoué à chaque tick doit rester **court** et **pointer** vers l'état plutôt que de
recopier la méthode :

```text
/loop 30m  Reprends la mission décrite dans <fichier d'état> jusqu'à l'objectif.
Relis l'état, fais le prochain lot, mets l'état à jour, rends un reçu d'une ligne.
Arrête-toi (et dis pourquoi) si l'objectif est atteint ou si le reste attend l'humain.
```

Pourquoi court : un prompt long qui recopie le plan dérive dès que le plan change, et il faut alors
rééditer la boucle. Un prompt qui pointe vers un fichier se met à jour en éditant le fichier.

Si une compétence (un skill) porte déjà la méthode métier, le prompt la nomme au lieu de la
recopier : `/loop 1h` suivi du nom de ta compétence. Attention : à chaque tick, seules les compétences que Claude
a le droit d'invoquer lui-même s'exécutent ; les commandes intégrées arrivent comme du texte.

Chaque réveil enchaîne : **relire l'état → prendre le plus gros lot sûr → vérifier son effet →
mettre l'état à jour → prendre le suivant tant que quelque chose de sûr reste faisable.** Ne pas
s'imposer « un lot par réveil » : une boucle qui rend la main après un seul geste alors qu'il en
reste dix paie dix réveils pour dix gestes.

## §3 Les conditions d'arrêt — la partie qui compte le plus

Une boucle bien faite sait s'arrêter. Cinq raisons légitimes, à écrire dans l'état dès le départ.

| Raison | Ce que ça veut dire | Geste |
|---|---|---|
| **Objectif atteint** | Le critère mesurable du §1 est vrai, preuve à l'appui | arrêter, écrire le bilan |
| **Le reste attend l'humain** | Une validation, une décision, un clic, un test à jouer par toi : rien de ce qui reste ne peut avancer sans toi | **arrêter**, pas ralentir |
| **Stop explicite** | Tu as dit stop | arrêter, aucune action résiduelle |
| **Budget ou plafond** | Nombre de réveils, jetons, durée, quota atteint | arrêter, dire ce qui reste |
| **Deux réveils vides de suite** | Le premier espace la cadence, le second arrête | arrêter |

### Attendre quelqu'un n'est pas un état de boucle

C'est la règle la plus souvent violée. Quand tout le reste dépend d'une décision humaine, **ralentir
la boucle** (« je vérifie toutes les heures si tu as répondu ») est une fausse économie : chaque
réveil paie un tour pour écrire « toujours en attente ». Le bon geste :

1. écrire dans l'état **ce qu'on attend et de qui**, et où la réponse sera déposée ;
2. **annuler la boucle** dans ce même tour (demander à Claude de l'annuler, ou supprimer la tâche
   planifiée) ;
3. le dire en une ligne à la personne ;
4. la réponse, quand elle arrive, **rallume** la boucle (§4).

Seule exception : le signal attendu arrive **sans toi** (une CI qui finit, un déploiement, une autre
session qui travaille vraiment, un délai d'observation écrit). Alors on programme le prochain
contrôle au premier instant où il a pu changer. Un contrôle inchangé espace ; un second contrôle
inchangé arrête.

### Ne jamais tourner dans le vide

- Un réveil qui ne fait rien d'utile le **dit** (« rien à faire parce que… ») et espace ou arrête.
- Jamais deux réveils à la même cadence pour constater deux fois la même absence de changement.
- Un échec répété du même geste n'est pas un motif de réessayer toutes les N minutes : c'est un
  motif de s'arrêter et de dire ce qui bloque.

### Jamais de boucle jumelle

Avant d'en créer une : **existe-t-il déjà une boucle sur le même objet ?** Demander à Claude de lister
les tâches planifiées. Même objet + même cible = on **reprend** la boucle existante, on n'en ouvre
pas une seconde. Deux boucles sur le même objet se marchent dessus, rejouent les mêmes lots et
doublent la facture.

## §4 Relancer efficacement : on rallume LA boucle, on ne la rejoue pas

Une boucle arrêtée n'a pas vu le monde bouger. Son plan, son critère de choix et ses compteurs datent
d'avant l'arrêt. La réarmer telle quelle, c'est lui faire rejouer un monde périmé — proprement,
silencieusement, à sa cadence. Le geste, dans cet ordre :

1. **Retrouver la boucle qui existe** (liste des tâches planifiées, fichier d'état). Même objet =
   reprise, jamais une jumelle. Si la session a été fermée, la restaurer d'abord (§5).
2. **Lire pourquoi elle s'est arrêtée** et vérifier que sa condition de reprise est levée. Un stop
   explicite ou un plafond atteint ne se lèvent pas par l'envie de repartir ; une attente se lève
   par la réponse attendue.
3. **Mesurer ce qui a changé pendant son sommeil.** C'est l'étape qu'on saute. Qu'est-ce qui a bougé
   dans le dépôt, l'outil, la file ? Quelles décisions ont été prises entre-temps ? Une boucle qui
   repart sur l'état d'avant son arrêt n'est pas en retard : elle est **fausse**.
4. **Mettre l'état à jour avec cet intervalle.** Ce qu'on a appris pendant l'arrêt — y compris ce qui
   a causé l'arrêt — entre dans le fichier d'état. Sinon la boucle repart avec la méthode qui l'avait
   fait éteindre.
5. **Corriger ce que l'arrêt a rendu faux** : le plan qu'elle consomme, son critère de choix du
   prochain lot, ses compteurs, ses adresses de fichiers.
6. **Réarmer la même boucle**, avec le même prompt stable. Comme il pointe vers l'état, les
   corrections des étapes 4 et 5 sont consommées dès le premier réveil.
7. **Recalculer la cadence sur le contrat neuf.** Une cadence réglée sur « une page par réveil » n'a
   plus de sens devant un reste de trois livrables.

> Contrôle avant de réarmer : *la boucle que je rallume consommerait-elle aujourd'hui un plan, un
> critère ou un compteur écrit **avant** son arrêt ?* Oui → ce n'est pas une relance, c'est le rejeu
> d'un monde périmé. On corrige d'abord.

## §5 Cadence et durée de vie — les faits à connaître

### Choisir l'intervalle

`/loop` accepte `s`, `m`, `h`, `d` (`/loop 5m …`, `/loop 2h …`, `/loop 1d …`). Les secondes sont
arrondies à la minute ; un intervalle qui ne tombe pas sur un pas de cron propre (`7m`, `90m`) est
arrondi et Claude te dit lequel. Sans intervalle, Claude choisit lui-même entre 1 minute et 1 heure
à chaque tour, selon ce qu'il observe.

Règle de choix : **la cadence suit la vitesse à laquelle le signal change, pas l'impatience.**

| Situation | Cadence |
|---|---|
| Un build, une CI, un déploiement en cours | 1 à 5 min (ou un moniteur plutôt qu'une boucle) |
| Un lot de travail réel à dérouler (migration, rédaction, corrections) | 10 à 30 min : assez pour qu'un pas soit fini |
| Une veille, un rapport, une vérification de fond | 1 h à 1 jour (`/loop 1d …`) |
| Le reste attend un humain | **pas de cadence : arrêter** (§3) |

Une cadence plus rapide que le temps nécessaire à un pas produit des réveils qui se chevauchent ou
qui constatent « rien n'a changé ». Un réveil se déclenche entre deux tours, jamais pendant une
réponse : si Claude est occupé, il attend.

### Ce qui survit, ce qui ne survit pas

Vérifié dans la documentation de Claude Code (https://code.claude.com/docs/en/scheduled-tasks) :

- **Une boucle est liée à la session.** Elle ne tire que tant que l'application est ouverte et la
  machine allumée. Fermer le terminal ou quitter la session l'arrête.
- **Reprise de session.** Avec `--resume` / `--continue` (ou en rouvrant l'application), les tâches
  récurrentes sont **restaurées si elles n'ont pas expiré**.
- **Expiration à 7 jours.** Une tâche récurrente expire 7 jours après sa création : elle tire une
  dernière fois puis se supprime. Pour aller plus loin, l'annuler et la recréer avant l'échéance —
  ou changer de mécanisme (ci-dessous).
- **Pas de rattrapage.** Un réveil manqué n'est pas rejoué : au plus un tir quand Claude redevient
  disponible, et à la reprise le prochain tir est le premier échu.
- **Une boucle à rythme libre** (sans intervalle) n'est pas restaurée au `--resume` : il faut relancer
  `/loop`.
- **Plafond** : 50 tâches planifiées par session. Un décalage aléatoire (jitter) s'applique, jusqu'à
  la moitié de l'intervalle et au plus 30 min : ne compter ni sur la minute exacte ni sur un
  enchaînement serré.
- **Version** : la persistance au `--resume` demande une version récente de Claude Code
  (v2.1.72 ou plus) ; vérifier avec `claude --version`.

Pour durer au-delà de 7 jours, sans session ouverte, ou machine éteinte :

| Mécanisme | Tourne sur | Machine allumée requise | Session ouverte requise | Intervalle minimum |
|---|---|---|---|---|
| `/loop` | ta machine | oui | oui | 1 min |
| Tâche planifiée du bureau (Desktop) | ta machine | oui | non | 1 min (par Claude) |
| Routine cloud | le cloud | **non** | non | 1 h |

## §6 Boucle ou routine ?

Il n'y a pas de « meilleur » : ce sont deux compromis différents.

| | Boucle (`/loop`) | Routine (cloud ou bureau) |
|---|---|---|
| **Contexte** | une seule session garde tout ce qu'elle a vu | chaque exécution repart de son prompt et de ses fichiers |
| **Coût** | le contexte grossit, chaque tour coûte plus cher avec le temps | chaque exécution est cadrée et peu chère |
| **Autonomie** | tant que la session est ouverte | indépendante de toute session |
| **Risque** | dérive, compaction, expiration à 7 jours | éparpillement : N routines, peu de contexte partagé |
| **Bon pour** | un chantier qui apprend en avançant, avec des décisions liées entre elles | un travail récurrent bien défini, à reproduire à l'identique |

Motif qui marche bien :

1. **Une session superviseur** conçoit la routine, la crée, puis **reste** pour l'améliorer à partir de
   ses résultats (elle lit ce que la routine a produit, corrige son prompt, ajuste sa cadence).
2. La routine travaille de façon autonome et peu coûteuse.
3. Ses résultats vont dans **une interface organisée par actions** (ce qu'il faut valider, ce qui
   est prêt, ce qui est bloqué) plutôt que dans vingt conversations. Le superviseur y lit l'état ; la
   personne n'y voit que ce qui demande son geste.

Règle pratique : un chantier de découverte → boucle ; un chantier compris → routine. Quand une boucle
s'est stabilisée au point que ses réveils se ressemblent, la promouvoir en routine.
Pour piloter un parc de sessions déjà ouvertes, voir `/claude-session-supervisor`.

## §7 Mission de bout en bout — être responsable du résultat

Quand on confie « prends tout en charge » ou « va jusqu'au bout », le mandat n'est pas d'exécuter un
plan : c'est **d'atteindre un résultat**. La différence se voit à un seul moment : **quand le plan est
fini**.

- Un plan terminé dans une mission qui continue **ne vaut pas « terminé »**. Il déclenche un **bilan** :
  l'objectif est-il atteint, mesuré ? Si oui, on s'arrête avec preuve. Si non, on **revoit la
  stratégie** : qu'est-ce qui a marché, qu'est-ce qui n'a rien changé, quelle autre voie ?
- On ne conserve pas une stratégie par inertie : on la **met à l'épreuve** (« qu'est-ce qui la ferait
  échouer ? ») puis on la garde si elle tient ou on la remplace.
- On **reprend avant de reconstruire** : relire l'état, le journal, l'historique de contrôle de
  version. Ne jamais refaire ce qui est déjà fait.
- On **exécute sans revalidation par lot** : la stratégie est validée une fois, au départ. Les
  vrais arrêts sont l'irréversible (suppression, dépense, envoi, publication), un goût ou une
  décision qui n'appartient pas à l'agent, et l'accès à des comptes.
- On **ne fabrique pas** une donnée absente : un chiffre inconnu reste inconnu.
- On **rend compte en peu de lignes** : ce qui a avancé, la preuve, ce qui attend.

Une mission n'active ni boucle ni minuteur toute seule : c'est le §1 qui arme, et le §3 qui arrête.

## §8 Anti-patterns à reconnaître

| Symptôme | Cause | Remède |
|---|---|---|
| Réveils qui écrivent « rien de neuf » | tout le reste attend l'humain, et la boucle continue | §3 : arrêter, écrire ce qu'on attend |
| Deux boucles font le même travail | création sans avoir listé l'existant | une seule ; annuler la jumelle |
| La boucle s'arrête « pour rien » | l'état ne dit pas ce qui reste, ou le critère est flou | objectif mesurable, reste explicite |
| La boucle ne s'arrête jamais | aucun critère d'arrêt écrit | §3 avant d'armer |
| Prompt de 40 lignes | méthode recopiée dans le tick | prompt court qui pointe vers l'état |
| Relancée, elle refait du travail déjà fait | état non relu ou périmé | §4, étapes 3 à 5 |
| Un seul gros réveil qui s'étire | un lot trop gros pour un tick | découper en lots qui tiennent dans un pas |
| Disparue après une semaine | expiration à 7 jours | annuler et recréer avant, ou passer en routine |
| Plus rien après fermeture de l'application | boucle liée à la session | rouvrir la session avec `--resume`, ou passer en routine |

## §9 Contrôle avant de laisser tourner

- [ ] Objectif mesurable, écrit dans le fichier d'état.
- [ ] Conditions d'arrêt écrites (§3), dont « le reste attend l'humain ».
- [ ] Aucune boucle existante sur le même objet.
- [ ] Prompt court qui pointe vers l'état.
- [ ] Premier travail du prochain réveil nommé.
- [ ] Cadence justifiée par la vitesse du signal ; échéance des 7 jours notée.
- [ ] Le premier réveil a été **observé** et a produit un fait, avant de dire « ça tourne ».

Une boucle « configurée » n'est pas une boucle « vivante » : tant qu'un réveil n'a pas produit un effet
visible dans l'état, elle est seulement décrite.
