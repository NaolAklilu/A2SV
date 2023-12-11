class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0 for _ in range(numCourses)]
        order = []
        
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        
        queue = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        
        while queue:
            curCourse = queue.popleft()
            order.append(curCourse)
            
            for neighbor in graph[curCourse]:
                indegree[neighbor] -= 1
                
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                
        if len(order) != numCourses:
            return False
        return True
    
    
        
        