class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        string = []
        for char in s:
            string.append(char)
            
        left, right = 0, len(s)-1
        
        while left<right:
            if string[left] != string[right]:
                if string[left] < string[right]:
                    string[right] = string[left]
                else:
                    string[left] = string[right]
                    
            left += 1
            right -= 1
            
        return "".join(string)