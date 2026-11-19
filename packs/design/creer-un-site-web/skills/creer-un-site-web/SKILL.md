---
name: creer-un-site-web
description: >-
  Quand on veut créer un site web : une vitrine, une page de vente ou le site d'une app (« crée-moi un site vitrine »,
  « refais le site de mon cabinet », « il me faut une page de vente », « je veux un site qui sorte sur Google », « où en
  est mon site ? ») → affiche l'état calculé depuis le dossier `projet-site/`, puis déroule dix étapes dans l'ordre : la
  carte des pages, le texte, la direction artistique, les composants, le référencement, la vitesse, l'accessibilité, la
  mesure, les formulaires et la conversion, l'amélioration continue. Cinq étapes (référencement, vitesse,
  accessibilité, conversion, amélioration continue) se jouent sur le site en ligne, pas sur une maquette. La vitesse
  et l'accessibilité se mesurent, elles ne se jugent pas à l'œil. Le test au lecteur d'écran reste à une personne. Se
  lance par `/creer-un-site-web:creer-un-site-web`. Déclencheurs : « créer un site web », « site vitrine », « refaire mon
  site », « landing page », « page d'accueil », « direction artistique ». Pas pour faire trouver et convertir un site
  déjà en ligne sans le refaire : `/referencer-son-site:referencer-son-site` et
  `/convertir-les-visiteurs:convertir-les-visiteurs`. Pas pour ajouter une page ou un écran à une app existante :
  `/faire-evoluer-une-app:faire-evoluer-une-app`. Pas pour créer une app entière : `/creer-une-app:creer-une-app`.
---

# Créer un site web : de la carte des pages à la conversion, mesuré

## Ce que ça résout

Un site demande une dizaine de gestes dans l'ordre, et pour chacun plusieurs compétences installées font à peu près
la même chose. Sans point d'entrée, on maquette avant d'avoir le texte, on juge la vitesse « à l'œil », on oublie le
référencement ou l'accessibilité, et il faut tout réexpliquer. Ici : l'ordre, l'état, le choix tranché, et des chiffres
là où un avis ne vaut rien.

**Résultat attendu** : un site dont les pages, le texte, le design, les composants, le référencement, la vitesse,
l'accessibilité, la mesure et la conversion sont faits dans l'ordre et prouvés ; un dossier `projet-site/` qui dit à
tout moment où on en est.

## Stratégie

1. **Une compétence par étape, la meilleure.** La table des étapes (plus bas) dit laquelle et pourquoi. Les règles de
   choix et les manques sont aussi dans `references/workflow.json`, qui reste la seule source de cette table : en cas
   de désaccord, c'est le fichier qui fait foi.
2. **L'état d'abord, toujours calculé** depuis les fichiers du dossier, jamais recopié.
3. **Deux temps : avant et après la mise en ligne.** Les étapes 1, 2, 3, 4 et 8 se font sur une maquette ou un site
   encore hors ligne. Les étapes 5, 6, 7, 9 et 10 sont marquées « sur le site en ligne » : elles mesurent ou améliorent
   un site que le public peut ouvrir. Pas de trace de vitesse sur une maquette. Entre les deux, le site passe par
   `/tester-et-securiser:tester-et-securiser`, puis `/mettre-en-ligne:mettre-en-ligne`.
4. **L'ordre protège la décision** : le texte avant le design (une maquette remplie de faux texte se refait toujours),
   le plan de suivi avant la mise en ligne. Sauter une étape reste possible sur demande ; le journal dit laquelle et
   pourquoi.
5. **Un chiffre sans trace n'est pas une preuve.** La vitesse se mesure sur une trace avant et après chaque correction ;
   l'accessibilité se vérifie en direct, puis dans le code.
6. **Un texte publié au nom de l'entreprise** se relit avant d'être montré (ton naturel, aucun chiffre inventé). C'est
   vrai du texte de l'étape 2, mais aussi des titres, des boutons et des messages d'erreur des autres étapes.
7. **`modern-web-guidance:modern-web-guidance` est un aperçu publié par l'équipe Chrome de Google**
   (https://github.com/GoogleChrome/modern-web-guidance). Il s'appelle par `npx -y modern-web-guidance@latest` : la
   version n'est pas épinglée, donc relire ce qu'il renvoie. Il envoie des statistiques d'usage anonymes à Google ;
   `DISABLE_TELEMETRY=1` les coupe. On le lance donc avec cette variable. En Bash :
   `DISABLE_TELEMETRY=1 npx -y modern-web-guidance@latest search "dialogue modal"` ; en PowerShell : poser
   `$env:DISABLE_TELEMETRY = '1'` avant la commande. Même chose pour `retrieve`, qui ouvre un guide par son
   identifiant.
8. **Une seule validation, à l'étape 1.** La carte des pages est la seule validation, parce que tout le reste en
   découle ; ensuite tout se déroule. Restent à la personne : le goût produit qu'aucune charte n'écrit (la direction
   artistique se propose avec sa raison et son contraire), un compte à créer (outil de mesure), la publication.
9. **Les décisions se notent** au journal à chaque étape : quelques lignes suffisent pour savoir, d'un site à l'autre,
   ce qui a marché.

<!-- prerequis:debut -->
## Prérequis

Ce workflow s'appuie sur des compétences publiques, installées à part. Aucune n'est indispensable : si l'une manque, le workflow le dit et fait l'étape à la main. Faire l'étape à la main veut dire suivre sa règle de choix, écrire ce qu'elle doit rendre (dans le fichier de l'étape, ou dans la réponse quand le workflow n'a pas de dossier) et dire ce qui reste à la charge de la personne.

```text
/plugin marketplace add addyosmani/agent-skills
/plugin marketplace add addyosmani/web-quality-skills
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin marketplace add coreyhaines31/marketingskills
/plugin marketplace add pbakaus/impeccable
/plugin install agent-skills@addy-agent-skills
/plugin install design@knowledge-work-plugins
/plugin install frontend-design@claude-plugins-official
/plugin install impeccable@impeccable
/plugin install marketing-skills@marketingskills
/plugin install modern-web-guidance@claude-plugins-official
/plugin install web-quality-skills@addy-web-quality-skills
npx skills add bmad-code-org/BMAD-METHOD --skill bmad-ux -a claude-code
npx skills add vercel-labs/agent-skills --skill composition-patterns -a claude-code
npx skills add vercel-labs/agent-skills --skill react-best-practices -a claude-code
npx skills add vercel-labs/agent-skills --skill web-design-guidelines -a claude-code
```

La commande `npx skills add` (CLI Vercel `skills`) demande Node.js 22.20 ou plus (vérifié le 06/11/2026, https://github.com/vercel-labs/skills). Claude Code installé avec l'installeur natif n'en a pas besoin.

Les workflows cités ici sont dans le même dépôt (le dépôt s'ajoute une fois : `/plugin marketplace add Gremelinn0/zerogravity-skills`) :

```text
/plugin install convertir-les-visiteurs@zerogravity
/plugin install creer-un-agent-ia@zerogravity
/plugin install creer-une-app@zerogravity
/plugin install faire-evoluer-une-app@zerogravity
/plugin install mettre-en-ligne@zerogravity
/plugin install referencer-son-site@zerogravity
/plugin install tester-et-securiser@zerogravity
```
<!-- prerequis:fin -->

Seules `react-best-practices` et `composition-patterns` sont inutiles pour un site en HTML simple.

## Étapes

### 0. Le dossier, puis l'état (lecture seule)

**Le dossier.** Le workflow travaille dans `projet-site/`, à la racine du dépôt du site. Appelé par un autre workflow
(par exemple `/creer-une-app:creer-une-app`), il écrit quand même dans son propre `projet-site/` : l'appelant garde
seulement une note qui renvoie vers ce dossier. Dans ce cas, le workflow s'arrête quand il ne reste plus d'étape
hors ligne et rend la main ; l'appelant le relance après la mise en ligne. Dossier absent ou vide : il n'y a encore rien de fait, l'état est
« étape 1 » et le dossier se crée au premier passage. Si le dossier courant n'est pas celui du site, le dire en une
ligne et demander où il vit : rien ne s'écrit avant.

**L'état**, calculé depuis le journal et les fichiers :

```text
Site               mon-site
En ligne           non
Étapes             01 ✓  02 ✓  03 ✓  04 ✓  05 -  06 -  07 -  08 -  09 -  10 -
Dernière décision  2026-11-06 · 04 · composants faits
Étape suivante     08 La mesure → marketing-skills:analytics
```

- Le journal `projet-site/journal.md` a une ligne par décision :
  `AAAA-MM-JJ · NN · fait | en attente | sans objet | sautée | corrigée · <une phrase>`.
- Pour chaque étape, la dernière ligne du journal qui la nomme fait foi. `✓` : cette ligne dit `fait` ou `corrigée` et
  le fichier de l'étape existe. `s.o.` : elle dit `sans objet` ou `sautée` (l'étape n'est plus proposée). `-` : aucune
  ligne, ou le fichier manque.
- `corrigée` : l'étape est refaite après une correction ; elle reste ✓ et la ligne dit ce qui a changé. `sautée` : la
  personne a choisi de passer ; la ligne dit pourquoi. Exemple de `sans objet` : l'étape 9 d'un site sans formulaire.
- **Le site est en ligne** quand le journal porte une ligne `AAAA-MM-JJ · 00 · fait · en ligne : <adresse officielle>`
  (00 désigne le site lui-même, pas une étape). `/mettre-en-ligne:mettre-en-ligne` rend l'adresse officielle mais n'écrit pas
  dans ce journal : la ligne s'écrit ici, à la reprise, dès que `mise-en-ligne/` porte son étape 3 faite (on lit l'adresse dans sa
  dernière ligne), ou par l'appelant quand ce workflow est appelé (étape 10 de `/creer-une-app:creer-une-app`). Si la personne a
  déjà un site en ligne, on lui demande l'adresse et on écrit la ligne tout de suite.
- `en attente` : l'étape est préparée, mais elle dépend d'un geste ou d'une réponse qui arrive hors de la conversation. La ligne du journal dit ce qu'on attend et de qui. L'état l'affiche `att.` avec ce texte : l'étape n'est pas `✓`, parce que préparé n'est pas fait. Le workflow s'arrête là et le dit ; il n'invente jamais la suite (ni réponse, ni résultat, ni geste qu'on ne lui a pas confirmé). Quand la personne apporte ce qui est arrivé, la ligne `fait` suit. Ici : le test au lecteur d'écran, joué par une personne (étape 7), et la mise en ligne du site, dont dépendent les étapes marquées « sur le site en ligne » (étapes 5, 6, 7, 9 et 10).
- L'étape suivante est la première étape `-` ou `att.`, dans l'ordre (devant une étape `att.`, on demande d'abord où en est l'attente). Tant que le site n'est pas en ligne, les étapes marquées
  « sur le site en ligne » (5, 6, 7, 9, 10) sont mises de côté : on prend la première étape `-` parmi les autres. S'il
  n'en reste aucune, on dit que le site doit d'abord être testé puis mis en ligne, et qu'on reprendra à l'étape 5.
  Si toutes les étapes sont `✓` ou `s.o.`, le workflow est terminé.

Le fichier de chaque étape est dans `projet-site/` : `01-pages.md`, `02-texte.md`, `03-design.md`, `04-composants.md`,
`05-referencement.md`, `06-vitesse.md`, `07-accessibilite.md`, `08-mesure.md`, `09-conversion.md`,
`10-amelioration-continue.md`. Chaque étape l'écrit, même quand elle confie le travail à un autre workflow : le fichier
porte alors le résultat, la décision et l'endroit où vit le dossier de l'autre workflow.

**Une question n'est pas un ordre.** « Où en est mon site ? » : on donne l'état et la prochaine action, puis on
s'arrête. La commande du workflow, « continue » ou « déroule » : on enchaîne jusqu'à la première étape en attente, puis on s'arrête et on le dit.

**Une demande au milieu du chemin** (« fais l'audit SEO de mon site », « il est lent ») : si le site est en ligne
(on demande l'adresse et on écrit la ligne 00 si elle manque), on fait l'étape qui porte la demande (5 ou 6), on
l'inscrit au journal et on dit ce qu'elle suppose. Un site déjà existant n'a pas à repasser par les étapes 1 à 4 : on
les inscrit `sautée` seulement si la personne le confirme. Si le site n'est pas en ligne, on le dit : il n'y a rien
à mesurer sur une maquette.

### 1. Lancer l'étape suivante

Lire l'étape dans le tableau ci-dessous, appliquer sa règle de choix, invoquer la compétence retenue, écrire sa
sortie dans le fichier de l'étape, inscrire `fait` au journal (ou `en attente`, voir plus haut), puis passer à la suivante sans redemander. Quatre
précisions :

- **Un site ou une app.** La carte des pages se fait avec la compétence de site ; dès qu'il y a des écrans d'app,
  `bmad-ux` s'y ajoute avant tout design (états vides, erreurs, permissions).
- **React ou Next ?** `react-best-practices` et `composition-patterns` ne servent qu'à l'étape 4 d'un site React ou
  Next. Un site en HTML simple ne les charge pas.
- **La mesure d'abord.** Aux étapes 6 et 7, le chiffre ou le défaut vient d'un outil (trace Chrome DevTools,
  Lighthouse) lancé sur le site en ligne, puis la correction, puis la même mesure : l'écart est la preuve.
- **L'accessibilité garde un manque déclaré** : le test au lecteur d'écran. Le W3C le dit : aucun outil seul ne peut
  établir la conformité, une évaluation humaine est nécessaire (https://www.w3.org/WAI/test-evaluate/, vérifié le
  06/11/2026). On prépare ce test prêt à faire pour la personne (NVDA sous Windows, VoiceOver sur Mac et iPhone)
  avec les parcours à passer : se connecter, remplir le formulaire principal, acheter ou prendre rendez-vous.

Un geste n'a pas de compétence publique et se fait à la main :

- **La boucle d'amélioration continue (étape 10).** Relire les trois mesures (vitesse, accessibilité, conversion),
  choisir l'écran le plus faible, le corriger, refaire la même mesure, noter l'écart au journal, puis passer à l'écran
  suivant. `web-quality-skills:best-practices` aide sur la sécurité et la qualité du code.

<!-- etapes:debut -->
| # | Étape | Compétences | Règle de choix |
|---|---|---|---|
| 1 | La carte des pages | La carte des pages : `marketing-skills:site-architecture` ; `bmad-ux` | site-architecture pour un site ; bmad-ux en plus dès qu'il y a des écrans d'app, avant tout design. C'est la seule validation du workflow. |
| 2 | Le texte | Écrire le texte d'une page : `marketing-skills:copywriting` ; `marketing-skills:copy-editing` | Le texte avant le design : une maquette remplie de faux texte se refait toujours. |
| 3 | La direction artistique | Tenir la charte et le design : `design:design-system` ; `impeccable:impeccable` ; `frontend-design:frontend-design` | impeccable:impeccable : d'abord sa commande shape (le plan de l'expérience avant tout code), puis la construction des écrans, puis critique et polish, et animate pour les transitions ; le contrat DESIGN.md vaut pour toutes les pages. |
| 4 | Les composants | `modern-web-guidance:modern-web-guidance` · `react-best-practices` · `composition-patterns` · Construire un écran : `agent-skills:frontend-ui-engineering` | modern-web-guidance:modern-web-guidance d'abord pour tout HTML, CSS et JavaScript du navigateur, avec DISABLE_TELEMETRY=1 ; react-best-practices et composition-patterns (les deux règles de Vercel) seulement pour React ou Next ; emil-design-eng pour les animations et les détails. Les transitions se règlent avec la commande animate de impeccable:impeccable. |
| 5 | Le référencement | `referencer-son-site` | Le référencement a son propre workflow : on le lance une fois le site en ligne, puis il tourne chaque semaine. Cette étape écrit une note qui dit où vit son dossier. |
| 6 | La vitesse | `web-quality-skills:core-web-vitals` · `web-quality-skills:performance` | Mesurer avant et après chaque correction, sur le site en ligne ; un chiffre sans trace n'est pas une preuve, et une maquette n'a rien à mesurer. |
| 7 | L'accessibilité | `web-quality-skills:accessibility` · `web-design-guidelines` | La mesure en direct, puis la revue du code ; un défaut trouvé par l'un se vérifie par l'autre après correction. Manque : un test au lecteur d'écran : une passe automatique ne couvre que 30 à 40 % des critères WCAG. un test au lecteur d'écran. Le W3C dit qu'aucun outil seul ne peut établir la conformité et qu'une évaluation humaine est nécessaire (https://www.w3.org/WAI/test-evaluate/, vérifié le 06/11/2026). Aucune compétence ne le fait ; on prépare les parcours à passer et une personne les joue avec NVDA sous Windows ou VoiceOver sur Mac et iPhone. |
| 8 | La mesure | `marketing-skills:analytics` | Le plan de suivi avant la mise en ligne, donc sans attendre les étapes en ligne ; les tests A/B se font dans /convertir-les-visiteurs:convertir-les-visiteurs. |
| 9 | Les formulaires et la conversion | `convertir-les-visiteurs` | La conversion a son propre workflow : le diagnostic de la page, le test, la capture, la ressource gratuite. Cette étape écrit une note qui dit où vit son dossier. |
| 10 | Améliorer le site en continu | Améliorer le site en continu : `web-quality-skills:best-practices` | La compétence par défaut de chaque tâche d'abord ; les autres selon le cas qu'elles disent. Un écran à la fois, rendu prouvé avant le suivant. Manque : aucune compétence publique pour la boucle elle-même : on relit les mesures de vitesse, d'accessibilité et de conversion, on choisit l'écran le plus faible, on le corrige, on refait la même mesure et on note l'écart avant de passer au suivant. |
<!-- etapes:fin -->

### 2. Clore un passage

À la fin de chaque séance, on écrit l'état (fait, reste, prochaine action) au journal. Si une compétence a déçu à une
étape, on le note aussi, pour rouvrir le choix de la compétence de cette étape.

## Pourquoi ces choix

- Dix étapes, de la carte des pages à l'amélioration continue, séparées de la création d'app pour servir aussi un site
  vitrine seul. La critique du design n'est pas une étape à part : `impeccable:impeccable` la fait.
- La vitesse se mesure avec `web-quality-skills:core-web-vitals` et `web-quality-skills:performance`, par Chrome
  DevTools : une seule paire de compétences, pour ne pas avoir deux mesures qui divergent.
- `modern-web-guidance:modern-web-guidance` est la seule à dire ce que le navigateur sait faire aujourd'hui : on la
  garde malgré son statut d'aperçu, avec la télémétrie coupée.

## Ce qui manque

- **Le test au lecteur d'écran** : aucune compétence ne le fait, et une passe automatique ne le remplace pas.
- **La boucle d'amélioration continue** (étape 10) : aucune compétence publique, elle se fait à la main.

## Frontières

| Demande | Va à |
|---|---|
| Créer une app, un SaaS (le site en est une étape) | `/creer-une-app:creer-une-app` |
| Ajouter une page ou un écran à une app existante, un défaut sur le site (un bouton ne répond pas) | `/faire-evoluer-une-app:faire-evoluer-une-app` |
| Tester, relire le code, sécuriser avant la sortie | `/tester-et-securiser:tester-et-securiser` |
| Mettre en ligne | `/mettre-en-ligne:mettre-en-ligne` |
| Un agent IA | `/creer-un-agent-ia:creer-un-agent-ia` |
| Faire trouver un site existant (référencement) | `/referencer-son-site:referencer-son-site` |
| Faire convertir un site existant (page, test, ressource gratuite) | `/convertir-les-visiteurs:convertir-les-visiteurs` |
