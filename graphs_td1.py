import networkx as nx
import matplotlib.pyplot as plt

__author__ = 'Romain Tavenard romain.tavenard[at]univ-rennes2.fr'


def sorted_dict(d):
    return sorted(d.items(), key=lambda t: t[1], reverse=True)


# Manip 1
g = nx.read_edgelist("data/graph1.txt")
print("Sommets du graphe g:", g.nodes())
print("Arêtes du graphe g:", g.edges())

# Manip 2
for n in g.nodes():
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
print("Sommets du graphe orienté g:", g.nodes())
print("Arêtes du graphe orienté g:", g.edges())
for n in g.nodes_iter():
    # leur demander le sens de `degree` et `neighbors` pour un graphe orienté
    print("Node %r, degree: %d, neighbors: %r" % (n, g.degree(n), g.neighbors(n)))
list_nodes = g.nodes()
for i in range(len(list_nodes)):
    for j in range(i + 1, len(list_nodes)):
        try:
            print(list_nodes[i], list_nodes[j], nx.dijkstra_path(g, list_nodes[i], list_nodes[j]))
        except nx.NetworkXNoPath:
            continue

h, a = nx.hits(g)
print("Hubs")
for k, v in sorted_dict(h):
    print(k, v)

print("Authorities")
for k, v in sorted_dict(a):
    print(k, v)

pr = nx.pagerank(g, alpha=0.9)  # leur faire recoder PageRank ne serait pas une mauvaise idée
print("PageRank")
for k, v in sorted_dict(pr):
    print(k, v)


plt.subplot(2, 1, 2)
nx.draw(g, with_labels=True, nodelist=pr.keys(), node_size=[v * 10 * 1000 for v in pr.values()])
plt.title("graphM1.txt")
plt.show()
