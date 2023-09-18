class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # Bottom-Up approach
        
        dp = [[0,0] for _ in range(len(prices)+1)]
        
        for pos in reversed(range(len(prices))):
            for bought in [True, False]:
                max_profit = 0
                
                if not bought:
                    max_profit = max(max_profit, dp[pos+1][True] - prices[pos] - fee)
                else:
                    max_profit = max(max_profit, dp[pos+1][False] + prices[pos])
                
                max_profit = max(max_profit, dp[pos+1][bought])
                
                dp[pos][bought] = max_profit

        
        return dp[0][False]
            
        
                
            