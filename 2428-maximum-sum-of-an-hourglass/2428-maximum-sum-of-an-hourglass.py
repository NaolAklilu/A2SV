class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        row, col = 0, 0
        lastRow = len(grid)-1
        lastCol = len(grid[0])-1
        maxSum = 0
        while row <= lastRow - 2 and col <= lastCol - 2:
            sum = 0
            for i in range(row, row+3):
                for j in range(col, col+3):
                    if ((i == row+1) and ((j == col) or (j == col+2))):
                        continue
                    else:
                        sum += grid[i][j]

            if maxSum < sum:
                maxSum = sum

            if col >= lastCol - 2:
                if row <= lastRow - 2:
                    row += 1
                    col = 0
                else:
                    break
            else:
                col += 1

        return maxSum
            
            
            


