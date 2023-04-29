while True:
    n = int(input())
    if n == 0:
        break
    edgeNumbers = int(input())
    graph = {}
    for i in range(1, n+1):
        graph[i] = []

    for _ in range(edgeNumbers):
        edge = list(map(int, input().split()))
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    color = [-1]*n
    color[0] = 0

    def dfs(graph, node,visited):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                color[neighbor-1] = 1-color[node-1]
                isPartite = dfs(graph, neighbor, visited)
                if isPartite == False:
                    return False
            else:
                if color[neighbor-1] != 1-color[node-1]:
                    return False
            
        return True
    
    isPartite = dfs(graph, 1, set())
    if isPartite:
        print("BICOLOURABLE.")
    else:
        print("NOT BICOLOURABLE.")
