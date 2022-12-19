graph = {
  'A' : ['B','C','G'],
  'B' : ['A', 'C','D'],
  'C' : ['A','B','D','E'],
  'D' : ['B','C','F'],
  'E' : ['C','F','G'],
  'F' : ['D','E'],
  'G' : ['A','E']
}
visited = set()  
def DFS(visited, graph, node):
  if node not in visited:
    print(node, end=" ")
    visited.add(node)
    for neighbour in graph[node]:
      DFS(visited, graph, neighbour)
print("The Depth-First Search:")
DFS(visited, graph, 'A')                                          