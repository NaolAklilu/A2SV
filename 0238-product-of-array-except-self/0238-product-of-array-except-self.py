class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProduct = [1] * len(nums)
        rightProduct = [1] * len(nums)
        
        for i in range(1, len(nums)):
            leftProduct[i] = leftProduct[i-1] * nums[i-1]
            
        for i in range(len(nums)-2, -1,-1):
            rightProduct[i] = rightProduct[i+1] * nums[i+1]
            
        for i in range(len(nums)):
            leftProduct[i] = leftProduct[i] * rightProduct[i]
            
        return leftProduct