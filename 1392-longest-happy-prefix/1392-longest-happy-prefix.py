class Solution:
    def longestPrefix(self, s: str) -> str:
        LPS = [0 for _ in range(len(s))]
        
        i, j = 0, 1
        while j < len(s):
            if s[i] == s[j]:
                LPS[j] = i+1 
                i += 1
                j += 1
            
            elif i == 0:
                j += 1

            else:
                i = LPS[i-1]
                
        if LPS[-1] == 0:
            return ""
        
        return s[-1*LPS[-1]:]