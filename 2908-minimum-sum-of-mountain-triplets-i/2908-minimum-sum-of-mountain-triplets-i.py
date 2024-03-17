class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        min_sum = float('inf')
        triplet = None

        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] < nums[j] and nums[j] > nums[k]:
                        curr_sum = nums[i] + nums[j] + nums[k]
                        if curr_sum < min_sum:
                            min_sum = curr_sum
                            triplet = (i, j, k)

        if triplet is None:
            return -1
        else:
            return min_sum