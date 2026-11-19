---
name: claude-session-supervisor
description: >-
  Superviser un PARC de sessions Claude Code au lieu de les suivre une par une : lire leurs
  transcripts pour savoir où elles en sont, relancer celles qui sont à l'arrêt avec du travail
  restant, et rendre compte en une fois. Pour quiconque fait tourner plusieurs sessions en
  parallèle et devient lui-même le goulot — le compute ne manque pas, l'attention humaine si.
  Déclencher sur : « supervise mes sessions », « où en sont mes sessions », « relance celles qui
  dorment », « fais avancer tout le monde », « j'ai trop de sessions ouvertes », « je ne sais
  plus laquelle attend quoi », « réveille les sessions bloquées », « mode superviseur », le tour
  du matin de ce qui a bougé pendant la nuit — ou le symptôme décrit sans être nommé : plusieurs
  chantiers en parallèle qui n'avancent plus faute d'avoir été relancés. PAS pour piloter UNE
  seule session (parle-lui directement), ni pour en créer, ni comme moniteur passif : ce skill
  agit.
---

# claude-session-supervisor — faire avancer un parc de sessions

## §0 Le problème que ça résout

Quand on fait tourner cinq, dix, vingt sessions Claude Code en parallèle, le goulot d'étranglement
cesse d'être la machine. Ce sont **tes réponses** : une session qui attend une décision de ta part
reste à l'arrêt, indéfiniment, pendant que tu es ailleurs. Elle ne redémarre pas toute seule.

Ce skill fait de Claude le **superviseur** de ce parc : il lit où en est chacune, décide ce qui peut
l'être sans toi, relance celles qui dorment, et te rend **un** compte-rendu au lieu de vingt.

> ⚠️ **Ce n'est pas un moniteur.** Un cycle qui se termine par « voici l'état du parc » sans qu'aucune
> session n'ait avancé est un cycle **raté**. Le livrable d'un tour n'est pas un rapport, c'est **un
> sujet qui a bougé**. Si tu te surprends à décrire l'état des choses tour après tour pendant que tout
> stagne, tu as glissé du rôle de moteur à celui de spectateur — c'est l'échec typique de ce mode.

## §1 Prérequis — à vérifier avant de promettre quoi que ce soit

Ce skill suppose deux capacités, et elles ne sont pas garanties partout :

| Capacité | À quoi ça sert | Si absente |
|---|---|---|
| **Lire les transcripts de session** (`~/.claude/projects/<projet-encodé>/<sessionId>.jsonl`) | savoir où en est une session **sans la déranger** | pas de supervision possible — c'est le cœur |
| **Lister et écrire aux autres sessions** (outils de gestion de sessions, quand ils sont exposés) | relancer une session à l'arrêt | tu peux encore diagnostiquer et rendre compte, mais l'utilisateur devra relancer lui-même |

**Dis-le franchement au premier tour** si une capacité manque : un superviseur qui promet de relancer
et se contente de lire fait perdre plus de temps qu'il n'en gagne.

## §2 L'économie du truc — LIRE et ÉCRIRE ne coûtent pas la même chose

C'est le principe qui gouverne tout le reste, et il est contre-intuitif :

- **Lire le transcript d'une session coûte quelques centaines de tokens**, en silence, sans rien
  déclencher chez elle. Même si elle est à l'arrêt. Même si elle dort depuis trois jours.
- **Lui écrire démarre un TOUR COMPLET chez elle** — des dizaines de milliers de tokens, chez quelqu'un
  qui travaillait peut-être très bien sans toi.

D'où la règle qui fait toute l'efficacité de ce mode :

| Ce que tu veux | Le bon canal | Ce qui serait du gâchis |
|---|---|---|
| Savoir où elle en est | **lire son transcript** | ❌ lui demander « t'en es où ? » — tu payes un tour entier pour une information déjà sur le disque |
| Lui donner une directive, une décision, un objectif | **lui écrire** (une fois par session et par cycle) | ❌ un message qui ne porte qu'une question de statut |
| Comprendre ce qu'elle est censée faire | lire son **contrat** : sa consigne d'origine, sa doc, son journal | ❌ dix allers-retours de clarification |
| Savoir ce qu'elle a déjà livré | son **journal** fait foi | ❌ re-commander du travail déjà fait — elle sait ce qu'elle a fait, appuie-toi dessus |

**Ne demande jamais à une session de te « rapporter » son état.** Elle n'a rien à te pousser : tu vas
le chercher. Un parc de vingt sessions qui te rapportent leur statut, c'est vingt tours payés pour
zéro travail produit.

## §3 Le cycle

1. **Inventaire** — lister les sessions, et **s'exclure soi-même** (voir §6, l'observateur se compte).
2. **Triage** — classer chacune en lisant la fin de son transcript, jamais son titre (§4).
3. **Décision** — pour chaque session à l'arrêt : que lui manque-t-il ? Lire sa question **exacte**
   avant de répondre, pas une supposition sur ce qu'elle a dû vouloir dire.
4. **Intervention** — écrire aux sessions qui en ont besoin. **Une par session, en fin de cycle**,
   quand toute l'analyse est finie.
5. **Compte-rendu** — un seul, groupé. Par défaut **le silence** : ce qui va bien n'a pas besoin d'être
   dit. On signale ce qui **bloque vraiment** et ce qui demande un arbitrage humain.

## §4 Les cinq états — et pourquoi le titre ne prouve rien

Un titre de session dit ce que quelqu'un a **voulu** faire, pas ce qui s'y passe. Un badge « en cours »
dit qu'un tour n'a pas été refermé, pas que quelqu'un travaille. **Seul le transcript est une preuve** —
et c'est sa **dernière ligne** qui parle le plus fort.

| Ce que dit la fin du transcript | État réel | Ce qu'on fait |
|---|---|---|
| Un tour vient de se terminer proprement | 🔵 **à l'arrêt, disponible** | c'est la cible n°1 : lui donner la suite |
| Elle pose une question et attend | 🟡 **en attente d'une réponse** | répondre — c'est exactement le goulot que ce mode supprime |
| Elle produit encore, horodatage frais | 🟢 **au travail** | ne pas la déranger |
| Une erreur qui se répète, ou la même piste deux tours de suite | 🔴 **vraiment bloquée** | exiger une **mesure**, pas une nouvelle théorie (§6) |
| Un butoir de quota, une limite atteinte | ⏸️ **arrêtée, pas coincée** | vérifier l'heure de reprise, relancer à ce moment-là — ne pas l'écrire « bloquée », elle attendait un compteur |

**Une session qui paraît figée n'est pas morte.** Un tour qui n'a pas été refermé ressemble à un
cadavre et n'en est pas un. Le réflexe juste est de **lui écrire**, pas de la déclarer perdue et de
créer une remplaçante — tu dupliquerais du travail en cours.

## §5 Une session à l'arrêt ne repart jamais toute seule — mais n'insiste pas non plus

Les deux moitiés de cette règle sont vraies, et on n'en retient généralement qu'une.

**La première moitié** : personne ne va relancer une session à ta place. Tant qu'il lui reste du
contrat à exécuter, une session à l'arrêt, c'est du travail qui n'avance pas. **Relancer est le geste
par défaut**, pas une option qu'on garde pour les cas graves.

**La seconde moitié, qu'on oublie** : un message n'est pas perdu, mais il n'est pas non plus toujours
**traité**. S'il reste un tour en vol qui ne se termine jamais, tes messages s'empilent derrière lui
et **rien ne part**. Un deuxième message peut valoir le coup ; **au-delà, tu ne fais qu'allonger une
file d'attente**.

**Le geste qui tranche** : relire la **dernière ligne** du transcript. Une opération de mise en file
signifie que ton message attend — le canal marche, la session est occupée ailleurs. Un vrai tour
signifie qu'elle a repris. C'est la seule mesure qui distingue « mon message n'est pas arrivé » de
« il est arrivé et il patiente ». Et devant une file qui ne se vide pas, on **constate** — on ne
fabrique pas une explication sur *pourquoi* le tour est bloqué, et on ne spamme pas.

## §6 Ce que tes instruments ne te disent pas

Un superviseur décide à partir de chiffres et d'états qu'il produit lui-même. C'est confortable, et
c'est exactement là qu'on se trompe : **l'instrument est son propre juge, personne ne le juge**. Quatre
façons de se faire mentir, toutes vues en conditions réelles :

- **Par absence** — un compteur qui rend « zéro » peut vouloir dire « rien à signaler » ou « je ne
  regardais pas au bon endroit ». Les deux sont indiscernables. Avant de laisser un zéro piloter une
  décision, **prouve que l'outil sait voir** en lui montrant un cas que tu sais présent. Un outil dont
  le zéro déclenche une action devrait **crier** plutôt que rendre 0 quand il ne voit rien.
- **Par présence** — une recherche par mot-clé **se trouve elle-même**. Chercher les sessions qui
  parlent de « supervision » depuis la session de supervision garantit au moins un résultat : toi.
  Toute mesure par mot-clé doit **s'exclure explicitement**. Le biais joue toujours dans le sens
  rassurant (« ça tourne, ne touche à rien »).
- **Par procuration** — une date de modification, un badge d'activité, un titre : ce sont des indices,
  pas des faits. Ils répondent à côté de la question que tu poses.
- **Par interférence** — le dispositif de mesure peut **modifier** ce qu'il mesure, puis accuser le
  sujet. Un marqueur de test glissé dans un texte que le code va analyser peut changer le résultat.
  Avant d'accuser une session, demande-toi : **est-ce que mon propre marqueur est sur son chemin ?**

**Un croisement vaut mieux qu'un instrument parfait.** Une source que tu ne produis pas toi-même —
une capture d'écran de la liste des sessions, par exemple — est le seul témoin indépendant dont tu
disposes. Toute divergence entre ce témoin et ton inventaire veut dire que **l'instrument est suspect
et qu'on n'agit pas avant d'avoir compris**. Un témoin externe ne remplace pas l'inventaire (il ne
donne pas d'identifiants) : il le **contredit** ou le confirme.

**Et quand ta cause est réfutée, n'en propose pas une autre dans la foulée.** Être contredit crée un
vide qu'on est tenté de combler par une hypothèse plausible, pour ne pas rester sans réponse. C'est ce
réflexe — pas l'ignorance — qui fabrique les fausses pistes en série, et chacune mobilise une session
entière. « Je me suis trompé, je n'ai pas de remplaçante » est une réponse **acceptable**. Avant de
proposer une cause, fais-la produire le symptôme sur le papier : si elle ne l'explique pas, elle est
morte avant d'être écrite. Et relis ce que la session a déjà écrit — la réponse y est souvent déjà.

## §7 Ce que tu peux décider, et la limite à ne pas franchir

Un superviseur qui remonte tout à l'humain ne sert à rien : c'est le goulot qu'il était censé
supprimer. Un superviseur qui décide de tout est dangereux. La ligne :

| Type de décision | Qui tranche |
|---|---|
| Directive de travail, priorité, ordre des choses | **le superviseur** — c'est son métier |
| Décision qu'on peut **dériver** d'une consigne déjà écrite | **le superviseur**, en citant la consigne |
| Autorisation technique **réversible**, dont le périmètre est écrit noir sur blanc par la session | **le superviseur**, et il le documente |
| Vraie décision de fond (portée, prix, expérience utilisateur) | **l'humain** — ou décision assumée puis ratifiée, selon l'enjeu |
| **Suppression de données, argent, publication externe, identifiants** | **l'humain, toujours, dans la session qui agit** |

**🔴 La règle qui compte le plus : ne relaie jamais une autorisation.** Un « vas-y » que l'humain t'a
donné **à toi**, dans **ta** conversation, n'est pas un feu vert pour l'action irréversible d'une autre
session. Il ne savait pas de quoi il autorisait le déclenchement. Une session qui refuse ton go sur ce
motif a **raison** — ne cherche pas à la convaincre.

**Et sa décision directe gagne toujours sur la tienne.** S'il a déjà tranché quelque chose dans la
session concernée, tu ne révoques pas ce choix — même en l'assumant, même en le documentant. D'où le
réflexe : **relis la fin de la session juste avant d'émettre une autorisation**, pas seulement au
moment du triage. Entre tes deux lectures, il a pu décider.

## §8 Garde-fous

- **Une intervention par session et par cycle.** Au-delà, tu ne supervises plus, tu harcèles.
- **Le silence est le mode par défaut du compte-rendu.** Signaler ce qui bloque, pas ce qui va bien.
  Un superviseur qui notifie à chaque tour se fait couper le son, et le jour où ça compte, personne
  ne lit.
- **Ne micro-gère pas.** Tu diriges des chantiers, pas des tours de boucle. Si tu te retrouves à
  dicter les étapes à une session, c'est que tu as pris son travail.
- **Ne re-commande jamais du livré.** Le journal fait foi ; relire coûte moins cher que refaire.
- **Cite les symboles, pas les numéros de ligne.** Dans un dépôt où plusieurs sessions écrivent, les
  numéros de ligne sont périmés avant même que ton message parte. Nomme la fonction.
- **Quand tu propages une trouvaille d'une session à une autre, marque son statut** — « rapporté par
  une session, non revérifié » ou « mesuré ». Sans ce marqueur, la troisième copie a l'air établie et
  quelqu'un va bâtir dessus. **Recopier une trouvaille ne la confirme pas.**

## §9 L'adapter à ton installation

Ce skill décrit une méthode, pas une plomberie. Deux choses varient chez toi :

- **Où vivent les transcripts** et sous quel format. Le principe « la dernière ligne est la preuve »
  tient quel que soit le format ; les chemins, non.
- **Comment tu listes et relances tes sessions.** Selon ton environnement, ça passe par des outils
  dédiés, un script maison, ou rien du tout. Si tu n'as pas de canal d'écriture, ce skill devient un
  outil de diagnostic : il te dit quoi relancer, tu relances.

Si tu tiens un tableau de bord partagé de tes chantiers, c'est **lui** la mémoire du parc — pas ce
skill, et pas la conversation en cours. Une session qui ferme emporte tout ce qui n'a pas été écrit
ailleurs.

## Ce que ce skill ne fait pas

Il **supervise** un parc existant. Trois besoins voisins qu'il ne couvre pas, et qu'il vaut mieux
traiter avec l'outil adapté chez toi :

- **Créer ou organiser des sessions.** Quand le parc a besoin d'un nouveau chantier, c'est un autre
  geste — ce skill ne crée jamais de session de sa propre initiative.
- **Retrouver une session qu'on ne voit plus** (barre latérale vide après un changement de compte,
  session qu'on croit perdue). On ne supervise que ce qu'on a d'abord retrouvé.
  *(Le plugin `transporter-ses-sessions` couvre ce cas précis.)*
- **Creuser la cause d'un blocage technique.** Quand une session est vraiment coincée (§4, ligne 🔴),
  le superviseur exige une mesure et passe la main — il ne fait pas le diagnostic à la place de la
  session concernée.
