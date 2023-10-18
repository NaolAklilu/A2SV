class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = {num:num for num in range(1, n+1)}
        rank = {num:1 for num in range(1, n+1)}
        
        def find(num):
            if num != parent[num]:
                parent[num] = find(parent[num])
            return parent[num]
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            
            if p1 != p2:
                if rank[p1] >= rank[p2]:
                    parent[p2] = p1
                    rank[p1] += rank[p2]
                else:
                    parent[p1] = p2
                    rank[p2] += rank[p1] 
            
        for row in range(n):
            for col in range(n):
                if isConnected[row][col] == 1:
                    union(row+1, col+1)
                    
        parents = set()
        for num in parent:
            parents.add(find(num))
        
        return len(parents)