class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        
        for row in range(2, numRows+1):
            curRow = []
            for index in range(row):
                left = index - 1
                right = index
                curValue = 0
                if left >= 0:
                    curValue += triangle[row-2][left]
                
                if right < len(triangle[row-2]):
                    curValue += triangle[row-2][right]
                
                curRow.append(curValue)
            
            triangle.append(curRow)
            
        
        return triangle
                    
        