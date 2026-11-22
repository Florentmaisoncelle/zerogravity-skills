# Prompt de setup — agent YouTube vers posts LinkedIn

Copiez ce prompt dans Claude Code, Codex ou un autre agent capable de travailler sur des fichiers et d'installer une routine.

---

Tu es chargé de **construire et tester** une routine éditoriale quotidienne, pas simplement de me produire un plan.

## Objectif

À partir d'une liste de chaînes YouTube de référence sur mon secteur, surveiller les nouvelles vidéos, sélectionner les plus pertinentes, récupérer les transcriptions autorisées, en extraire tous les sujets **réellement indépendants**, vérifier les faits et créer des brouillons LinkedIn dans **ma propre base**. Chaque brouillon garde son lien avec la vidéo et les passages utilisés. Je veux pouvoir le relire, le modifier, le programmer provisoirement ou le réutiliser plus tard.

**Aucun post n'est publié ou validé automatiquement.**

## Mes paramètres

Lis `config.yaml` (adapté de `config.exemple.yaml`) avant toute opération. N'invente ni chaîne ni identifiant. Demande uniquement les valeurs réellement indispensables si elles manquent : thématique, liste de chaînes ou URLs, système de stockage/droits, environnement d'exécution et fréquence.

## Avant de développer

1. Audite mes scripts, skills, connecteurs, bases et routines existants. Réutilise les briques disponibles au lieu de créer un second système parallèle.
2. Montre brièvement ce qui existe et ce qui manque ; choisis la solution la plus simple à maintenir.
3. Ne modifie pas mes routines actives, mes permissions de publication ni mes données existantes sans nécessité. Les secrets restent dans un coffre/variables d'environnement, jamais dans le dépôt.
4. Prévois une commande pour **traiter une vidéo à la demande** et une commande distincte pour la **surveillance RSS**.

## Pipeline à implémenter

### 1. Sources et détection

- Vérifie pour chaque chaîne son `channel_id` YouTube et conserve sa page publique.
- Lis le RSS `https://www.youtube.com/feeds/videos.xml?channel_id=...`, avec temporisation, gestion d'erreurs et checkpoint durable.
- Utilise `(channel_id, video_id)` comme identité stable ; n'analyse pas deux fois une vidéo inchangée.
- Classe les vidéos par pertinence, fraîcheur, spécificité et valeur pratique ; ne confonds pas popularité et qualité.

### 2. Extraction et preuve

- Récupère le titre, la date, la description, les liens, les chapitres et la transcription **lorsqu'elle est accessible légalement**. Conserve les timestamps et la langue.
- Si la vidéo ou le transcript est indisponible, arrête ce traitement proprement et enregistre `transcript_missing` ou `source_unavailable`. Ne fabrique aucun passage.
- Pour tout claim externe sensible à la date (nouvelle commande, version, prix, limitations, résultat), vérifie dans une documentation primaire. Conserve URL et date de contrôle.
- Ne transforme pas une opinion du vidéaste en expérience personnelle du rédacteur.

### 3. Découpage multi-sujets

Pour chaque vidéo, crée une liste de sujets possibles comportant :
`topic_id`, intitulé précis, mécanisme, bénéfice lecteur, timestamps de la vidéo, éléments de preuve, source de vérification, score de valeur, limites et recommandation `retenir/fusionner/rejeter`.

- Un sujet retenu doit pouvoir tenir **un post autonome** sans avoir besoin du reste de la vidéo.
- Fusionne les passages qui expliquent le même mécanisme ; sépare les fonctionnalités qui résolvent des problèmes distincts.
- Une vidéo peut donner **zéro à plusieurs** posts. Jamais de quota artificiel ou de post récapitulatif ajouté par défaut.
- Cherche les doublons contre les sujets déjà produits. Une même source ne doit pas recréer indéfiniment les mêmes posts.

### 4. Production de brouillons

Pour chaque sujet retenu :
- Choisis le type éditorial adapté. Produis **une seule candidate** LinkedIn en français, avec une accroche précise, un mécanisme concret, une preuve ou un exemple vérifié et une limite utile.
- Rédige en voix professionnelle de praticien, sans formules génériques ni histoire inventée. Termine à la dernière conséquence pertinente. N'ajoute pas de CTA décoratif.
- Prépare un premier commentaire uniquement s'il porte une vraie ressource utile.
- Crée ou récupère un visuel original lorsque sa valeur est réelle. Ne réutilise pas les images d'un tiers sans droits. Vérifie le téléchargement et la prévisualisation si le stockage prend des médias en charge.
- Conserve tous les liens sources en métadonnées, même quand le corps du post n'en contient pas.

### 5. Stockage et validation

Utilise **le stockage choisi dans la configuration**, sans imposer une plateforme : Notion, Supabase, Airtable, Google Sheets ou autre.

Prévois des enregistrements reliés : `channels`, `videos`, `topics`, `posts` (ou un schéma équivalent dans l'existant). Conserve :
- `video_id`, `topic_id`, entreprise/projet, titre, URL, timestamps, source factuelle, note de valeur, texte, média, statut, date de dernière analyse ;
- l'état de traitement et les motifs d'échec ;
- la version du texte et le contrôle de concurrence pour ne jamais écraser une correction humaine.

Statuts minimum : `a_traiter`, `extrait`, `a_verifier`, `brouillon`, `a_valider`, `valide_par_humain`, `erreur` (adapte-les aux états existants plutôt que de créer des statuts concurrents).

Aucune action automatique ne doit poser `valide_par_humain`, publier, envoyer un message ni engager une dépense sans l'autorisation requise.

### 6. Récurrence et observabilité

- Implémente un lanceur quotidien piloté par les paramètres ; journalise les vidéos vues, sujets retenus, brouillons créés, doublons évités et échecs.
- Reprise après panne par checkpoint, retries limités, verrouillage d'exécution si nécessaire.
- Expose un mode `dry-run` sans écriture ; un traitement d'une seule URL ; une vue/listing de tout ce qui a été produit.
- **N'active pas la planification sans mon accord explicite**. Fournis la commande ou la configuration d'activation.

## Tests obligatoires

Exécute et montre les résultats : nouveau RSS, même RSS rejoué, vidéo multi-sujets, vidéo sans transcript, deux sujets redondants, correction humaine conservée, récupération d'image, échec de stockage, aucun post publié ou validé par l'agent.

## Livrables

Dans le dépôt existant du propriétaire du système :
1. scripts/connecteurs exécutables et configuration d'exemple sans secrets ;
2. documentation d'installation, droits minimaux et limites ;
3. prompts versionnés, mode manuel et mode RSS ;
4. résultats d'un essai sur une vidéo réelle avec liens vers les brouillons ;
5. compte rendu bref : fichiers changés, tests passés/échoués, coûts observables, étapes restant à faire.

Si l'environnement ne permet pas une étape, signale précisément le blocage, conserve les éléments réalisés et n'annonce jamais la routine comme opérationnelle avant la vérification de bout en bout.
