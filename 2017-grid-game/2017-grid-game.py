class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        length = len(grid[0])
        prefixGrid = [[0]*length for _ in range(2)]
        
        for j in range(2):
            for i in range(length-1,-1,-1):
                if length-1 == i:
                    prefixGrid[j][i] = grid[j][i]
                else:
                    prefixGrid[j][i] = grid[j][i] + prefixGrid[j][i+1]
               
            
        x, y = 0, 0
        prefixGrid[y][x] = 0
        while x < length:
            if y == 0:
                if x == length-1:
                    prefixGrid[y][x] = 0
                    grid[y][x] = 0
                    y += 1
                    
                elif prefixGrid[y][x] >= (prefixGrid[1][0] - prefixGrid[1][x]) and prefixGrid[y][x+1] < (prefixGrid[1][0] - prefixGrid[1][x+1]):
                    prefixGrid[y][x] = 0
                    grid[y][x] = 0
                    y += 1
                    
                else:
                    prefixGrid[y][x] = 0
                    grid[y][x] = 0
                    x += 1
                    
                    
            else:
                prefixGrid[y][x] = 0
                grid[y][x] = 0
                x += 1
                

        for j in range(2):
            for i in range(length-1,-1,-1):
                if length-1 == i:
                    prefixGrid[j][i] = grid[j][i]
                else:
                    prefixGrid[j][i] = grid[j][i] + prefixGrid[j][i+1]
                    
                    
        x, y = 0, 0
        curSum = grid[y][x]
        while x < length:
            if y == 0:
                if x == length-1:
                    curSum += grid[y][x]
                    y += 1
                    
                elif prefixGrid[y][x+1] >= prefixGrid[y+1][x]:
                    curSum += grid[y][x]
                    x += 1
                else:
                    curSum += grid[y][x]
                    y += 1
                    
            else:
                curSum += grid[y][x]
                x += 1
        
        return curSum