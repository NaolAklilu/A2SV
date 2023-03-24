class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):                    
                if nums[i] != (i+1) :
                    if nums[nums[i]-1] == nums[i]:
                        nums[i] = 0
                        i += 1
                
                    elif nums[i] == 0:
                        i += 1
                        
                    else:
                        nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1] 
                
                else:
                    i += 1
          
        res = []
        for i in range(len(nums)):
            if nums[i] == 0:
                res.append(i+1)
        
        return res
                    
            
            
            
                
                    