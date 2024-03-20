class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (days[-1] + 1)
        for i in range(days[-1] + 1):
            if i not in days:
                dp[i] = dp[i-1]
            else:
                one_day = dp[i-1] + costs[0] if i-1 >= 0 else costs[0]
                seven_days = dp[i-7] + costs[1] if i-7 >= 0 else costs[1]
                thirty_days = dp[i-30] + costs[2] if i-30 >= 0 else costs[2]
                dp[i] = min(one_day, seven_days, thirty_days)
        return dp[-1]