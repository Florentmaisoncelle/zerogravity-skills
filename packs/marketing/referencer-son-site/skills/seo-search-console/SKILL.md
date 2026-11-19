---
name: seo-search-console
description: >-
  Quand il faut lire les vraies données de Google Search Console d'un site (mots-clés proches de la première page, pages qui perdent du trafic, répartition mobile et ordinateur) → connexion en lecture seule une fois, puis trois analyses prêtes : requêtes en position 4 à 20 avec leur page, pages en baisse de plus de 30 % entre deux périodes de même longueur, et appareils. Triggers : « quels mots-clés sont proches de la page 1 », « quelles pages perdent du trafic », « lis Search Console », « mon trafic mobile a baissé », « pages à rafraîchir en priorité », « branche Search Console », « opportunités SEO rapides ».
metadata:
  scope: lecture de Search Console pour un site, lecture seule
  owns: la connexion locale à Search Console (jeton hors dépôt), les trois analyses et leurs seuils
  consumes: marketing-skills:seo-audit, marketing-skills:content-strategy, marketing-skills:analytics, marketing-relire-un-changement
---

# /seo-search-console : voir ce que Google dit vraiment du site

<!-- capitaliser:squelette-v1 -->
<!-- dev-qa-link -->
**Dev / Test / QA** : AUCUNE QA jumelle (script de lecture) ; la preuve est `scripts/test_search_console.py` (fonctions d'analyse, faux transport, garde-fous du jeton, sans réseau) ; la connexion réelle et les appels réels à Google se vérifient au premier usage chez la personne concernée.

## Ce que la compétence résout

Sans les chiffres de Search Console, on rafraîchit des pages au hasard et on découvre une chute de trafic des semaines trop tard. Résultat attendu : une liste courte et datée des requêtes proches de la première page (avec la page à travailler), des pages qui perdent beaucoup, et l'état des appareils, avec les limites de lecture écrites à côté.

## Stratégie

1. Lecture seule, partout. La portée demandée à Google est `webmasters.readonly` : rien ne peut être modifié dans Search Console.
2. Le jeton reste sur le poste, hors de tout dépôt, et ne contient que le jeton de renouvellement. Le script refuse un chemin situé dans un dépôt git.
3. Comparer deux périodes de même longueur, la plus récente se terminant 3 jours avant aujourd'hui (Google publie avec retard).
4. Un chiffre est un indice, pas une cause : toute sortie rappelle de vérifier la saison, l'indexation et le suivi avant d'agir.
5. L'agent prépare la liste, une personne décide quelles pages travailler. Aucune modification de site depuis cette compétence.

## Étapes

Scripts dans `scripts/`, sans bibliothèque à installer (Python standard).

1. **Préparer l'accès (une fois, gratuit)** : dans Google Cloud, créer un projet, activer « Google Search Console API », créer un identifiant OAuth « Application de bureau ». Garder le fichier téléchargé hors de tout dépôt et pointer `GOOGLE_CREDENTIALS_FILE` dessus (ou définir `GOOGLE_CLIENT_ID` et `GOOGLE_CLIENT_SECRET`). Le compte Google doit avoir accès à la propriété dans Search Console.
2. **Se connecter** : `python scripts/connexion_search_console.py`. Le navigateur s'ouvre, la personne accepte la lecture seule, le jeton est enregistré (par défaut `~/.config/zerogravity/search-console/jeton.json`, ou `GSC_TOKEN_FILE`). Cette étape se fait par la personne, dans son navigateur : l'agent ne tape jamais de mot de passe.
3. **Choisir la propriété** : `python scripts/lire_search_console.py sites`, puis définir `GSC_SITE_URL` (adresse avec barre finale, ou `sc-domain:exemple.fr`).
4. **Requêtes proches de la première page** : `proches-page-1 --jours 28 --exclure <nom de marque>`. Sortie triée par impressions, avec la page concernée. Seuils : position 4 à 20, au moins 50 impressions (réglables).
5. **Pages en baisse** : `pages-en-baisse --jours 28 --seuil 30`. Compare la période récente à la précédente. Une page doit avoir au moins 30 clics avant pour compter (réglable : en dessous, une variation n'est que du bruit). Une page disparue compte comme -100 %.
6. **Appareils** : `appareils --jours 28`. Utile quand une baisse touche surtout le mobile.
7. **Lire avec méthode** : voir `references/lire-les-resultats.md` (limites des données, ordre de traitement, passage à la relecture). Ajouter `--json` pour une sortie exploitable ailleurs. Le résultat peut contenir des requêtes d'utilisateurs : ne pas les publier tel quel.

## Frontières

- Audit complet d'un site (technique, contenu, liens) : `marketing-skills:seo-audit`.
- Choisir quoi écrire pour répondre à une requête : `marketing-skills:content-strategy`.
- Suivre les conversions et le trafic côté analyse : `marketing-skills:analytics`.
- Dire si un changement de page a marché : `/marketing-relire-un-changement` (les fenêtres SEO y sont).
- Volumes de recherche, difficulté, concurrents : outils de mots-clés tiers, hors de cette compétence.
- Toute écriture (mise à jour de page, envoi d'une URL à l'indexation) : hors périmètre, geste humain.

## Décisions et rejets

- **Bibliothèques Google et module de requêtes : remplacés par des appels HTTP en Python standard.** Moins de dépendances, et le transport se simule pour tester. Réouverture : si l'API change de forme.
- **Brief de contenu avec classement « mots-clés d'argent » : rejeté.** Il reposait sur des termes d'agence écrits en dur et sur un outil payant.
- **Veille de tendances : rejetée ici.** Elle relève de la veille du matin.
- **Détection des baisses de page : écrite ici.** Le client d'origine ne la faisait pas, elle venait d'un script écarté.
- **Jeton gardé dans le dossier du script (origine) : rejeté.** Risque de commit ; chemin hors dépôt imposé et vérifié.

## Preuves restantes

- Testé sans réseau : fenêtres de dates, filtre 4 à 20, exclusion de marque, baisse de 30 % (limite incluse), page disparue, petite page ignorée, appareils, jeton refusé dans un dépôt git, état de retour OAuth falsifié refusé, appel API simulé en lecture avec propriété encodée.
- NON EXÉCUTÉ ici : la connexion OAuth réelle et les appels réels à Google (aucune clé disponible dans cette session). Le point d'API `searchAnalytics/query` et la réponse sont écrits d'après la documentation publique de Google, à confirmer au premier usage réel.
- NON MESURÉ : combien de pages en baisse viennent vraiment d'un défaut du site plutôt que de la saison.

## Crédit

Retravaillé depuis seo-ops d'AI Marketing Skills (Single Grain, MIT), https://github.com/ericosiu/ai-marketing-skills (gsc_client.py et gsc_auth.py seuls) ; ce qu'on a changé : texte et scripts réécrits en français ; transport en Python standard au lieu des bibliothèques Google ; connexion avec état de retour vérifié et PKCE, jeton réduit au renouvellement et refusé dans un dépôt ; ajout de la détection des pages en baisse (seuil et volume minimal) et de la comparaison par appareil ; requêtes liées à leur page ; ordre de lecture et limites des données ; retrait du brief de contenu, de la veille de tendances, du préambule de suivi d'usage et de la vérification de version. Licence : `LICENSE-single-grain.txt`.
