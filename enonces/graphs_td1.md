# Fouille de graphes

Dans ce TD, vous allez utiliser le _package_ `NetworkX` qui propose un ensemble de routines pour la manipulation de 
graphes en Python. Lorsque vous aurez besoin d'aide concernant ce paquet, vous pourrez vous référer à sa 
[documentation en ligne](http://networkx.readthedocs.io/en/latest/reference/index.html).

Pour importer ce package, vous utiliserez la commande :
```python
import networkx as nx
```

Ainsi, les fonctions et objets de ce package seront ensuite accessibles avec la syntaxe :

```python
import networkx as nx

nx.nom_de_la_fonction(...)
```

Comme indiqué [à cette page](http://networkx.readthedocs.io/en/latest/reference/classes/index.html), `NetworkX` définit
plusieurs types de graphes. 
Nous nous intéresserons principalement dans cette série de TD aux types `Graph` et `DiGraph`.

## Graphes non orientés

1. Stockez dans une variable le graphe non orienté contenu dans le fichier `data/graph1.txt` (le format de ce fichier 
est appelé [_Edge List_](http://networkx.readthedocs.io/en/latest/reference/readwrite/edgelist.html) dans la 
nomenclature `NetworkX`). 
Affichez la liste de ses noeuds et la liste de ses liens.

2. Affichez, pour chacun des noeuds de ce graphe, son degré et la liste de ses voisins dans le graphe.

3. Affichez, pour chaque paire de noeuds du graphe, un chemin menant d'un noeud à l'autre dans le graphe, s'il en 
existe.

## Graphes orientés

4. Répétez les actions de la section précédente (manipulations 1 à 3) pour le graphe orienté stocké dans le fichier 
`data/graphM2.txt`, représentant un réseau social imaginaire vous impliquant, vous et vos camarades.
Que signifient les termes "degré" et "voisin" dans le cas d'un graphe orienté ? Comment obtenir les degrés entrant 
et sortant d'un noeud ?

5. Implémentez une fonction `pagerank` qui calcule, pour un graphe et une valeur de $\alpha$ donnés, l'indice en 
question. Quels sont les noeuds les plus influents du graphe créé à la manipulation précédente ?

_NB :_ en pratique, `NetworkX` offre 
[une implémentation de cet algorithme](http://networkx.readthedocs.io/en/latest/reference/algorithms/link_analysis.html) 
qui sera probablement plus efficace que la vôtre et qu'il vous est donc conseillé d'utiliser en priorité.

6. Repérez les autres fonctions d'analyse des liens proposées par `NetworkX` et affichez les noeuds du graphe par 
ordre décroissant d'importance selon chacun de ces critères.

## Visualisation de graphes

`NetworkX` permet également de visualiser les graphes manipulés. 
Pour cela, `NetworkX` s'aide du _package_ `matplotlib` qui est le _package_ de référence pour tout ce qui concerne les
tracés en Python.

### `matplotlib` en 5 minutes

Pour utiliser le _package_ `matplotlib`, commencez par ajouter la ligne suivante à la liste de vos imports en début de 
fichier :

```python
import matplotlib.pyplot as plt
```

Ensuite, la création d'un graphique se fait toujours en trois étapes :

1. création d'une nouvelle figure / d'un emplacement où dessiner le graphique ;
2. ajout des éléments nécessaires au graphique ;
3. affichage du graphique à l'écran ou enregistrement du graphique sous forme de fichier.

Voici un exemple de ces trois étapes (dans cet exemple, chaque étape prend une ligne) :

```python
import matplotlib.pyplot as plt
import numpy

x = [0., 0.1, 0.2, 0.3, 0.4, 0.5]  # abscisse des points à tracer

plt.figure()  # création d'une nouvelle figure
plt.plot(x, numpy.sin(x))  # ajout d'une courbe sinus
plt.show()  # affichage à l'écran du graphique obtenu
```


### Retour à `NetworkX`

Dans le schéma précédent, si l'on souhaite représenter un graphe, on peut remplacer commande `plt.plot(...)` par
[une commande de tracé de graphe](http://networkx.readthedocs.io/en/stable/reference/drawing.html)  spécifique à 
`NetworkX`.

7. Tracez, tour à tour, les deux graphes manipulés dans ce TD. 
Pour le graphe orienté vu dans la deuxième partie du TD, vous ferez en sorte que la taille des noeuds du graphe soit
proportionnelle à leur importance dans le graphe telle qu'évaluée par la fonction `pagerank`.


