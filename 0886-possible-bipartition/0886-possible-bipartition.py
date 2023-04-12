class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        groups = [-1 for i in range(n)]
        groups[0] = 1
        
        graph = defaultdict(list)
        for node1, node2 in dislikes:
            graph[node1].append(node2)
            graph[node2].append(node1)
            
        
        def bipartite(node):
            for neighbor in graph[node]:
                if groups[neighbor-1] == -1:
                    groups[neighbor-1] = 1 - groups[node-1]
                    bipartite(neighbor)
                
                else:
                    if groups[neighbor-1] == groups[node-1]:
                        return False
                    
                
                        
            return True
        
        for i in range(1,n+1):
            result = bipartite(i)
            if result == False:
                return False
            
        return True
            
                    
        
         
            
        
        
        return True