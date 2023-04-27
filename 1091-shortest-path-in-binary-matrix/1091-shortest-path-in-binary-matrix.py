class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [(1,0),(-1,0), (0,1), (0,-1), (1,1), (-1, -1), (-1, 1), (1, -1)]
        visited = set()
        n = len(grid)
        
        def inbound(row, col):
            return (0<=row<len(grid) and 0 <= col < len(grid))
        
        queue = deque()
        if grid[0][0] != 0:
            return -1
        
        queue.append((0,0))
        
        count = 0
        while queue:
            count += 1
            curLength = len(queue)
            
            if (n-1, n-1) in queue:
                return count
            
            for _ in range(curLength):
                row, col = queue.popleft()
                
                for row_change, col_change in directions:
                    new_row = row_change + row
                    new_col = col_change + col
                    
                    if (new_row, new_col) not in visited and inbound(new_row, new_col):
                        visited.add((new_row, new_col))
                        

                        if grid[new_row][new_col] == 0:
                            queue.append((new_row, new_col))
                            
                            
        return -1
                            
            

                    
        