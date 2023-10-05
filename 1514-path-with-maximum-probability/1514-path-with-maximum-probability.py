class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        graph = defaultdict(list)
        for i in range(len(edges)):
            start, end = edges[i]
            val = succProb[i]
            
            graph[start].append((val, end))
            graph[end].append((val, start))

        visited = set()
        success = [-1*float(inf) for i in range(n)]
        success[start_node] = 0
        queue = [(0, start_node)]
        
        while queue:
            val, node = heappop(queue)
            if node in visited:
                continue
                
            visited.add(node)
            
            for succVal, neighbor in graph[node]:
                curVal = succVal
                if val != 0:
                    curVal = succVal * -1*val
                    
                if curVal > success[neighbor]:
                    success[neighbor] = curVal
                    heappush(queue, (-1*curVal, neighbor))
        
        if success[end_node] == -1*float(inf):
            return 0
        return success[end_node]
            