class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        validPoints = []
        for point in points:
            if point[0] == x or point[1] == y:
                validPoints.append(point)
        
        if len(validPoints) == 0:
            return -1
        
        mahDistance = abs(x - validPoints[0][0]) + abs(y - validPoints[0][1])
        resPointIndex = points.index(validPoints[0])
        if len(validPoints) == 1:
            return resPointIndex
        
        for index, point in enumerate(validPoints, 0):
            curMahDistance = abs(x - point[0]) + abs(y - point[1])
            if curMahDistance < mahDistance:
                mahDistance = curMahDistance
                resPointIndex = points.index(point)
                
        return resPointIndex