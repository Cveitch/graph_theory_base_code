# CSVGraffReader.py
# Conan Veitch, 4/18/2020
#
# Description: Creates a CSVGraffReader object with utility to parse CSV files containing edge-lists,
# adjacency lists, and adjacency matrices.

import numpy as np


class CSVGraffReader:
    def __init__(self, file_name):
        self.fname = file_name

    def csv_to_adj_list(self):
        # This is unfortunate, but due to the way networkx parses edgelists we need to pass the csv to edgelist_reader
        return self.fname

    def csv_to_edge_list(self):
        # Same as adj_list
        return self.fname

    def csv_to_adj_matrix(self, labels=False):
        # label implies that the adjacency matrix has named columns and rows in the csv.
        csvadjmat = np.genfromtxt(self.fname, delimiter=' ')
        if labels:
            adjmat = csvadjmat[1:, 1:]
        else:
            adjmat = csvadjmat
        return adjmat
