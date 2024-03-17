class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_val = float('-inf')
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    triplet_val = (nums[i] - nums[j]) * nums[k]
                    if triplet_val > max_val:
                        max_val = triplet_val
        return max_val if max_val > 0 else 0