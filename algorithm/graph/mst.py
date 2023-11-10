import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

G.add_nodes_from(nodes) 

edges = [
   ("A", "B", 3),
   ("A", "C", 4),
   ("B", "C", 2),
   ("B", "D", 5),
   ("B", "D", 1),
   ("B", "E", 6),
   ("C", "D", 2),
]

G.add_weighted_edges_from(edges)

mst = nx.minimum_spanning_tree(G)

nx.draw(mst, with_labels=True, arrows=True)
labels = nx.get_edge_attributes(mst, 'weight')

plt.figure()  # Create a new figure
nx.draw_networkx_edge_labels(G, pos=nx.spring_layout(G), edge_labels=labels)
plt.show()