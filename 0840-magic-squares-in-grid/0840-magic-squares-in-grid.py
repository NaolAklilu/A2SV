class Solution:
    
    def isMagicSquare(self, curSum, squareMat):
        # Check each row
        for row in squareMat:
            if sum(row) != curSum:
                return 0
            
        # Check each column
        for i in range(3):
            columnSum = 0
            for row in squareMat:
                columnSum += row[i]
                
            if columnSum != curSum:
                return 0
            
        # Left bottom diagonal
        diagonalSum = squareMat[0][0] + squareMat[1][1] + squareMat[2][2]
        if diagonalSum != curSum:
            return 0
        
        # right bottom diagonal
        diagonalSum = squareMat[0][2] + squareMat[1][1] + squareMat[2][0]
        if diagonalSum != curSum:
            return 0
        
        return 1
        
        
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        row, col = 0, 0
        lastRow, lastCol = len(grid)-1, len(grid[0])-1
        magicSquareCount = 0
        
        while row <= lastRow-2 and col <= lastCol-2:
            curMat = []
            curSum = grid[row][col] + grid[row][col+1] + grid[row][col+2]
            
            isOkay = True
            curSet = set()
            for i in range(row, row+3):
                curRow = []
                for j in range(col, col+3):
                    if grid[i][j] not in curSet:
                        curSet.add(grid[i][j])
                    else:
                        isOkay = False
                        
                    if grid[i][j] > 9 or grid[i][j] < 1:
                        isOkay = False
                        
                    curRow.append(grid[i][j])
                    
                if isOkay == False:
                    break
                   
                curMat.append(curRow)
            
            if isOkay == True: 
                magicSquareCount += self.isMagicSquare(curSum, curMat)
            
            if col >= lastCol-2:
                if row <= lastRow-2:
                    row += 1
                    col = 0
                else:
                    break
            else:
                col += 1
            
        return magicSquareCount