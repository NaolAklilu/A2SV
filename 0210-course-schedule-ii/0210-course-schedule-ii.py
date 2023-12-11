class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0 for _ in range(numCourses)]
        orders = []
        
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
            
        queue = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
                
        while queue:
            curCourse = queue.popleft()
            orders.append(curCourse)
            
            for pre in graph[curCourse]:
                indegree[pre] -= 1
                
                if indegree[pre] == 0:
                    queue.append(pre)
                    
        if len(orders) != numCourses:
            return []
        return orders
        
        