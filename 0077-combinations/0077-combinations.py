class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.cur = []
        self.arr = []
        def backtrack(level):
            if len(self.cur) == k:
                self.arr.append(self.cur[:])
                return
                
            for candidate in range(1, n+1):
                if candidate in self.cur:
                    continue
                
                if self.cur and self.cur[-1] >= candidate:
                    continue

                self.cur.append(candidate)
                backtrack(level + 1)
                self.cur.pop()
                
        backtrack(0)
        
        return self.arr
                
        