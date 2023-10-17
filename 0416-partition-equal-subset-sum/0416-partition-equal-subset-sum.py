class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum%2 != 0:
            return False
        
        half = totalSum // 2
        
        @cache
        def dp(index, curSum):
            if index == len(nums):
                if curSum == 0:
                    return True
                return False
            
            res = dp(index+1, curSum)
            if res == True:
                return True
            
            if nums[index] <= curSum:
                res2 = dp(index+1, curSum - nums[index])
                if res2 == True:
                    return True
                
            return False
        
        return dp(0, half)
            
            
        