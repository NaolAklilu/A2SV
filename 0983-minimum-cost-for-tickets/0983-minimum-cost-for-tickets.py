class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * 366
        
        for day in days:
            dp[day] = 1
            
        for i in range(1, days[len(days)-1]+1):
            if dp[i] == 0:
                dp[i] = dp[i-1]
                continue
                
            curCost = dp[i-1] + costs[0]
            curCost = min(curCost, dp[max(0, i - 7)] + costs[1])
            curCost = min(curCost, dp[max(0, i - 30)] + costs[2])

            dp[i] = curCost
        
        return dp[days[len(days) - 1]];