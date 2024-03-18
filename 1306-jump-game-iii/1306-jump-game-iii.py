class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = [False] * n
        queue = deque([start])
        visited[start] = True
        
        while queue:
            node = queue.popleft()
            
            if arr[node] == 0:
                return True
            
            if node + arr[node] < n and not visited[node + arr[node]]:
                queue.append(node + arr[node])
                visited[node + arr[node]] = True
            
            if node - arr[node] >= 0 and not visited[node - arr[node]]:
                queue.append(node - arr[node])
                visited[node - arr[node]] = True
        
        return False