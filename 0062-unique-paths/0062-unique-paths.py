class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        memo = {}
        
        def factorial(num):
            if num <= 1:
                return 1
            
            if num not in memo:
                memo[num] = num*factorial(num-1)
            
            return memo[num]
        
        total = m-1 + n-1
        
        return factorial(total)//(factorial(m-1)*factorial(n-1))
        
        
        