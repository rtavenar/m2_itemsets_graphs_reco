# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt

__author__ = 'Romain Tavenard romain.tavenard[at]univ-rennes2.fr'


def sorted_dict(d):
    return sorted(d.items(), key=lambda t: t[1], reverse=True)


def pagerank(g, alpha=0.9, max_iter=100):
    n_nodes = g.number_of_nodes()
    pagerank_dict = {node: 1. / n_nodes for node in g.nodes()}
    for iter in range(max_iter):
        pagerank_dict_new = {node: (1. - alpha) / n_nodes for node in g.nodes()}
        for node_j in g.nodes():
            for node_i in g.predecessors(node_j):
                pagerank_dict_new[node_j] += alpha * (pagerank_dict[node_i] / g.out_degree(node_i))
        pagerank_dict = pagerank_dict_new.copy()
    return pagerank_dict


# Manip 1
g = nx.read_edgelist("data/graph1.txt")
print("Noeuds du graphe g:", g.nodes())
print("Liens du graphe g:", g.edges())

# Manip 2
for n in g.nodes():
    print("Noeud %r, degré: %d, voisins: %r" % (n, g.degree(n), g.neighbors(n)))

# Manip 3
list_nodes = g.nodes()
for i in range(len(list_nodes)):
    for j in range(i + 1, len(list_nodes)):
        try:
            print(list_nodes[i], list_nodes[j], nx.dijkstra_path(g, list_nodes[i], list_nodes[j]))
        except nx.NetworkXNoPath:
            continue


plt.figure()
nx.draw(g, with_labels=True)
plt.title("graph1.txt")
plt.show()

# Manip 4
g = nx.read_edgelist("data/graphM1.txt", create_using=nx.DiGraph())
print("Noeuds du graphe orienté g:", g.nodes())
print("Liens du graphe orienté g:", g.edges())
for n in g.nodes_iter():
    print("Noeud %r, degré: %d, voisins: %r, degré entrant: %d, degré sortant: %d" % (n,
                                                                                      g.degree(n),
                                                                                      g.neighbors(n),
                                                                                      g.in_degree(n),
                                                                                      g.out_degree(n)))
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

print("Autorités")
for k, v in sorted_dict(a):
    print(k, v)

pr = nx.pagerank(g, alpha=0.9)
print("PageRank")
for k, v in sorted_dict(pr):
    print(k, v)

my_pr = pagerank(g, alpha=0.9, max_iter=500)
print("Mon PageRank")
for k, v in sorted_dict(pr):
    print(k, v, my_pr[k])


plt.figure()
nx.draw(g, with_labels=True, nodelist=pr.keys(), node_size=[v * 10 * 1000 for v in pr.values()])
plt.title("graphM1.txt")
plt.show()
