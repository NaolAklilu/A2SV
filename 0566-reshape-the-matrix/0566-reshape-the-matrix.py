class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        
        if r*c != n*m:
            return mat
        
        reshapedMat = [[0]*c for _ in range(r)]
        
        for num in range(n*m):
            matRow = num // m
            matCol = num % m
            matValue = mat[matRow][matCol]
            
            # find row and col of the reshapedMat
            row = num // c
            col = num % c
            reshapedMat[row][col] = matValue
        
        return reshapedMat
        