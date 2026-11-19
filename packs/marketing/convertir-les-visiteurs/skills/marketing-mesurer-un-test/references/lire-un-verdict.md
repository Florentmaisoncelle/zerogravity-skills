# Lire le verdict d'un test

| Statut | Ce que ça veut dire | Quoi faire |
|---|---|---|
| en_cours | Pas assez de données. Aucune p-valeur affichée volontairement. | Continuer à journaliser jusqu'au minimum prévu. |
| gagnant_propose | Une variante est meilleure de façon significative (après correction) ET d'au moins l'écart utile. | Une personne relit l'intervalle, puis `valider`. Elle change ensuite l'outil réel. |
| base_conservee | Toutes les variantes sont nettement moins bonnes. | Garder la référence, noter ce qu'on a appris. |
| ecart_trop_faible | Différence réelle probable, mais sous l'écart utile. | Ne pas changer pour si peu, sauf si la variante est plus simple ou moins chère. |
| sans_difference | Pas de différence nette, et l'intervalle écarte un gain utile. | Garder la variante la plus simple. Tester autre chose. |
| non_concluant | Pas de différence nette, mais l'intervalle laisse la place à un gain utile. Le test n'a pas pu trancher. | Prolonger (`etendre`) ou arrêter en assumant l'incertitude. Ne jamais lire « égalité ». |

## Points de vigilance

- **L'intervalle compte plus que le p.** Il dit de combien la variante peut battre la référence, dans les deux sens. Il est ajusté au nombre de variantes.
- **Alerte moyenne et médiane de sens opposés** : quelques valeurs extrêmes (un post viral) font le résultat. Regarder les données avant d'adopter.
- **Regarder trop souvent** : scorer à chaque nouvelle donnée fait apparaître des gagnants qui n'existent pas. Un seul scorage, au minimum prévu. Après une prolongation, un nouveau scorage unique.
- **Plusieurs variantes** : chaque variante ajoutée durcit la correction. Avec peu de volume, deux variantes valent mieux que six.
- **Volume** : 30 valeurs par variante (ou 200 essais et 10 succès) est un plancher. Pour détecter un petit écart, il en faut bien davantage. En cas de doute, partir de `marketing-skills:ab-testing` pour estimer la taille nécessaire.
- **Taux très faibles** (moins de 1 %) : les 10 succès par variante sont la vraie contrainte, pas le nombre d'essais.
