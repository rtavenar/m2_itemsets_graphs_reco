import networkx as nx
import matplotlib.pyplot as plt

__author__ = 'Romain Tavenard romain.tavenard[at]univ-rennes2.fr'


# Manip 1
g = nx.read_edgelist("data/graph1.txt")

# Manip 2
for n in g.nodes_iter():
    print("Node %r, degree: %d, neighbors: %r" % (n, g.degree(n), g.neighbors(n)))

# Manip 3
list_nodes = g.nodes()
for i in range(len(list_nodes)):
    for j in range(i + 1, len(list_nodes)):
        try:
            print(list_nodes[i], list_nodes[j], nx.dijkstra_path(g, list_nodes[i], list_nodes[j]))
        except nx.NetworkXNoPath:
            continue


plt.figure()
plt.subplot(2, 1, 1)
nx.draw(g, with_labels=True)
plt.title("graph1.txt")

# Manip 4
g = nx.read_edgelist("data/graphM1.txt", create_using=nx.DiGraph())
for n in g.nodes_iter():
    print("Node %r, degree: %d, neighbors: %r" % (n, g.degree(n), g.neighbors(n)))  # leur demander le sens de `degree` et `neighbors` pour un graphe orienté
list_nodes = g.nodes()
for i in range(len(list_nodes)):
    for j in range(i + 1, len(list_nodes)):
        try:
            print(list_nodes[i], list_nodes[j], nx.dijkstra_path(g, list_nodes[i], list_nodes[j]))
        except nx.NetworkXNoPath:
            continue

h, a = nx.hits(g)
print("Hubs")
for k, v in sorted(h.items(), key=lambda t: t[1], reverse=True):
    print(k, v)

print("Authorities")
for k, v in sorted(a.items(), key=lambda t: t[1], reverse=True):
    print(k, v)

pr = nx.pagerank(g, alpha=0.9)  # leur faire recoder PageRank ne serait pas une mauvaise idée
print("PageRank")
for k, v in sorted(pr.items(), key=lambda t: t[1], reverse=True):
    print(k, v)


plt.subplot(2, 1, 2)
nx.draw(g, with_labels=True)
plt.title("graphM1.txt")
plt.show()
