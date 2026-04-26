class Graph:
  def __init__(self, vertex):
    self.matrix = [[0]*vertex for _ in range(vertex)]
    self.size = vertex
    
  def add_edge(self, src, dest): ## weight
    if (src >= self.size or dest >= self.size):
      print("Invalid edge")
    else:
      self.matrix[src][dest] = 1
      self.matrix[dest][src] = 1
      

  def print_graph(self):
     for row in self.matrix:
       print(' '.join(map(str,row)))
      
      
  def dfs(self, src):
    visited = [False]*self.size
    stack = [src]
    
    while stack:
      vertex = stack.pop()
      
      if visited[vertex] == False:
         print(vertex, end="->")
         visited[vertex] = True
         
      for i in (self.size-1):
        if self.matrix[vertex][i] == 1 and visited[i] == False:
          stack.append(i)