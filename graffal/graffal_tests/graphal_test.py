# graphal_test.py
# Conan Veitch, 4/18/2020
#
# Description: Test cases for graffal project.
#

import graffal.graff_gen.GraffWrapper as gmake
import graffal.complexity.ComplexityWrapper as cwrap
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx


def get_test_graph(k):
    if k == 1:
        # Mark's graph
        cgr = "test_data/adj_list_csv.csv"
        g = gmake.GraffWrapper(cgr, 2)
    if k == 2:
        cgr = "test_data/edge_list_csv.csv"
        g = gmake.GraffWrapper(cgr, 1)
    if k == 3:
        cgr = "test_data/adj_mat_csv.csv"
        g = gmake.GraffWrapper(cgr, 3)
    if k == 4:
        cgr = "test_data/test_edge.csv"
        g = gmake.GraffWrapper(cgr, 1)
    if k == 5:
        cgr = "test_data/test_edge.csv"
        g = gmake.GraffWrapper(cgr, 1)
        g.set_new_graff(nx.erdos_renyi_graph(50, 0.1))
    if k == 6:
        cgr = "test_data/test_edge.csv"
        g = gmake.GraffWrapper(cgr, 1)
        g.set_new_graff(nx.watts_strogatz_graph(50, 4, 0.1))
    if k == 7:
        cgr = "test_data/test_edge.csv"
        g = gmake.GraffWrapper(cgr, 1)
        g.set_new_graff(nx.barabasi_albert_graph(50, 1))
    return g


def plot_test_graphs(graff, grafftype, grafflets, complexity=True):
    cwrapper = cwrap.ComplexityWrapper(graff, grafflet_nodes=grafflets)

    if complexity:
        cwrapper.print_complexity_suite()
    cwrapper.write_complexity_suite_file(grafftype)
    rich = cwrapper.get_node_richness()
    nlc = cwrapper.get_nlc_measure()
    orp = cwrapper.get_node_orp()
    grp = cwrapper.get_global_richness_proportion()
    anr = cwrapper.get_node_average_richness()

    # graff.graff_update()
    # graff.save_graff(300, spec=False, colmap=True, grou='node_complexity', nodelabel=True, file_name=grafftype+"_graph")
    #
    # graff.graff_update()
    # graff.save_diversity_graph(rich, nlc, xa=[0, 16], ya=[0, 4.8], x="Orbit Richness", y="Diversity",
    #                             filename=grafftype+"_Richness_vs_Diversity")
    # graff.graff_update()
    # graff.save_diversity_graph(rich, orp, xa=[0, 16], ya=[0, 7.5], x="Orbit Richness", y="Orbit Relative Proportion",
    #                             filename=grafftype+"_richness_vs_relprop")
    # graff.graff_update()
    # graff.save_diversity_graph(nlc, orp, xa=[0, 4.8], ya=[0, 7.5], x="Diversity", y="Orbit Relative Proportion",
    #                             filename=grafftype+"_Diversity_vs_relprop")
    #
    # graff.graff_update()
    # graff.save_dict_keyed_graph(grp, xa=[0, 16], ya=[0, 1], x="Richness", y="Global Richness Proportion",
    #                             filename=grafftype + "richness_vs_richprop")
    graff.graff_update()
    graff.save_diversity_colourmap_graph(rich, anr, 'node_complexity', xa=[0, 16], ya=[4, 16], x="Richness", y="Node First-Order Richness",
                                filename=grafftype + "richness_vs_fiorrich")



grafflet_nodes = 4

graff1 = get_test_graph(1)

plot_test_graphs(graff1, "Mark_Dale_full_orbit_graph", grafflet_nodes, complexity=False)

# graff2 = get_test_graph(5)
# plot_test_graphs(graff2, "Erdos_Renyi_graph", grafflet_nodes, complexity=False)
#
# graff3 = get_test_graph(6)
# plot_test_graphs(graff3, "Watts_Strogatz_graph", grafflet_nodes, complexity=False)
#
# graff4 = get_test_graph(7)
# plot_test_graphs(graff4, "Barabasi_Albert_graph", grafflet_nodes, complexity=False)
#
















