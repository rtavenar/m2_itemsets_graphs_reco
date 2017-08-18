import networkx as nx
import math

__author__ = 'Romain Tavenard romain.tavenard[at]univ-rennes2.fr'


def top_k_adamic_adar(triplets, k):
    return sorted(triplets, key=lambda t: t[2], reverse=True)[:k]


def user_based_collaborative_filtering(g, scores, target, n_neighbors=5, similarity_fun=None):
    if similarity_fun is None:
        similarity_fun = nx.adamic_adar_index
    target_user, target_item = target
    list_neighbors = [n for n in g.nodes_iter() if (n, target_item) in scores.keys()]
    triplets = similarity_fun(g, [(n, target_user) for n in list_neighbors])
    target_score = 0.
    sum_weights = 0.
    for n, _, score in top_k_adamic_adar(triplets=triplets, k=n_neighbors):
        user_grades = [v for k, v in scores.items() if k[0] == n]
        target_score += (scores[n, target_item] - sum(user_grades) / len(user_grades)) * score
        sum_weights += score
    if sum_weights == 0.:
        return None
    target_score /= sum_weights
    target_user_scores = [v for k, v in scores.items() if k[0] == target_user]
    if len(target_user_scores) == 0:
        target_score += sum(scores.values()) / len(scores)
    else:
        target_score += sum(target_user_scores) / len(target_user_scores)
    return target_score


def directed_graph_common_neighbors(g, u, v):
    list_common_neighbors = []
    for w in g.nodes_iter():
        if (g.has_edge(u, w) and g.has_edge(w, v)) or (g.has_edge(v, w) and g.has_edge(w, u)):
            list_common_neighbors.append(w)
    return list_common_neighbors


def directed_graph_adamic_adar(g, ebunch=None):
    if ebunch is None:
        ebunch = nx.non_edges(g)

    def predict(u, v):
        return sum([1. / math.log(g.degree(w)) for w in directed_graph_common_neighbors(g, u, v)])

    return [(u, v, predict(u, v)) for u, v in ebunch]


# Manipulations 6-7
g = nx.read_edgelist("data/graph1.txt")
g_directed = nx.read_edgelist("data/graphM1.txt", create_using=nx.DiGraph())

print("graph1.txt")
triplets = list(nx.adamic_adar_index(g))
for source, dest, sim in top_k_adamic_adar(triplets=triplets, k=2):
    print("(%r, %r) -> %.8f" % (source, dest, sim))

print("graphM1.txt")
for source, dest, sim in directed_graph_adamic_adar(g_directed):
    print("(%r, %r) -> %.8f" % (source, dest, sim))

# Manipulation 8
grades = {("A", "iPad"): 10,
          ("A", "iPhone"): 10,
          ("A", "S4"): 0,
          ("A", "Bidule"): 0,

          ("B", "iPad"): 5,
          ("B", "iPhone"): 5,
          ("B", "GalaxyTab"): 5,
          ("B", "S4"): 5,

          ("C", "iPad"): 10,
          ("C", "iPhone"): 10,
          ("C", "GalaxyTab"): 0,
          ("C", "S4"): 0,

          ("D", "iPad"): 0,
          ("D", "iPhone"): 0,
          ("D", "GalaxyTab"): 10,
          ("D", "S4"): 10}
print("Note pour (A, GalaxyTab):", user_based_collaborative_filtering(g, grades, target=("A", "GalaxyTab")))

g.add_edge("A", "C")
print("Note pour (A, GalaxyTab):", user_based_collaborative_filtering(g, grades, target=("A", "GalaxyTab")))

# Manipulation 9
grades = {("GAUTIER_RONAN", "R"): 12,
          ("GAUTIER_RONAN", "NN"): 16,
          ("HEBERT_FLORIAN", "SQL"): 15,
          ("HEBERT_FLORIAN", "R"): 9,
          }
print("Note pour (GAUTIER_RONAN, SQL):", user_based_collaborative_filtering(g_directed,
                                                                            grades,
                                                                            target=("GAUTIER_RONAN", "SQL"),
                                                                            similarity_fun=directed_graph_adamic_adar))
