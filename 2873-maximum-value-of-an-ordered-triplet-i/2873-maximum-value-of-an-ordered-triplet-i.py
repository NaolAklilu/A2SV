class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_value = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    triplet_value = (nums[i] - nums[j]) * nums[k]
                    if triplet_value > max_value:
                        max_value = triplet_value
        return max_value