class Solution:
    def tribonacci(self, n: int) -> int:
        
        if n == 0:
            return 0
        if n <= 2:
            return 1
        
        memo = [0 for _ in range(n+1)]
        memo[0] = 0
        memo[1] = 1
        memo[2] = 1
        
        for index in range(3, n+1):
            memo[index] = memo[index-1] + memo[index-2] + memo[index-3]
        
        return memo[-1]
        