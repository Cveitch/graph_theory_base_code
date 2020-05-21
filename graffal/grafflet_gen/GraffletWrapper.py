# GraffletWrapper.py
# Conan Veitch, 2020-05-07
#
# Description: Wrapper for grafflet-gen utilities
#               Provides dictionaries for grafflet frequency, grafflet counts, orbit counts
#               And an edge list of every graphlet found in the original graph
#

import graffal.grafflet_gen.GraffletCounter as gcounter
import networkx as nx

class GraphletWrapper:
    def __init__(self, graff, option=1):
        # Option 1 is going to default to 2-5 node graphlets, option 2 is 2-4.
        gcount2node = gcounter.GraffletCounter(graff, 2)
        gcount3node = gcounter.GraffletCounter(graff, 3)
        gcount4node = gcounter.GraffletCounter(graff, 4)

        if option < 1 or option >2:
            exit("Invalid Graphlet Wrapper Parameter")
        elif option == 1:
            gcount5node = gcounter.GraffletCounter(graff, 5)
            self.grafflet_freq = {**gcount2node.grafflet_freq, **gcount3node.grafflet_freq,
                                  **gcount4node.grafflet_freq, **gcount5node.grafflet_freq}
            self.grafflet_count = {2: gcount2node.grafflet_count, 3: gcount3node.grafflet_count,
                                   4: gcount4node.grafflet_count, 5: gcount5node.grafflet_count}
            self.grafflet_edges = gcount2node.grafflet_edges + gcount3node.grafflet_edges \
                                  + gcount4node.grafflet_edges + gcount5node.grafflet_edges
            self.orbit_counts = {}
            for node in graff.nodes:
                self.orbit_counts[node] = gcount2node.orbit_counts[node] + gcount3node.orbit_counts[node]\
                                          + gcount4node.orbit_counts[node] + gcount5node.orbit_counts[node]
        elif option == 2:
            self.grafflet_freq = {**gcount2node.grafflet_freq, **gcount3node.grafflet_freq,
                                  **gcount4node.grafflet_freq}
            self.grafflet_count = {2: gcount2node.grafflet_count, 3: gcount3node.grafflet_count,
                                   4: gcount4node.grafflet_count}
            self.grafflet_edges = gcount2node.grafflet_edges + gcount3node.grafflet_edges \
                                  + gcount4node.grafflet_edges
            self.orbit_counts = {}
            for node in graff.nodes:
                self.orbit_counts[node] = gcount2node.orbit_counts[node] + gcount3node.orbit_counts[node] \
                                          + gcount4node.orbit_counts[node]
            nx.set_node_attributes(graff, self.orbit_counts, 'orbit_count')

    def get_grafflet_count(self):
        return self.grafflet_count

    def get_grafflet_edges(self):
        return self.grafflet_edges

    def get_grafflet_freq(self):
        return self.grafflet_freq
