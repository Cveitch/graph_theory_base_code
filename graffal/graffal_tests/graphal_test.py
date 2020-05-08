# graphal_test.py
# Conan Veitch, 4/18/2020
#
# Description: Test cases for graffal project.
#

import graffal.graff_gen.GraffWrapper as gmake
import graffal.grafflet_gen.GraffletWrapper as gwrap
import graffal.complexity.ComplexityMeasurer as comeas


cgr = "test_edge.csv"
G = gmake.GraffWrapper(cgr)
gwrapper = gwrap.GraphletWrapper(G.get_graff())


def print_edgelist():
    print("Graphlets edge list:")
    print(*gwrapper.get_grafflet_edges(), sep="\n")


def print_total_graphlets():
    for i in range(2, 6):
        print("There are:", gwrapper.grafflet_count[i], "total", i, "node graphlets.")


def print_graphlet_frequency():
    for node, freq in gwrapper.get_grafflet_freq().items():
        print("Graphlet", node, "has frequency:", freq)


def print_node_orbits():
    for node, orb in gwrapper.get_orbit_counts().items():
        print("Node", node, "has orbits:", orb)


def print_shannon_diversity_measure():
    sdm = comeas.shannon_diversity_measure(gwrapper.get_grafflet_freq())
    print("Shannon Diversity Measure is: ", sdm)


def print_local_complexity_measure():
    lcm = comeas.local_complexity_measure(gwrapper.get_orbit_counts())
    for node in lcm:
        print("Local Complexity Measure of node", node, "is:", lcm[node])


#print_edgelist()
print_node_orbits()
print_total_graphlets()
#print_graphlet_frequency()
print_shannon_diversity_measure()
print_local_complexity_measure()

G.draw_graff()