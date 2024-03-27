class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        def search(groups):
            if not nums:
                return True
            v = nums[-1]
            for i, group in enumerate(groups):
                if group + v <= target:
                    nums.pop()
                    groups[i] += v
                    if search(groups):
                        return True
                    nums.append(v)
                    groups[i] -= v
                if not group:
                    break
            return False

        nums.sort()
        if sum(nums) % k:
            return False
        target = sum(nums) // k
        if nums[-1] > target:
            return False
        while nums and nums[-1] == target:
            nums.pop()
            k -= 1
        return search([0] * k)