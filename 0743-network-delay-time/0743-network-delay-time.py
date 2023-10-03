class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for start, end, weight in times:
            graph[start].append((end, weight))
        
        
        distances = {node:float(inf) for node in range(1, n+1)}
        distances[k] = 0
        visited = set()
        
        queue = []
        queue.append((0, k))
        
        while queue:
            distance, node = heappop(queue)
            
            if node in visited:
                continue
            
            visited.add(node)
            
            for neighbor, weight in graph[node]:
                curDistance = weight + distance
                if distances[neighbor] > curDistance:
                    distances[neighbor] = curDistance
                    heappush(queue, (curDistance, neighbor))
        
        maxTime = max(distances.values())
        if maxTime == float(inf):
            return -1
        return  maxTime