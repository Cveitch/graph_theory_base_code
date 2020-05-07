# graphal_test.py
# Conan Veitch, 4/18/2020
#
# Description: Test cases for graffal project.
#


import graffal.graff_gen.CSVGraffReader as csvgr
import graffal.graff_gen.UndirectedGraff as ugraff
import graffal.grafflet_gen.GraffletCounter as gcounter
import graffal.graff_gen.GraffWriter as gwrite


graf = ugraff.UndirectedGraff()

cgr = csvgr.CSVGraffReader('adj_list_csv.csv')
graf.build_from_adj_list(cgr.csv_to_adj_list())

n = 5
gcount = gcounter.GraffletCounter(graf.G, n)
print(n, "node graphlets edge list:")
print(*gcount.grafflet_edges, sep="\n")
print("There are:", gcount.grafflet_count, "total", n, "node graphlets.")

for node, orb in gcount.orbit_counts.items():
    print("Node", node, "has orbits:", orb)

for node, freq in gcount.grafflet_freq.items():
    print("Graphlet", node, "has frequency:", freq)

gwriter = gwrite.GraffWriter(graf)
gwriter.graff_to_file()
gwriter.plot_graff()



# cgr = csvgr.CSVGraffReader('edge_list_csv.csv')
# graf.build_from_edge_list(cgr.csv_to_edge_list())



#cgr = csvgr.CSVGraffReader('adj_mat_csv.csv')
#graf.build_from_adj_matrix(cgr.csv_to_adj_matrix())



#graflet = grflt.Grafflet(27)


#print(gcount.orbit_counts, sep="\n")

#print(*gcount.orbit_counts, sep="\n")
#print(graflet.get_node_orbit(4))

#This is how we get nodes from graffs
#print(list(graf.G.nodes())[8])

#graf.G.degree[0]

