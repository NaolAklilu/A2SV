class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dp(n):
            # Return the cached result if it's already computed
            if n in memo: return memo[n]
            # If the amount is 0, no coins are needed
            if n == 0: return 0
            # If the amount is less than 0, return -1
            if n < 0: return -1
            res = float('inf')
            for coin in coins:
                subproblem = dp(n - coin)
                if subproblem == -1: continue
                res = min(res, 1 + subproblem)
            # Cache the result
            memo[n] = res if res != float('inf') else -1
            return memo[n]

        memo = {}
        return dp(amount)