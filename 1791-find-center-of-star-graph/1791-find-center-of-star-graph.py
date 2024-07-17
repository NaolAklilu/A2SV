class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        nodes = defaultdict(int)
        
        for start, end  in edges:
            nodes[start] += 1
            nodes[end] += 1
            
        for node in nodes:
            if nodes[node] > 1:
                return node