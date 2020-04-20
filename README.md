# graph_theory_base_code
Code base for graph theory work

Package designed for research into graphlets and graph complexity algorithms,
should be general enough for anything beyond that.

#Early notes:
graphal is intended to be used with white space delimited files.
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
   
   ![Edge list graph](https://github.com/Cveitch/graph_theory_base_code/blob/master/graphal/graphal_tests/edge_list_graph_example.png)
   
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
   
   ![Edge list graph](https://github.com/Cveitch/graph_theory_base_code/blob/master/graphal/graphal_tests/adj_list_graph_example.png)
   
   3) Or an adjacency matrix,
    ```
    * a b c d
    a 0 1 0 1
    b 1 0 1 0
    c 0 1 0 1
    d 1 0 1 0
    ```
   will produce the following graph:
   
   ![Edge list graph](https://github.com/Cveitch/graph_theory_base_code/blob/master/graphal/graphal_tests/adj_matrix_graph_example.png)
   
   
