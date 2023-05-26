class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        memo = defaultdict(int)
        
        def dp(n):
            if n < 0:
                return 0
            
            elif n == 0:
                memo[n] = cost[n]
                return memo[n]
            
            if n not in memo:
                memo[n] = cost[n]
                memo[n] += min(dp(n-1), dp(n-2))
                       
            return memo[n]
        
        return dp(len(cost)-1)
    