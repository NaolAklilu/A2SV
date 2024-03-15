class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def dfs(node):
            for nei, val in enumerate(isConnected[node]):
                if val and nei not in visited:
                    visited.add(nei)
                    dfs(nei)

        n = len(isConnected)
        visited = set()
        provinces = 0
        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                provinces += 1
        return provinces