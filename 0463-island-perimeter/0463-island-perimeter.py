class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        visited = set()
        
        def inBound(row, col):
            return (0<=row<len(grid) and 0<=col<len(grid[0]))
        
        self.count = 0
        self.boundary = 0
        
        def dfs(row, col):
            visited.add((row, col))
            if grid[row][col] == 1:
                self.count += 1
                
                for newRow, newCol in directions:
                    curRow = row + newRow
                    curCol = col + newCol                    
                    
                    if inBound(curRow, curCol):
                        if grid[curRow][curCol] == 1:
                            self.boundary += 1
                            
                        if (row, col) not in visited:
                            dfs(curRow, curCol)
                        
            return
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in visited:
                    dfs(r, c)
        
        return (self.count*4)-self.boundary
                        