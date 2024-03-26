class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = dict()

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == m or j == n:
                return float('inf')
            if i == m - 1 and j == n - 1:
                return grid[i][j]
            ans = grid[i][j] + min(dp(i+1, j), dp(i, j+1))
            memo[(i, j)] = ans
            return ans

        return dp(0, 0)