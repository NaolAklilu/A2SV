class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefixSum = [0]*len(nums)
        curSum = 0
        for i in range(len(nums)):
            curSum += self.nums[i]
            self.prefixSum[i] = curSum
        
    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum[right]-self.prefixSum[left]+self.nums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)