---
name: faire-evoluer-une-app
description: >-
  Quand on veut faire évoluer une app qui existe déjà, par une fonctionnalité de plus ou par un défaut corrigé → afficher
  l'état calculé depuis le dossier `evolutions/<évolution>/`, puis dérouler les six étapes dans l'ordre (partir de la
  demande, comprendre le code qui l'accueille, construire, tester, mettre en ligne, documenter), chacune par la
  meilleure compétence publique ou par le workflow frère qui la porte. Deux entrées à l'étape 1 : une fonctionnalité
  s'écrit d'abord ; un défaut se reproduit et sa cause se prouve d'abord, et le correctif doit faire remarcher le geste
  décrit par la personne, avec ses mots. Dit franchement ce qui se fait à la main : creuser la cause d'un défaut qui
  revient. Se lance par `/faire-evoluer-une-app:faire-evoluer-une-app`. Déclencheurs : « ajouter une fonctionnalité »,
  « nouvelle fonctionnalité », « rajoute un bouton », « ajoute une page à mon app », « évolution de l'app », « bug »,
  « corriger un défaut », « ça marche pas », « ça plante », « régression », « ça a cassé ». Pas pour créer une app de
  zéro (/creer-une-app:creer-une-app). Pas pour un site vitrine (/creer-un-site-web:creer-un-site-web). Pas pour un agent
  IA (/creer-un-agent-ia:creer-un-agent-ia). Pas pour tester sans demande précise
  (/tester-et-securiser:tester-et-securiser).
---

# Faire évoluer une app : de « j'aimerais que l'app fasse ça » ou « ça ne marche plus » au geste qui marche, prouvé en ligne

## Ce que ce workflow résout

Faire évoluer une app qui existe se rate de deux façons, et le piège est le même : coder tout de suite.

- Pour une **fonctionnalité** : sans avoir écrit ce qu'elle doit faire, sans avoir lu le code qui l'accueille, sans
  test, sans documentation, ce qui existait casse sans bruit.
- Pour un **défaut** : on corrige avant d'avoir la cause (il revient), on corrige autre chose que ce que la personne a
  décrit (un meilleur message d'erreur à la place du geste qui marche), ou on corrige sans test (il revient à la version
  suivante).

Sans point d'entrée, la session part de la ligne de code qu'elle voit ou du premier correctif plausible. Ici : l'ordre,
l'état, une entrée adaptée à la demande, et la boucle de construction, de test et de mise en ligne déjà tranchée.

**Résultat attendu** : une fonctionnalité écrite, construite test d'abord, testée, en ligne, documentée ; ou un défaut
reproduit, sa cause prouvée, un test qui l'attrapait et qui passe, la correction relue, en ligne, et le geste de la
personne rejoué avec ses mots. Un dossier `evolutions/<évolution>/` qui dit à tout moment où on en est.

## Stratégie

1. **Les étapes, leurs compétences et leurs règles de choix** sont dans `references/workflow.json`, d'où le tableau
   plus bas est tiré. En cas de désaccord, c'est ce fichier qui fait foi.
2. **Une compétence, un seul endroit.** Les grosses étapes (construire, tester, mettre en ligne) ont leur workflow
   frère, partagé avec les autres workflows : l'étape cite ce workflow, jamais ses membres.
3. **Deux entrées, un seul chemin.** La demande dit laquelle : une fonctionnalité de plus, ou un geste qui ne marche
   plus. Seule l'étape 1 change de compétence ; les étapes 3, 4 et 5 sont communes. Les étapes 2 et 6 sont celles d'une
   fonctionnalité (sans objet pour un défaut, dont l'étape 1 a déjà tracé le code en cause).
4. **L'état d'abord, toujours calculé** depuis les fichiers de l'évolution, jamais recopié.
5. **L'ordre protège la décision** : pas de code sans fonctionnalité écrite ou sans cause prouvée, pas de construction
   sans avoir compris le code qui l'accueille (fonctionnalité), aucune annonce avant que le test passe, pas de mise en
   ligne sans le verdict des tests. Sauter une étape reste possible sur demande ; le journal dit laquelle et pourquoi.
6. **Une seule boucle de construction.** La compréhension du code s'arrête à l'architecture de la fonctionnalité ; la
   construction passe ensuite par `/construire:construire`, pour ne pas avoir deux boucles qui divergent. Pour un
   défaut, elle se réduit à une tâche : le test qui reproduit, puis la correction.
7. **Le correctif d'un défaut doit faire remarcher le geste décrit par la personne, avec ses mots.** Le geste s'écrit
   tel qu'elle l'a dit dans `01-demande.md`, et c'est lui qu'on rejoue à l'étape 4 puis en ligne à l'étape 5. Un
   meilleur message d'erreur, un journal plus parlant ou un filet de secours n'est pas une correction : le geste reste
   cassé. Une correction possible ne se remplace pas par une note de passation. On ne corrige que ce qu'on a prouvé.
8. **Un défaut qui revient change de méthode.** Déjà revenu une fois, ou touchant plusieurs endroits : on creuse
   jusqu'à la cause structurelle avant de recorriger, pas une deuxième rustine.
9. **Une seule validation, à l'étape 1** : la fonctionnalité écrite (pour qui, quel parcours, les critères
   d'acceptation, ce qui n'en est pas), ou le défaut reproduit avec le geste à faire remarcher. Ensuite tout se
   déroule. Les questions de l'étape 2 se tranchent d'abord dans le dépôt et le document produit ; seul un goût
   produit non écrit remonte. Restent à la personne : l'irréversible, ses machines et ses comptes, et, si l'app est
   faite pour un tiers, l'ouverture au public.
10. **Aucune donnée personnelle dans le dossier d'état.** Un défaut reproduit sur un compte réel s'écrit avec un
    identifiant de la base ou « un compte de test », jamais un nom ni une adresse e-mail.
11. **Chaque passage se ferme au journal** : une correction devient une règle, un test ou une ligne du workflow.

<!-- prerequis:debut -->
## Prérequis

Ce workflow s'appuie sur des compétences publiques, installées à part. Aucune n'est indispensable : si l'une manque, le workflow le dit et fait l'étape à la main. Faire l'étape à la main veut dire suivre sa règle de choix, écrire ce qu'elle doit rendre (dans le fichier de l'étape, ou dans la réponse quand le workflow n'a pas de dossier) et dire ce qui reste à la charge de la personne.

```text
/plugin marketplace add JuliusBrussee/caveman
/plugin marketplace add addyosmani/agent-skills
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin install agent-skills@addy-agent-skills
/plugin install caveman@caveman
/plugin install engineering@knowledge-work-plugins
/plugin install feature-dev@claude-plugins-official
/plugin install superpowers@claude-plugins-official
npx skills add bmad-code-org/BMAD-METHOD --skill bmad-prd -a claude-code
```

La commande `npx skills add` (CLI Vercel `skills`) demande Node.js 22.20 ou plus (vérifié le 06/11/2026, https://github.com/vercel-labs/skills). Claude Code installé avec l'installeur natif n'en a pas besoin.

Les workflows cités ici sont dans le même dépôt (le dépôt s'ajoute une fois : `/plugin marketplace add Florentmaisoncelle/zerogravity-skills`) :

```text
/plugin install construire@zerogravity
/plugin install creer-un-agent-ia@zerogravity
/plugin install creer-un-site-web@zerogravity
/plugin install creer-une-app@zerogravity
/plugin install mettre-en-ligne@zerogravity
/plugin install tester-et-securiser@zerogravity
```
<!-- prerequis:fin -->

## Étapes

### 0. Le dossier, puis l'état (lecture seule)

**Le dossier.** L'évolution s'écrit dans le dépôt de l'app concernée, dans `evolutions/<évolution>/`, où `<évolution>`
est un nom court (par exemple « export-csv » ou « bouton-muet »). Une évolution = un sous-dossier, avec son propre journal.
Évolution par défaut : la plus récente qui n'est pas terminée, ou celle que la personne nomme. Si toutes sont terminées,
ou si elle demande une nouvelle évolution, on crée le sous-dossier suivant et on repart à l'étape 1. Dossier absent ou
vide : il n'y a encore rien de fait, l'état est « étape 1 » et le dossier se crée au premier passage. Si le dossier
courant n'est pas celui de l'app (ou appartient à un autre produit), le dire en une ligne et demander où vit l'app :
rien ne s'écrit avant.

**L'état**, calculé depuis le journal et les fichiers (l'entrée se lit à la première ligne de `01-demande.md`, de la
forme `Type : fonctionnalité` ou `Type : défaut` ; pour un défaut, la deuxième ligne est `Geste : « ses mots »`) :

```text
Demande         export-csv (fonctionnalité)
Geste à rejouer « <ses mots> »            ← défaut seulement
Étapes          01 ✓  02 ✓  03 -  04 -  05 -  06 -
Dernière décision  2026-11-06 · 02 · carte du code faite
Étape suivante  03 Construire → /construire:construire
```

- Le journal `evolutions/<évolution>/journal.md` a une ligne par décision :
  `AAAA-MM-JJ · NN · fait | en attente | sans objet | sautée | corrigée · <une phrase>`.
- Pour chaque étape, la dernière ligne du journal qui la nomme fait foi. `✓` : cette ligne dit `fait` ou `corrigée` et
  le fichier de l'étape existe. `s.o.` : elle dit `sans objet` ou `sautée` (l'étape n'est plus proposée ; les étapes 2
  et 6 d'un défaut sont `sans objet`). `-` : aucune ligne, ou le fichier manque.
- `corrigée` : l'étape est refaite après une correction ; elle reste ✓ et la ligne dit ce qui a changé. `sautée` : la
  personne a choisi de passer ; la ligne dit pourquoi.
- `en attente` : l'étape est préparée, mais elle dépend d'un geste ou d'une réponse qui arrive hors de la conversation. La ligne du journal dit ce qu'on attend et de qui. L'état l'affiche `att.` avec ce texte : l'étape n'est pas `✓`, parce que préparé n'est pas fait. Le workflow s'arrête là et le dit ; il n'invente jamais la suite (ni réponse, ni résultat, ni geste qu'on ne lui a pas confirmé). Quand la personne apporte ce qui est arrivé, la ligne `fait` suit. Ici : la validation de la demande (étape 1), le verdict des tests (étape 4) et la mise en ligne (étape 5), qui se jouent dans les workflows frères.
- L'étape suivante est la première étape `-` ou `att.`, dans l'ordre (devant une étape `att.`, on demande d'abord où en est l'attente). Si aucune ne l'est, l'évolution est terminée, et on peut en
  ouvrir une autre.

**Les étapes confiées à un workflow frère** (3, 4, 5) écrivent leur travail dans le dossier du frère, à la racine du
dépôt de l'app : `construction/`, `tests/` et `mise-en-ligne/`. Ces dossiers servent à toutes les évolutions, l'une
après l'autre : si le dossier du frère porte encore le passage d'une évolution précédente, le frère ouvre un nouveau
passage avant de commencer (voir sa propre règle). Chaque étape déléguée écrit dans le dossier de l'évolution une note
courte, dans son propre fichier (`03-construction.md`, `04-tests.md`, `05-mise-en-ligne.md`) : le résultat, la décision
et le dossier du frère où lire son état. L'étape est inscrite `fait` quand le frère a fini son passage ; pour les
tests, seulement avec le verdict « on met en ligne ».

**Après un verdict « on ne met pas en ligne »**, le workflow s'arrête avant l'étape 5. La note de l'étape 4 garde le
verdict et la personne choisit :

- **corriger** : retour à l'étape 3 (inscrite `corrigée`, avec ce qui change), puis l'étape 4 est refaite ;
- **ranger l'évolution sans la sortir** : les étapes 5 et 6 sont inscrites `sautée`, avec la raison, et le travail
  reste sur sa branche ou dans son dépôt.

**Une question n'est pas un ordre.** « Où en est ma fonctionnalité ? », « où en est la correction ? » → l'état et la
prochaine action, puis on s'arrête. La commande `/faire-evoluer-une-app:faire-evoluer-une-app`, « continue » ou
« déroule » → on enchaîne jusqu'à la première étape en attente, puis on s'arrête et on le dit.

**Une demande au milieu du chemin** (« code-moi ça tout de suite », « corrige ça tout de suite ») : l'étape 3 exige la
fonctionnalité écrite et la carte du code, ou la cause prouvée. Sans `01-demande.md`, on écrit d'abord la
fonctionnalité (une page, ses critères d'acceptation) et on la fait valider, ou on reproduit et on prouve la cause,
même vite. Jamais de construction à l'aveugle, jamais une correction sur une hypothèse.

### 1. Lancer l'étape suivante

Lire l'étape dans le tableau ci-dessous, appliquer sa **règle de choix**, invoquer la compétence retenue (ou le
workflow frère), écrire dans le fichier de l'étape sa sortie ou, si la compétence écrit ailleurs, une ligne qui dit où
elle vit, inscrire `fait` au journal (ou `en attente`, voir plus haut), puis passer à la suivante sans redemander. Quatre précisions :

- **Étape 1, une fonctionnalité** : le document produit de l'app se met à jour, il ne se double pas. Sans document
  produit, on en écrit un court, centré sur la fonctionnalité.
- **Étape 1, un défaut** : écrire d'abord le geste de la personne en ses mots, puis la reproduction, puis la cause
  prouvée par une mesure (une sortie, un journal frais). Une cause sans mesure n'est pas prouvée. Un défaut déjà
  revenu une fois passe de la méthode par défaut à la recherche de cause structurelle : aucune compétence publique,
  on la fait à la main, en creusant du symptôme à la racine, preuves à l'appui (journaux frais).
- **Étape 3, un défaut** : le test qui reproduit le défaut s'écrit d'abord et doit échouer pour la bonne raison (celle
  de l'étape 1), pas parce qu'il est mal écrit. La construction est réduite à cette seule tâche.
- **Étapes 4 et 5** : le scan de sécurité en profondeur n'a lieu que si la fonctionnalité touche la connexion, le
  paiement ou les données d'un client de l'app (son coût s'annonce avant de le lancer) ; sinon, la vérification du lot
  suffit. Pour un défaut, elles rejouent le geste de la personne, avec ses mots, d'abord sur la version testée puis en
  ligne.

<!-- etapes:debut -->
| # | Étape | Compétences | Règle de choix |
|---|---|---|---|
| 1 | Partir de la demande | `bmad-prd` · `superpowers:systematic-debugging` · Trouver la cause d'un défaut : `caveman:investigate-first` | Pour une fonctionnalité : le document produit existant se met à jour ; sans document, bmad-prd en écrit un court, centré sur la fonctionnalité. Pour un défaut : superpowers:systematic-debugging par défaut ; dès que le défaut est déjà revenu une fois ou touche plusieurs endroits, aucune compétence publique : on creuse à la main, du symptôme à la cause structurelle, prouvée par des journaux frais. Le correctif doit faire remarcher le geste décrit par l'utilisateur, avec ses mots ; un meilleur message d'erreur n'est pas une correction. |
| 2 | Comprendre le code qui l'accueille (pour une fonctionnalité) | `feature-dev:feature-dev` · Explorer le code qui accueille le changement : `caveman:caveman-explore` · Répertorier la dette technique : `engineering:tech-debt` | feature-dev jusqu'à l'architecture de la fonctionnalité (découverte, exploration, questions, architecture) ; la construction passe ensuite par la brique Construire, pour garder une seule boucle. |
| 3 | Construire | `construire` · Retirer ou migrer un ancien système : `agent-skills:deprecation-and-migration` · Migrer sans casser : `caveman:migration` · Restructurer le code : `caveman:safe-refactor` · Corriger un défaut : `caveman:surgical-patch` | Par /construire:construire, sur la fonctionnalité de l'étape 1 et l'architecture de l'étape 2. Pour un défaut, le test qui le reproduit s'écrit d'abord et doit échouer pour la bonne raison. |
| 4 | Tester et sécuriser | `tester-et-securiser` | Par /tester-et-securiser:tester-et-securiser ; claude-security seulement si la fonctionnalité touche la connexion, le paiement ou les données d'un client. Pour un défaut, sur le diff de la correction et le parcours qui était cassé. Avec le verdict « on ne met pas en ligne », on corrige (retour à l'étape 3) ou on range l'évolution sans la sortir. |
| 5 | Mettre en ligne | `mettre-en-ligne` | Par /mettre-en-ligne:mettre-en-ligne ; une fonctionnalité risquée sort derrière un interrupteur. Pour un défaut, la vérification en ligne rejoue le geste décrit par l'utilisateur. |
| 6 | Documenter (pour une fonctionnalité) | `agent-skills:documentation-and-adrs` | La documentation part avec le code, dans le même lot ; une décision qui a coûté un débat s'écrit en décision d'architecture. |
<!-- etapes:fin -->

### 2. Clore un passage

À la fin de chaque séance, on écrit l'état au journal : ce qui est fait, ce qui reste, la prochaine action. Une
compétence qui a déçu à une étape se signale au journal, pour rouvrir le choix de cette étape.

## Pourquoi ces choix

- Six étapes pour une fonctionnalité, de la fonctionnalité écrite à la documentation, et quatre pour un défaut, de la
  cause à la vérification en ligne. Les trois grosses étapes (construire, tester, mettre en ligne) sont partagées
  avec « créer une app » : un seul endroit à tenir à jour. On ne corrige que ce qu'on a prouvé.
- **Ajouter une fonctionnalité et corriger un défaut sont un seul workflow à deux entrées**, dans la même étape 1.
- **Le document produit existe déjà** : on le met à jour par le mode « mettre à jour » de BMAD, au lieu d'écrire un
  second document pour la fonctionnalité.
- **La construction n'est pas faite par la méthode de compréhension du code** : elle s'arrête à l'architecture de la
  fonctionnalité, et le workflow de construction prend le relais.
- **Une fonctionnalité risquée sort derrière un interrupteur** : le workflow de mise en ligne le prévoit dans ses
  paliers d'ouverture.

## Ce qui manque

- **Creuser la cause structurelle d'un défaut qui revient** : aucune compétence publique, on le fait à la main. La
  méthode : lister tous les endroits où le symptôme apparaît ; pour chacun, remonter l'appel jusqu'à la première
  valeur ou le premier état faux, avec une sortie ou un journal frais à l'appui ; chercher ce que ces endroits ont en
  commun (une fonction, une donnée, une hypothèse) ; corriger cet endroit commun, pas chaque symptôme ; écrire le test
  qui échouait avant et réussit après.
- **Écrire la documentation** : seule `agent-skills:documentation-and-adrs` couvre les décisions d'architecture, l'API et
  le README ; pour le reste de la documentation, on le fait à la main avec la règle de l'étape.

## Frontières

| Demande | Va à |
|---|---|
| Créer une app, un SaaS, une plateforme de zéro | `/creer-une-app:creer-une-app` |
| Créer ou refaire un site vitrine | `/creer-un-site-web:creer-un-site-web` |
| Créer un agent ou un système IA | `/creer-un-agent-ia:creer-un-agent-ia` |
| Construire un plan déjà écrit, sans le reste | `/construire:construire` |
| Tester, relire le code, sécuriser, sans demande précise | `/tester-et-securiser:tester-et-securiser` |
| Mettre en ligne une version déjà prête | `/mettre-en-ligne:mettre-en-ligne` |
