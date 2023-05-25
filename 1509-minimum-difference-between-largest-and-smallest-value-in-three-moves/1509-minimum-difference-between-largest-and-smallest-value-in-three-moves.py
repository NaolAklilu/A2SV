class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        
        nums.sort()
        n = len(nums)
        minDiff = float(inf)
        
        minDiff = min(minDiff, nums[n-1]-nums[3])
        minDiff = min(minDiff, nums[n-2]-nums[2])
        minDiff = min(minDiff, nums[n-3]-nums[1])
        minDiff = min(minDiff, nums[n-4]-nums[0])
        
        return minDiff