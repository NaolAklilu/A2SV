class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        result = [ set() for _ in range(n)]
        queue = deque()
        
        for source, destination in edges:
            indegree[destination] += 1
            graph[source].append(destination)
            
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
                
        while queue:
            node = queue.popleft()
            
            for neighbor in graph[node]:
                result[neighbor].add(node)
                result[neighbor].update(result[node])
                indegree[neighbor] -= 1
                
                if indegree[neighbor] == 0:
                    queue.append(neighbor)               
        
        for i in range(n):
            result[i] = list(result[i])
            result[i].sort()
     
        return result
                    
                