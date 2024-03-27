class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        nums.sort(reverse=True)
        if nums[0] > target:
            return False

        def dfs(groups):
            if not nums:
                return True
            v = nums[0]
            for i, group in enumerate(groups):
                if group + v <= target:
                    nums.pop(0)
                    groups[i] += v
                    if dfs(groups):
                        return True
                    nums.insert(0, v)
                    groups[i] -= v
                if not group:
                    break
            return False

        return dfs([0] * k)