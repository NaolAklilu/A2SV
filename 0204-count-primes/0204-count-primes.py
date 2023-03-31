class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        
        primes = [True for i in range(n)]
        primes[0] = False
        primes[1] = False
        
        count = 0
        i = 2
        while i*i <= n:
            if primes[i]:
                j = i*i
                while j < n:
                    primes[j] = False
                    j += i     
            i += 1

        for value in primes:
            if value:
                count += 1
            
        return count
        