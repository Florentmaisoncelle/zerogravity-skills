# claude-session-supervisor

Supervise un **parc** de sessions Claude Code au lieu de les suivre une par une.

## Le problème que ça résout

Quand tu fais tourner cinq, dix, vingt sessions Claude Code en parallèle, le goulot d'étranglement
cesse d'être la machine. C'est **toi** : une session qui attend une décision de ta part reste à
l'arrêt, indéfiniment, pendant que tu es ailleurs. Elle ne redémarre pas toute seule.

Ce plugin fait de Claude le superviseur de ce parc : il lit où en est chacune, décide ce qui peut
l'être sans toi, relance celles qui dorment, et te rend **un** compte-rendu au lieu de vingt.

Ce n'est **pas** un moniteur. Un tour qui se termine par « voici l'état du parc » sans qu'aucune
session n'ait avancé est un tour raté — le livrable, c'est un sujet qui a bougé.

## L'idée centrale : lire et écrire ne coûtent pas la même chose

C'est le principe qui rend le mode viable, et il est contre-intuitif :

- **Lire le transcript d'une session coûte quelques centaines de tokens**, en silence, sans rien
  déclencher chez elle — même si elle dort depuis trois jours.
- **Lui écrire démarre un tour complet chez elle**, des dizaines de milliers de tokens.

D'où la règle : pour savoir **où elle en est**, on lit. Pour lui donner une **directive**, on écrit.
Demander « t'en es où ? » à vingt sessions, c'est payer vingt tours pour une information déjà sur le
disque.

## Les skills

| Skill | Ce qu'il fait |
|---|---|
| **`/claude-session-supervisor`** | Inventorie, trie les sessions en cinq états lus dans leur transcript (jamais dans leur titre), décide ce qui peut l'être sans toi, relance, et rend un compte-rendu unique. |
| **`/loop-creator`** | Conçoit, lance et relance une boucle `/loop` : objectif mesurable écrit là où le réveil suivant le relit, conditions d'arrêt (objectif atteint, le reste attend l'humain, stop, plafond, jamais de boucle jumelle), relance efficace d'une boucle arrêtée, choix de la cadence, durée de vie réelle d'une boucle, et boucle ou routine. |

`/claude-session-supervisor` embarque aussi ce qui s'apprend en conditions réelles et pas en théorie : pourquoi un troisième
message à une session qui ne répond pas ne sert à rien, comment distinguer « mon message n'est pas
arrivé » de « il attend », les quatre façons dont tes propres instruments de mesure te mentent, et la
limite à ne jamais franchir — **ne relaie jamais une autorisation** qu'on t'a donnée à toi vers
l'action irréversible d'une autre session.

## Installation

```
/plugin marketplace add Florentmaisoncelle/zerogravity-skills
/plugin install superviser-ses-sessions@zerogravity
```

Les deux skills sont installés ensemble.

## ⚠️ Prérequis — à vérifier avant d'y compter

Ce plugin suppose deux capacités, et elles ne sont pas garanties dans tous les environnements :

1. **Pouvoir lire les transcripts de session** (les fichiers `.jsonl` sous `~/.claude/projects/`).
   C'est le cœur : sans ça, pas de supervision, puisque tout repose sur le fait de savoir où en est
   une session **sans la déranger**.
2. **Pouvoir lister les autres sessions et leur écrire.** Selon ton installation, c'est exposé ou non.
   Sans ce canal, le plugin reste utile en **diagnostic** — il te dit quoi relancer, tu relances.

Le skill est écrit pour dire franchement, dès le premier tour, si une capacité manque. Un superviseur
qui promet de relancer et se contente de lire fait perdre plus de temps qu'il n'en gagne.

## 🌍 Portabilité

**`loop-creator` demande Claude Code ≥ v2.1.72** (persistance des tâches `/loop` à la reprise de session). Une boucle reste liée à la session : elle expire 7 jours après sa création, exige la machine allumée et l'application ouverte, et ne rattrape pas les réveils manqués. Au-delà, utiliser une tâche planifiée du bureau ou une routine cloud (le skill explique le choix).

**Classe : ADAPTABLE.** Aucun chemin, compte ou dépôt de l'auteur — mais le plugin suppose une façon
de travailler. Voici quoi adapter :

| Point | État | Ce que tu dois adapter |
|---|---|---|
| **Chemins / comptes** | Aucun en dur | Rien |
| **Système** | Indépendant de l'OS | Rien |
| **Emplacement des transcripts** | Le principe (« la dernière ligne est la preuve ») tient quel que soit le format ; les chemins, non | Le chemin chez toi, si ton installation diffère |
| **Canal pour relancer une session** | Selon l'environnement : outils dédiés, script maison, ou rien | Sans canal, le plugin devient un outil de diagnostic |
| **Mémoire du parc** | Le skill n'impose **aucun** tableau de bord | Si tu en tiens un, c'est lui la mémoire — pas la conversation |
| **Langue** | Le skill est rédigé en français | — |

## Sa philosophie, en une ligne

Un superviseur qui remonte tout à l'humain ne sert à rien — c'est le goulot qu'il était censé
supprimer. Un superviseur qui décide de tout est dangereux. Tout le skill tient dans le placement de
cette ligne.

