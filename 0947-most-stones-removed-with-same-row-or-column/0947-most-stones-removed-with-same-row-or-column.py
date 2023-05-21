class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {}
        size = {}
        for xCor, yCor in stones:
            parent[(xCor, yCor)] = (xCor, yCor)
            size[(xCor, yCor)] = 0
            
        def find(cord):
            if cord == parent[cord]:
                return cord
            
            parent[cord] = find(parent[cord])
            return parent[cord]
        
        def union(coord1):
            coordParent = find(coord1)
            neighborCoord = None
            for coord in parent:
                if coord == coord1:
                    continue
                    
                if coord[0]==coord1[0] or coord[1] == coord1[1]:
                    neighborCoord = coord
                    neighborParent = find(neighborCoord)

                    if neighborParent != coordParent:
                        if size[neighborParent] > size[coordParent]:
                            parent[coordParent] = neighborParent
                            if size[coordParent] == 0:
                                size[neighborParent] += 1
                            else:
                                size[neighborParent] += size[coordParent]
                        else:
                            parent[neighborParent] = coordParent
                            if size[neighborParent] == 0:
                                size[coordParent] += 1 
                            else:
                                size[coordParent] += size[neighborParent]
                                
        for stone in stones:
            union((stone[0], stone[1]))

        roots = set()
        for stone in stones:
            root = find((stone[0], stone[1]))
            roots.add(root)
        
        return len(stones)-len(roots)
        
                    
            
                    
            