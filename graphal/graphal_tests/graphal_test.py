# graphal_test.py
# Conan Veitch, 4/18/2020
#
# Description: Test cases for graphal project.
#

import graphal.graff_gen.CSVGraffReader as csvgr
import graphal.graff_gen.UndirectedGraff as ugraff
import matplotlib.pyplot as plt
import networkx as nx

graf = ugraff.UndirectedGraff()

cgr = csvgr.CSVGraffReader('adj_mat_csv.csv')

graf.build_from_adj_matrix(cgr.csv_to_adj_matrix())

nx.draw(graf.G, node_size=500, with_labels=True)
plt.show()