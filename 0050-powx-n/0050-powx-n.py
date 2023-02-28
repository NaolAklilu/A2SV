class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 1:
            return 1
        if x == 0:
            return 0
        if n < 0:
            x = 1/x
            n = abs(n)
            
        if n == 1:
            return x
        if n == 0:
            return 1
        
        powe = self.myPow(x, n//2)
        if n%2 == 0:
            return (powe )**2
        else:
            return x * (powe )**2