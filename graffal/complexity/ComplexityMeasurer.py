# ComplexityMeasurer.py
# Conan Veitch, 2020-05-06
#
# Description: Different complexity measures for graphs.
#               NOTE: Both orbit functions are hard-coded with the value 30 (there are 29 graphlets)
#                     Fix this later on.
#

import math
import networkx as nx
import numpy

from tqdm import tqdm


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


# Graph Distance Complexity has been broken into multiple functions for clarity.
def graph_distance_complexity(graff):
    cdg = 0
    ev = nx.eccentricity(graff)
    nkv = gdc_get_nkv(graff)
    rvi = {}
    rg = 0

    for node in graff:
        rvi[node] = gdc_weighted_sum(nkv[node], ev[node])
        rg += gdc_weighted_sum(nkv[node], ev[node])
    for node in graff:
        vd = gdc_vertex_distance_comp(nkv[node], ev[node])
        cdg += (rvi[node] / rg) * vd
    return (-1) * cdg


def gdc_get_nkv(graff):
    radius_graph = {}
    for node in graff:
        rgi = nx.ego_graph(graff, node)
        radius_graph[node] = rgi.number_of_nodes()
    return radius_graph


def gdc_weighted_sum(nkv, ev):
    # nkv is the number of nodes within distance k of a given node,
    # ev is max distance from node to any other node
    rv = 0
    for k in range(1, ev+1):
        rv += k * nkv
    return rv


def gdc_vertex_distance_comp(nkv, ev):
    vd = 0
    for k in range(1, ev+1):
        rv = gdc_weighted_sum(nkv, ev)
        vd += nkv * (k / rv) * math.log2(k/rv)
    return vd


def total_walk_count(adj_mat, big_k):
    twc = 0
    n = adj_mat.shape[0]
    for k in range(1, big_k+1):
        adjm = numpy.linalg.matrix_power(adj_mat, k)
        for i in range(0, n):
            for j in range(0, n):
                twc += adjm[i, j]
    return twc


def topological_info_complexity(self):
    # Unlikely to be implemented - no polynomial time algorithm exists.
    return 0


# Both Frequency Information and Orbital Distribution measures implement the Shannon Diversity Measure.
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


def node_richness_measure(orbits):
    richness = {}
    for node in orbits:
        #for orb in node:
        orbset = set(orbits[node])
        num_orbits = len(orbset)
        richness[node] = num_orbits
    return richness

def node_orbit_relative_proportion(orbits):
    richness = node_richness_measure(orbits)
    orp = {}
    for node in richness:
        orp[node] = 0
        totorb = 0
        for n in richness:
            if richness[node] == richness[n]:
                totorb += 1
        orp[node] = totorb / richness[node]
    return orp


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


def total_richness_proportion(orbits):
    richness = node_richness_measure(orbits)
    global_richness = []
    richness_proportion = {}
    for x in richness:
        if richness[x] not in global_richness:
            global_richness.append(richness[x])
    global_richness.sort()
    for x in global_richness:
        for y in richness:
            if x == richness[y]:
                if x not in richness_proportion:
                    richness_proportion[x] = 1
                else:
                    richness_proportion[x] += 1
        richness_proportion[x] /= len(richness)
    return richness_proportion


def node_average_richness(orbits, graff, node_richness, n):
    richness = {}
    for node in orbits:
        # for orb in node:
        orbset = set(orbits[node])
        num_orbits = len(orbset)
        richness[node] = num_orbits

    average_richness = {}

    for node in graff:
        aver = node_richness[node]
        numNeigh = 1
        for neighbor in graff.neighbors(node):
            aver += node_richness[neighbor]
            numNeigh += 1
        average_richness[node] = aver / numNeigh
    return average_richness
