class Solution:
    def countGoodNumbers(self, n: int) -> int:
        primeCount = n // 2
        evenCount = n - primeCount
        
        goodCount = (pow(5, evenCount, 10**9 + 7))* (pow(4, primeCount, 10**9 + 7))
        return goodCount % (10**9 + 7)
            