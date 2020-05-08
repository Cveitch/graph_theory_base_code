# ComplexityMeasurer.py
# Conan Veitch, 2020-05-06
#
# Description: 
#
import math
from collections import Counter


def vertex_degree_info_measure(self):
    return 0


def complexity_b(self):
    return 0


def graph_distance_complexity(self):
    return 0


def total_walk_count(self):
    return 0


def topological_info_complexity(self):
    return 0


def shannon_diversity_measure(freq):
    total_freq = 0
    for nodes in freq:
        total_freq += freq[nodes]
    h_gam = 0
    for nodes in freq:
        if freq[nodes] != 0:
            freq_prop = freq[nodes] / total_freq
            h_gam += freq_prop * math.log2(freq_prop)
    return (-1) * h_gam


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
