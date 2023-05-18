class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parent = { node: node for node in range(1, n+1)}
        size = { node: 1 for node in range(1, n+1)}
        minimum = { node: float(inf) for node in range(1, n+1)}
        
        def find(node):
            if parent[node] == node:
                return node
            
            nodeParent = find(parent[node])
            parent[node] = nodeParent
                
            return nodeParent
        
        def union(node1, node2, cost):
            node1Rep = find(node1) 
            node2Rep = find(node2)
            size1 = size[node1Rep]
            size2 = size[node2Rep]
            
            if size1 >= size2:
                parent[node2Rep] = node1Rep
                size[node1Rep] += size2
                size[node2Rep] 
                minimum[node1Rep] = min(cost, min(minimum[node1Rep], minimum[node2Rep]))

            else:
                parent[node1Rep] = node2Rep
                size[node2Rep] += size1
                size[node1Rep] = 1
                minimum[node2Rep] = min(cost, min(minimum[node1Rep], minimum[node2Rep]))

            
        for edge in roads:
            union(edge[0], edge[1], edge[2])
            
        sourceParent = find(1)
        destinationParent = find(n)
            
        return minimum[sourceParent]