class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == len(grid) or j == len(grid[0]):
                return float('inf')
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return grid[i][j]
            ans = grid[i][j] + min(dfs(i+1, j), dfs(i, j+1))
            memo[(i, j)] = ans
            return ans

        return dfs(0, 0)