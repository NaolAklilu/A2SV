class Solution:
    def tribonacci(self, n: int) -> int:
        memo = defaultdict(int)
        
        def TribonNumber(num):
            if num == 0:
                memo[num] = num
                return memo[num]
            
            elif num <= 2:
                memo[num] = 1
                return memo[num]
            
            if num not in memo:
                memo[num] = TribonNumber(num-1) + TribonNumber(num-2) + TribonNumber(num-3)
                
            return memo[num]
        
        return TribonNumber(n)
                
            
        