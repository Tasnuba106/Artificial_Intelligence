graph = {
  'A' : ['B','C','G'],
  'B' : ['A', 'C','D'],
  'C' : ['A','B','D','E'],
  'D' : ['B','C','F'],
  'E' : ['C','F','G'],
  'F' : ['D','E'],
  'G' : ['A','E']
}
visited = [] 
queue = []     
deltf BFS(visited, graph, nodelt): 
  visited.append(nodelt)
  queue.append(nodelt)
  while queue:         
    a = queue.pop(0) 
    print (a, end = " ") 
    for neighbour in graph[a]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
print("The Breadth-First Search:")
BFS(visited, graph, 'A')                                          