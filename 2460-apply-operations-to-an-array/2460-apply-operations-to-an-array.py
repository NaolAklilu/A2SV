class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:        
        for i in range(len(nums)):
            if i < len(nums)-1:
                if nums[i] == nums[i+1] and nums[i] != 0:
                    nums[i] *= 2
                    nums[i+1] = 0
                
            if i > 0 and nums[i] != 0:
                j = i-1
                while j >= 0 and nums[j] == 0:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    j -= 1
        
        return nums
                    
            
                
                
                
                