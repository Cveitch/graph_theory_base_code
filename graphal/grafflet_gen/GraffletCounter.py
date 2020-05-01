# GraffletCounter.py
# Conan Veitch, 2020-04-27
#
# Description: Counts graphlet automorphism orbits of 3, 4, 5 node grafflet_gen.
# Note that the g# values in the gen_graphlet functions match grafflet_gen.png in the documentation.
#

from tqdm import tqdm
import graphal.grafflet_gen.GraffletCollection as graffcol
import networkx as nx
import itertools

class GraffletCounter:
    def __init__(self, graff_name, nodes):
        self.my_graff = graff_name
        self.grafflet_count, self.grafflet_edges = self.count_n_graphlets(nodes)

    def update_graff(self, new_graff):
        self.my_graff = new_graff

    def count_n_graphlets(self, n):
        # Enumerate n-grafflet_gen from graph my_graff.
        grafflets = graffcol.GraffletCollection(n).g_list
        graphlet_count = 0
        graff_edges = []
        for x in tqdm(range(len(grafflets)), desc="Counting Graphlets"):
            for s_nodes in itertools.combinations(self.my_graff.nodes(), len(grafflets[x].G.nodes())):
                s_g = self.my_graff.subgraph(s_nodes)
                if nx.is_connected(s_g) and nx.is_isomorphic(s_g, grafflets[x].G):
                    graff_edges.append(s_g.nodes)
                    graphlet_count += 1
        return graphlet_count, graff_edges
