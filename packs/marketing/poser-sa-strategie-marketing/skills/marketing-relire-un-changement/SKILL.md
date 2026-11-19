---
name: marketing-relire-un-changement
description: >-
  Quand un changement marketing, SEO ou de contenu est en ligne (page rafraîchie, nouveau texte, correctif technique, nouvelle séquence, prompt d'agent modifié) et qu'il faut dire s'il a marché → méthode de relecture sans code : fixer avant la métrique et la date, relever les chiffres réels avant et après, écarter les parasites, puis conclure promouvoir, continuer à tester, annuler ou non prouvé. Triggers : « est-ce que ça a marché », « relis le résultat de ce changement », « quand regarder après un rafraîchissement », « on garde ou on annule », « bilan avant et après », « readback », « le trafic a bougé, est-ce notre changement ».
metadata:
  scope: la relecture d'un changement déjà publié, avec fenêtres avant et après
  owns: le relevé de résultat (champs obligatoires, règles de promotion, fenêtres de relecture SEO)
  consumes: marketing-skills:analytics, marketing-skills:attribution, marketing-skills:seo-audit, marketing:performance-report, seo-search-console, marketing-mesurer-un-test
---

# /marketing-relire-un-changement : juger sur les chiffres, pas sur l'impression

<!-- capitaliser:squelette-v1 -->
<!-- dev-qa-link -->
**Dev / Test / QA** : AUCUNE jumelle (méthode sans code) ; la preuve est un relevé rempli dont chaque ligne a sa source de chiffres, relu par la personne qui décide ; le jugement final (garder, annuler) reste humain.

## Ce que la compétence résout

Un changement est souvent déclaré réussi parce que son auteur l'aime, ou parce qu'une courbe a monté la même semaine. Résultat attendu : pour chaque changement, un relevé écrit qui dit ce qui a changé, ce qu'on a mesuré avant et après, ce qui peut fausser la lecture, et une décision parmi quatre, avec la prochaine date de relecture.

## Stratégie

1. Écrire la règle de lecture AU MOMENT du changement : métrique principale, fenêtre avant, fenêtre après, date de relecture. On ne choisit pas la métrique en regardant le résultat.
2. Les chiffres viennent de l'outil qui les mesure (analyse de trafic, Search Console, CRM, plateforme d'envoi), jamais d'une impression ni d'un souvenir. Lecture seule.
3. Un changement ne se promeut que s'il bat l'avant sur la métrique principale, sans dégrader nettement les autres, ou s'il révèle un signal qui se répète.
4. Dans le doute, « non prouvé » est une réponse honnête. Il vaut mieux que deux conclusions contraires.
5. Une personne décide. L'agent prépare le relevé.

## Étapes

1. **Poser le relevé avant de publier** (modèle : `references/modele-de-releve.md`) : changement, responsable, page ou requête concernée, métrique principale, métriques secondaires, fenêtre avant, fenêtre après, date de relecture, ce qui annulerait le changement.
2. **Attendre la fenêtre.** Dates usuelles : `references/fenetres-de-relecture.md`. Relire plus tôt ne donne que du bruit.
3. **Relever** les chiffres des deux fenêtres, de même longueur, si possible sur les mêmes jours de la semaine. Noter la source et l'état de chaque lecture (réussie, partielle, échouée).
4. **Chercher les parasites** : saison, campagne en parallèle, pic de marque, retard d'indexation, changement de suivi, autre modification du site, volume trop faible. Chaque parasite trouvé est écrit.
5. **Conclure** avec la règle ci-dessous, puis noter la prochaine modification et la prochaine relecture.
6. **Faire valider** : la personne responsable lit le relevé et tranche. La publication, le rétablissement d'une ancienne version ou toute écriture dans un outil externe passent par elle.

## Règle de décision

- **Promouvoir** : la métrique principale s'améliore au-delà du bruit habituel, et les métriques à surveiller ne se dégradent pas nettement ; ou un signal se répète sur plusieurs pages ou segments.
- **Continuer à tester** : amélioration plausible mais volume faible, ou fenêtre encore courte. Fixer la nouvelle date.
- **Annuler** : dégradation de la métrique principale confirmée sur toute la fenêtre.
- **Non prouvé** : aucune lecture exploitable, ou parasites trop forts pour attribuer l'effet. Ce n'est pas un échec.
- **Ne jamais promouvoir** si : volume trop faible, attribution sale, saisonnalité qui explique l'écart, connecteur en échec, ou seul l'auteur est convaincu.

Un changement qu'on peut répartir au hasard entre deux groupes (objet d'e-mail, accroche) se mesure mieux avec `/marketing-mesurer-un-test`.

## Frontières

- Concevoir ou régler le suivi (événements, objectifs) : `marketing-skills:analytics` et `marketing-skills:conversion-tracking`.
- Choisir le modèle d'attribution des revenus : `marketing-skills:attribution`, puis `/marketing-relier-le-contenu-aux-contrats` pour le chiffrer.
- Un audit de référencement avant de modifier : `marketing-skills:seo-audit`. Lire Search Console : `/seo-search-console`.
- Mettre en forme le rapport final pour un client : `marketing:performance-report`.
- Test avec tirage au hasard et variantes : `/marketing-mesurer-un-test`; pour le concevoir : `marketing-skills:ab-testing`.

## Décisions et rejets

- **Relecture après changement seulement, pas de boucle d'auto-amélioration d'agents.** Le texte d'origine mêlait relecture marketing et amélioration de compétences d'IA ; seule la première est reprise.
- **Blocs par plateforme sociale et vidéo détaillés : rejetés.** Une liste générale de métriques par surface suffit (voir le modèle).
- **Noms d'outils d'une marque tierce : retirés.** Le texte nomme la fonction (suivi de pages, plateforme d'envoi), pas un produit.
- **Aucun script.** Un script ne remplace pas le jugement sur les parasites. Si une mesure statistique est nécessaire : `/marketing-mesurer-un-test`.

## Preuves restantes

- NON MESURÉ : première utilisation sur un changement réel. Après elle, noter dans le relevé si les fenêtres proposées étaient adaptées au site (certains sites s'indexent plus lentement).
- Les fenêtres de relecture sont des repères de départ, pas des règles prouvées.

## Crédit

Retravaillé depuis closed-loop-analytics-upgrade d'AI Marketing Skills (Single Grain, MIT), https://github.com/ericosiu/ai-marketing-skills, avec les fenêtres de relecture du bloc SEO de seo-ops ; ce qu'on a changé : réécrit en français comme une méthode de relecture sans code ; métrique et date fixées avant le changement ; quatre décisions et règles de non-promotion conservées ; fenêtres de relecture SEO reprises comme repères ; retrait des noms d'outils commerciaux et de la promotion d'un produit, des blocs par réseau social et des remarques d'humour ; promotion toujours validée par une personne. Licence : `LICENSE-single-grain.txt`.
