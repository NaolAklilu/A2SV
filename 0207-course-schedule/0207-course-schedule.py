class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        course_pre = defaultdict(list)
        indegree = [0 for _ in range(numCourses)]
        orders = []
        
        for course, pre in prerequisites:
            course_pre[pre].append(course)
            indegree[course] += 1
            
        queue = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
                
        while queue:
            course = queue.popleft()
            orders.append(course)
            
            for pre in course_pre[course]:
                indegree[pre] -= 1
                
                if indegree[pre] == 0:
                    queue.append(pre)
        
        if len(orders) != numCourses:
            return False
        
        return True
        