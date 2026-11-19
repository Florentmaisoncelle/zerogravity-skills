---
name: marketing-mesurer-un-test
description: >-
  Quand il faut savoir si une variante (titre, objet d'e-mail, accroche, page, annonce) bat vraiment l'actuelle, surtout avec peu de volume ou plusieurs variantes → tient un carnet local de tests, calcule un verdict honnête (écart significatif après correction des comparaisons multiples ET écart assez grand pour compter), refuse de conclure trop tôt et PROPOSE un gagnant sans jamais l'appliquer. Triggers : « est-ce que la variante B gagne », « mon test est-il concluant », « combien de données avant de conclure », « j'ai 5 variantes d'objet », « le test n'a pas de différence, que faire », « garde la trace de mes tests », « quel test lancer ensuite ».
metadata:
  scope: mesurer un test marketing (A/B ou jusqu'à 10 variantes) avec un carnet local et un verdict prudent
  owns: la règle de décision d'un test (double seuil, correction des comparaisons multiples, minimum d'échantillons), le carnet des gagnants validés
  consumes: marketing-skills:ab-testing (concevoir le test), marketing-skills:analytics (récupérer les chiffres), marketing-relire-un-changement (relire un changement non randomisé)
---

# /marketing-mesurer-un-test : un verdict de test qu'on peut défendre

<!-- capitaliser:squelette-v1 -->
<!-- dev-qa-link -->
**Dev / Test / QA** : AUCUNE QA jumelle (compétence de méthode avec un script local) ; la preuve est `scripts/test_moteur_de_tests.py` (cas gagnant, sans différence, petit volume, plusieurs variantes, parcours complet en ligne de commande) ; le jugement (quoi tester, adopter ou non) reste à la personne qui valide.

## Ce que la compétence résout

Un test lancé avec peu de volume donne presque toujours un « gagnant » : du bruit pris pour un effet. Résultat attendu : pour chaque test, une règle de décision écrite AVANT de regarder, un verdict qui dit l'un de ces cinq états (gagnant proposé, référence conservée, écart trop faible, sans différence, non concluant), et un carnet des seuls gagnants qu'une personne a validés.

## Stratégie

1. Fixer la règle à la création : seuil de significativité, écart utile, minimum par variante. Elle ne se retouche pas après avoir vu les chiffres.
2. Deux seuils, toujours ensemble : l'écart doit être significatif APRÈS correction des comparaisons multiples (méthode de Holm quand il y a plusieurs variantes) ET atteindre l'écart utile. Un écart net mais minuscule n'est pas une raison de changer.
3. Aucun verdict avant le minimum prévu : le script n'affiche alors aucune p-valeur, seulement l'avancement.
4. Distinguer « l'effet utile est écarté » de « le test n'a pas pu trancher ». Le second n'est pas la preuve que les variantes se valent.
5. L'agent calcule et propose, la personne valide. Rien n'est écrit dans un outil externe.

## Étapes

Le script : `scripts/moteur_de_tests.py` (numpy et scipy, aucun réseau, aucune clé). Données dans `--dossier`, la variable `MESURER_TESTS_DIR`, sinon `./donnees-tests`.

1. **Créer** : `creer --canal email --hypothese "..." --variable objet --variantes '["actuel","court"]' --metrique ouvertures`. La première variante est la référence. Choisir le type : `valeurs` (une valeur par unité publiée) ou `taux` (`--type taux`, succès sur essais). Sens `baisse` si plus bas est mieux. Écart utile par défaut 15 %, à régler selon ce qui justifie vraiment de changer.
2. **Journaliser** : `journaliser --id TEST-001 --variante court --valeur 42` (ou `--valeurs '[12,15,9]'`, ou `--succes 12 --essais 340`). Une mesure sans valeur est refusée, jamais comptée zéro.
3. **Scorer** : `scorer --id TEST-001`, une seule fois, quand le minimum est atteint. Relancer à chaque nouvelle donnée augmente les faux gagnants. Le verdict est enregistré et le test se clôt.
4. **Si non concluant** : décider d'arrêter ou de prolonger (`etendre --id ... --min-echantillons N`, décision tracée), puis scorer de nouveau une fois le nouveau minimum atteint.
5. **Valider** : `valider --id TEST-001 --decision oui|non`. Seul ce geste humain inscrit le gagnant au carnet (`carnet`). Changer la vraie page ou l'envoi reste à faire dans l'outil, par une personne.
6. **Suivant** : `suggerer --canal email` propose les variables pas encore testées. `lister` donne l'état et les gagnants en attente de validation.

Lecture des cinq états : voir `references/lire-un-verdict.md`.

## Frontières

- Concevoir le test (hypothèse, trafic nécessaire, partage de l'audience) : `marketing-skills:ab-testing`. Ici on mesure et on tranche.
- Récupérer les chiffres sources et vérifier le suivi : `marketing-skills:analytics`.
- Un changement qu'on ne peut pas randomiser (refonte de page, nouvelle accroche sur tout le site) : `/marketing-relire-un-changement`.
- Choisir comment attribuer des revenus à un contenu : `marketing-skills:attribution` puis `/marketing-relier-le-contenu-aux-contrats`.
- Un diagnostic de page avant de tester : `marketing-skills:seo-audit` ou la compétence de conversion du workflow.

## Décisions et rejets

- **Promotion automatique du gagnant vers un playbook : rejetée.** Chez nous un agent propose, une personne valide. Réouverture : jamais sans décision de la personne qui pilote.
- **Seuil de 10 échantillons pour l'e-mail et le contenu : rejeté.** Trop bas pour un test de rangs. Plancher actuel : 30 valeurs, ou 200 essais et 10 succès par variante. C'est un plancher, pas une garantie de puissance.
- **Test unilatéral et absence de correction : rejetés.** Test bilatéral, correction de Holm, intervalles ajustés au nombre de comparaisons.
- **Alerte de rythme de campagne branchée sur des API de pipeline : retirée.** Hors du sujet et dépendante d'outils tiers.
- **Mode « lot » séparé : retiré.** Jusqu'à 10 variantes sont acceptées partout, avec un avertissement au-delà de 4.

## Preuves restantes

- Testé sans réseau sur données inventées : gagnant, sans différence, bruit large (non concluant), écart significatif trop faible, variante pire, petit volume, 8 variantes sans effet, parcours en ligne de commande avec validation humaine.
- NON MESURÉ : le comportement sur de vraies données de campagne (distributions très asymétriques, nombreux zéros) et la puissance réelle des planchers choisis. Premier usage réel : relever le résultat dans le carnet et le comparer à ce que `marketing-relire-un-changement` observe après adoption.

## Crédit

Retravaillé depuis growth-engine d'AI Marketing Skills (Single Grain, MIT), https://github.com/ericosiu/ai-marketing-skills ; ce qu'on a changé : texte et script réécrits en français ; test bilatéral avec correction de Holm sur les variantes multiples ; plancher d'échantillons relevé et aucun verdict avant ; ajout du type « taux » (test exact) ; état « non concluant » distinct de « sans différence » ; règle fixée à la création ; promotion du gagnant proposée et validée par une personne ; suppression du préambule de suivi d'usage, de la vérification de version, de l'alerte de rythme et du tableau de bord hebdomadaire. Licence : `LICENSE-single-grain.txt`.
