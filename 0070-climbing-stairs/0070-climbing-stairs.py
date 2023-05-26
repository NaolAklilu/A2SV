class Solution:
    def __init__(self):
        self.memo = defaultdict(int)
        
    def climbStairs(self, n: int) -> int:
        if n < 0:
            return 0
        elif n == 0:
            self.memo[n] = 1
            return self.memo[n]
        
        if n not in self.memo:
            self.memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        
        return self.memo[n]