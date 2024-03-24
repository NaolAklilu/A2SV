class Solution:
    def maxScore(self, nums: List[int]) -> int:
        memo = {}
        
        def dp(nOperation, numSet):
            if nOperation == len(nums)//2 +1:
                return 0
            
            if (nOperation, tuple(numSet)) in memo:
                return memo[(nOperation, tuple(numSet))]
            
            score = 0
            for i in range(len(nums)):
                if i in numSet:
                    continue

                for j in range(i+1, len(nums)):
                    if j in numSet:
                        continue
                    curSet = numSet.copy()
                    curSet.add(i)
                    curSet.add(j)
                    curScore = nOperation * math.gcd(nums[i], nums[j]) + dp(nOperation+1, curSet)
                    score = max(score, curScore)
                
            memo[(nOperation, tuple(numSet))] = score
            return score 
        
        return dp(1, set())