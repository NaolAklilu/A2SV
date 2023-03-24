class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] != i+1:
                if nums[nums[i]-1] == nums[i]:
                    print(nums)
                    return nums[i]
                
                else:
                    nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
                
            else:
                i +=1
         
        
        