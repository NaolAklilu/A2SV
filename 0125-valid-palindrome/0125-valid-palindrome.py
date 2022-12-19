class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        string = "".join(filter(str.isalnum, s.lower()))
        
        begin, end = 0, len(string) - 1
        
        if len(string) <= 1:
            return True
        
        while begin < end:
            if string[begin] != string[end]:
                return False
            else:
                begin += 1
                end -= 1
                
        return True