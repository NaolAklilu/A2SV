class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(n)] for j in range(m)] 
        dp[-1][-1] = 1
        
        def inBound(row, col):
            if 0<= row < m and 0<= col < n:
                return dp[row][col]
            return 0
        
        for row in range(m-1, -1,-1):
            for col in range(n-1, -1,-1):
                if (row, col) == (m-1, n-1):
                    continue
                dp[row][col] = inBound(row+1, col) + inBound(row, col+1)
               
        return dp[0][0]
            
        
        
            