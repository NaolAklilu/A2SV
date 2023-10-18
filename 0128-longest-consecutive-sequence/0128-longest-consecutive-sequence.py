class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:        
        if len(nums) <= 1:
            return len(nums)
        
        maxCount = 0
        nums.sort()
        
        curCount = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                curCount += 1
            else:
                if nums[i] == nums[i-1]:
                    continue
                maxCount = max(curCount, maxCount)
                curCount = 1
                
        maxCount = max(maxCount, curCount)
        
        return maxCount
            