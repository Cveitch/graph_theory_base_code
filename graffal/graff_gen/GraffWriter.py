# GraffWriter.py
# Conan Veitch, 4/18/2020
#
# Description: Creates GraffWriter object, outputs visualizations and csv file representations of Graff objects.
#               TODO: csv representations
#

import matplotlib.pyplot as plt
import networkx as nx


class GraffWriter:
    def __init__(self, graff_name):
        self.my_graff = graff_name

    def update_graff_writer(self):
        plt.clf()
        nx.draw(self.my_graff.G, node_size=500, with_labels=True)

    def plot_graff(self):
        self.update_graff_writer()
        plt.show()

    def graff_to_file(self, file_name="temp_graff", file_ext="png"):
        #Saves graph visualization to graffal/graffal_tests/
        self.update_graff_writer()
        fname = "../graffal_tests/"+file_name+"."+file_ext
        plt.savefig(fname)
