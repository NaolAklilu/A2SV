class Solution:
    
    def helper(self, n, s):
        if n == 1:
            reversedString  = list(reversed(s))
            for i in range(len(reversedString)):
                if reversedString[i] == "0":
                    reversedString[i] = "1"
                else:
                    reversedString[i] = "0"
                    
            s += ["1"] + reversedString
            return s
        
        else:
            reversedString  = list(reversed(s))
            for i in range(len(reversedString)):
                if reversedString[i] == "0":
                    reversedString[i] = "1"
                else:
                    reversedString[i] = "0"
                    
            s += ["1"] + reversedString
            
            s = self.helper(n-1, s)
            return s
            
    
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            s = "0"
            return s[k-1]
        
        s = ["0"]
        s = self.helper(n-1, s)
        
        return s[k-1]
        