class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        graph = defaultdict(list)
        colors = [0 for i in range(len(edges))]
        visited = set()
        
        def findCycle(node):
            if colors[node] == 1:
                return (True, 1, node)
            
            colors[node] = 1
            for neighbor in graph[node]:
                if colors[neighbor] == 2 or neighbor == -1:
                    continue
                isCycle, length, source = findCycle(neighbor)
                if isCycle:
                    colors[node] = 2
                    if source == node:
                        visited.add(node)
                        return True, length, source
                    else:
                        if source in visited:
                            return True, length, source
                        else:
                            return True, length+1, source
                
            colors[node] = 2
            return (False, 0, -10)

        
        for i in range(len(edges)):
            graph[i].append(edges[i])
            

        maxCycle = -1      
        for i in range(len(edges)):
            if colors[i] != 0:
                continue
            
            isCycle, length, node = findCycle(i)
            if isCycle:
                maxCycle = max(maxCycle, length)
            
        
        return maxCycle
