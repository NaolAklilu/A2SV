class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        colors = [0 for _ in range(numCourses)]
        orders = []
        
        for course, req in prerequisites:
            graph[req].append(course)
            
        def dfs(course):
            colors[course] = 1
            
            for pre in graph[course]:
                if colors[pre] == 2:
                    continue
                elif colors[pre] == 1:
                    return False
                else:
                    if not dfs(pre):
                        return False
                    
            orders.append(course)
            colors[course] = 2
            return True
        
        for course in range(numCourses):
            if colors[course] == 0:
                if not dfs(course):
                    return []
                
        if len(orders) != numCourses:
            return []
        return orders[::-1]
                