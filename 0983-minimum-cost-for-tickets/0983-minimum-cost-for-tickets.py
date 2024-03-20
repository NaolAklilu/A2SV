class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        def dp(day, memo):
            if day < 0:
                return 0
            if day in memo:
                return memo[day]
            if day not in days:
                memo[day] = dp(day - 1, memo)
                return memo[day]
            one_day = dp(day - 1, memo) + costs[0]
            seven_days = dp(day - 7, memo) + costs[1]
            thirty_days = dp(day - 30, memo) + costs[2]
            memo[day] = min(one_day, seven_days, thirty_days)
            return memo[day]

        return dp(days[-1], {})