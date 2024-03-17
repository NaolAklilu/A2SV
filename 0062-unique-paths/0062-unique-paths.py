class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
    
        def countPaths(i: int, j: int) -> int:
            if i == 0 or j == 0:
                return 1
            if dp[i][j] != 0:
                return dp[i][j]
            dp[i][j] = countPaths(i-1, j) + countPaths(i, j-1)
            return dp[i][j]

        return countPaths(m-1, n-1)