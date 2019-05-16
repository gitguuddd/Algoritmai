# Kruskal_c++ by Mindaugas Kasiulis
## Funkcijos

- ```AddWeightedEdge``` adds a single weighted edge to the initial tree ```G```
- ```find_set``` finds the representative of the set, to which the verticle belongs
- ```union_set``` adds both verticles to the same set by equalizing their representatives
- ```kruskal``` generates a mst by using sorting the edges from lightest to heaviest, ```find_set``` and ```union_set``` functions
- ```print``` prints out the edges of the mst and their respective edges