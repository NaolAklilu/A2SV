class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        left = 0
        right = 1
        
        if len(nums) == 1:
            return 0
        
        count = 0
        while left < len(nums) and right < len(nums):
            if nums[left] == nums[right]:
                count += 1
                if right + 1 == len(nums):
                    left += 1
                    right = left + 1
                
                else:
                    right += 1
            
            else:
                if right + 1 == len(nums):
                    left += 1
                    right = left + 1
                
                else:
                    right += 1
                    
        return count