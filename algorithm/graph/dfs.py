

graph = {
   'A' : ['B','C'],
   'B' : ['D', 'E'],
   'C' : ['F'],
   'D' : [],
   'E' : ['F'],
   'F' : ['A','C','D']
}

def dfs(graph, start):
   visited = []
   stack = []

   visited.append(start)
   stack.append(start)

   while stack:
      stack.pop()

      for nd in graph:
         if nd not in visited:
            visited.append(nd)
            stack.append(nd)

   return visited

print(dfs(graph, 'A'))