class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle[-1])
        m = len(triangle)
        memo = defaultdict(int)
        
        def bottomUp(row, col):
            if 0<= row < m and 0<= col < m:
                return memo[(row, col)]
            
            return 0
            
        for row in range(m-1, -1,-1):
            for col in range(n-(n-row), -1, -1):
                memo[(row, col)] = triangle[row][col]
                memo[(row, col)] += min(memo[(row+1, col)], memo[(row+1, col+1)])
        
        return memo[(0,0)]