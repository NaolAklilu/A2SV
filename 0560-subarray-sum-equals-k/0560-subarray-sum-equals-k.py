class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumDic = defaultdict(int)
        count = 0
        
        curSum = 0
        for index in range(len(nums)):
            curSum += nums[index]
            
            if curSum == k:
                count += 1
            
            prevSum = curSum - k
            if prevSum in sumDic:
                count += (sumDic[prevSum])
            sumDic[curSum] += 1
            
        
        return count