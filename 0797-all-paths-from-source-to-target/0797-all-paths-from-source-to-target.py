class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        ans = []
        # adjacencyList = defaultdict(list)
        # for node1, node2 in graph:
        #     adjacencyList[node1].append(node2)
            
            
        def pathFinding(node, arr):
            curArray = arr[:]
            curArray.append(node)
            if node == len(graph)-1:
                ans.append(curArray)
                return
                
            for neighbor in graph[node]:
                pathFinding(neighbor, curArray)
            
            return
        
        
        pathFinding(0, [])
        return ans
            
                
            