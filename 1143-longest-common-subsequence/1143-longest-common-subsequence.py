class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @cache
        def dp(ptr1, ptr2):
            if ptr1 == len(text1) or ptr2 == len(text2):
                return 0
            
            curCount = 0
            if text1[ptr1] == text2[ptr2]:
                curCount += 1
                res = dp(ptr1+1, ptr2+1)
                curCount += res
            
            one = dp(ptr1+1, ptr2)
            two = dp(ptr1, ptr2+1)
            
            return max(curCount, one, two)
        
        return dp(0, 0)
        
            