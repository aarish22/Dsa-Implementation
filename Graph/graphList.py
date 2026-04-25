class Graph:
  def __init__(self):
    self.adj_list = {}
    
  def add_vertex(self, vertex):
    if vertex not in self.adj_list:
      self.adj_list[vertex] = []
      
  def addEdge(self, src, dest):
    self.add_vertex(src)
    self.add_vertex(dest)
    
    self.adj_list[src].append(dest)
    self.adj_list[dest].append(src)
    
  def print_graph(self):
    for vertex in self.adj_list:
      print(vertex, "->", self.adj_list[vertex])
      


graph = Graph()
graph.addEdge("A", "B")
graph.addEdge("A", "C")
graph.addEdge("B", "D")
graph.addEdge("C", "D")

graph.print_graph()