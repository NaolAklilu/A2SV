class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parent = { node:node for node in range(1, len(edges)+1)}
        rank = {node:1 for node in range(1, len(edges)+1)}
        
        def find(node):
            if node == parent[node]:
                return node
            
            parent[node] = find(parent[node])
            return parent[node]
        
        
        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)
            
            if root1 != root2:
                if rank[root1] > rank[root2]:
                    parent[root2] = root1
                    rank[root1] += rank[root2]
                else:
                    parent[root1] = root2
                    rank[root2] += rank[root1]
        
        
        result = []
        for node1, node2 in edges:
            if find(node1) == find(node2):
                result = [node1, node2]
            else:
                union(node1, node2)
        
        return result