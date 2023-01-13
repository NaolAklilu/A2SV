class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        diagonalDic = {}
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row-col in diagonalDic.keys():
                    if diagonalDic[row-col] != matrix[row][col]:
                        return False
                else:
                    diagonalDic[row-col] = matrix[row][col]
                    
        return True