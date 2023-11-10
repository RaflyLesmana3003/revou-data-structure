import networkx as nx

Graph = nx.Graph()

Graph.add_node("KOTA A")
Graph.add_node("KOTA B")
Graph.add_node("KOTA C")
Graph.add_node("KOTA D")
Graph.add_node("KOTA E")
Graph.add_node("KOTA F")

Graph.add_edge("KOTA A", "KOTA B", weight=2)
Graph.add_edge("KOTA A", "KOTA C", weight=5)
Graph.add_edge("KOTA B", "KOTA D", weight=4)
Graph.add_edge("KOTA C", "KOTA D", weight=3)
Graph.add_edge("KOTA C", "KOTA E", weight=1)
Graph.add_edge("KOTA D", "KOTA E", weight=2)

# find shortest path from source node to all other node
source_node = "KOTA A"
shortest_path = nx.single_source_dijkstra(Graph, source_node)

for target_node, distance in shortest_path[0].items():
   print(f"shortest path from {source_node} to {target_node} : {shortest_path[1][target_node]} with distance {distance}")


shortest_path_dijkstra = nx.dijkstra_path(Graph, source_node, "KOTA E")

print(shortest_path_dijkstra)