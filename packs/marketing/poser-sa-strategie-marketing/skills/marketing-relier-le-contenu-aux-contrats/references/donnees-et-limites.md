# Données attendues et limites de lecture

## Format du fichier de contrats (`--contrats`)
```json
[{"montant": 12000, "date_signature": "2026-03-15",
  "parcours": [{"url": "/blog/exemple", "date": "2026-01-05"},
               {"url": "/etude-de-cas/exemple", "date": "2026-02-10"}]}]
```
Les autres champs éventuels (nom d'affaire, identifiant, contact) sont ignorés et n'apparaissent jamais dans le rapport. Mieux vaut ne pas les exporter.

## Où trouver un vrai parcours
- Un export du CRM des pages vues par chaque contact associé au contrat, avec leur date.
- Un export de l'outil de suivi (parcours par utilisateur) si l'identifiant du visiteur est relié au contact.
- À défaut, `--hubspot` fournit seulement la première et la dernière page vue par contact. Les modèles linéaire et décroissance se distinguent alors peu du premier contact : le rapport l'écrit en avertissement.

## Fichier de visites (`--ga4-fichier`)
```json
[{"page_path": "/blog/exemple", "sessions": 400, "users": 300, "conversions": 4}]
```

## Fichier de coûts (`--couts`)
Un montant par type de contenu pour la période : `{"article": 2400, "etude_de_cas": 1800}`. Types par défaut : article, etude_de_cas, webinaire, podcast, video, outil, page_offre, comparatif, autre.

## Règles de classement des adresses
Les motifs par défaut sont dans le script (`/blog/`, `/etude`, `/webinar`...). Un site qui range autrement fournit `--regles-url regles.json` avec deux clés, `types` et `etapes`, qui remplacent les défauts. Étapes : decision, consideration, decouverte ; l'ordre du fichier compte (la première qui correspond gagne).

## Limites à garder en tête
- **Attribution n'est pas causalité** : un article lu avant la signature n'est pas forcément ce qui l'a provoquée.
- **Visiteurs non identifiés** : ce qui a été lu avant que la personne devienne un contact est souvent perdu. Le premier contact est alors le premier contact connu, pas le premier contact réel.
- **Cycle long** : sur des cycles de plusieurs mois, la fenêtre doit couvrir le début des parcours. Les pages vues avant le début de la fenêtre comptent, mais celles que l'outil de suivi a déjà purgées non.
- **Plusieurs contacts par affaire** : le script lit jusqu'à cinq contacts par affaire ; les pages de tous sont fusionnées.
- **Petit volume** : sous 10 contrats exploitables, tout classement est anecdotique.
- **Devise** : tous les montants sont supposés dans la devise du plan.
- **Données personnelles** : les adresses de pages sont réduites à leur chemin, sans paramètres ; un segment contenant une arobase est masqué. Ne pas remonter les fichiers sources dans un document partagé.
