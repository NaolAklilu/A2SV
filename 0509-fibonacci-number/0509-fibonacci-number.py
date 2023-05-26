class Solution:
    
    def __init__(self):
        self.memory = defaultdict(int)
    
    def fib(self, n: int) -> int:
        if n <= 1:
            self.memory[n] = n
            return self.memory[n]
        
        result = self.fib(n-1) + self.fib(n-2)
        self.memory[n] = result
        
        return result
    
    