class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        graph = defaultdict(list)
        isReachable = [[False for _ in range(numCourses)] for _ in range(numCourses)]
        
        for pre, course in prerequisites:
            graph[course].append(pre)
        
        def bfs(index):
            queue = deque()
            queue.append(index)
            visited = set()
            
            while queue:
                course = queue.popleft()
                isReachable[index][course] = True
                visited.add(course)
                
                for pre in graph[course]:
                    if pre not in visited:
                        queue.append(pre)
                        
        for i in range(numCourses):
            bfs(i)
        
        result = []
        for pre, course in queries:
            result.append(isReachable[course][pre])
            
        return result