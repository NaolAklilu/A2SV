class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainderDic = defaultdict(int)
        curSum, count = 0, 0
        
        for i in range(len(nums)):
            curSum += nums[i]
            
            if curSum%k == 0:
                count += 1
                
            prevRemainder = curSum%k
            if prevRemainder in remainderDic:
                count += remainderDic[prevRemainder]
            
            remainderDic[curSum%k] += 1
        
        return count
            
        