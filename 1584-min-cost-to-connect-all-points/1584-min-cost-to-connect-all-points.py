class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        parent = {}
        rank = {}
        
        def find(point):
            if point == parent[point]:
                return point
            
            parent[point] = find(parent[point])
            return parent[point]
        
        def union(p1, p2, cost):
            p1Rep = find(p1)
            p2Rep = find(p2)
            
            if p2Rep != p1Rep:
                if rank[p1Rep] > rank[p2Rep]:
                    parent[p2Rep] = p1Rep
                    rank[p1Rep] += rank[p2Rep]
                    
                else:
                    parent[p1Rep] = p2Rep
                    rank[p2Rep] += rank[p1Rep]
                    
                return cost
            
            return 0
        
        for xCoord, yCoord in points:
            parent[(xCoord, yCoord)] = (xCoord, yCoord)
            rank[(xCoord, yCoord)] = 1
            
        pairs = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                distance = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                pairs.append([tuple(points[i]), tuple(points[j]), distance])

        pairs.sort(key=lambda x:x[2])
        
        totalCost = 0
        for p1, p2, cost in pairs:
            totalCost += union(p1, p2, cost)
        
        return totalCost
                
            
        