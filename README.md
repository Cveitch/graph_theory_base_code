# graph_theory_base_code
Code base for graph theory work

Package designed for research into graphlets and graph complexity algorithms,
should be general enough for anything beyond that.

##Early notes:
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
   
   ![Edge list graph](https://github.com/Cveitch/graph_theory_base_code/blob/master/graphal/graphal_tests/adj_matrix_graph_example.png)
   