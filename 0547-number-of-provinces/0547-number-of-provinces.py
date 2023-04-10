class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        count = 0
        
        def dfs(node):
            visited.add(node)
            for neighbor in dic[node]:
                if neighbor not in visited:
                    dfs(neighbor)   
            return
        
        
        dic = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1:
                    dic[i+1].append(j+1)
                    
        for num in dic.keys():
            if len(dic[num]) > 0:
                if num not in visited:
                    count += 1
                    dfs(num)
                
        return count