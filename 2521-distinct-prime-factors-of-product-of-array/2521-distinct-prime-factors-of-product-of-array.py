class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        primes = set()
        for num in nums:
            d = 2
            while d*d <= num:
                while num % d == 0:
                    primes.add(d)
                    num //= d
                d += 1

            if num > 1:
                primes.add(num)

        return len(primes)
                
        
        