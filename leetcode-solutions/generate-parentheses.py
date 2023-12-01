class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def dp(arr, openingCount, closingCount):
            curArr = arr[:]
            if openingCount == n and closingCount==n:
                ans.append("".join(curArr))
            elif openingCount == 0 or openingCount == closingCount:
                curArr.append('(')
                dp(curArr, openingCount+1, closingCount)
            elif openingCount > closingCount and openingCount < n:
                curArr.append("(")
                dp(curArr, openingCount+1, closingCount)
                
                curArr.pop()
                curArr.append(")")
                dp(curArr, openingCount, closingCount+1)
            elif openingCount == n and closingCount < n:
                    curArr.append(")")
                    dp(curArr, openingCount, closingCount+1)
            
        dp([], 0, 0)
        return ans
            
            
                