class Solution(object):
    def possibleBipartition(self, n, dislikes):
        """
        :type n: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(n+1)]
        colors = [0 for _ in range(n+1)]

        for dislike in dislikes:
            graph[dislike[0]].append(dislike[1])
            graph[dislike[1]].append(dislike[0])

        def dfs(node, color):
            colors[node] = color
            for neighbor in graph[node]:
                if colors[neighbor] == color:
                    return False
                if colors[neighbor] == 0 and not dfs(neighbor, -color):
                    return False
            return True

        for node in range(1, n+1):
            if colors[node] == 0 and not dfs(node, 1):
                return False

        return True