class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        if len(nums) == 1:
            if target <= nums[left]:
                return left
            else:
                return left + 1
        
        while left <= right:
            mid = left + (right - left)//2
            
            if target < nums[left]:
                return left
            
            if nums[mid] < target:
                left = mid
            
            elif nums[mid] >= target:
                right = mid
                
            if nums[left] == target:
                return left
            
            if left+1 == right:
                if nums[right] >= target:
                    return right
                else:
                    return right + 1
                
            