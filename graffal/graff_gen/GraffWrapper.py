# GraffWrapper.py
# Conan Veitch, 2020-05-07
#
# Description: Wrapper for graff_gen utilities
#               Options: 1 for edge list, 2 for adjacency list, 3 for adjacency matrix
#

import graffal.graff_gen.CSVGraffReader as csvgr
import graffal.graff_gen.UndirectedGraff as ugraff
import graffal.graff_gen.GraffWriter as gwriter
import networkx as nx


class GraffWrapper:
    def __init__(self, fname, option=1):
        self.graf = ugraff.UndirectedGraff()
        if fname:
            cgr = csvgr.CSVGraffReader(fname)
            if option < 1 or option > 3:
                exit('Incorrect file option')
            elif option == 1:
                self.graf.build_from_edge_list(cgr.csv_to_edge_list())
            elif option == 2:
                self.graf.build_from_adj_list(cgr.csv_to_adj_list())
            elif option == 3:
                self.graf.build_from_adj_matrix(cgr.csv_to_adj_matrix())
        self.graf.build_adj_matrix()
        self.gwrite = gwriter.GraffWriter(self.graf)

    def get_graff(self):
        return self.graf.G

    def get_edges(self):
        return self.graf.G.edges

    def set_new_graff(self, g):
        self.graf.G = g
        self.graf.build_adj_matrix()
        self.gwrite = gwriter.GraffWriter(self.graf)

    def set_nodes(self, ndict, key):
        nx.set_node_attributes(self.graf.G, ndict, key)

    def get_nodes(self, key):
        return nx.get_node_attributes(self.graf.G, key)

    def get_adj_matrix(self):
        return self.graf.adj_matrix

    def draw_graff(self, nsize=500, spec=True, colmap=True, grou=None, nodelabel=True):
        self.gwrite.plot_graff(nsize, spectral=spec, colourmap=colmap, group=grou, nodlabel=nodelabel)
        #self.gwrite.update_graff_writer_colourmap('node_complexity')

    def graff_update(self):
        self.gwrite.clear_graff_writer()

    def show_graff(self):
        self.gwrite.live_plot()

    def save_diversity_graph(self, richness, nlc, xa=None, ya=None, x="x", y="y", filename="temp"):
        self.gwrite.diversity_graphs(richness, nlc, xax=xa, yax=ya, file_name=filename, xl=x, yl=y)

    def save_dict_keyed_graph(self, grp, xa=None, ya=None, x="x", y="y", filename="temp", file_ext="png"):
        self.gwrite.dictionary_keyed_graph(grp, xax=xa, yax=ya, xl=x, yl=y, file_name=filename, file_ext=file_ext)

    def save_graff(self, nsize, spec=True, colmap=True, grou=None, nodelabel=True,
                   file_name="temp_graff", file_ext="png"):
        self.gwrite.plot_graff(nsize, spectral=spec, colourmap=colmap, group=grou, nodlabel=nodelabel)
        self.gwrite.graff_to_file(nsize, file_name=file_name, file_ext=file_ext)

    def save_diversity_colourmap_graph(self, richness, nlc, group, xa=None, ya=None, x="x", y="y", filename="temp"):
        self.gwrite.diversity_graph_colourmap(richness, nlc, group, xax=xa, yax=ya, file_name=filename, xl=x, yl=y)