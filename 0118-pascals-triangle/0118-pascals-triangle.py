class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = {}
        
        def dfs(level, row, col):
            if row-1 < 0 and col-1 < 0:
                triangle[(row, col)] = 1
                return triangle[(row, col)]
            
            left, right = 0, 0
            if row-1 >= 0 and col-1 >= 0:
                if (row-1, col-1) not in triangle:
                    left += dfs(level-1, row-1, col-1)
                else:
                    left += triangle[(row-1, col-1)]
            
            if col < level-1 and col >= 0:
                if (row-1, col) not in triangle:
                    right += dfs(level-1, row-1, col)
                else:
                    right += traingle[(row-1, col)]
            
            triangle[(row, col)] = left+right
            
            return triangle[(row, col)]
        
        for i in range(numRows):
            dfs(numRows, numRows-1, i)

        result = [[] for _ in range(numRows)]
        for i in range(numRows):
            for k in range(i+1):
                result[i].append(triangle[(i, k)])                
        
        return result
        
        
                    
        