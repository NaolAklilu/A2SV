class Solution:
    def minSteps(self, n: int) -> int:
        
        if n == 1:
            return 0
        
        def dp(curLength, curCopied, operationCount):
            if curLength == n:
                return operationCount
            
            elif curLength > n:
                return float(inf)
            
            else:
                operation1 = dp(curLength+curLength, curLength, operationCount+2)
                operation2 = dp(curLength+curCopied, curCopied, operationCount+1)
            
            return min(operation1, operation2)
        
        return dp(1, 1, 1)
        