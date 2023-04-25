class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        
        graph = defaultdict(list)
        result = [0 for i in range(n)]
        
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        
        def dfs(node, parent):
            curDic = defaultdict(int)
            curDic[labels[node]] = 1
            for neighbor in graph[node]:
                if neighbor != parent:
                    res = dfs(neighbor, node)
                    for label in res:
                        curDic[label] += res[label]
            
            result[node] = curDic[labels[node]]
            
            return curDic

        
        dfs(0, -1)
        
        return result
                
            
                
            