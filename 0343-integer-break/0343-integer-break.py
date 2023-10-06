class Solution:
    def integerBreak(self, n: int) -> int:
        maxProduct = 0
        
        if n == 2:
            return 1
        
        for i in range(2, n):
            if n%i == 0:
                quo = n // i
                maxProduct = max(maxProduct, i**quo)
                
            else:
                rem = n%i
                quo = n//i
                
                if quo > 1:
                    curProduct = max((i**(quo-1)) * (i+rem), (i**quo) * rem)
                else:
                    curProduct = i**quo * rem
                maxProduct = max(maxProduct, curProduct)
                
        return maxProduct