import networkx as nx
import matplotlib.pyplot as plt


Graph = nx.DiGraph()

Graph.add_node(1)
Graph.add_node(2)
Graph.add_node(3)

Graph.add_edge(1, 2, weight=2)
Graph.add_edge(2, 3, weight=2)
Graph.add_edge(3, 1, weight=2)

labels = nx.get_edge_attributes(Graph, 'weight')
nx.draw(Graph, with_labels=True, arrows=True)
nx.draw_networkx_edge_labels(Graph, pos=nx.spring_layout(Graph), edge_labels=labels)
plt.show()