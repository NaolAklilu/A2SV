class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        sources = set()
        sinks = set()
        
        for edge in edges:
            sources.add(edge[0])
            sinks.add(edge[1])
            
        res = []
        for i in range(n):
            if i not in sinks:
                res.append(i)
        
        return res
        
        