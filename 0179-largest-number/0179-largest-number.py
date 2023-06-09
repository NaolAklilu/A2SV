class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        def swap(index1, index2):
            nums[index1], nums[index2] = nums[index2], nums[index1]
        
        for i in range(len(nums)):
             for j in range(i+1,len(nums)):
                if int(str(nums[i])+str(nums[j])) < int(str(nums[j])+str(nums[i])):
                    swap(i, j)
           
        nums = map(str, nums)
        nums = "".join(nums)
        if nums.count("0") == len(nums):
            return "0"
        
        return nums