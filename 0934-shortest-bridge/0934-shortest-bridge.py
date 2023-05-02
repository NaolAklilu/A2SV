class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def inbounds(row, col):
            return (0<=row<len(grid) and 0<=col<len(grid[0]))
        
        queue = deque()
        visited = set()
        
        island = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    island.append((i, j))
        
        queue.append(island[0])
        islands = [island[0]]
        count = 0
        while queue:
            length = len(queue)
            
            for _ in range(len(queue)):
                row, col = queue.popleft()
                
                for row_change, col_change in directions:
                    new_row = row_change + row
                    new_col = col_change + col
                    
                    if inbounds(new_row, new_col) and (new_row, new_col) not in visited:
                        visited.add((new_row, new_col))
                        if grid[new_row][new_col] == 1:
                            islands.append((new_row, new_col))
                            queue.append((new_row, new_col))
        
        visited = set()
        for island in islands:
            queue.append(island)
            visited.add(island)
            
        count = -1
        while queue:
            count += 1
            length = len(queue)
            
            for _ in range(len(queue)):
                row, col = queue.popleft()
                
                for row_change, col_change in directions:
                    new_row = row_change + row
                    new_col = col_change + col
                    
                    if inbounds(new_row, new_col):                        
                        if (new_row, new_col) not in visited:
                            if grid[new_row][new_col] == 1:
                                return count
                            visited.add((new_row, new_col))
                            queue.append((new_row, new_col))
                            
                            