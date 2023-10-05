class Solution:
    def knightDialer(self, n: int) -> int:
        directions = [(-2, -1), (-2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2), (2, -1), (2, 1)]
        symbols = {(3, 0), (3, 2)}
        visited = {}
        
        def isBound(row, col):
            return 0<=row<4 and 0<=col<3
                            
        def dfs(row, col, count):
            if count == n:
                return 1
            
            curCount = 0
            for r, c in directions:
                if isBound(r+row, c+col) and (r+row, c+col) not in symbols:
                    if (r+row, c+col, count+1) not in visited:
                        visited[(row+r, c+col, count+1)] = dfs(r+row, c+col, count + 1)
                        curCount += visited[(row+r, c+col, count+1)]
                    else:
                        curCount += visited[(r+row, c+col, count+1)]
                
            return curCount
        
        totalCount = 0
        for row in range(4):
            for col in range(3):
                if (row, col) not in symbols:
                    totalCount += dfs(row, col, 1)
                    
        return totalCount%(10**9 + 7)
                    
            
            