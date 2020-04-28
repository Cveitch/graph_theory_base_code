# GraphletCounter.py
# Conan Veitch, 2020-04-27
#
# Description: Counts graphlet automorphism orbits of 3, 4, 5 node graphlets.
# Note that the g# values in the gen_graphlet functions match graphlets.png in the documentation.
#

import networkx as nx
import itertools

class GraphletCounter:
    def __init__(self, graff_name):
        self.my_graff = graff_name

    def count_n_graphlets(self, n):
        # Enumerate n-graphlets from graph my_graff.
        if n < 3 or n > 5:
            exit(1)

        graphlet_count = 0
        if n == 3:
            graphlets = self.gen_3_graphlets()
        elif n == 4:
            graphlets = self.gen_4_graphlets()
        elif n == 5:
            graphlets = self.gen_5_graphlets()

        for x in range(len(graphlets)):
            for s_nodes in itertools.combinations(self.my_graff.nodes(), len(graphlets[x].nodes())):
                s_g = self.my_graff.subgraph(s_nodes)
                s_g
                if nx.is_connected(s_g) and nx.is_isomorphic(s_g, graphlets[x]):
                    print(s_g.nodes)
                    graphlet_count += 1
        return graphlet_count

    def gen_3_graphlets(self):
        # Returns an array with all possible 3-node graphlets
        g1 = nx.Graph()
        g1.add_edge(1, 2)
        g1.add_edge(2, 3)

        g2 = nx.Graph()
        g2.add_edge(1, 2)
        g2.add_edge(2, 3)
        g2.add_edge(3, 1)

        graphlet_array = [g1, g2]
        return graphlet_array

    def gen_4_graphlets(self):
        # Returns an array with all possible 3-node graphlets
        g3 = nx.Graph()
        g3.add_edge(1, 2)
        g3.add_edge(2, 3)
        g3.add_edge(3, 4)
        g4 = nx.Graph()
        g4.add_edge(1, 2)
        g4.add_edge(2, 3)
        g4.add_edge(2, 4)
        g5 = nx.Graph()
        g5.add_edge(1, 2)
        g5.add_edge(2, 3)
        g5.add_edge(3, 4)
        g5.add_edge(4, 1)
        g6 = nx.Graph()
        g6.add_edge(1, 2)
        g6.add_edge(2, 3)
        g6.add_edge(2, 4)
        g6.add_edge(3, 4)
        g7 = nx.Graph()
        g7.add_edge(1, 2)
        g7.add_edge(2, 3)
        g7.add_edge(3, 4)
        g7.add_edge(4, 1)
        g7.add_edge(1, 3)
        g8 = nx.Graph()
        g8.add_edge(1, 2)
        g8.add_edge(2, 3)
        g8.add_edge(3, 4)
        g8.add_edge(4, 1)
        g8.add_edge(1, 3)
        g8.add_edge(2, 4)

        graphlet_array = [g3, g4, g5, g6, g7, g8]
        return graphlet_array

    def gen_5_graphlets(self):
        # Returns an array with all possible 3-node graphlets
        g9 = nx.Graph()
        g9.add_edge(1, 2)
        g9.add_edge(2, 3)
        g9.add_edge(3, 4)
        g9.add_edge(4, 5)

        g10 = nx.Graph()
        g10.add_edge(1, 2)
        g10.add_edge(2, 3)
        g10.add_edge(2, 4)
        g10.add_edge(4, 5)

        g11 = nx.Graph()
        g11.add_edge(1, 2)
        g11.add_edge(2, 3)
        g11.add_edge(2, 4)
        g11.add_edge(2, 5)

        g12 = nx.Graph()
        g12.add_edge(1,2)
        g12.add_edge(2,3)
        g12.add_edge(3, 4)
        g12.add_edge(3, 5)
        g12.add_edge(2, 5)

        g13 = nx.Graph()
        g13.add_edge(1, 2)
        g13.add_edge(2, 3)
        g13.add_edge(3, 4)
        g13.add_edge(3, 5)
        g13.add_edge(4, 5)

        g14 = nx.Graph()
        g14.add_edge(1, 2)
        g14.add_edge(2, 3)
        g14.add_edge(2, 4)
        g14.add_edge(2, 5)
        g14.add_edge(4, 5)

        g15 = nx.Graph()
        g15.add_edge(1, 2)
        g15.add_edge(2, 3)
        g15.add_edge(3, 4)
        g15.add_edge(4, 5)
        g15.add_edge(5, 1)

        g16 = nx.Graph()
        g16.add_edge(1, 2)
        g16.add_edge(2, 3)
        g16.add_edge(3, 4)
        g16.add_edge(4, 5)
        g16.add_edge(5, 2)

        g17 = nx.Graph()
        g17.add_edge(1, 2)
        g17.add_edge(2, 3)
        g17.add_edge(3, 4)
        g17.add_edge(4, 5)
        g17.add_edge(5, 2)
        g17.add_edge(2, 4)

        g18 = nx.Graph()
        g18.add_edge(1, 2)
        g18.add_edge(2, 3)
        g18.add_edge(2, 4)
        g18.add_edge(2, 5)
        g18.add_edge(1, 5)
        g18.add_edge(3, 4)

        g19 = nx.Graph()
        g19.add_edge(1, 2)
        g19.add_edge(2, 3)
        g19.add_edge(3, 4)
        g19.add_edge(4, 5)
        g19.add_edge(5, 2)
        g19.add_edge(3, 5)

        g20 = nx.Graph()
        g20.add_edge(1, 2)
        g20.add_edge(2, 3)
        g20.add_edge(3, 4)
        g20.add_edge(4, 5)
        g20.add_edge(5, 2)

        g21 = nx.Graph()
        g21.add_edge(1, 2)
        g21.add_edge(2, 3)
        g21.add_edge(3, 4)
        g21.add_edge(4, 5)
        g21.add_edge(5, 1)
        g21.add_edge(2, 5)

        g22 = nx.Graph()
        g22.add_edge(1, 2)
        g22.add_edge(2, 3)
        g22.add_edge(3, 4)
        g22.add_edge(4, 5)
        g22.add_edge(4, 1)
        g22.add_edge(5, 2)
        g22.add_edge(2, 4)

        g23 = nx.Graph()
        g23.add_edge(1, 2)
        g23.add_edge(2, 3)
        g23.add_edge(3, 4)
        g23.add_edge(4, 5)
        g23.add_edge(5, 2)
        g23.add_edge(2, 4)
        g23.add_edge(3, 5)

        g24 = nx.Graph()
        g24.add_edge(1, 2)
        g24.add_edge(2, 3)
        g24.add_edge(3, 4)
        g24.add_edge(4, 5)
        g24.add_edge(5, 1)
        g24.add_edge(5, 2)
        g24.add_edge(5, 3)

        g25 = nx.Graph()
        g25.add_edge(1, 2)
        g25.add_edge(2, 3)
        g25.add_edge(3, 4)
        g25.add_edge(4, 1)
        g25.add_edge(4, 5)
        g25.add_edge(5, 2)
        g25.add_edge(5, 3)

        g26 = nx.Graph()
        g26.add_edge(1, 2)
        g26.add_edge(2, 3)
        g26.add_edge(3, 4)
        g26.add_edge(4, 5)
        g26.add_edge(5, 1)
        g26.add_edge(2, 5)
        g26.add_edge(2, 4)
        g26.add_edge(3, 5)

        g27 = nx.Graph()
        g27.add_edge(1, 2)
        g27.add_edge(2, 3)
        g27.add_edge(3, 4)
        g27.add_edge(4, 1)
        g27.add_edge(4, 5)
        g27.add_edge(5, 1)
        g27.add_edge(5, 2)
        g27.add_edge(5, 3)

        g28 = nx.Graph()
        g28.add_edge(1, 2)
        g28.add_edge(2, 3)
        g28.add_edge(3, 4)
        g28.add_edge(4, 1)
        g28.add_edge(4, 5)
        g28.add_edge(5, 1)
        g28.add_edge(5, 3)
        g28.add_edge(1, 3)
        g28.add_edge(5, 2)

        g29 = nx.Graph()
        g29.add_edge(1, 2)
        g29.add_edge(2, 3)
        g29.add_edge(3, 4)
        g29.add_edge(4, 5)
        g29.add_edge(5, 1)
        g29.add_edge(1, 3)
        g29.add_edge(1, 4)
        g29.add_edge(2, 5)
        g29.add_edge(2, 4)
        g29.add_edge(3, 5)

        graphlet_array = [g9, g10, g11, g12, g13, g14, g15, g16, g17, g18, g19, g20, g21, g22, g23, g24, g25,
                          g26, g27, g28, g29]
        return graphlet_array