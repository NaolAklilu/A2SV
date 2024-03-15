class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegrees = defaultdict(int)
        for a, b in prerequisites:
            graph[b].append(a)
            indegrees[a] += 1

        queue = deque([i for i in range(numCourses) if indegrees[i] == 0])
        result = []

        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)

        if len(result) != numCourses:
            return []
        else:
            return result