class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = float(inf)
        start = 0
        windowSum = 0
        isChanged = False
        
        for end in range(len(nums)):
            windowSum += nums[end]
            while start <= end and windowSum >= target:
                isChanged = True
                minLength = min(minLength, end-start+1)
                windowSum -= nums[start]
                start += 1
                
        return minLength if isChanged else 0
            
                        
                    