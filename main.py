#importing networkx
import networkx as nx
 
#importing matplotlib.pyplot
import matplotlib.pyplot as plt
import numpy  as np


edgelist = [(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]
#Create a Graph
# G=nx.from_numpy_array(np.array([[0,1,0],
#                                 [1,1,1],
#                                  [0,0,0]]))

G = nx.Graph()
# or we have the second method
# G=nx.from_edgelist(edgelist)

# or we can also do
# G=nx.Graph()
G.add_edges_from(edgelist)


#print(nx.adjacency_matrix(G))



#add edges
# G.add_edge(1,2)
# G.add_edge(2,3 , weight=0.9 )
# G.add_edge("A","B")
# G.add_edge("B","B")


#add a node
# G.add_node("C")
# G.ads_node(print)

nx.draw_cirlcular(G, with_labels=True)
plt.show()

# nx.draw_circular(G, with_labels=True)
# plt.show()

# nx.draw_shell(G, with_labels=True)
# plt.show()

# nx.draw_spectral(G, with_labels=True)
# plt.show()

# nx.draw_random(G, with_labels=True)
# plt.show()

# nx.draw_planar(G, with_labels=True)
# plt.show()

#Degree of nodes
print(dict(G.degree))

#Degree of a specific node
print(dict(G.degree)[2])


#To create a direct graph
#             