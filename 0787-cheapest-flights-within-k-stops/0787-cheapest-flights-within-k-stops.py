class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for start, dest, price in flights:
            graph[start].append((dest, price))
            
        queue = []
        queue.append((0, 0, src))
        visited = defaultdict(int)
        visited[src] = 0
        
        while queue:
            count, cost, node = heappop(queue)
            if count > k:
                break
            
            for neighbor, price in graph[node]:
                if neighbor not in visited or visited[neighbor] > cost + price:
                    visited[neighbor] = cost + price
                    heappush(queue, (count+1, cost+price, neighbor))
        
        if dst in visited:
            return visited[dst]
        return -1
                    
            
            