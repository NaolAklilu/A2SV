class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        tree = defaultdict(list)
        heights = defaultdict(int)
        indegree = [0 for i in range(n)]
        visited = set()
        
        if len(edges) == 0:
            return [0]
        
        for source, des in edges:
            tree[source].append(des)
            tree[des].append(source)
          
        queue = deque()
        for i in range(n):
            indegree[i] = len(tree[i])
            
            if indegree[i] == 1:
                visited.add(i)
                queue.append(i)
            
        while queue:
            length = len(queue)
            if max(indegree) == 1:
                return queue
            
            for _ in range(length):
                node = queue.popleft()

                for neighbor in tree[node]:
                    indegree[neighbor] -= 1
                   
                    if neighbor not in visited:
                        if indegree[neighbor] <= 1:
                            visited.add(neighbor)
                            queue.append(neighbor)
           
        return []              
                    