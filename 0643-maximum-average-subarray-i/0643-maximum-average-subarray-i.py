class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left, right = 0, 0
        
        curSum = 0
        for i in range(k):
            curSum += nums[i]
            right = i
         
        maxAve = curSum/k
        while right < len(nums)-1:
            curSum -= nums[left]
            left += 1
            right += 1
            
            curSum += nums[right]
            maxAve = max(maxAve, curSum/k)
         
        return maxAve