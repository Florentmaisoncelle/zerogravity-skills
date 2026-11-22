# Agent YouTube → Posts LinkedIn

Une routine configurable qui surveille des chaînes YouTube choisies, analyse les vidéos pertinentes et prépare **un brouillon LinkedIn par sujet autonome**, avec ses sources et son média lorsque c'est utile.

La transcription d'une vidéo peut contenir un, trois ou huit sujets : **aucun quota ne force la création de posts**.

## Ce que contient cette ressource

- [Prompt de configuration](PROMPT_SETUP.md) : à remettre à Claude Code, Codex ou un agent capable de coder et de connecter vos outils, pour installer le système.
- [Prompt quotidien](PROMPT_QUOTIDIEN.md) : contrat du traitement récurrent, à réutiliser dans votre automatisation.
- [Configuration exemple](config.exemple.yaml) : paramètres à adapter à votre secteur, vos chaînes et votre base.

**Périmètre exact :** prompts et architecture réutilisables, **pas un service SaaS clé en main**. L'installation, les autorisations et l'exécution dépendent des outils disponibles dans votre environnement. Aucun contenu n'est publié automatiquement.

## Configuration en pratique

1. Choisissez vos sujets, 3 à 10 chaînes et un stockage : Notion, Supabase, Airtable ou Google Sheets, par exemple. Les IDs exacts des chaînes sont à vérifier.
2. Dupliquez `config.exemple.yaml`, remplissez vos choix et fournissez-le avec le prompt de setup à votre agent de développement.
3. Faites exécuter un pilote sur **une vidéo réelle**. Vérifiez les fiches vidéo, les posts, les sources, les médias et l'absence de doublons.
4. Activez ensuite la récurrence quotidienne dans le planificateur de votre choix **après votre validation**.

## Sorties attendues

- **Chaîne** : ID YouTube, URL, sujets couverts, statut du suivi.
- **Vidéo** : ID, URL, date, titre, transcription horodatée quand disponible, état d'extraction et dernière analyse.
- **Sujet** : ID stable, intérêt éditorial, source et timestamps, preuves, raison de fusion ou rejet.
- **Post** : titre, texte candidat, statut "à relire", sources, visuel autorisé, lien vers vidéo/sujet, historique de validation.

Le système doit rester **idempotent** : relancer une analyse ne recrée pas les mêmes fiches et n'écrase pas les modifications humaines.

## Méthode et limites

- Surveillance via le flux RSS public d'une chaîne : `https://www.youtube.com/feeds/videos.xml?channel_id=<ID>`.
- Une vidéo trouvée n'implique pas qu'une transcription soit disponible. Si elle manque ou si l'accès est refusé, conserver l'erreur et passer à une revue manuelle, sans inventer des propos.
- Le transcript atteste les affirmations du créateur, **pas leur exactitude**. Les nouvelles fonctionnalités, commandes, chiffres et disponibilités sont vérifiés dans les sources primaires.
- Les images et captures de tiers ne sont pas automatiquement réutilisables. Préférer une démonstration originale, un visuel créé pour le post ou un média pour lequel les droits sont clairs.
- La routine prépare le contenu. **Seul l'humain valide une éventuelle publication.**

Ressource publique proposée par ZeroGravity. Exemple de prompt de workflow, à adapter à votre environnement et à tester avant usage récurrent.
