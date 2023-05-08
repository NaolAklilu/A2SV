class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        colors = [0 for _ in range(len(graph))]
        order = [] 
        
        def topSort(node, colors, order):
            if colors[node] == 1:
                return False
            colors[node] = 1
            for neighbor in graph[node]:
                if colors[neighbor] == 2:
                    continue
                if not topSort(neighbor, colors, order):
                    return False
            
            colors[node] = 2
            order.append(node)
            return True
        
        for node in range(len(graph)):
            if colors[node] != 0:
                continue
                
            topSort(node, colors, order)
                
        return sorted(order)
            
            
        