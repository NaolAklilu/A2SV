class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @cache
        def topDown(index, curAmount):
            if index == len(coins):
                if curAmount == 0:
                    return 1
                return 0
            
            count = topDown(index+1, curAmount)
            
            if coins[index] <= curAmount:
                count += topDown(index, curAmount - coins[index])
                
            return count
        
        return topDown(0, amount)