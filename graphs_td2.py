# -*- coding: utf-8 -*-

import networkx as nx
import math

__author__ = 'Romain Tavenard romain.tavenard[at]univ-rennes2.fr'


def top_k_triplets(triplets, k):
    return sorted(triplets, key=lambda t: t[2], reverse=True)[:k]


def user_based_collaborative_filtering(g, scores, target, n_neighbors=5, similarity_fun=None):
    if similarity_fun is None:
        similarity_fun = nx.adamic_adar_index
    target_user, target_item = target
    list_neighbors = [n for n in g.nodes_iter() if (n, target_item) in scores.keys()]
    triplets = similarity_fun(g, [(n, target_user) for n in list_neighbors])
    target_score = 0.
    sum_weights = 0.
    for n, _, score in top_k_triplets(triplets=triplets, k=n_neighbors):
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


def generic_common_neighbors(g, u, v):
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

# Manipulation 3
grades = {("A", "iPad"): 10,
          ("A", "iPhone"): 10,
          ("A", "S4"): 0,

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

# Manipulation 4
g.add_edge("A", "C")
print("Note pour (A, GalaxyTab):", user_based_collaborative_filtering(g, grades, target=("A", "GalaxyTab")))

# Manipulation 5
grades = {("AZNAGUE_ABDESSAMAD", "R"): 12,
          ("AZNAGUE_ABDESSAMAD", "NN"): 16,
          ("BAI_HUIQIAN", "SQL"): 15,
          ("BAI_HUIQIAN", "R"): 9,
          }
print("Note pour (AZNAGUE_ABDESSAMAD, SQL):", user_based_collaborative_filtering(g_directed,
                                                                                 grades,
                                                                                 target=("AZNAGUE_ABDESSAMAD", "SQL"),
                                                                                 similarity_fun=generic_adamic_adar))
