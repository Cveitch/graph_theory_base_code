# GraffletCollection.py
# Conan Veitch, 2020-04-30
#
# Description: Creates 3, 4, or 5 node grafflet_gen
#

import graffal.grafflet_gen.Grafflet as grflt


class GraffletCollection:
    def __init__(self, n):
        if n < 2 or n > 5:
            exit("Invalid Graphlet Node Count")
        if n == 2:
            self.g_list = self.gen_2_grafflets()
        if n == 3:
            self.g_list = self.gen_3_grafflets()
        elif n == 4:
            self.g_list = self.gen_4_grafflets()
        elif n == 5:
            self.g_list = self.gen_5_grafflets()

    def gen_2_grafflets(self):
        g0 = grflt.Grafflet(0)
        grafflets = [g0]
        return grafflets

    def gen_3_grafflets(self):
        # Returns an array with all possible 3-node grafflet_gen
        g1 = grflt.Grafflet(1)
        g2 = grflt.Grafflet(2)
        grafflets = [g1, g2]
        return grafflets

    def gen_4_grafflets(self):
        # Returns an array with all possible 4-node grafflet_gen
        g1 = grflt.Grafflet(3)
        g2 = grflt.Grafflet(4)
        g3 = grflt.Grafflet(5)
        g4 = grflt.Grafflet(6)
        g5 = grflt.Grafflet(7)
        g6 = grflt.Grafflet(8)
        grafflets = [g1, g2, g3, g4, g5, g6]
        return grafflets

    def gen_5_grafflets(self):
        # Returns an array with all possible 5-node grafflet_gen
        g1 = grflt.Grafflet(9)
        g2 = grflt.Grafflet(10)
        g3 = grflt.Grafflet(11)
        g4 = grflt.Grafflet(12)
        g5 = grflt.Grafflet(13)
        g6 = grflt.Grafflet(14)
        g7 = grflt.Grafflet(15)
        g8 = grflt.Grafflet(16)
        g9 = grflt.Grafflet(17)
        g10 = grflt.Grafflet(18)
        g11 = grflt.Grafflet(19)
        g12 = grflt.Grafflet(20)
        g13 = grflt.Grafflet(21)
        g14 = grflt.Grafflet(22)
        g15 = grflt.Grafflet(23)
        g16 = grflt.Grafflet(24)
        g17 = grflt.Grafflet(25)
        g18 = grflt.Grafflet(26)
        g19 = grflt.Grafflet(27)
        g20 = grflt.Grafflet(28)
        g21 = grflt.Grafflet(29)
        grafflets = [g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, g14, g15, g16, g17, g18, g19, g20, g21]
        return grafflets
