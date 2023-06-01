class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = defaultdict(int)
          
        def find(amount):
            best = float(inf)
            
            if amount == 0:
                return 0
            
            if amount < 0:
                return best
            
            for coin in coins:
                if (amount-coin) in memo:
                    best = min(best, memo[amount-coin])
                else:
                    best = min(best, find(amount-coin))
                    
            memo[amount] = best+1
                
            return memo[amount]
        
        result = find(amount)
        if result == float(inf):
            return -1
        return result


            
        