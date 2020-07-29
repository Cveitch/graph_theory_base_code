# ComplexityWrapper.py
# Conan Veitch, 2020-05-28
#
# Description: Wrapper for Graph complexity functions.
# Legend:   vdi     -   vertex degree information
#           fisd    -   frequency information shannon diversity
#           odisd   -   orbit distribution information shannon diversity
#           nlc     -   node local complexity
#           cB      -   complexity-B
#           gdc     -   graph-distance complexity
#

import graffal.complexity.ComplexityMeasurer as comeas
import graffal.grafflet_gen.GraffletWrapper as gwrap
import networkx as nx
import textwrap as tw


class ComplexityWrapper:
    node_richness: int

    def __init__(self, graff, walk_length=3, grafflet_nodes=5):
        self.G = graff
        self.walk = walk_length
        self.gwrapper = gwrap.GraphletWrapper(self.G.get_graff(), grafflet_nodes)
        nx.set_node_attributes(self.G.get_graff(), self.gwrapper.orbit_counts, 'orbit_count')
        self.edge_list = self.gwrapper.get_grafflet_edges()
        self.total_grafflets = self.gwrapper.grafflet_count
        self.graphlet_frequency = self.gwrapper.get_grafflet_freq()
        # self.node_orbits = nx.get_node_attributes(self.G.get_graff(), 'orbit count')
        self.node_orbits = self.G.get_nodes('orbit_count')
        self.orp = comeas.node_orbit_relative_proportion(self.node_orbits)
        self.total_walk_count = comeas.total_walk_count(self.G.get_adj_matrix(), walk_length)
        self.vdi_measure = comeas.vertex_degree_info_measure(self.G.get_graff())
        self.fisd_measure = comeas.frequency_info_sdm(self.gwrapper.get_grafflet_freq())
        self.odisd_measure = comeas.orbit_distribution_info_sdm(self.G.get_nodes('orbit_count'))
        self.node_richness = comeas.node_richness_measure(self.node_orbits)
        # nx.set_node_attributes(self.G.get_graff(), self.gwrapper.orbit_counts, 'node_complexity')
        lcm = comeas.local_complexity_measure(self.G.get_nodes('orbit_count'))
        self.G.set_nodes(lcm, 'node_complexity')
        self.nlc_measure = self.G.get_nodes('node_complexity')
        self.cB_measure = comeas.complexity_b(self.G.get_graff())
        self.gdc_measure = comeas.graph_distance_complexity(self.G.get_graff())
        self.node_complexity = self.G.set_nodes(self.nlc_measure, 'node_complexity')
        self.proportional_richness = comeas.total_richness_proportion(self.G.get_nodes('orbit_count'))
        self.node_average_richness = comeas.node_average_richness(self.node_orbits, self.G.get_graff(), self.get_node_richness(),1)
        #nx.set_node_attributes(self.G.get_graff),

    def get_total_walk_count(self):
        return self.total_walk_count

    def get_grafflet_edge_list(self):
        return self.edge_list

    def get_total_graphlets(self):
        return self.total_grafflets

    def get_graphlet_frequency(self):
        return self.graphlet_frequency

    def get_node_orbits(self):
        return self.node_orbits

    def get_vdi_measure(self):
        return self.vdi_measure

    def get_fisd_measure(self):
        return self.fisd_measure

    def get_odisd_measure(self):
        return self.odisd_measure

    def get_nlc_measure(self):
        return self.nlc_measure

    def get_cB_measure(self):
        return self.cB_measure

    def get_gdc_measure(self):
        return self.gdc_measure

    def get_node_richness(self):
        return self.node_richness

    def get_node_orp(self):
        return self.orp

    def get_global_richness_proportion(self):
        return self.proportional_richness

    def get_node_average_richness(self):
        return self.node_average_richness

    def print_edgelist(self):
        print("Graphlets edge list:")
        print(*self.edge_list, sep="\n")

    def print_total_graphlets(self):
        rang = len(self.total_grafflets)
        for i in range(2, rang + 2):
            print("There are:", self.total_grafflets[i], "total", i, "node graphlets.")

    def print_graphlet_frequency(self):
        for node, freq in self.graphlet_frequency.items():
            if freq > 0:
                print("Graphlet", node, "has frequency:", freq)

    def print_node_orbits(self):
        for node in self.G.get_graff():
            # print(self.node_orbits)
            print("Node", node, "has orbits:", self.node_orbits[node])

    def print_vdi_measure(self):
        print("Vertex Degree Information measure is: ", self.vdi_measure)

    def print_fisd_measure(self):
        print("Frequency Information measure is: ", self.fisd_measure)

    def print_odisd_measure(self):
        print("Orbit Distribution Information measure is ", self.odisd_measure)

    def print_nlc_measure(self):
        for node in self.G.get_nodes('node_complexity'):
            print("Local Complexity Measure of node", node, "is:", self.nlc_measure[node])

    def print_cB_measure(self):
        print("Complexity B is:", self.cB_measure)

    def print_gdc_measure(self):
        print("Graph Distance Complexity is:", self.gdc_measure)

    def print_total_walk_count(self):
        print("The Total Walk Count of length ", self.walk, "or less is:", self.total_walk_count)

    def print_complexity_suite(self):
        # self.print_edgelist()
        self.print_total_graphlets()
        self.print_graphlet_frequency()
        self.print_total_walk_count()
        self.print_node_orbits()
        self.print_vdi_measure()
        self.print_cB_measure()
        self.print_gdc_measure()
        self.print_fisd_measure()
        self.print_odisd_measure()
        self.print_nlc_measure()

    def write_complexity_suite_file(self, file_name="temp"):
        fname = "../graffal_tests/saved/"+file_name+"_complexity_suite.txt"
        f = open(fname, "w+")

        f.write("The edge list for {} is:\n".format(file_name))
        edgelist = list(self.G.get_edges())
        count = 0
        for n in range(0, len(edgelist)):
            if count == 0:
                f.write("\n")
            f.write(('({}, {}), '.format(edgelist[n][0], edgelist[n][1])))
            count = (count +1) % 5
        f.write("\n\n\n")

        f.write("Total i-node graphlets:")
        f.write("\n\n")
        rang = len(self.total_grafflets)
        for i in range(2, rang + 2):
            f.write("There are: {} total {}-node graphlets.\n".format(self.total_grafflets[i], i))
        f.write("\n\n")

        f.write("Graphlet Frequency:\n")
        f.write("\n")
        for node, freq in self.graphlet_frequency.items():
            if freq > 0:
                f.write("Graphlet {} has frequency {}.\n".format(node, freq))
        f.write("\n\n")

        f.write("Node Orbits:\n")
        for node in self.G.get_graff():
            count = 0
            f.write("\nNode {} takes part in {} orbits: ".format(node, len(self.node_orbits[node])))
            for i in self.node_orbits[node]:
                if count == 0:
                    f.write("\n")
                f.write("{} ".format(i))
                count = (count + 1) % 20
        f.write("\n\n\n")

        f.write("Node Richness:\n\n")
        for node in self.get_node_richness():
            f.write("The richness of node {} is {}.\n".format(node, self.get_node_richness()[node]))
        f.write("\n\n")

        f.write("Node Richness:\n\n")
        for node in self.get_node_average_richness():
            f.write("The average richness of node {} with its first order neighbours is {}.\n".format(node,
                                                                                        self.get_node_average_richness()[node]))
        f.write("\n\n")

        f.write("Node Diversity:\n\n")
        for node in self.get_nlc_measure():
            f.write("The diversity of node {} is {}.\n".format(node, self.get_nlc_measure()[node]))
        f.write("\n\n")

        f.write("Global Richness Proportion:\n\n")
        for x in self.get_global_richness_proportion():
            f.write("The number of nodes with a richness of {} is {}.\n".format(x, self.get_global_richness_proportion()[x]))
        f.write("\n\n")

        f.write("The Orbit Distribution Information measure of {} is {}.".format(file_name, self.get_odisd_measure()))
        f.write("\n\n\n")

        f.write("The Vertex Degree Information measure of {} is {}.".format(file_name, self.get_vdi_measure()))
        f.write("\n\n\n")

        f.write("The Frequency Degree Information measure of {} is {}.".format(file_name, self.get_fisd_measure()))
        f.write("\n\n\n")

        f.write("The Complexity B of {} is {}".format(file_name, self.get_cB_measure()))
        f.write("\n\n\n")

        f.write("The Graph-Distance Complexity of {} is {}.".format(file_name, self.get_gdc_measure()))
        f.write("\n\n\n")

        f.write("The Total Walk Count of length {} or less is {}.".format(self.walk, self.get_total_walk_count()))
        f.write("\n\n\n")
