---
name: marketing-relier-le-contenu-aux-contrats
description: >-
  Quand il faut savoir quels contenus (articles, études de cas, webinaires, pages d'offre) ont précédé les contrats gagnés, ou ce que rapporte un type de contenu → fixe la question et le modèle avant de regarder, croise les affaires gagnées du CRM (HubSpot, lecture seule) et les visites GA4, attribue le revenu selon trois modèles (premier contact, linéaire, décroissance), montre si le classement tient d'un modèle à l'autre et signale les étapes du parcours sans contenu. Triggers : « quels contenus font signer », « le contenu rapporte-t-il », « attribue les contrats à mes articles », « coût par contrat de mes contenus », « quel contenu avant la signature », « relie mes pages aux deals gagnés », « ROI du contenu ».
metadata:
  scope: attribution du revenu gagné aux contenus consultés avant la signature, lecture seule
  owns: le plan de mesure fixé avant lecture, les trois modèles, les avertissements de qualité des données
  consumes: marketing-skills:attribution, marketing-skills:analytics, marketing-skills:revops, marketing:performance-report, marketing-relire-un-changement
---

# /marketing-relier-le-contenu-aux-contrats : relier ce qu'on publie à ce qu'on signe

<!-- capitaliser:squelette-v1 -->
<!-- dev-qa-link -->
**Dev / Test / QA** : AUCUNE QA jumelle (script de lecture) ; la preuve est `scripts/test_attribuer_les_contrats.py` (trois modèles, petit volume, classement instable, absence de donnée nominative, faux transport HubSpot, refus sans plan ni source) ; le jugement (quelle question, que décider d'un classement) reste à la personne.

## Ce que la compétence résout

On publie beaucoup et on ne sait pas quels contenus comptent avant une signature. Les rapports d'attribution flattent : modèle choisi après coup, trois contrats pris pour une tendance, données d'exemple prises pour de vraies. Résultat attendu : un rapport daté qui dit la question posée, le modèle choisi avant, le nombre de contrats réellement exploitables, ce qui est écarté, si le classement résiste au changement de modèle, et rappelle qu'un contenu vu avant une signature n'est pas la preuve qu'il l'a provoquée.

## Stratégie

1. **Fixer avant de regarder** : question, métrique (revenu ou nombre de contrats), modèle principal, fenêtre, demi-vie. Le plan est daté et ne se modifie pas : un autre choix donne un nouveau plan.
2. **Trois modèles côte à côte** : premier contact, linéaire, décroissance. Le modèle principal décide, les deux autres servent de test de solidité. Si le haut du classement change, on ne conclut pas.
3. **Le volume avant tout** : sous 10 contrats exploitables, le rapport le dit en tête et se lit comme des exemples.
4. **Jamais de donnée inventée** : une source illisible arrête le script. Les contrats sans parcours, sans montant ou sans date sont comptés et écartés, jamais complétés.
5. **Lecture seule et données minimales** : HubSpot et GA4 en lecture. Ni nom d'affaire, ni identifiant, ni coordonnées de contact dans le rapport ; adresses de pages réduites à leur chemin.
6. **L'agent prépare, une personne décide** : le rapport informe une décision de contenu, il n'en déclenche aucune.

## Étapes

Script : `scripts/attribuer_les_contrats.py` (Python standard ; `google-analytics-data` seulement pour `--ga4`).

1. **Cadrer** : choisir avec la personne ce qu'elle veut décider (quoi publier de plus ? où couper ?). Choisir le modèle principal avec `marketing-skills:attribution` ; la demi-vie suit la durée du cycle de vente.
2. **Fixer** : `fixer --question "..." --metrique revenu --modele-principal decroissance --debut 2026-01-01 --fin 2026-06-30 --demi-vie 30 --sortie plan.json`.
3. **Rassembler les données** (voir `references/donnees-et-limites.md`) :
   - parcours complets : un fichier `--contrats` exporté (montant, date de signature, pages vues avec leur date) ;
   - ou `--hubspot` : jeton `HUBSPOT_TOKEN` (droits de lecture des affaires et des contacts seulement). Parcours réduit à la première et à la dernière page vue par contact : le rapport l'indique.
   - visites : `--ga4-fichier` (export) ou `--ga4` avec `GA4_PROPERTY_ID` et `GA4_CREDENTIALS_JSON` (compte de service avec droit de lecture).
4. **Produire** : `rapport --plan plan.json --contrats contrats.json --ga4-fichier ga4.json --sortie rapport.json`. Option `--couts couts.json` pour un coût par contrat attribué par type de contenu ; `--regles-url` si les adresses du site ne suivent pas les motifs par défaut (`/blog/`, `/etude-de-cas/`...).
5. **Lire dans l'ordre** : avertissements, qualité des données, stabilité entre modèles, contenus, types, étapes du parcours sans contenu, coûts.
6. **Décider avec la personne** : quel contenu renforcer, lequel arrêter, quel trou examiner. Un changement décidé se relit ensuite avec `/marketing-relire-un-changement`.

## Frontières

- Choisir un modèle d'attribution, comprendre ses biais : `marketing-skills:attribution`.
- Régler le suivi (événements, objectifs, canaux) : `marketing-skills:analytics` et `marketing-skills:conversion-tracking`.
- Le CRM lui-même (étapes, propriétés, hygiène) : `marketing-skills:revops`.
- Mettre en forme un rapport pour un client : `marketing:performance-report`.
- Savoir si un changement précis a marché : `/marketing-relire-un-changement`; tester deux versions : `/marketing-mesurer-un-test`.
- Écouter les appels de vente pour en tirer objections et signaux : hors de cette compétence (compétences de vente).

## Décisions et rejets

- **Modèle « dernier contact » : retiré.** Il favorise les pages de tarif et de contact, qui ne disent rien du contenu éditorial. Trois modèles suffisent. Réouverture : si la question est justement la page de conversion.
- **Données d'exemple substituées en cas d'échec : supprimées.** L'original affichait un rapport sur des données d'exemple quand une source échouait. Un rapport faux qui a l'air vrai est pire qu'une erreur.
- **Pages vues après la signature : ignorées.** L'original leur donnait un poids supérieur à 1 dans le modèle de décroissance.
- **Rapport client multi-sources, extraction d'appels de vente, boucle d'amélioration en double : non repris.** Hors périmètre ou couverts ailleurs.
- **Coût par « conversion » GA4 : remplacé par coût par contrat attribué.** Une conversion de site n'est pas un contrat.
- **Seuil de 30 % pour signaler une étape sans contenu : gardé comme repère arbitraire**, réglable, et dit tel quel dans l'aide.

## Preuves restantes

- Testé sans réseau sur données inventées : modèles à valeur connue, somme des parts égale au montant, contenu vu après signature, contrats écartés, petit volume, classement instable, absence de donnée nominative, pagination et lecture seule avec un faux HubSpot, refus sans plan, sans source ou sans jeton.
- NON EXÉCUTÉ ici : la lecture réelle de HubSpot et de GA4 (aucun jeton dans cette session). Les noms de propriétés HubSpot du parcours (première et dernière page vue) et la métrique de conversion GA4 sont écrits d'après la documentation publique et se règlent par variables d'environnement ; à confirmer au premier usage.
- NON MESURÉ : le nombre de contrats nécessaire avant qu'un classement soit stable sur un vrai site ; le seuil de 10 est un repère prudent, pas un calcul.

## Crédit

Retravaillé depuis revenue-intelligence d'AI Marketing Skills (Single Grain, MIT), https://github.com/ericosiu/ai-marketing-skills (revenue_attribution.py seul, lu en entier) ; ce qu'on a changé : texte et script réécrits en français ; trois modèles au lieu de quatre ; plan de mesure fixé avant le rapport ; suppression du repli silencieux sur des données d'exemple ; pages vues après la signature ignorées ; avertissements de volume, de parcours courts, de classement instable et de suivi incomplet ; adresses réduites à leur chemin et aucune donnée nominative dans le rapport ; coût par contrat attribué ; lecture HubSpot en pagination et parcours à deux points explicité ; retrait du rapport client, de l'extraction d'appels, du préambule de suivi d'usage et de la vérification de version. Licence : `LICENSE-single-grain.txt`.
