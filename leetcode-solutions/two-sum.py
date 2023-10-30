class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            nums[i] = (nums[i], i)
        
        nums.sort()
        left, right = 0, len(nums)-1
        
        while left < right:
            curSum = nums[left][0]+nums[right][0]
            if curSum == target:
                return [nums[left][1], nums[right][1]]
            elif curSum > target:
                right -= 1
            else:
                left += 1
                
    
            