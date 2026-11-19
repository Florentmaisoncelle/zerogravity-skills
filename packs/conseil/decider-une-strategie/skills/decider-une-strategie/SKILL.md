---
name: decider-une-strategie
description: >-
  Quand une décision d'affaires est floue (marché, offre, produit, investissement, priorités, business case) ou qu'on veut que l'IA raisonne comme un consultant en stratégie → nommer la décision, la structurer sans recouvrement, tenir un registre des faits et des hypothèses, comparer de vraies options, choisir la bonne méthode d'analyse, analyser les 20 % qui peuvent renverser la décision, éprouver la recommandation contre son meilleur contre-cas, puis répondre en commençant par la recommandation. Se lance par `/decider-une-strategie:decider-une-strategie`. Déclencheurs : « aide-moi à trancher », « quelle stratégie », « business case », « investir ou non », « quelles priorités », « raisonne comme un consultant ». Ce qui manque : aucune compétence publique n'est appelée, sauf pour une question technique bornée (étape 6, par un workflow du même dépôt) ; toutes les autres étapes sont menées par le workflow lui-même, et chaque étape sans compétence le dit. Pas pour une stratégie marketing (positionnement, canaux, campagnes : `/poser-sa-strategie-marketing:poser-sa-strategie-marketing`), ni pour enquêter sur un système ou une cause technique (`/reflechir-a-fond:reflechir-a-fond`).
---

# Décider d'une stratégie d'affaires, la recommandation d'abord

## Objectif

Transformer une question d'affaires, de produit ou de stratégie floue en une **recommandation structurée, appuyée sur des preuves, prête à décider**.

Le but n'est pas de nommer des cadres d'analyse. Le but est d'utiliser le minimum de structure de conseil nécessaire pour mieux décider.

Principes : la structure avant l'analyse ; les hypothèses avant la recherche exhaustive ; les faits séparés des hypothèses ; de vraies options avant la recommandation ; le 80/20 (une petite part des causes explique l'essentiel du résultat : on analyse celle-là) ; des compromis explicites ; la réponse d'abord ; dire ce qui changerait la réponse.

Ce workflow n'écrit aucun fichier de lui-même. La réponse de l'étape 8 se garde là où la personne range ses décisions. Quand la décision attend quelqu'un d'autre (le dirigeant, un spécialiste, un client), la réponse le dit en tête sous « En attente : ce qu'on attend, de qui ». Le workflow s'arrête là : il ne devine pas cette décision et n'invente pas la suite.

## Avec les workflows voisins

Pour une mission d'IA ou d'automatisation chez un client, c'est `/implementer-l-ia-en-entreprise:implementer-l-ia-en-entreprise` qui porte les livrables (diagnostic, exigences, matrice d'options, business case, plan). Ce workflow-ci n'est pas appelé par elle : elle le cite seulement dans ses frontières, pour une question de stratégie d'entreprise. Il apporte la discipline de décision utile quand un choix se présente en cours de mission : cadrage, vraies options, contre-cas, conditions d'arrêt, synthèse en commençant par la réponse.

Quand `/reflechir-a-fond:reflechir-a-fond` est installé :

- ce workflow tient les décisions de marché, de produit, d'allocation, d'économie et de priorités ;
- la réflexion à fond tient l'enquête sur un système, l'architecture, la preuve en production, la recherche de cause et les problèmes techniques transverses.

**Passage de relais.**

Du conseil vers la réflexion à fond :
- formuler une seule question technique ou système, bornée ;
- demander les faits, les contradictions et les inconnues ;
- rapporter le résultat dans la décision d'affaires.

De la réflexion à fond vers le conseil :
- transmettre la base de faits déjà établie ;
- n'utiliser ce workflow que pour les options, l'économie, les priorités et la recommandation.

Pas de relais en cascade : un seul workflow tient la phase en cours.

<!-- prerequis:debut -->
## Prérequis

Ce workflow s'appuie sur des compétences publiques, installées à part. Aucune n'est indispensable : si l'une manque, le workflow le dit et fait l'étape à la main. Faire l'étape à la main veut dire suivre sa règle de choix, écrire ce qu'elle doit rendre (dans le fichier de l'étape, ou dans la réponse quand le workflow n'a pas de dossier) et dire ce qui reste à la charge de la personne.

```text
/plugin marketplace add addyosmani/agent-skills
/plugin install agent-skills@addy-agent-skills
```

Les workflows cités ici sont dans le même dépôt (le dépôt s'ajoute une fois : `/plugin marketplace add Gremelinn0/zerogravity-skills`) :

```text
/plugin install cadrer-un-chantier@zerogravity
/plugin install consultant-ia@zerogravity
/plugin install poser-sa-strategie-marketing@zerogravity
/plugin install reflechir-a-fond@zerogravity
```
<!-- prerequis:fin -->

En pratique, ce workflow n'appelle aucune compétence publique d'un autre projet : les seuls renvois sont les workflows du dépôt listés ci-dessus, tous facultatifs.

## Les étapes

<!-- etapes:debut -->
| # | Étape | Compétences | Règle de choix |
|---|---|---|---|
| 1 | Nommer la décision | à la main | Si le contexte manque, on pose des hypothèses provisoires (H) et on continue : jamais une réponse faite seulement de questions. Manque : aucune compétence ne pose la décision : le workflow l'écrit lui-même, depuis la question et ses faits. |
| 2 | Structurer le problème | à la main | Pas d'arbre géant pour une décision simple à deux issues : la structure s'arrête là où elle cesse de changer la décision. Manque : aucune compétence ne dessine cette structure : le workflow la construit lui-même. |
| 3 | Tenir le registre des preuves | Garder le journal des décisions : `agent-skills:documentation-and-adrs` | Une valeur proposée par l'analyste puis acceptée par le décideur devient un fait, avec cette décision pour source. Un chiffre donné de mémoire reste une hypothèse, avec qui peut le confirmer. Un accord entre plusieurs modèles n'est pas une preuve. Manque : aucune compétence ne tient ce registre : le workflow marque lui-même chaque chiffre et chaque jugement. |
| 4 | Générer de vraies options | à la main | Les options s'examinent à égalité : l'option préférée ne gagne pas par défaut parce que les autres n'ont pas été regardées. Quand les faits viennent déjà de /reflechir-a-fond:reflechir-a-fond, on entre ici : ce workflow ne sert alors qu'aux options, à l'économie, aux priorités et à la recommandation. Manque : aucune compétence ne génère ces options : le workflow les établit lui-même. |
| 5 | Choisir la bonne lentille | à la main | Une seule lentille, celle que le problème choisit. Porter, SWOT, BCG, JTBD, RICE ou un arbre des profits sont des outils, jamais des défauts : une salade de cadres, ou un SWOT à la place de l'analyse, est une erreur. Manque : les huit lentilles de strategy-skills-for-claude, que ce workflow sait déléguer, ne sont pas installées : il applique lui-même la lentille choisie. Pour un risque stratégique majeur, la lentille « risques et parades » n'a de toute façon pas de compétence propre. Aucune compétence publique n'est appelée pour ces méthodes : le workflow applique lui-même celle qui est choisie. |
| 6 | Analyser les 20 % qui peuvent renverser la décision | `reflechir-a-fond` | Une seule question technique bornée à la fois, formulée avant de passer la main, et son résultat revient dans la décision d'affaires. Pas de relais en cascade : un seul workflow tient la phase en cours. Le reste de l'étape est le travail du workflow : on n'analyse pas l'océan. |
| 7 | Mettre la recommandation à l'épreuve | à la main | Si le contre-cas est plus fort que la recommandation, on change la recommandation. Manque : aucune compétence ne tient le contre-cas : le workflow le fait lui-même. |
| 8 | Rendre la réponse d'abord | à la main | La recommandation d'abord, puis ce qui la renverserait. Une recommandation sans responsable, sans test ni prochain geste, ou sans condition qui la renverserait, est à refaire. Manque : aucune compétence ne rédige cette synthèse : le workflow l'écrit lui-même. |
<!-- etapes:fin -->

## Le détail de chaque étape

### 1. Nommer la décision

Écrire : la décision à prendre ; qui décide et pour qui ; le résultat voulu ; les contraintes ; l'horizon de temps ; ce qui est dans le périmètre et ce qui n'y est pas.

Si le contexte manque, poser des hypothèses provisoires (H) et continuer, au lieu de ne rendre que des questions.

### 2. Structurer le problème

Construire la plus petite structure utile, sans recouvrement et complète : on dit MECE (en anglais, « mutuellement exclusives, collectivement exhaustives »).

Une bonne structure :
- ses branches ne se recouvrent pas ;
- ensemble, elles couvrent ce qui peut changer la décision ;
- chaque branche peut se tester.

Pas d'arbre géant pour une décision simple à deux issues.

### 3. Tenir le registre des preuves

Marquer chaque affirmation importante :

- **F, fait** : observé, sourcé, ou décision ou contrainte énoncée par celui qui en est responsable ;
- **H, hypothèse** : jugement qui comble un trou, ou chiffre donné de mémoire, avec qui peut le confirmer ;
- **E, estimation** : calculée à partir de faits et d'hypothèses, calcul montré.

Une déduction tirée de faits s'écrit E quand elle est calculée, H sinon. Une valeur proposée par l'analyste puis acceptée par le décideur devient un F, avec cette décision pour source.

Pour chaque hypothèse qui porte la décision, noter : son importance, la force de sa preuve, la confiance, le test qui pourrait l'invalider, l'action si elle tombe.

### 4. Générer de vraies options

Créer un petit nombre de chemins vraiment différents. Pour chacun : l'avantage, le compromis, la faisabilité, le risque, l'économie si elle compte, l'adéquation stratégique, ce qui doit être vrai pour qu'il marche.

L'option préférée ne gagne pas par défaut parce que les autres n'ont pas été examinées à égalité. Quand les faits viennent déjà de `/reflechir-a-fond:reflechir-a-fond`, on entre ici directement.

### 5. Choisir la bonne méthode d'analyse

Seulement quand elle est pertinente, et une seule. C'est le problème qui choisit, pas l'habitude.

| Le problème | La méthode classique qui convient |
|---|---|
| on ne sait pas où l'on en est | un diagnostic de départ : quelques indicateurs chiffrés, leurs tendances, les écarts avec l'objectif |
| les croyances sont fragiles | la liste des hypothèses, classées par importance et par force de preuve, chacune avec son test |
| il faut choisir un chemin | une comparaison des options sur des critères pondérés (matrice de décision) |
| un investissement à justifier | un dossier chiffré : coûts, gains, délai de retour, point mort, trois scénarios (bas, central, haut) |
| trop d'initiatives pour les moyens | un classement par impact et effort, ou par score RICE (portée × impact × confiance ÷ effort) |
| il faut anticiper les concurrents ou le marché | les cinq forces de Porter (clients, fournisseurs, nouveaux entrants, substituts, rivalité), puis un jeu de rôle : que ferait chaque concurrent en réponse ? |
| un risque stratégique majeur | un tableau des risques (probabilité et gravité), avec pour chacun une parade et une option de repli |
| passer de la stratégie à l'exécution | une feuille de route par étapes, avec un responsable et un jalon chacune |
| une décision à écrire pour un dirigeant | une note d'une page : recommandation, trois raisons, risques, prochain geste |

Autres outils connus, à prendre seulement si le problème les appelle : le SWOT (forces, faiblesses, opportunités, menaces), la matrice BCG (croissance du marché contre part de marché), l'approche JTBD (le travail que le client « engage » un produit à faire) et l'arbre des profits (le profit découpé en revenus et en coûts). Une salade de cadres, ou un SWOT à la place de l'analyse, est une erreur.

Aucune compétence publique n'est appelée pour ces méthodes : le workflow applique lui-même celle qui est choisie.

### 6. Analyser les 20 % qui peuvent renverser la décision

Prioriser :
- les hypothèses qui pèsent le plus sur la recommandation ;
- les plus mal prouvées parmi les plus importantes ;
- les quelques données qui pourraient tuer une option.

On n'analyse pas l'océan. Quand un point technique ou système peut renverser la décision (est-ce faisable, est-ce vrai en production), on formule cette seule question avant de passer la main à `/reflechir-a-fond:reflechir-a-fond`, et son résultat revient dans la décision d'affaires.

### 7. Mettre la recommandation à l'épreuve

Avant de conclure :

- le contre-argument le plus fort ;
- l'hypothèse qui renverserait la décision ;
- un scénario défavorable ;
- la réaction probable des concurrents ou des clients ;
- un signal d'alerte ;
- une condition d'arrêt ;
- l'option de repli, testée avec la même rigueur.

Si le contre-cas (le meilleur argument contre la recommandation) est plus fort, on change la recommandation.

### 8. Rendre la réponse d'abord

Format par défaut :

```text
Décision :
Recommandation :
Pourquoi (3 raisons au plus, celles qui portent) :
Preuves :
Hypothèses critiques :
Options et compromis :
Contre-cas et mise à l'épreuve :
Risques et parades :
Conditions d'arrêt :
Prochains tests et actions :
```

Une recommandation sans responsable, sans test ni prochain geste, ou sans condition qui la renverserait, est à refaire.

## Mauvais réflexes

- la salade de cadres ;
- le SWOT à la place de l'analyse ;
- une option présentée comme inévitable ;
- des chiffres de marché sans source ;
- l'accord entre plusieurs modèles pris pour une preuve ;
- une longue recherche qui ne change pas la décision ;
- une recommandation vague, sans responsable, test ni prochain geste ;
- une recommandation sans condition qui la renverserait.

## Sources d'inspiration

Ce workflow est écrit avec nos mots, à partir de pratiques courantes du conseil en stratégie : le raisonnement par hypothèses, la structure sans recouvrement (MECE) et la réponse d'abord. Il a aussi été inspiré par le projet [gcamilo/management-consulting](https://github.com/gcamilo/management-consulting), sous licence MIT, dont aucun texte n'est copié. Ce workflow n'implique ni affiliation ni aval de la part d'un cabinet de conseil.

## Ce qui manque

- Les étapes 1 à 5 et 7 à 8 n'ont aucune compétence publique à appeler : le workflow pose la décision, la structure, le registre, les options, la méthode d'analyse, le contre-cas et la synthèse lui-même.
- Seule l'étape 6 peut passer la main, et seulement pour une question technique bornée, à un workflow du même dépôt.

## Frontières

| Demande | Va à |
|---|---|
| Un système, une cause, une architecture, un défaut qui revient | `/reflechir-a-fond:reflechir-a-fond` |
| Cadrer un chantier neuf avant de le lancer | `/cadrer-un-chantier:cadrer-un-chantier` |
| Une mission d'IA ou d'automatisation chez un client | `/implementer-l-ia-en-entreprise:implementer-l-ia-en-entreprise` |
| Une stratégie marketing (positionnement, canaux, campagnes) | `/poser-sa-strategie-marketing:poser-sa-strategie-marketing` |
