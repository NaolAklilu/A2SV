class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        directions = [(1, 0), (0, 1)]
        nRows = len(obstacleGrid)
        nCols= len(obstacleGrid[0])
        visited = {}
        
        
        def inBound(row, col):
            return 0<=row<nRows and 0<=col<nCols
        
        def dfs(row, col):
            if row == nRows-1 and col == nCols-1:
                if obstacleGrid[row][col] == 1:
                    return 0
                
                visited[(row, col)] = 1
                return visited[(row, col)]
            
            if obstacleGrid[row][col] == 1:
                visited[(row, col)] = 0
                return visited[(row, col)]
            
            count = 0
            for r, c in directions:
                if inBound(r+row, c+col):
                    if (r+row, c+col) not in visited:
                        visited[(r+row, c+col)] = dfs(r+row, c+col)
                    count += visited[(r+row, c+col)]
                    
            return count
        
        return dfs(0, 0)
                
            