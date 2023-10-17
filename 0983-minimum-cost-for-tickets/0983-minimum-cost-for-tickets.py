class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        endDay = max(days)
        memo = defaultdict(int)
        memo[0] = 0
        
        for day in days:
            memo[day] = 1
        
        @cache
        def dp(day):
            if day == 0:
                return memo[0]
            
            if memo[day] == 0:
                memo[day] = dp(max(0, day-1))
            
            else:
                oneDay = dp(max(0, day-1)) + costs[0]
                oneWeek = dp(max(0, day - 7)) + costs[1]
                oneMonth = dp(max(0, day - 30)) + costs[2]
                memo[day] = min(oneDay, oneWeek, oneMonth)
            return memo[day]
        
        result = dp(endDay)
        return result