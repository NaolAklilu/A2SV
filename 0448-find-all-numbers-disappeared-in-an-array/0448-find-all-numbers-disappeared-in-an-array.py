class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)):
            while nums[i] != i+1:
                if nums[nums[i]-1] == nums[i]:
                    nums[i] = 0
                    break
                
                if nums[i] == 0:
                    break
                else:
                    nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]  
          
        res = []
        for i in range(len(nums)):
            if nums[i] == 0:
                res.append(i+1)
        
        return res
                    
            
            
            
                
                    