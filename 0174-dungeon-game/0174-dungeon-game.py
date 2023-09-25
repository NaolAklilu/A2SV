class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon[0]),  len(dungeon)
        memo = [[0 for i in range(m)] for j in range(n)]
        
        for row in range(n-1,-1, -1):
            for col in range(m-1, -1, -1):
                right, down = dungeon[row][col], dungeon[row][col]
                
                if col+1>=m and row+1 < n:
                    memo[row][col] = down
                    
                    if memo[row+1][col] < 0:
                        memo[row][col] += memo[row+1][col]                        
                
                elif col+1 < m and row+1 >= n:
                    memo[row][col] = right
                    
                    if memo[row][col+1] < 0:
                        memo[row][col] += memo[row][col+1]
                
                elif col+1 >= m and row+1 >= n:
                    memo[row][col] = dungeon[row][col]
                
                else:
                    if memo[row+1][col] < 0 and memo[row][col+1] < 0:
                        memo[row][col] = dungeon[row][col] + max(memo[row][col+1], memo[row+1][col])
                    else:
                        memo[row][col] = dungeon[row][col]
                        
                    
        result = memo[0][0]
        if result <= 0:
            result -= 1
            return abs(result)
        else:
            return 1
            
        