# ComplexityMeasurer.py
# Conan Veitch, 2020-05-06
#
# Description: Different complexity measures for graphs.
#               NOTE: Both orbit functions are hard-coded with the value 30 (there are 29 graphlets)
#                     Fix this later on.
#

import math
import networkx as nx
import itertools
from collections import Counter


def vertex_degree_info_measure(graff):
    # Order here doesn't matter, so we use a list for degrees.
    degrees = [val for (node, val) in graff.degree()]
    degree_val = 0
    for ai in degrees:
        if ai > 0:
            degree_val += ai * math.log2(ai)
    return degree_val


def complexity_b(graff):
    b = 0
    degrees = dict(graff.degree)
    inter_node_d = dict(nx.all_pairs_shortest_path_length(graff))
    d = {}
    for nodes in inter_node_d:
        for other_nodes in inter_node_d:
            if nodes not in d:
                d[nodes] = inter_node_d[nodes][other_nodes]
            else:
                d[nodes] += inter_node_d[nodes][other_nodes]
    for nodes in inter_node_d:
        ai = degrees[nodes]
        di = d[nodes]
        b += ai / di
    return b


def graph_distance_complexity(graff, k):

    return 0


def total_walk_count(self):
    return 0


def topological_info_complexity(self):
    return 0


def frequency_info_sdm(freq):
    total_freq = 0
    hgf = 0
    for nodes in freq:
        total_freq += freq[nodes]
    for nodes in freq:
        if freq[nodes] != 0 and total_freq != 0:
            p_i = freq[nodes] / total_freq
            hgf += p_i * math.log2(p_i)
    return (-1) * hgf


def orbit_distribution_info_sdm(orbits):
    total_freq = 0
    hgd = 0
    orbit_freq = {}
    for i, j in orbits.items():
        for orbs in j:
            total_freq += 1
    for i in range(30):
        for j, k in orbits.items():
            for orbs in k:
                if orbs == i:
                    if i not in orbit_freq:
                        orbit_freq[i] = 1
                    else:
                        orbit_freq[i] += 1
    for orb in orbit_freq:
        p_i = orbit_freq[orb] / total_freq
        hgd += p_i * math.log2(p_i)
    return (-1) * hgd


def local_complexity_measure(orbits):
    h_gam = {}
    orbit_counts = {}
    for i in range(30):
        for nodes in orbits:
            if i not in orbit_counts:
                orbit_counts[i] = orbits[nodes].count(i)
            else:
                orbit_counts[i] += orbits[nodes].count(i)
    for nodes in orbits:
        h_gam[nodes] = 0
        for i in range(30):
            if i in orbits[nodes]:
                freq_orb = orbits[nodes].count(i) / orbit_counts[i]
                h_gam[nodes] += freq_orb * math.log2(freq_orb)
    for nodes in orbits:
        h_gam[nodes] *= (-1)
    return h_gam
