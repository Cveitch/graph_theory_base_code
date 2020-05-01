# graphal_test.py
# Conan Veitch, 4/18/2020
#
# Description: Test cases for graphal project.
#


import graphal.graff_gen.CSVGraffReader as csvgr
import graphal.graff_gen.UndirectedGraff as ugraff
import matplotlib.pyplot as plt
import networkx as nx
import graphal.grafflet_gen.GraffletCounter as gcounter
import graphal.grafflet_gen.Grafflet as graphlet


graf = ugraff.UndirectedGraff()




# cgr = csvgr.CSVGraffReader('edge_list_csv.csv')
# graf.build_from_edge_list(cgr.csv_to_edge_list())

cgr = csvgr.CSVGraffReader('adj_list_csv.csv')
graf.build_from_adj_list(cgr.csv_to_adj_list())

#cgr = csvgr.CSVGraffReader('adj_mat_csv.csv')
#graf.build_from_adj_matrix(cgr.csv_to_adj_matrix())

gcount = gcounter.GraffletCounter(graf.G, 3)
print(*gcount.grafflet_edges, sep="\n")
print(gcount.grafflet_count)
#print(gcounter.count_n_graphlets(3))


grflt = graphlet.Grafflet(27)
print(grflt.get_node_orbit(4))




#nx.draw(graf.G, node_size=500, with_labels=True)
#plt.show()
