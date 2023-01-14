class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, top = 0, 0 
        right, bottom = len(matrix[0])-1, len(matrix)-1
        
        resultList = []
        
        while left<=right and top <= bottom:
            # append left to right element to result list
            for i in range(left, right+1):
                resultList.append(matrix[top][i])
            top += 1
            
            # append element from top to bottom
            for j in range(top, bottom+1):
                resultList.append(matrix[j][right])
            right -= 1
            
            # move from right to left
            if top <= bottom:
                for k in range(right, left-1, -1):
                    resultList.append(matrix[bottom][k])
                bottom -= 1
                
            # move from bottom to top
            if left <= right:
                for l in range(bottom, top-1, -1):
                    resultList.append(matrix[l][left])
                left += 1
                
        return resultList

        