# graph_theory_base_code
Code base for graph theory work

Package designed for research into graphlets and graph complexity algorithms,
should be general enough for anything beyond that.

# Early notes:
graffal is intended to be used with white space delimited files.
There are three types of file that will create a graph using this program:
1) An edge list,
    ```
    a b
    a c
    b e
    b h
    b c
    c g
    e h
    f g
    g h
   ```
   will produce the following graph:
   
   ![Edge list graph](https://github.com/Cveitch/graph_theory_base_code/blob/master/graffal/graffal_tests/edge_list_graph_example.png)
   
2) An adjacency list,
    ```
   a b d
    b a c
    c b d
    d b c g
    e h
    f h g
    g d f
    h e i
    i h
    ```
   will produce the following graph:
   
   ![Edge list graph](https://github.com/Cveitch/graph_theory_base_code/blob/master/graffal/graffal_tests/adj_list_graph_example.png)
   
   3) Or an adjacency matrix,
    ```
    * a b c d
    a 0 1 0 1
    b 1 0 1 0
    c 0 1 0 1
    d 1 0 1 0
    ```
   will produce the following graph:
   
   ![Edge list graph](https://github.com/Cveitch/graph_theory_base_code/blob/master/graffal/graffal_tests/adj_matrix_graph_example.png)
   
Graffal can write these visualizations to file - the file name and extension
type is up to the user.  Default name is temp, default extension is .png.
The file will be written to graffal/graffal_tests/.
   
## Graphlets
Graphlets are connected induced subgraphs of a graph, each of which has been 
enumerated by researchers as below:
![Edge list graph](https://github.com/Cveitch/graph_theory_base_code/blob/master/graffal/documentation/assets/graphlets.png)

(Pržulj, 2007)

Given a "graff" object G, graffal can generate all n-node graphlets from G.  
With this graffal can count the frequency of each graphlet occuring in G.

Alternatively, graffal can count how many graphlet automorphism orbits each
node of G takes part in.


## Complexity Measures
Measures to gauge the complexity of a graph are widespread and varied.
Graffal implements the following measures of complexity:

- **The Vertex Degree Information Measure**

    Measure based on each nodes vertex degree.
    
- **The Complexity B Measure**

    Measure based on the proportion of vertex degree to inter-node distance row and column totals.
    
- **The Graph Distance Complexity Measure**

    Measure based on the weighted sum of vertex distance complexities of individual nodes.
    
- **The Total Walk Count**

    Measures the total number of all k-walks, k-1 walks, ... 1-walks.
    
### Graphlet Complexity Measures
The following measures gauge the complexity of a graph by using information derived from its graphlets.

- **Graphlet Frequency Information**

    Measure based on the frequency counts of the graphlets.
    
- **Graphlet Orbit Distribution Information**

    Measure based on the counts of nodes in all possible graphlet automorphism orbits.
    
- **Local Node Complexity Measure**

    Evaluates the complexity of a graph by measuring the complexity of each of it's nodes orbit diversity.