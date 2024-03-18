class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = [False] * n
        
        def dfs(node):
            if node < 0 or node >= n or visited[node]:
                return False
            
            if arr[node] == 0:
                return True
            
            visited[node] = True
            
            return dfs(node + arr[node]) or dfs(node - arr[node])
        
        return dfs(start)