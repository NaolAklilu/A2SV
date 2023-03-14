class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        left = -1
        right = len(nums)
        
        if len(nums) == 1:
            return 0
        
        while left+1 < right:
            mid = left + (right-left)//2
            if mid+1 < len(nums) and nums[mid] < nums[mid+1]:
                left = mid
            
            elif mid+1 == len(nums):
                if nums[mid] > nums[left]:
                    return mid
                else:
                    return left
                    
            else:
                right = mid
                    
        return right