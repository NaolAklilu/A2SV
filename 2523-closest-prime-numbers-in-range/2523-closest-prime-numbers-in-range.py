class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = [True for i in range(right+1)]
        primes[0] = False
        primes[1] = False
        
        i = 2

        while i * i <= right:
            if primes[i]:
                j = i * i
                while j <= right:
                    primes[j] = False
                    j += i
            i += 1
            
        
        all_primes = []
        for i in range(left, right+1):
            if primes[i] == True:
                all_primes.append(i)
                
        if len(all_primes) < 2:
            return [-1, -1]
        
        ptr1, ptr2 = 0, 1
        num1, num2 = all_primes[ptr1], all_primes[ptr2]
        min_diff = num2 - num1
        
        while ptr2 < len(all_primes):
            if (all_primes[ptr2] - all_primes[ptr1]) < min_diff:
                num1, num2 = all_primes[ptr1], all_primes[ptr2]
                min_diff = num2 - num1
                
            ptr1 += 1
            ptr2 += 1
        
        return [num1, num2]
        
        
                    
                    