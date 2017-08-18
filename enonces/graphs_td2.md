# Fouille de graphes (suite)

Dans ce TD, nous allons travailler sur les mêmes graphes que lors du TD précedent. Commencez-donc par les re-charger en 
mémoire.

## Prédiction de liens

La section [_Link Prediction_](http://networkx.readthedocs.io/en/latest/reference/algorithms/link_prediction.html) de
la documentation de `NetworkX` pourrait vous être utile ici.

1. Évaluez la similarité, au sens de l'indice Adamic/Adar, entre toutes les paires de noeuds du graphe non orienté
manipulé au TD précédent. Comme indiqué dans la documentation, la fonction que vous avez utilisée n'est disponible que 
pour les graphes non orientés. Proposez une implémentation du calcul de cet indice qui soit 

2. Pour chacun des deux graphes, quels sont les trois liens manquants les plus "prévisibles" ?

## Recommandation

3. Étant données les notes fournies dans le tableau suivant, inférez la note que pourrait souhaiter attribuer 
l'utilisateur `A` du graphe non orienté déja considéré précédemment à l'objet `GalaxyTab`. Vous utiliserez pour cela la 
méthode dite _User-based Collaborative Filtering_ (que vous devrez implémenter).

| Utilisateur | Objet      | Score |
| ----------- | ---------- | ----- |
| A           | iPad       | 10    |
| A           | iPhone     | 10    |
| A           | S7         | 0     |
|             |            |       |
| B           | iPad       | 5     |
| B           | iPhone     | 5     |
| B           | S7         | 5     |
| B           | Galaxy Tab | 5     |
|             |            |       |
| C           | iPad       | 10    |
| C           | iPhone     | 10    |
| C           | S7         | 0     |
| C           | Galaxy Tab | 0     |
|             |            |       |
| D           | iPad       | 0     |
| D           | iPhone     | 0     |
| D           | S7         | 10    |
| D           | Galaxy Tab | 10    |

4. Répétez l'opération après avoir ajouté une arête entre les sommets `A` et `C` dans le graphe.

5. Proposez un ensemble de paires sommet/note pour le graphe orienté et inférez une note non fournie.