class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # Top-Down approach
        @lru_cache(None)  # Does caching which avoid repeated computation
        def dp(pos, bought):
            if pos == len(prices):
                return 0
            
            max_price = 0
            if not bought:
                max_price = max(max_price, dp(pos+1, True)-prices[pos]-fee)
            else:
                max_price = max(max_price, dp(pos+1, False) + prices[pos])
                
            max_price = max(max_price, dp(pos+1, bought))
            
            return max_price
            
        return dp(0, False)
                
            