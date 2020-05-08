# GraffWrapper.py
# Conan Veitch, 2020-05-07
#
# Description: Wrapper for graff_gen utilities
#               Options: 1 for edge list, 2 for adjacency list, 3 for adjacency matrix
#

import graffal.graff_gen.CSVGraffReader as csvgr
import graffal.graff_gen.UndirectedGraff as ugraff
import graffal.graff_gen.GraffWriter as gwriter


class GraffWrapper:
    def __init__(self, fname, option=1):
        self.graf = ugraff.UndirectedGraff()
        cgr = csvgr.CSVGraffReader(fname)
        if option < 1 or option > 3:
            exit('Incorrect file option')
        elif option == 1:
            self.graf.build_from_edge_list(cgr.csv_to_edge_list())
        elif option == 2:
            self.graf.build_from_adj_list(cgr.csv_to_adj_list())
        elif option == 3:
            self.graf.build_from_adj_matrix(cgr.csv_to_adj_matrix())
        self.gwrite = gwriter.GraffWriter(self.graf)

    def get_graff(self):
        return self.graf.G

    def draw_graff(self):
        self.gwrite.plot_graff()

    def save_graff(self, file_name="temp_graff", file_ext="png"):
        self.gwrite.graff_to_file(file_name, file_ext)
