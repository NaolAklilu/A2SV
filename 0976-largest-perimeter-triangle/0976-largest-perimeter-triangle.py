class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        side1, side2, side3 = n-3, n-2, n-1
        
        while side1 >= 0:
            if nums[side1] + nums[side2] > nums[side3]:
                return nums[side1] + nums[side2] + nums[side3]
            else:
                side1 -= 1
                side2 -= 1
                side3 -= 1
                
        return 0