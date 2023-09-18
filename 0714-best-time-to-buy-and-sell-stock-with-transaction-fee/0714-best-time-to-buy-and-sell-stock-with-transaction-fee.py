class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # Top-Down approach        
        memo = defaultdict(int)
        
        def dp(pos, bought):
            if pos == len(prices):
                return 0
            
            if (pos, bought) in memo:
                return memo[(pos, bought)]
            
            max_price = 0
            if not bought:
                max_price = max(max_price, dp(pos+1, True)-prices[pos]-fee)
            else:
                max_price = max(max_price, dp(pos+1, False) + prices[pos])
                
            max_price = max(max_price, dp(pos+1, bought))
            
            memo[(pos, bought)] = max_price
            return max_price
            
        return dp(0, False)
                
            