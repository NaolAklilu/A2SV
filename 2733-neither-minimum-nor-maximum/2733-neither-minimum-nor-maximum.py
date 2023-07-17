class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nums.sort()
        numCount = defaultdict(int)
        for num in nums:
            numCount[num] += 1
            
        if len(numCount) <= 2:
            return -1
        else:
            return nums[numCount[nums[0]]]
        