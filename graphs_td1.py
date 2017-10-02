# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt
import math

__author__ = 'Romain Tavenard romain.tavenard[at]univ-rennes2.fr'


def sorted_dict(d):
    return sorted(d.items(), key=lambda t: t[1], reverse=True)


def top_k_triplets(triplets, k):
    return sorted(triplets, key=lambda t: t[2], reverse=True)[:k]


def pagerank(g, alpha=0.9, max_iter=100):
    # TODO: comment this out for online version
    n_nodes = g.number_of_nodes()
    pagerank_dict = {node: 1. / n_nodes for node in g.nodes()}
    for iter in range(max_iter):
        pagerank_dict_new = {node: (1. - alpha) / n_nodes for node in g.nodes()}
        for node_j in g.nodes():
            for node_i in g.predecessors(node_j):
                pagerank_dict_new[node_j] += alpha * (pagerank_dict[node_i] / g.out_degree(node_i))
        pagerank_dict = pagerank_dict_new.copy()
    return pagerank_dict


def generic_common_neighbors(g, u, v):
    # TODO: comment this out for online version
    list_common_neighbors = []
    for w in g.nodes_iter():
        if (g.has_edge(u, w) and g.has_edge(w, v)) or (g.has_edge(v, w) and g.has_edge(w, u)):
            list_common_neighbors.append(w)
    return list_common_neighbors


def generic_adamic_adar(g, ebunch=None):
    if ebunch is None:
        ebunch = nx.non_edges(g)

    def predict(u, v):
        return sum([1. / math.log(g.degree(w)) for w in generic_common_neighbors(g, u, v)])

    return [(u, v, predict(u, v)) for u, v in ebunch]


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
        if nx.has_path(g, list_nodes[i], list_nodes[j]):
            print(list_nodes[i], list_nodes[j], nx.dijkstra_path(g, list_nodes[i], list_nodes[j]))


plt.figure()
nx.draw(g, with_labels=True)
plt.title("graph1.txt")
plt.show()

# Manip 4
g_directed = nx.read_edgelist("data/graphM2.txt", create_using=nx.DiGraph())
print("Noeuds du graphe orienté g_directed:", g_directed.nodes())
print("Liens du graphe orienté g_directed:", g_directed.edges())
for n in g_directed.nodes_iter():
    print("Noeud %r, degré: %d, voisins: %r, degré entrant: %d, degré sortant: %d" % (n,
                                                                                      g_directed.degree(n),
                                                                                      g_directed.neighbors(n),
                                                                                      g_directed.in_degree(n),
                                                                                      g_directed.out_degree(n)))
list_nodes = g_directed.nodes()
for i in range(len(list_nodes)):
    for j in range(i + 1, len(list_nodes)):
        if nx.has_path(g_directed, list_nodes[i], list_nodes[j]):
            print(list_nodes[i], list_nodes[j], nx.dijkstra_path(g_directed, list_nodes[i], list_nodes[j]))

h, a = nx.hits(g_directed)
print("Hubs")
for k, v in sorted_dict(h):
    print(k, v)

print("Autorités")
for k, v in sorted_dict(a):
    print(k, v)

pr = nx.pagerank(g_directed, alpha=0.9)
print("PageRank")
for k, v in sorted_dict(pr):
    print(k, v)

my_pr = pagerank(g_directed, alpha=0.9, max_iter=500)
print("Mon PageRank")
for k, v in sorted_dict(pr):
    print(k, v, my_pr[k])


plt.figure()
nx.draw(g_directed, with_labels=True, nodelist=pr.keys(), node_size=[v * 10 * 1000 for v in pr.values()])
plt.title("graphM1.txt")
plt.show()


# Manipulations 8-9
print("graph1.txt")
triplets = list(nx.adamic_adar_index(g))
for source, dest, sim in top_k_triplets(triplets=triplets, k=3):
    print("(%r, %r) -> %.8f" % (source, dest, sim))

print("graph1.txt avec la fonction générique")
triplets = generic_adamic_adar(g)
for source, dest, sim in top_k_triplets(triplets=triplets, k=3):
    print("(%r, %r) -> %.8f" % (source, dest, sim))

print("graphM2.txt")
triplets = generic_adamic_adar(g_directed)
for source, dest, sim in top_k_triplets(triplets=triplets, k=3):
    print("(%r, %r) -> %.8f" % (source, dest, sim))
