class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        minDifference = float(inf)
        left, right = 0, 0
        
        if k <= 1:
            return 0
        
        while right < len(nums):
            if right-left + 1 < k:
                right += 1
            else:
                minDifference = min(minDifference, nums[right] - nums[left])
                left += 1
                right += 1
                
        return minDifference
    