class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        
        def getAreaOfIsland(row, col):
            grid[row][col] = 0
            area = 1
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                
                if inbound(new_row, new_col) and grid[new_row][new_col] == 1:
                    area += getAreaOfIsland(new_row, new_col)
                    
            return area
                    
            
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    area = getAreaOfIsland(row, col)
                    maxArea = max(maxArea, area)
                    
        return maxArea
                        
                    