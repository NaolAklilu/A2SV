class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = -1, len(nums)
        
        while left+1 < right:
            mid = left + (right-left)//2
            
            if nums[mid] <= target:
                left = mid
            else:
                right = mid
            
        if left > -1 and nums[left] == target:
            return left
        return -1
        