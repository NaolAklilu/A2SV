class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []            
            
        def pathFinding(node, arr):
            curArray = arr[:]
            curArray.append(node)
            if node == len(graph)-1:
                paths.append(curArray)
                return
                
            for neighbor in graph[node]:
                pathFinding(neighbor, curArray)
            
            return
        
        pathFinding(0, [])
        return paths
            
                
            