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
      
  