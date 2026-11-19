# Modèles prêts à copier

Trois modèles courts pour le skill `loop-creator` : le fichier d'état, le prompt de réveil, le reçu.

## 1. Fichier d'état de la boucle

À créer dans un endroit relu à chaque réveil (par exemple `loops/<nom>/ETAT.md` dans ton dépôt).

```markdown
# Boucle : <nom court>

## Objectif (mesurable)
<une phrase : à quoi on reconnaît que c'est fini>
Critère de preuve : <commande, fichier, chiffre qui le montre>

## Conditions d'arrêt
- Objectif atteint (preuve ci-dessus)
- Le reste attend l'humain : arrêter la boucle, écrire ce qu'on attend et de qui
- Stop explicite
- Plafond : <nombre de réveils, durée ou budget>
- Deux réveils vides de suite

## Fait
- <date> <lot terminé> — preuve : <où>

## Reste (dans l'ordre)
1. <prochain lot, premier travail du prochain réveil>
2. ...

## En attente de quelqu'un
- <quoi> — de <qui> — réponse à déposer dans <endroit>

## Boucle
- Créée le <date> (expire 7 jours après), cadence <intervalle> parce que <raison>
- Dernier réveil : <date> — résultat : <une ligne>
- Réveils vides consécutifs : 0
```

## 2. Prompt de réveil

```text
/loop 30m  Reprends la mission décrite dans <chemin de l'état> jusqu'à l'objectif.
Relis l'état, fais le prochain lot du reste, vérifie son effet, mets l'état à jour,
puis enchaîne tant qu'un lot sûr reste faisable. Rends un reçu d'une ligne.
Si l'objectif est atteint, ou si tout le reste attend quelqu'un : annule cette boucle,
écris pourquoi dans l'état, et dis-le en une ligne.
```

## 3. Reçu de fin de réveil (une ligne)

```text
<date> · lots faits : N · preuve : <où> · reste : M · prochaine action : <laquelle> · boucle : active | arrêtée (<raison>)
```

Un reçu qui dit « lots faits : 0 » deux fois de suite signifie : arrêter la boucle.

## 4. Relance d'une boucle arrêtée — fiche de contrôle

1. Retrouver la boucle existante (liste des tâches planifiées + fichier d'état).
2. Lire la raison de l'arrêt ; la condition de reprise est-elle levée ?
3. Qu'est-ce qui a changé depuis l'arrêt ? (historique du dépôt, décisions, fichiers modifiés)
4. Écrire cet intervalle dans l'état.
5. Corriger ce qui est devenu faux (plan, compteurs, adresses).
6. Réarmer la même boucle avec le même prompt stable.
7. Recalculer la cadence sur le reste réel.
