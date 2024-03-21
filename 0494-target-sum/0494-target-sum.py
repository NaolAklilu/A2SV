class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = {0: 1}
        for num in nums:
            newTotal = {}
            for curNum, curCount in total.items():
                newTotal[curNum + num] = newTotal.get(curNum + num, 0) + curCount
                newTotal[curNum - num] = newTotal.get(curNum - num, 0) + curCount
            total = newTotal
        return total.get(target, 0)