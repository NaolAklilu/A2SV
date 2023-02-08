class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left, right = 0, 0
        curPtr = 0
        while left < len(s):
            right = curPtr
            while right < len(t):
                if s[left] == t[right]:
                    curPtr = right+1
                    left += 1 
                    break 
                else:
                    right += 1
                    
            if right == len(t):
                return False
            
        return True