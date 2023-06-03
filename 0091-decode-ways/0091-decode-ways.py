class Solution:
    def numDecodings(self, s: str) -> int:
        
        memo =[ 0 for i in range(len(s))]
        if int(s[len(s)-1]) > 0:
            memo[len(s)-1] = 1
            
        if len(s) >= 2:
            if int(s[len(s)-2]) > 0:
                if int(s[len(s)-2:]) <= 26:
                    memo[len(s)-2] = memo[len(s)-1] + 1
                    
                else:
                    memo[len(s)-2] = memo[len(s)-1]
        
        for i in range(len(s)-3, -1, -1):
            if int(s[i]) > 0:
                if int(s[i:i+2]) <= 26:
                    memo[i] = memo[i+1] + memo[i+2]
                else:
                    memo[i] = memo[i+1]
                    
            else:
                memo[i] = memo[i-1]
        
        return 0 if int(s[0]) == 0 else memo[0]
