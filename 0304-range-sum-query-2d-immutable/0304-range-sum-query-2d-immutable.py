class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefixSum = [[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]
        
        for rowIndex in range(len(matrix)):
            for colIndex in range(len(matrix[0])):
                i = rowIndex+1
                j = colIndex+1
                self.prefixSum[i][j] = self.prefixSum[i-1][j] + self.prefixSum[i][j-1] - self.prefixSum[i-1][j-1] + self.matrix[rowIndex][colIndex]
            

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        rangeSum = self.prefixSum[row2+1][col2+1] - self.prefixSum[row2+1][col1] - self.prefixSum[row1][col2+1] + self.prefixSum[row1][col1]
        return rangeSum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)