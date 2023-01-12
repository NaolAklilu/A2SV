class Solution:
    
    def NumberToRowCol(self, matrix, num, columnLength):
        row = num // columnLength
        col = num % columnLength
        
        return matrix[row][col]
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        columnLength = len(matrix[0])
        left = 0
        right = len(matrix)*columnLength - 1
        
        mid = (left+right)//2
        
        if self.NumberToRowCol(matrix, left, columnLength) == target:
            return True
        elif self.NumberToRowCol(matrix, right, columnLength) == target:
            return True

        while mid != left:            
            curNum = self.NumberToRowCol(matrix, mid, columnLength)
            if curNum == target:
                return True
            elif curNum < target:
                left = mid
            else:
                right = mid
                
            mid = (left+right) // 2
            
        curNum = self.NumberToRowCol(matrix, mid, columnLength)
        if curNum == target:
            return True
            
        return False
             
            