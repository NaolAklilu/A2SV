class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        
        count = 0
        i = 0
        
        while i < len(points):
            count += 1
            curEnd = points[i][1]
            
            for j in range(i+1, len(points)):
                if points[j][0] > curEnd:
                    i = j
                    break 
            else:
                break
        
        return count