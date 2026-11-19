# Agent sur WhatsApp : ce qu'il faut savoir avant d'en bâtir un

À lire aux étapes 3 à 5 de `/creer-un-agent-ia:creer-un-agent-ia`.

Un agent WhatsApp est un agent **déclenché par un événement, en cloud** : chaque message reçu réveille un serveur.
Un agent local ne convient pas, un message arrivé pendant que le poste dort serait perdu. Le type et ses briques :
`types-d-agents.md`.

## Ce que dit la politique de WhatsApp Business

Source : https://whatsappbusiness.com/fr/policy/ (page ouverte le 06/11/2026, mise à jour par l'éditeur le 23/09/2026).
Elle change : la relire à chaque projet. Pages pour les développeurs : https://developers.facebook.com/docs/whatsapp/pricing/
et https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in.

| Règle | Ce que ça impose |
|---|---|
| Accord préalable (opt-in) | écrire seulement à une personne qui a accepté explicitement de recevoir des messages de l'entreprise |
| Ouvrir une conversation | seulement avec un modèle de message approuvé par WhatsApp |
| Fenêtre de 24 heures | on répond librement tant que la personne a écrit il y a moins de 24 heures ; la fenêtre se renouvelle à chaque message de la personne |
| Voie vers un humain | une conversation automatisée doit offrir un moyen d'atteindre une personne |
| Produits interdits à la vente | l'alcool, le tabac, les médicaments sur ordonnance et les armes sont interdits ; des exceptions existent pour une liste limitée de pays, avec un âge minimum de 18 ans, et la France métropolitaine n'était pas dans cette liste le 06/11/2026 |

Une relance ou une newsletter écrit en premier : elle exige l'accord préalable **et** un modèle approuvé. Un agent qui
n'envoie que du texte libre ne sait pas le faire.

**Les assistants d'IA généralistes.** Les conditions de Meta écartent de l'API WhatsApp Business les chatbots d'IA
généralistes depuis le 15 janvier 2026, et la Commission européenne a ouvert une procédure sur ce point (communiqué :
https://ec.europa.eu/commission/presscorner/detail/en/ip_26_1276). Le texte exact des conditions n'a pas été relu ici :
à vérifier avant toute mission, surtout si l'agent répond à des questions sans lien avec l'activité de l'entreprise.

## Dire que c'est une IA

Le premier message le dit (voir `types-d-agents.md`, section « Dire que c'est une IA »). Sur WhatsApp, un numéro
d'entreprise ne rend pas la chose évidente : compter sur l'exception serait une erreur.

## Ce qu'un agent WhatsApp doit tenir

- **File d'attente durable** : le message s'écrit en base avant de répondre à Meta, et le traitement se reprend
  après un arrêt. Répondre d'abord et traiter ensuite perd le message si le serveur tombe entre les deux.
- **Effacement complet** : conversations, fichiers et demandes, tout ce que la page légale promet d'effacer. Un
  test vérifie que plus rien ne reste.
- **Transparence sur les tiers** : les conversations partent chez le fournisseur du modèle. Ne jamais écrire
  qu'aucun tiers ne les voit.
- **Aucune demande de données sensibles** : pas de numéro de carte, de compte ou de pièce d'identité complets dans la
  conversation. Les données de santé relèvent d'un cadre légal strict (RGPD pour les personnes dans l'Union) : ne pas les
  traiter sans l'avoir cadré.
- **Un mode qui agit pour de vrai ne s'active pas par omission** : l'envoi réel demande un choix écrit, l'essai se
  fait sur un numéro de test.
- **Ce qu'il sait faire, et rien de plus** : un rendez-vous suppose de lire un agenda, une qualification un score
  et un CRM. Sinon, on parle d'une demande enregistrée.
