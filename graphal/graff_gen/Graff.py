# Graff.py
# Conan Veitch, 4/18/2020
#
# Description: Creates an empty Graff object, utility to create adjacency matrix, edge list and
# adjacency list representations.


class Graff:
    def __init__(self):
        self.adj_mat = 0
        self.adj_list = 0
        self.edge_list = 0

    def set_adj_list(self, alist):
        self.adj_list = alist

    def set_adj_mat(self, amat):
        self.adj_mat = amat

    def set_edge_list(self, elist):
        self.edge_list = elist

    def adj_mat_to_adj_list(self, amat):
        alist = amat
        return alist

    def adj_mat_to_edge_list(self, amat):
        elist = amat
        return elist

    def edge_list_to_adj_mat(self, elist):
        amat = elist
        return amat

    def edge_list_to_adj_list(self, elist):
        alist = elist
        return alist

    def adj_list_to_adj_mat(self, alist):
        amat = alist
        return amat

    def adj_list_to_edge_list(self, alist):
        elist = alist
        return elist
