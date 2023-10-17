class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @cache
        def dp(index, curAmount):
            
            if index == len(coins):
                if curAmount == 0:
                    return 0            
                return float('inf')
            
            notTake = 0 + dp(index+1, curAmount)
            
            take = float('inf')
            if coins[index] <= curAmount:
                take = 1 + dp(index, curAmount - coins[index])
            
            return min(notTake, take)
        
        result = dp(0, amount)
        if result == float('inf'):
            return -1
        return result
            