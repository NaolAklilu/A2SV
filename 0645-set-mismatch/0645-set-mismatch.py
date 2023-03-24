class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = []
        i = 0
        while i < len(nums):                    
                if nums[i] != (i+1) :
                    if nums[i] == 0:
                        i += 1
                        
                    elif nums[nums[i]-1] == nums[i]:
                        res.append(nums[i])
                        nums[i] = 0
                        i += 1
                
                    else:
                        nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1] 
                
                else:
                    i += 1
          
        
        for i in range(len(nums)):
            if nums[i] == 0:
                res.append(i+1)
        
        return res