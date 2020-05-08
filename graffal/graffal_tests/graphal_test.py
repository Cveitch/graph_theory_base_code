# graphal_test.py
# Conan Veitch, 4/18/2020
#
# Description: Test cases for graffal project.
#


import graffal.graff_gen.GraffWrapper as gmake
import graffal.grafflet_gen.GraffletWrapper as gwrap
import graffal.grafflet_gen.GraffletCounter as gcounter

cgr = "test_edge.csv"
G = gmake.GraffWrapper(cgr)
gwrapper = gwrap.GraphletWrapper(G.get_graff())

# n = 4
# gcount = gcounter.GraffletCounter(G.get_graff(), n)
#
# print(*gcount.grafflet_edges, sep="\n")
# print("There are:", gcount.grafflet_count, "total", n, "node graphlets.")
#




print("Graphlets edge list:")
print(*gwrapper.get_grafflet_edges(), sep="\n")

for i in range(2, 6):
    print("There are:", gwrapper.grafflet_count[i], "total", i, "node graphlets.")

for node, freq in gwrapper.get_grafflet_freq().items():
    print("Graphlet", node, "has frequency:", freq)

for node, orb in gwrapper.get_orbit_counts().items():
    print("Node", node, "has orbits:", orb)

G.draw_graff()

#print(gcount.orbit_counts, sep="\n")

#print(*gcount.orbit_counts, sep="\n")
#print(graflet.get_node_orbit(4))

#This is how we get nodes from graffs
#print(list(graf.G.nodes())[8])

#graf.G.degree[0]
