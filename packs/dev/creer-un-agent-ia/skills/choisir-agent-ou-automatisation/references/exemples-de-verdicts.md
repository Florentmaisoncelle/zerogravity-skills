# Exemples de verdicts par défaut

> Ce sont des propositions de départ, tirées d'un travail de relevé sur des besoins courants autour d'un CRM. Ce n'est
> pas un classement par fréquence d'usage : aucun classement de ce genre n'est publié. Chaque verdict se confirme
> par un pilote. Le CRM est ici le terrain d'exemple ; le raisonnement vaut pour une facturation, un support, un
> recrutement ou tout autre outil.

## Lecture rapide

- La plupart des besoins se règlent par l'outil existant ou par une automatisation.
- Les cas d'agent sont ceux où la tâche est de **résumer, rédiger ou expliquer** à partir de texte libre.
- Les deux cas où un agent seul serait le plus risqué : une **prédiction sans historique** et un **document financier**.

## Table

| Besoin | Verdict par défaut | Validation humaine |
|---|---|---|
| Enrichir une fiche contact ou entreprise | automatisation (source publique ou outil d'enrichissement), étape IA possible ; rapatrier d'abord la donnée | lot validé, base légale vérifiée |
| Noter et qualifier un contact entrant | outil existant d'abord (notation intégrée) ; note calculée par script ; agent seulement pour expliquer | proposition de note et de responsable |
| Attribuer un contact au bon responsable | automatisation (règle écrite) ; agent seulement si le critère est dans du texte libre | proposition d'attribution |
| Faire entrer un formulaire dans l'outil | outil existant ou automatisation, jamais un agent | création à côté, relue |
| Résumer un appel ou une réunion | agent (résumé et extraction de champs) | proposition de note, jamais d'écriture directe |
| Journaliser mails et rendez-vous | outil existant (synchronisation intégrée) d'abord ; sinon automatisation | par lot |
| Relancer ce qui dort | vérifier l'existant ; sinon sélection par script et brouillon par agent | brouillon, jamais d'envoi ; accord à chaque envoi |
| Alerter sur un dossier à risque | règle déterministe ; agent pour expliquer l'alerte | alerte seulement |
| Prédire un départ de client | pas maintenant : sans historique ni mesure, rien ; un prédictif intégré est une boîte noire | alerte seulement, si un jour |
| Synchroniser deux outils | automatisation (intégration native, n8n, Make), jamais un agent | création à côté, relue |
| Dédoublonner et auditer la qualité des données | détection par script, fusion en lot validé | fusion jamais seule |
| Préparer un rendez-vous ou un point quotidien | agent (synthèse), lecture seule | aucune écriture |
| Accueillir un client signé | automatisation (parcours fixe) ; texte du message rédigé à part | par lot de parcours |
| Facturer depuis une affaire gagnée | automatisation avec validation humaine ; hors de l'outil de vente | validation à chaque facture |
| Rapport hebdomadaire et coaching | l'agent rédige à partir de chiffres calculés par script | lecture seule |

## Ce qui fait changer un verdict

- **Du texte libre apparaît** là où une règle suffisait : une étape IA, voire un agent.
- **Le coût d'une erreur monte** (visible d'un client, irréversible) : on passe d'une validation par lot à une
  validation à chaque action, ou à « jamais seul ».
- **Le volume tombe** : le coût de mise en place ne s'amortit plus, le verdict devient « rien ».
- **L'outil déjà payé change** (une fonction intégrée arrive ou disparaît) : refaire la question 1 de la grille.
