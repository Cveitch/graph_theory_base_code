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
    graff.graff_update()
    graff.save_graff(300, spec=False, colmap=True, grou='node_complexity', nodelabel=True, file_name=grafftype+"_graph")
    graff.graff_update()
    graff.save_diversity_graph(rich, nlc, x="Orbit Richness", y="Diversity",
                                filename=grafftype+"_Richness_vs_Diversity")
    graff.graff_update()
    graff.save_diversity_graph(rich, orp, x="Orbit Richness", y="Orbit Relative Proportion",
                                filename=grafftype+"_richness_vs_relprop")
    graff.graff_update()
    graff.save_diversity_graph(nlc, orp, x="Diversity", y="Orbit Relative Proportion",
                                filename=grafftype+"_Diversity_vs_relprop")

grafflet_nodes = 4

graff1 = get_test_graph(1)
plot_test_graphs(graff1, "Mark_Dale_full_orbit_graph", grafflet_nodes, complexity=False)

graff2 = get_test_graph(5)
plot_test_graphs(graff2, "Erdos_Renyi_graph", grafflet_nodes, complexity=False)

graff3 = get_test_graph(6)
plot_test_graphs(graff3, "Watts_Strogatz_graph", grafflet_nodes, complexity=False)

graff4 = get_test_graph(7)
plot_test_graphs(graff4, "Barabasi_Albert_graph", grafflet_nodes, complexity=False)






# # set width of bar
# barWidth = 0.2
#
# bars1 = []
# bars2 = []
# bars3 = []
# bars4 = []
# # set height of bar
#
# if grafflet_nodes == 4:
#     total_glets = 15
# else:
#     total_glets = 30
#
# # Plotting options
# rd_opt = 0
# # rd_opt 0 for Diversity, 1 for richness.
# plot_label = 'Graphlet Richness'
#
#
# if rd_opt == 0:
#     for i in range(total_glets):
#         if i in cwrapper1.node_diversity:
#             bars1.append(cwrapper1.node_diversity[i])
#         else:
#             bars1.append(0)
#
#     for i in range(total_glets):
#         if i in cwrapper2.node_diversity:
#             bars2.append(cwrapper2.node_diversity[i])
#         else:
#             bars2.append(0)
#
#     for i in range(total_glets):
#         if i in cwrapper2.node_diversity:
#             bars3.append(cwrapper3.node_diversity[i])
#         else:
#             bars3.append(0)
#
#     for i in range(total_glets):
#         if i in cwrapper2.node_diversity:
#             bars4.append(cwrapper4.node_diversity[i])
#         else:
#             bars4.append(0)
# elif rd_opt == 1:
#     for i in range(total_glets):
#         if i in cwrapper1.node_richness:
#             bars1.append(cwrapper1.node_richness[i])
#         else:
#             bars1.append(0)
#
#     for i in range(total_glets):
#         if i in cwrapper2.node_richness:
#             bars2.append(cwrapper2.node_richness[i])
#         else:
#             bars2.append(0)
#
#     for i in range(total_glets):
#         if i in cwrapper2.node_richness:
#             bars3.append(cwrapper3.node_richness[i])
#         else:
#             bars3.append(0)
#
#     for i in range(total_glets):
#         if i in cwrapper2.node_richness:
#             bars4.append(cwrapper4.node_richness[i])
#         else:
#             bars4.append(0)
#
#
#
# #Set position of bar on X axis
# r1 = np.arange(len(bars1))
# r2 = [x + barWidth for x in r1]
# r3 = [x + barWidth for x in r2]
# r4 = [x + barWidth for x in r3]
#
# # Make the plot
# plt.bar(r1, bars1, color='#0CFCA0', width=barWidth, edgecolor='white', label='Dale Graph')
# plt.bar(r2, bars2, color='#CC0A4E', width=barWidth, edgecolor='white', label='Erdos-Renyi Graph')
# plt.bar(r3, bars3, color='#0C2CFC', width=barWidth, edgecolor='white', label='Watts-Strogatz Graph')
# plt.bar(r4, bars4, color='#FCFC0C', width=barWidth, edgecolor='white', label='Barabasi-Albert Graph')
#
# # Add xticks on the middle of the group bars
# plt.xlabel(plot_label, fontweight='bold')
# #plt.xticks([r + barWidth for r in range(len(bars1))], ['A', 'B', 'C', 'D', 'E'])
#
# # Create legend & Show graphic
# plt.legend()
# plt.show()

