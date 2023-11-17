class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSum = []
        for i in range(len(nums)):
            if len(self.prefixSum) == 0:
                self.prefixSum.append(nums[i])
            else:
                self.prefixSum.append(self.prefixSum[-1] + nums[i])

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefixSum[right]
        else:
            return self.prefixSum[right] - self.prefixSum[left-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)