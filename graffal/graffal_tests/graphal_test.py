# graphal_test.py
# Conan Veitch, 4/18/2020
#
# Description: Test cases for graffal project.
#

import graffal.graff_gen.GraffWrapper as gmake
import graffal.grafflet_gen.GraffletWrapper as gwrap
import graffal.complexity.ComplexityMeasurer as comeas


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


def print_vertex_degree_info_measure():
    vdim = comeas.vertex_degree_info_measure(G.get_graff())
    print("Vertex Degree Information measure is: ", vdim)


def print_frequency_info_sdm():
    sdm = comeas.frequency_info_sdm(gwrapper.get_grafflet_freq())
    print("Frequency Information measure is: ", sdm)


def print_orbit_distribution_info_sdm():
    sdm = comeas.orbit_distribution_info_sdm(gwrapper.get_orbit_counts())
    print("Orbit Distribution Information measure is ", sdm)


def print_local_complexity_measure():
    lcm = comeas.local_complexity_measure(gwrapper.get_orbit_counts())
    for node in lcm:
        print("Local Complexity Measure of node", node, "is:", lcm[node])


def print_complexity_b():
    print("Complexity B is:", comeas.complexity_b(G.get_graff()))


def print_graph_distance_complexity():
    print("Graph Distance Complexity is:", comeas.graph_distance_complexity(G.get_graff()))


def print_total_walk_count(n):
    print("The Total Walk Count of length ", n, "or less is:", comeas.total_walk_count(G.get_adj_matrix(), n))


def get_test_graph(k):
    if k == 1:
        cgr = "adj_list_csv.csv"
        G = gmake.GraffWrapper(cgr, 2)
    if k == 2:
        cgr = "edge_list_csv.csv"
        G = gmake.GraffWrapper(cgr, 1)
    if k == 3:
        cgr = "adj_mat_csv.csv"
        G = gmake.GraffWrapper(cgr, 3)
    if k == 4:
        cgr = "test_edge.csv"
        G = gmake.GraffWrapper(cgr, 1)
    return G

G = get_test_graph(1)
#gwrapper = gwrap.GraphletWrapper(G.get_graff(), 1)

#print_edgelist()
#print_node_orbits()
#print_total_graphlets()
#print_graphlet_frequency()

#print_frequency_info_sdm()
#print_orbit_distribution_info_sdm()
#print_vertex_degree_info_measure()
#print_complexity_b()
#print_local_complexity_measure()
#print_graph_distance_complexity()
print_total_walk_count(4)

G.draw_graff()

