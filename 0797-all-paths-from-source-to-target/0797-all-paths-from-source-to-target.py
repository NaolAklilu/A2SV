class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        
        def dfs(node, arr):
            curArray = arr[:]
            curArray.append(node)
            
            if node == len(graph)-1:
                ans.append(curArray)
                return
            
            for neighbor in graph[node]:
                dfs(neighbor, curArray)
            
        dfs(0, [])
        return ans