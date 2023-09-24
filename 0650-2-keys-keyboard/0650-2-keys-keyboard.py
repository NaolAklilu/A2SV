class Solution:
    def minSteps(self, n: int) -> int:
        
        if n==1:
            return 0
        
        count = 0
        i = 2
        
        while i**2 <= n:
            if n%i == 0:
                count += i
                n /= i
            else:
                i += 1
                
        return int(count + n)
        
        
        