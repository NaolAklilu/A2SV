class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        
        def inBound(row, col):
            return 0<=row<len(grid[0]) and 0<=col<len(grid[0])
        
        visited = set()
        queue = []
        queue.append([grid[0][0], (0, 0)])
        time = 0
        
        while queue:
            val, (row, col) = heappop(queue)
            visited.add((row, col))
            
            time = max(time, val)
            
            if row == n-1 and col == n-1:
                break
                
            for rw, cl in directions:
                curRow = rw + row
                curCol = cl + col
                
                if inBound(curRow, curCol) and (curRow, curCol) not in visited:
                    heappush(queue, [grid[curRow][curCol], (curRow, curCol)])
                
        return time
            
            
        
        
                        
                
                