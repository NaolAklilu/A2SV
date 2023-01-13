class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        row, col = 0, 0
        lastRow = len(grid)-1
        lastCol = len(grid[0])-1
        
        length = len(grid)-2
        
        maxLocal = [[0]*length for _ in range(length)]
        
        for i in range(length):
            for j in range(length):
                maxLocal[i][j] = grid[i][j]
                
        
        while row <= lastRow-length+1 and col <= lastCol-length+1:
            for i in range(row, row+length):
                for j in range(col, col+length):
                    curRow = i - row
                    curCol = j - col
                    if grid[i][j] > maxLocal[curRow][curCol]:
                        maxLocal[curRow][curCol] = grid[i][j] 

            if col >= lastCol-length+1:
                if row <= lastRow-length+1:
                    row += 1
                    col = 0
                else:
                    break
            else:
                col += 1
        
        return maxLocal
                