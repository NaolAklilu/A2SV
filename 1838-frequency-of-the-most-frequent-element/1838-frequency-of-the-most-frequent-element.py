class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        left = 0
        total = 0
        res = 0
        
        for right in range(n):
            total += nums[right]
            while total + k < nums[right] * (right - left + 1):
                total -= nums[left]
                left += 1
            res = max(res, right - left + 1)
        
        return res