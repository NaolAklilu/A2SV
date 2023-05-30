class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = defaultdict(tuple)
        
        def findPath(x, y):
            if x == n-1 or y == m-1:
                return 1
            
            if (x, y) not in memo:
                memo[(x, y)] = findPath(x+1, y) + findPath(x, y+1)
                
            return memo[(x, y)]
        
        return findPath(0, 0)
            