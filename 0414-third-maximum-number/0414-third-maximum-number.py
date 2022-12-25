class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        sorted_nums = sorted(list(set(nums)))
        
        if len(sorted_nums) >= 3:
            return sorted_nums[-3]
        else:
            return sorted_nums[-1]