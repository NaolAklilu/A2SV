class Solution:
    def numTrees(self, n: int) -> int:
        def helper(n, memo):
            if n in memo:
                return memo[n]
            if n <= 1:
                return 1
            total = 0
            for i in range(1, n+1):
                total += helper(i-1, memo) * helper(n-i, memo)
            memo[n] = total
            return total

        memo = {}
        return helper(n, memo)