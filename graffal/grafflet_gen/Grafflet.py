# Grafflet.py
# Conan Veitch, 2020-04-30
#
# Description: Creates graphlet n, where n maps to one of the graphlets in graphlets.png in the documentation.
#              This is ugly, but I don't want to rely on arbitrary whitespace delimited or csv files.
#

import networkx as nx


class Grafflet:
    def __init__(self, g_num):
        if g_num < 0 or g_num > 29:
            exit("Invalid Graphlet Enumeration")
        self.G = self.gen_grafflet(g_num)
        self.graphlet_enum = g_num

    def get_node_orbit(self, n):
        orb = self.G.nodes[n]['orbit']
        return orb

    def gen_grafflet(self, n):
        g = nx.Graph()
        # Three node graphlets
        if n == 0:
            g.add_edge(1, 2)
            orb = {1: 0, 2: 0}
        # Three node graphlets
        if n == 1:
            g.add_edge(1, 2)
            g.add_edge(2, 3)
            orb = {1: 1, 2: 2, 3: 1}
        elif n == 2:
            g.add_edge(1, 2)
            g.add_edge(2, 3)
            g.add_edge(3, 1)
            orb = {1: 3, 2: 3, 3: 3}
        # Four node graphlets
        elif n == 3:
            g = nx.Graph()
            g.add_edge(1, 2)
            g.add_edge(2, 3)
            g.add_edge(3, 4)
            orb = {1: 4, 2: 5, 3: 5, 4: 4}
        elif n == 4:
            g.add_edge(1, 2)
            g.add_edge(2, 3)
            g.add_edge(2, 4)
            orb = {1: 6, 2: 7, 3: 6, 4: 6}
        elif n == 5:
            g.add_edge(1, 2)
            g.add_edge(2, 3)
            g.add_edge(3, 4)
            g.add_edge(4, 1)
            orb = {1: 8, 2: 8, 3: 8, 4: 8}
        elif n == 6:
            g.add_edge(1, 2)
            g.add_edge(2, 3)
            g.add_edge(2, 4)
            g.add_edge(3, 4)
            orb = {1: 9, 2: 11, 3: 10, 4: 10}
        elif n == 7:
            g.add_edge(1, 2)
            g.add_edge(2, 3)
            g.add_edge(3, 4)
            g.add_edge(4, 1)
            g.add_edge(1, 3)
            orb = {1: 13, 2: 12, 3: 13, 4: 12}
        elif n == 8:
            g.add_edge(1, 2)
            g.add_edge(2, 3)
            g.add_edge(3, 4)
            g.add_edge(4, 1)
            g.add_edge(1, 3)
            g.add_edge(2, 4)
            orb = {1: 14, 2: 14, 3: 14, 4: 14}
        # Five node graphlets
        elif n == 9:
            g.add_edge(1, 2)
            g.add_edge(2, 3)
            g.add_edge(3, 4)
            g.add_edge(4, 5)
            orb = {1: 15, 2: 16, 3: 17, 4: 16, 5: 15}
        elif n == 10:
            g.add_edge(1, 2)
            g.add_edge(2, 3)
            g.add_edge(2, 4)
            g.add_edge(4, 5)
            orb = {1: 19, 2: 21, 3: 19, 4: 20, 5: 18}
        elif n == 11:
            g.add_edge(1, 2)
            g.add_edge(2, 3)
            g.add_edge(2, 4)
            g.add_edge(2, 5)
            orb = {1: 22, 2: 23, 3: 22, 4: 22, 5: 22}
        elif n == 12:
            g.add_edge(1, 2)
            g.add_edge(2, 3)
            g.add_edge(3, 4)
            g.add_edge(3, 5)
            g.add_edge(2, 5)
            orb = {1: 24, 2: 26, 3: 26, 4: 24, 5: 25}
        elif n == 13:
            g.add_edge(1, 2)
            g.add_edge(2, 3)
            g.add_edge(3, 4)
            g.add_edge(3, 5)
            g.add_edge(4, 5)
            orb = {1: 27, 2: 28, 3: 30, 4: 29, 5: 29}
        elif n == 14:
            g.add_edge(1, 2)
            g.add_edge(2, 3)
            g.add_edge(2, 4)
            g.add_edge(2, 5)
            g.add_edge(4, 5)
            orb = {1: 31, 2: 33, 3: 31, 4: 32, 5: 32}
        elif n == 15:
            g.add_edge(1, 2)
            g.add_edge(2, 3)
            g.add_edge(3, 4)
            g.add_edge(4, 5)
            g.add_edge(5, 1)
            orb = {1: 34, 2: 34, 3: 34, 4: 34, 5: 34}
        elif n == 16:
            g.add_edge(1, 2)
            g.add_edge(2, 3)
            g.add_edge(3, 4)
            g.add_edge(4, 5)
            g.add_edge(5, 2)
            orb = {1: 35, 2: 38, 3: 37, 4: 36, 5: 37}
        elif n == 17:
            g.add_edge(1, 2)
            g.add_edge(2, 3)
            g.add_edge(3, 4)
            g.add_edge(4, 5)
            g.add_edge(5, 2)
            g.add_edge(2, 4)
            orb = {1: 39, 2: 42, 3: 40, 4: 41, 5: 40}
        elif n == 18:
            g.add_edge(1, 2)
            g.add_edge(2, 3)
            g.add_edge(2, 4)
            g.add_edge(2, 5)
            g.add_edge(1, 5)
            g.add_edge(3, 4)
            orb = {1: 43, 2: 44, 3: 43, 4: 43, 5: 43}
        elif n == 19:
            g.add_edge(1, 2)
            g.add_edge(2, 3)
            g.add_edge(3, 4)
            g.add_edge(4, 5)
            g.add_edge(5, 2)
            g.add_edge(3, 5)
            orb = {1: 45, 2: 47, 3: 48, 4: 46, 5: 48}
        elif n == 20:
            g.add_edge(1, 2)
            g.add_edge(2, 3)
            g.add_edge(3, 4)
            g.add_edge(4, 5)
            g.add_edge(5, 2)
            g.add_edge(4, 1)
            orb = {1: 50, 2: 50, 3: 50, 4: 50, 5: 49}
        elif n == 21:
            g.add_edge(1, 2)
            g.add_edge(2, 3)
            g.add_edge(3, 4)
            g.add_edge(4, 5)
            g.add_edge(5, 1)
            g.add_edge(2, 5)
            orb = {1: 52, 2: 53, 3: 51, 4: 51, 5: 53}
        elif n == 22:
            g.add_edge(1, 2)
            g.add_edge(2, 3)
            g.add_edge(3, 4)
            g.add_edge(4, 5)
            g.add_edge(4, 1)
            g.add_edge(5, 2)
            g.add_edge(2, 4)
            orb = {1: 54, 2: 55, 3: 54, 4: 55, 5: 54}
        elif n == 23:
            g.add_edge(1, 2)
            g.add_edge(2, 3)
            g.add_edge(3, 4)
            g.add_edge(4, 5)
            g.add_edge(5, 2)
            g.add_edge(2, 4)
            g.add_edge(3, 5)
            orb = {1: 56, 2: 58, 3: 57, 4: 57, 5: 57}
        elif n == 24:
            g.add_edge(1, 2)
            g.add_edge(2, 3)
            g.add_edge(3, 4)
            g.add_edge(4, 5)
            g.add_edge(5, 1)
            g.add_edge(5, 2)
            g.add_edge(5, 3)
            orb = {1: 59, 2: 60, 3: 60, 4: 59, 5: 61}
        elif n == 25:
            g.add_edge(1, 2)
            g.add_edge(2, 3)
            g.add_edge(3, 4)
            g.add_edge(4, 1)
            g.add_edge(4, 5)
            g.add_edge(5, 2)
            g.add_edge(5, 3)
            orb = {1: 62, 2: 63, 3: 64, 4: 63, 5: 64}
        elif n == 26:
            g.add_edge(1, 2)
            g.add_edge(2, 3)
            g.add_edge(3, 4)
            g.add_edge(4, 5)
            g.add_edge(5, 1)
            g.add_edge(2, 5)
            g.add_edge(2, 4)
            g.add_edge(3, 5)
            orb = {1: 65, 2: 67, 3: 66, 4: 66, 5: 67}
        elif n == 27:
            g.add_edge(1, 2)
            g.add_edge(2, 3)
            g.add_edge(3, 4)
            g.add_edge(4, 1)
            g.add_edge(4, 5)
            g.add_edge(5, 1)
            g.add_edge(5, 2)
            g.add_edge(5, 3)
            orb = {1: 68, 2: 68, 3: 68, 4: 68, 5: 69}
        elif n == 28:
            g.add_edge(1, 2)
            g.add_edge(2, 3)
            g.add_edge(3, 4)
            g.add_edge(4, 1)
            g.add_edge(4, 5)
            g.add_edge(5, 1)
            g.add_edge(5, 3)
            g.add_edge(1, 3)
            g.add_edge(5, 2)
            orb = {1: 71, 2: 70, 3: 71, 4: 70, 5: 71}
        elif n == 29:
            g.add_edge(1, 2)
            g.add_edge(2, 3)
            g.add_edge(3, 4)
            g.add_edge(4, 5)
            g.add_edge(5, 1)
            g.add_edge(1, 3)
            g.add_edge(1, 4)
            g.add_edge(2, 5)
            g.add_edge(2, 4)
            g.add_edge(3, 5)
            orb = {1: 72, 2: 72, 3: 72, 4: 72, 5: 72}

        nx.set_node_attributes(g, orb, 'orbit')
        return g


#G.degree[0]