import math

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        
        @cache
        def dp(nOperation, mask):
            if nOperation == len(nums)//2 +1:
                return 0
            
            score = 0
            for i in range(len(nums)):
                if (mask >> i) & 1:
                    continue

                for j in range(i+1, len(nums)):
                    if (mask >> j) & 1:
                        continue
                        
                    curMask = (1 << i) | (1 << j) | mask
                    curGcd = nOperation * math.gcd(nums[i], nums[j])
                    
                    curScore =curGcd  + dp(nOperation+1, curMask)
                    score = max(score, curScore)
                
            return score 
        
        return dp(1, 0)
                
                        
                    