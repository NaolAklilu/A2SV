class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        ptr = 1
        
        minDiff = float('inf')
        while ptr <= len(nums)-1:
            minDiff = min(minDiff, abs(nums[ptr] - nums[ptr-1]))
            ptr += 1
        return minDiff