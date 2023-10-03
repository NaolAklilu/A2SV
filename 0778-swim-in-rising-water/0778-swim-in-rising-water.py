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
            queue.sort()
            queue.reverse()
            val, (rw, cl) = queue.pop()
            
            visited.add((rw, cl))
            
            time = max(time, val)
            
            if rw == n-1 and cl==n-1:
                break
            
            for row, col in directions:
                curRow = rw + row
                curCol = cl + col
                
                if inBound(curRow, curCol) and (curRow, curCol) not in visited:
                    queue.append([grid[curRow][curCol], (curRow, curCol)])
                        
        return time
                        
                
                