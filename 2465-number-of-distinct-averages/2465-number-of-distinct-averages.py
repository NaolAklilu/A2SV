class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        averages = defaultdict(int)
        
        nums.sort()
        left, right = 0, len(nums)-1
        aveCount = 0
        while left < right:
            ave = nums[left] + nums[right]
            averages[ave/2] += 1
            
            left += 1
            right -= 1
                
        return len(averages)
            