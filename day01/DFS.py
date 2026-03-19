def dfs(graph, start):
    visited = set()
    order = []

    def _dfs(node):
        visited.add(node)
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                _dfs(neighbor)

    _dfs(start)
    return order

graph = {
    'A' : ['B','C'],
    'B' : ['A','D'],
    'C' : ['A','D'],
    'D' : ['B','C','E'],
    'E' : ['D']
}

result = dfs(graph,'A')
print('방문 순서: ', result)