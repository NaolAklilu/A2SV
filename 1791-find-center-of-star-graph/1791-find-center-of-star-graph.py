class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:        
        edge1 = edges[0]
        edge2 = edges[1]
        
        if edge1[0] == edge2[0]:
            return edge1[0]
        elif edge1[0] == edge2[1]:
            return edge1[0]
        elif edge1[1] == edge2[0]:
            return edge1[1]
        else:
            return edge1[1]
            