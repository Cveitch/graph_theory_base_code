# GraffletCounter.py
# Conan Veitch, 2020-04-27
#
# Description: Counts graphlet automorphism orbits of 3, 4, 5 node grafflet_gen.
# Note that the g# values in the gen_graphlet functions match grafflet_gen.png in the documentation.
#

from tqdm import tqdm
import graffal.grafflet_gen.GraffletCollection as graffcol
import networkx as nx
import itertools


class GraffletCounter:
    def __init__(self, graff_name, nodes):
        self.my_graff = graff_name
        self.grafflet_count, self.grafflet_edges, self.grafflet_freq, self.node_freq = self.count_n_grafflets(nodes)
        self.orbit_counts = self.count_orbits(nodes)

    def update_graff(self, new_graff):
        self.my_graff = new_graff
        self.grafflet_count, self.grafflet_edges, self.grafflet_freq, self.node_freq = self.count_n_grafflets(nodes)
        self.orbit_counts = self.count_orbits(nodes)

    def count_n_grafflets(self, n):
        # How many n-grafflets from graph my_graff.
        grafflets = graffcol.GraffletCollection(n).g_list
        grafflet_frequency = {}
        grafflet_count = 0
        graff_edges = []
        node_frequency = {}
        #node = 0
        for x in tqdm(range(len(grafflets)), desc="Counting "+str(n)+"-node Graphlets"):
            grafflet_frequency[grafflets[x].graphlet_enum] = 0
            for s_nodes in itertools.combinations(self.my_graff.nodes(), len(grafflets[x].G.nodes())):
                s_g = self.my_graff.subgraph(s_nodes)
                if nx.is_connected(s_g) and nx.is_isomorphic(s_g, grafflets[x].G):
                    graff_edges.append(s_g.nodes)
                    grafflet_count += 1
                    grafflet_frequency[grafflets[x].graphlet_enum] += 1
                    for node in self.my_graff.nodes():
                        if node in s_g:
                            if node not in node_frequency:
                                node_frequency[node] = 1
                            elif node in node_frequency:
                                node_frequency[node] += 1
            #node += 1
        return grafflet_count, graff_edges, grafflet_frequency, node_frequency

    def count_orbits(self, n):
        orbs = {}
        grafflets = graffcol.GraffletCollection(n).g_list
        for x in tqdm(range(len(grafflets)), desc="Counting Orbits"):
            for s_nodes in itertools.combinations(self.my_graff.nodes(), len(grafflets[x].G.nodes())):
                s_g = self.my_graff.subgraph(s_nodes)
                if nx.is_connected(s_g) and nx.is_isomorphic(s_g, grafflets[x].G):
                    s_g_d = dict(s_g.degree)
                    grafflets_d = dict(grafflets[x].G.degree)
                    for gnode in s_g_d:
                        node_orb = []
                        if gnode not in orbs:
                            orbs[gnode] = node_orb
                        for gletnode in grafflets_d:
                            if s_g_d[gnode] == grafflets_d[gletnode]:
                                orbs[gnode].append(grafflets[x].get_node_orbit(gletnode))
                                break
        return orbs
