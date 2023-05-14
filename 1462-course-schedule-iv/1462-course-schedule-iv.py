class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        course_pre = defaultdict(list)
        indegree = defaultdict(int)
        allPrerequisites = defaultdict(set)
        
        for pre, course in prerequisites:
            course_pre[pre].append(course)
            allPrerequisites[course].add(pre)
            indegree[course] += 1
            
        queue = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
            
        while queue:
            pre = queue.popleft()
            
            for course in course_pre[pre]:
                indegree[course] -= 1
                allPrerequisites[course].update(allPrerequisites[pre])
                
                if indegree[course] == 0:
                    queue.append(course)

        result = []
        for query in queries:
            if query[0] in allPrerequisites[query[1]]:
                result.append(True)
            else:
                result.append(False)
        
        return result
                
        