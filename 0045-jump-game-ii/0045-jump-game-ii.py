class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        max_pos = nums[0]
        max_steps = nums[0]
        jumps = 1

        for i in range(1, n):
            if max_steps < i:
                jumps += 1
                max_steps = max_pos
            max_pos = max(max_pos, nums[i] + i)

        return jumps