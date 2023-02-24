class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1 = list(s1)
        s1.sort()
        
        left, right = 0, len(s1)-1
        while right<len(s2):
            curSubstring = list(s2[left: right+1])
            curSubstring.sort()
            
            if curSubstring == s1:
                return True
            
            right += 1
            left += 1
            
        return False
        
        