class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
       
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]

        for pair in prerequisites:
            x, y = pair
            graph[x].append(y)

        def is_cyclic(v, visited, stack):
            visited[v] = 1
            stack[v] = 1

            for neighbor in graph[v]:
                if visited[neighbor] == 0 and is_cyclic(neighbor, visited, stack) == True:
                    return True
                elif stack[neighbor] == 1:
                    return True

            stack[v] = 0
            return False

        for v in range(numCourses):
            if visited[v] == 0:
                if is_cyclic(v, visited, [0]*numCourses) == True:
                    return False

        return True