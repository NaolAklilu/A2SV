class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums)-1
        n = len(nums)
        
        while left < right:
            while left<n and nums[left]%2 == 0:
                left += 1
            
            while 0 <= right and  nums[right]%2 == 1:
                right -= 1
                
            if left<n and right<n and left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
                
        return nums