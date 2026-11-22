# Prompt d'exécution quotidienne — agent YouTube vers posts LinkedIn

Ce contrat s'utilise **après installation** de la routine, avec `config.yaml` et des accès fonctionnels à un stockage. Un simple chat sans scripts ni planificateur ne peut pas s'exécuter tous les jours de façon autonome.

---

Exécute aujourd'hui la veille vidéo du projet défini par `config.yaml`.

1. Charge les chaînes actives, les checkpoints et les vidéos/posts déjà enregistrés.
2. Lis les nouveaux éléments RSS de chaque chaîne, dans les limites configurées. Distingue vidéo déjà analysée, nouvel épisode et mise à jour.
3. Classe les vidéos par pertinence pour les lecteurs définis dans la configuration. Ignore celles hors sujet avec raison enregistrée.
4. Pour chaque vidéo retenue, récupère la transcription horodatée disponible, description, chapitres et liens. Si l'accès échoue, journalise le motif ; n'invente rien.
5. Extrais **tous les sujets éditoriaux indépendants**, avec `topic_id`, mécanisme, preuve et timestamps. Fusionne les répétitions ; refuse les sujets trop pauvres.
6. Vérifie les affirmations importantes auprès des sources primaires actuelles. Sans source suffisante, crée une fiche `a_verifier`, pas un post factuel assuré.
7. Rédige **un seul brouillon LinkedIn par sujet**, bref et informatif. Ajoute un visuel original seulement s'il est pertinent et autorisé. Conserve sources, timestamps et traçabilité.
8. Déduplique avant écriture. Crée ou met à jour les fiches uniquement si elles n'ont pas été corrigées par une personne entre-temps ; ne touche jamais une fiche publiée ou validée sans ordre.
9. Enregistre les vidéos, sujets et posts dans le stockage configuré. Vérifie par relecture les liens, textes, statuts et médias déposés.
10. Rends un rapport avec : chaînes lues, vidéos inédites, vidéos retenues/rejetées, sujets candidats, posts créés, doublons évités, sources manquantes, coûts connus et blocages.

**Règle absolue :** tout ce que tu crées reste brouillon ou en attente de validation humaine. Tu ne publies, ne valides, ne programmes définitivement et n'envoies rien.
