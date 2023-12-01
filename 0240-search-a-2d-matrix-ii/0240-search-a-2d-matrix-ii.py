class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        for r in range(row-1, -1, -1):
            for c in range(col-1, -1, -1):
                if matrix[r][c] == target:
                    return True
                
                if matrix[r][c] < target:
                    break
                
        return False