class Solution:             
    
    def predictHelper(self, nums, left, right):
        if left == right:
            return nums[right]
        
        return max(nums[left]-self.predictHelper(nums, left+1, right), nums[right]-self.predictHelper(nums, left, right-1))
        
    
    def PredictTheWinner(self, nums: List[int]) -> bool:
        left, right = 0, len(nums)-1
        
        val = self.predictHelper(nums, left, right)
        
        return val >= 0
            