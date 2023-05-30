class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = defaultdict(tuple)
        
        def findTarget(i, curSum):
            if i == len(nums):
                if curSum == target:
                    return 1
                return 0
            
            if (i, curSum) not in memo:
                memo[(i, curSum)] = findTarget(i+1, curSum + nums[i]) + findTarget(i+1, curSum-nums[i])
            
            return memo[(i, curSum)]
     
        return findTarget(0, 0)
        
            
            
            