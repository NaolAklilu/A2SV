class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        s = list(s)         
        prefix = [0]*len(s)
        
        for shift in shifts:
            if shift[2] == 0:
                prefix[shift[0]] -= 1
                if shift[1]+1 < len(s):
                    prefix[shift[1]+1] += 1
                
            else:
                prefix[shift[0]] += 1
                if shift[1]+1 < len(s):
                    prefix[shift[1]+1] -= 1
                    
        for i in range(1, len(prefix)):
            prefix[i] += prefix[i-1]
                
        for i in range(len(s)):
            prefixValue = prefix[i]%26
            charOrd = 97 + ((ord(s[i])-97) + prefixValue + 26)%26
            s[i] = chr(charOrd)
        
        return "".join(s)