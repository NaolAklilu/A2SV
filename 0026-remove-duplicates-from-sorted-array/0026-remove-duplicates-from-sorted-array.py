class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr = 0
        while ptr < len(nums)-1:
            if nums[ptr] == nums[ptr+1]:
                nums.pop(ptr)
            
            else:
                ptr += 1
                
        