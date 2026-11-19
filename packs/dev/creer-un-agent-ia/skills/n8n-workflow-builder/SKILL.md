---
name: n8n-workflow-builder
description: >-
  Construit un workflow n8n complet, soit un fichier JSON à importer dans l'interface, soit un déploiement par l'API de n8n. Sert pour l'étape « Construire » d'un agent sur n8n (assistant, planifié ou déclenché) quand la compétence officielle de n8n ne convient pas : instance ancienne, accès fermés, pas de connecteur.
  Déclencheurs : « construis un workflow n8n », « génère le JSON n8n », « déploie ce workflow par l'API », « un agent planifié sur n8n », « une automatisation déclenchée par un webhook ».
---

# Construire un workflow n8n

## Quand l'utiliser

Tu as décidé que ton agent tourne sur n8n (voir `creer-un-agent-ia:choisir-agent-ou-automatisation`). Il faut maintenant produire le workflow lui-même.

Commence par la compétence officielle de n8n (`n8n-skills:n8n-workflow-lifecycle-official`) si elle est installée et si Claude a un accès direct à ton instance. Cette compétence-ci prend le relais dans trois cas : l'instance est ancienne ou auto-hébergée sans le connecteur officiel, les accès sont fermés (pas d'API ouverte), ou tu veux un fichier JSON que tu relis avant de toucher à l'instance.

Pour réparer un workflow qui échoue, passe plutôt par `n8n-skills:n8n-debugging-official`.

## Étape 1. Poser le besoin

Avant d'écrire une ligne de JSON, relève (dans la conversation ou dans la fiche de l'agent) :

- **Le déclencheur** : un message de chat (assistant), un horaire (planifié), un appel entrant ou un événement d'une application (déclenché), ou un lancement à la main pour tester.
- **La source** : d'où viennent les données, avec quelle application et quel droit d'accès.
- **La destination** : où le résultat est écrit, envoyé ou enregistré.
- **La logique** : filtres, calculs, branches, et ce que l'agent décide lui-même par rapport à ce qui est fixe.
- **Les champs à faire passer** : liste exacte, avec leur nom côté source et côté destination.
- **Le mode de livraison** : un JSON à importer, ou un déploiement par l'API.

Si une de ces réponses manque, demande-la. Un champ deviné (nom d'un attribut personnalisé, espace de noms, identifiant d'un pipeline) casse le workflow en silence.

## Étape 2. Choisir la forme

| Forme | Point de départ | Quand |
|---|---|---|
| Assistant | un déclencheur de chat, puis le nœud d'agent avec son modèle et ses outils | quelqu'un pose des questions et l'agent répond |
| Planifié | un déclencheur à horaire (Schedule) | un travail régulier : relevé, tri, relance, rapport |
| Déclenché | un Webhook ou le déclencheur d'une application | l'agent réagit à un événement |

Une forme simple vaut mieux qu'un agent avec dix outils. Si le chemin est toujours le même, écris des nœuds fixes et réserve le nœud d'agent à l'étape qui demande du jugement.

## Étape 3. Choisir le mode de livraison

Pose la question si elle n'est pas tranchée : « Un fichier JSON à importer à la main, ou un déploiement direct par l'API ? » Par défaut, produis le JSON : c'est le plus sûr, tu relis avant d'importer.

## Étape 4A. Produire un JSON importable

Le fichier s'importe par le menu de l'interface n8n (Import from file ou coller le JSON).

**Règles de forme**
- Un objet avec `name`, `nodes`, `connections`, et `settings`.
- Chaque nœud porte un `id` unique (format UUID), un `name` unique, un `type`, un `typeVersion`, une `position` `[x, y]` et des `parameters`.
- Les `typeVersion` dépendent de ta version de n8n. Le plus sûr : ajouter un nœud de chaque type dans l'interface, l'exporter, et recopier sa version. Un `typeVersion` trop récent est refusé par une instance ancienne.
- Types courants : `n8n-nodes-base.webhook`, `n8n-nodes-base.scheduleTrigger`, `n8n-nodes-base.if`, `n8n-nodes-base.set`, `n8n-nodes-base.code`, `n8n-nodes-base.httpRequest`. Pour un agent : le déclencheur de chat et le nœud d'agent du paquet LangChain de n8n, s'ils sont présents sur ton instance.
- Les connexions se déclarent par le nom du nœud : `{ "Nœud A": { "main": [[{ "node": "Nœud B", "type": "main", "index": 0 }]] } }`. Un nœud `if` a deux sorties : la première pour vrai, la seconde pour faux.
- Une expression commence par `=` et s'écrit `{{ $json.champ }}`.

**Enchaînement standard**

```
Déclencheur → IF (filtre) → HTTP Request (lecture) → Set (mappage des champs) → HTTP Request (écriture)
```

**Squelette minimal**

```json
{
  "name": "Exemple : webhook vers filtre",
  "nodes": [
    {
      "id": "00000000-0000-4000-8000-000000000001",
      "name": "Réception",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [240, 300],
      "parameters": { "path": "exemple", "httpMethod": "POST" },
      "notes": "Reçoit l'événement envoyé par l'application source."
    },
    {
      "id": "00000000-0000-4000-8000-000000000002",
      "name": "Est concerné ?",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [460, 300],
      "parameters": {
        "conditions": {
          "string": [
            { "value1": "={{ $json.body.statut }}", "operation": "equal", "value2": "actif" }
          ]
        }
      },
      "notes": "Laisse passer seulement les éléments au statut actif."
    }
  ],
  "connections": {
    "Réception": { "main": [[{ "node": "Est concerné ?", "type": "main", "index": 0 }]] }
  },
  "settings": {}
}
```

## Étape 4B. Déployer par l'API

Il te faut l'adresse de l'instance (par exemple `https://ton-n8n.exemple` ou `http://localhost:5678`) et une clé d'API (Réglages, API, créer une clé). Ne la colle jamais dans le JSON ni dans un fichier partagé : mets-la dans une variable d'environnement du terminal.

```bash
# 1. Créer le workflow (le corps ne garde que name, nodes, connections, settings)
curl -X POST "$N8N_URL/api/v1/workflows" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" \
  -H "Content-Type: application/json" \
  -d @workflow.json

# 2. L'activer, avec l'identifiant rendu par la création
curl -X POST "$N8N_URL/api/v1/workflows/ID_DU_WORKFLOW/activate" \
  -H "X-N8N-API-KEY: $N8N_API_KEY"
```

Ces deux appels sont à vérifier dans la documentation de l'API de ta version de n8n : les routes changent d'une version à l'autre. L'API refuse souvent les champs en trop (`id`, `active`, `tags`) à la création : retire-les du corps. Si l'activation par l'API échoue sur ta version, active le workflow dans l'interface. Crée-le d'abord inactif, teste, puis active.

## Règles qui comptent

- **Aucun secret dans le JSON.** Les identifiants se créent dans n8n (menu Credentials) et le nœud les référence par leur nom. Laisse le champ vide ou un repère, la personne choisit son identifiant à l'import.
- **Gestion d'erreur.** Ajoute un workflow d'erreur (déclencheur d'erreur qui te prévient) ou, dans un nœud Code, un bloc qui attrape l'exception. Un workflow planifié qui échoue sans bruit est pire qu'un workflow qui n'existe pas.
- **Notes sur chaque nœud** : une phrase qui dit ce qu'il fait, pour la personne qui reprendra le workflow.
- **Un nom de nœud parlant** (« Est un client actif ? »), pas « IF 2 ».
- **Tester avant le réel.** Pointe d'abord l'écriture vers une adresse de test (un récepteur de webhook jetable), regarde ce qui sort, puis branche la vraie destination.
- **Valeurs exactes avec le client.** Les noms de champs personnalisés, d'espaces de noms ou de statuts se confirment avant de construire : certaines applications sont strictes sur la casse et l'orthographe.
- **Pas de boucle infinie** quand deux workflows se synchronisent dans les deux sens : marque ce que l'autre vient d'écrire (un champ « dernière origine ») et ignore-le au retour.
- **Un horaire se lit avec un fuseau.** Règle le fuseau du workflow, sinon « tous les jours à 8 h » part à l'heure du serveur.

## Pièges courants

- Un JSON qui s'importe mais dont un nœud reste en erreur : le `typeVersion` ne correspond pas à l'instance. Recopie-le depuis un nœud exporté.
- Un filtre qui laisse tout passer parce que la comparaison est faite sur du texte alors que la valeur est un booléen. Compare le type réel, ou convertis avant.
- Un déclencheur webhook testé sur l'adresse de test et oublié : l'adresse de production est différente. Vérifie laquelle l'application source appelle.
- Une clé d'API collée dans un nœud HTTP Request « pour aller vite » : elle part avec le JSON partagé. Passe par un identifiant n8n.

## Ce que tu rends

Toujours cette présentation, suivie du JSON complet :

```
# Workflow généré : [NOM]

Déclencheur : [description]
Nœuds : [liste]
Enchaînement : [A → B → C]

Pour l'importer dans n8n :
1. Ouvrir n8n, menu, Import from file (ou coller le JSON)
2. Choisir ou créer les identifiants de chaque nœud
3. Lancer un test à la main avec une donnée d'essai
4. Activer le workflow

Ce qui reste à confirmer : [champs, valeurs ou accès non vérifiés]
```

Termine en listant ce qui n'a pas été testé sur ton instance. Un workflow livré sans test est annoncé comme « à tester ».

## Après la construction

Passe à `creer-un-agent-ia:tester-solution` pour le jeu d'essai, puis à `creer-un-agent-ia:piloter-mise-en-service` pour la mise en service.
