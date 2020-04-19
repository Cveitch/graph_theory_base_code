# UndirectedGraff.py
# Conan Veitch, 4/18/2020
#
# Description: Creates an empty Graff object, utility to create adjacency matrix, edge list and
# adjacency list representations.

import networkx as nx
import numpy as np


class UndirectedGraff:
    def __init__(self):
        self.G = nx.Graph()

    def build_from_edge_list(self, elist):
        # elist is an edge list (list of comma delimited edge tuples)
         self.G = nx.read_edgelist(elist, delimiter=',')

    def build_from_adj_matrix(self, adjmat):
        # adjmat is an adjacency matrix (numpy array)
        rows, cols = np.where(adjmat == 1)
        edges = zip(rows, cols)
        self.G.add_edges_from(edges)

    def build_from_adj_list(self, adjlist):
        # adjlist is an adjacency list (list of comma delimited adjlist tuples)
        self.G = nx.parse_adjlist(adjlist)




