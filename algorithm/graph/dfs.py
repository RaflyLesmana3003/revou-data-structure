

graph = {
   'A' : ['B','C'],
   'B' : ['D', 'E'],
   'C' : ['F'],
   'D' : [],
   'E' : ['F'],
   'F' : ['A','C','D']
}

# O(n^2)
def dfs(graph, start):
   visited = [] # O(1)
   stack = [] # O(1)

   visited.append(start) # O(n)
   stack.append(start) # O(n)

   while stack: # O(n)
      stack.pop() # O(1)

      for nd in graph:  # O(n^2)
         if nd not in visited: # O(1)
            visited.append(nd) # O(n)
            stack.append(nd) # O(n)

   return visited # O(1)



print(dfs(graph, 'A'))