from collections import deque

graph = {
   'A' : ['B','C'],
   'B' : ['D', 'E'],
   'C' : ['A'],
   'D' : [],
   'E' : ['F'],
   'F' : ['A', 'B']
}

def bfs(graph, node):
   visited = []
   queue = deque()

   visited.append(node)
   queue.append(node)

   # nested looping
   while queue:
      removed_node = queue.popleft()
      print(removed_node, end=",")

      for nd in graph:
         if nd not in visited:
            visited.append(nd)
            queue.append(nd)
   
   return visited

visited = bfs(graph, 'C')
print(visited)