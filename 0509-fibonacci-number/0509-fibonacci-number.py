class Solution:
    
    def __init__(self):
        self.memory = defaultdict(int)
    
    def fib(self, n: int) -> int:
        if n <= 1:
            self.memory[n] = n
            return self.memory[n]
        
        self.memory[n] = self.fib(n-1) + self.fib(n-2)
        
        return self.memory[n]
    
    