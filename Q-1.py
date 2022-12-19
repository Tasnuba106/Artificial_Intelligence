graph = {
  'A' : ['B','C','D'],
  'B' : ['A', 'C','D','E'],
  'C' : ['A','B','E','G'],
  'D' : ['A','B','E','F'],
  'E' : ['B','C','D','F','G'],
  'F' : ['D','E','G','B'],
  'G' : ['C','E','F']
}
visited = set() 
def dfs(visited, graph, node): 
    if node not in visited:
        print (node, end = " ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
print("The Depth-First Search:")
dfs(visited, graph, 'A')                                       