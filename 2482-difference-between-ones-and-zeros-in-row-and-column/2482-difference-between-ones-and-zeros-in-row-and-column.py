class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid[0])
        m = len(grid)
        oneInRows = [0] * m
        oneInColumns = [0] * n
        
        newGrid = []
        print(newGrid)
        
        # Count one in each row and store in oneInRows list
        for i in range(m):
            oneInRows[i] += grid[i].count(1)
        
        # Count one in each column and store in oneInColumns list
        for j in range(n):
            for row in grid:
                if row[j] == 1:
                    oneInColumns[j] += 1
                    
                    
        # find the difference between one and zeros
        for i in range(m):
            curRow = []
            for j in range(n):
                oneCount = oneInRows[i] + oneInColumns[j]
                zeroCount = (n + m) - oneCount
                curRow.append(oneCount - zeroCount)
                
            newGrid.append(curRow)                

        return newGrid
                
                