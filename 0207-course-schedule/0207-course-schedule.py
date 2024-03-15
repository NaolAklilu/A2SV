class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegrees = defaultdict(int)

        for a, b in prerequisites:
            graph[b].append(a)
            indegrees[a] += 1

        queue = deque([i for i in range(numCourses) if indegrees[i] == 0])

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)

        return all(x == 0 for x in indegrees.values())