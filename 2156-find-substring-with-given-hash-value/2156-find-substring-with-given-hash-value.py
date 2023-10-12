class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        string = s[::-1]
        left, right = 0, 0
        curHash = 0
        
        m = pow(power, k, modulo)
        leftPtr, rightPtr = -1, -1
        
        while right < k:
            curHash += (((ord(string[right]) - ord('a')) + 1) * pow(power, k-(right - left)-1, modulo))
            curHash %= modulo
            right += 1
            
        if curHash == hashValue:
            leftPtr, rightPtr = left, right-1
           
        while right < len(string):
            curHash = (power*curHash - m*((ord(string[left]) - ord('a')) + 1) + ((ord(string[right]) - ord('a')) + 1)) % modulo
            
            left += 1
            if curHash == hashValue:
                leftPtr, rightPtr = left, right
            
            right += 1
        
        curString = string[leftPtr:rightPtr+1]
        return curString[::-1]
        
        
                    
        