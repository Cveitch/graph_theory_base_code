# GraffWriter.py
# Conan Veitch, 4/18/2020
#
# Description: Creates GraffWriter object, outputs visualizations and csv file representations of Graff objects.
#               TODO: csv representations
#

import matplotlib.pyplot as plt
import networkx as nx
from itertools import count


class GraffWriter:
    def __init__(self, graff_name):
        self.my_graff = graff_name
        self.my_spectral_graff = nx.spectral_layout(self.my_graff.G)

    def clear_graff_writer(self):
        plt.clf()

    def live_plot(self):
        plt.show()

    def update_graff_writer(self, option, nsize):
        plt.clf()
        if option == 0:
            nx.draw(self.my_graff.G, node_size=500, with_labels=True)
        elif option == 1:
            nx.draw_spectral(self.my_graff.G, node_size=500, with_labels=True)

    def update_graff_writer_colourmap(self, nsize, group, spec=True, nlabel=True):
        groups = nx.get_node_attributes(self.my_graff.G, group).values()
        mapping = dict(zip(sorted(groups), count()))
        nods = self.my_graff.G.nodes()
        colours = list(groups)
        # drawing nodes and edges separately so we can capture collection for colobar
        if spec:
            pos = nx.spectral_layout(self.my_graff.G)
        else:
            #pos = nx.spring_layout(self.my_graff.G)
            pos = nx.kamada_kawai_layout(self.my_graff.G)
        ec = nx.draw_networkx_edges(self.my_graff.G, pos, alpha=0.2)
        nc = nx.draw_networkx_nodes(self.my_graff.G, pos, nodelist=nods, node_color=colours,
                                    with_labels=nlabel, node_size=nsize, cmap=plt.cm.rainbow)
        if nlabel:
            lc = nx.draw_networkx_labels(self.my_graff.G, pos)
        plt.colorbar(nc)
        plt.axis('off')

    def plot_graff(self, nsize, spectral=True, colourmap=False, group=None, nodlabel=True):
        if colourmap:
            self.update_graff_writer_colourmap(nsize, group, spec=spectral, nlabel=nodlabel)
        else:
            if spectral:
                self.update_graff_writer(1, nsize)
            else:
                self.update_graff_writer(0, nsize)

    def graff_to_file(self, nsize, spectral=True, file_name="temp_graff", file_ext="png"):
        # Saves graph visualization to graffal/graffal_tests/saved
        fname = "../graffal_tests/saved/"+file_name+"."+file_ext
        plt.savefig(fname)

    def diversity_graphs(self, xcoord, ycoord, xax=None, yax=None, xl="x", yl="y", file_name="temp", file_ext="png"):
        coords = {}
        for node in xcoord:
            coords[node] = [xcoord[node], ycoord[node]]
            print(xcoord[node], ycoord[node])
        xs, ys = zip(*coords.values())
        labels = coords.keys()

        # plt.figure(figsize=(10, 8))
        # plt.title('Scatter Plot', fontsize=15)
        plt.xlabel(xl, fontsize=15)
        plt.ylabel(yl, fontsize=15)
        plt.scatter(xs, ys, marker='o')

        if xax is not None:
            plt.xlim(xax[0], xax[1])
        if yax is not None:
            plt.ylim(yax[0], yax[1])

        # add labels
        for label, x, y in zip(labels, xs, ys):
            plt.annotate(label, xy=(x, y))

        fname = "../graffal_tests/saved/" + file_name + "." + file_ext
        plt.savefig(fname)

    def dictionary_keyed_graph(self, grp, xax=None, yax=None, xl="x", yl="y", file_name="temp", file_ext="png"):
        coords = {}
        for node in grp:
            coords[node] = [node, grp[node]]
        xs, ys = zip(*coords.values())
        labels = coords.keys()

        # plt.figure(figsize=(10, 8))
        # plt.title('Scatter Plot', fontsize=15)
        plt.xlabel(xl, fontsize=15)
        plt.ylabel(yl, fontsize=15)
        plt.scatter(xs, ys, marker='o')
        if xax is not None:
            plt.xlim(xax[0], xax[1])
        if yax is not None:
            plt.ylim(yax[0], yax[1])
        # add labels
        # for label, x, y in zip(labels, xs, ys):
        #     plt.annotate(label, xy=(x, y))

        fname = "../graffal_tests/saved/" + file_name + "." + file_ext
        plt.savefig(fname)



    def diversity_graph_colourmap(self, xcoord, ycoord, group, xax=None, yax=None, xl="x", yl="y", file_name="temp", file_ext="png"):
        groups = nx.get_node_attributes(self.my_graff.G, group).values()
        nods = self.my_graff.G.nodes()
        colours = list(groups)

        coords = {}
        for node in xcoord:
            coords[node] = [xcoord[node], ycoord[node]]
            print(xcoord[node], ycoord[node])
        xs, ys = zip(*coords.values())
        labels = coords.keys()

        # plt.figure(figsize=(10, 8))
        # plt.title('Scatter Plot', fontsize=15)
        plt.xlabel(xl, fontsize=15)
        plt.ylabel(yl, fontsize=15)
        plt.scatter(xs, ys, c=colours, cmap=plt.cm.rainbow, marker='o')

        cbar = plt.colorbar()
        cbar.set_label(group)

        if xax is not None:
            plt.xlim(xax[0], xax[1])
        if yax is not None:
            plt.ylim(yax[0], yax[1])

        # add labels
        for label, x, y in zip(labels, xs, ys):
            plt.annotate(label, xy=(x, y))

        fname = "../graffal_tests/saved/" + file_name + "." + file_ext
        plt.savefig(fname)