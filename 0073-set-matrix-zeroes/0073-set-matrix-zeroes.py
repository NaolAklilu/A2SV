class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zerosIndex = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zerosIndex.append((i, j))
                    
        for index in zerosIndex:
            for row in range(len(matrix)):
                for col in range(len(matrix[0])): 
                    if row == index[0]:
                        matrix[row][col] = 0
                    
                    if col == index[1]:
                        matrix[row][col] = 0