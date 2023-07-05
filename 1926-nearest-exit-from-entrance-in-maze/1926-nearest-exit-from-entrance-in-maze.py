class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        directions = [(1,0),(-1,0), (0,1), (0,-1)]
        
        def inbound(row, col):
            return (0<=row<len(maze) and 0<=col<len(maze[0]))
        
        def inboundary(row, col):
            return (row == 0 or row == len(maze)-1 or col == 0 or col == len(maze[0])-1)
        
        queue = deque([(entrance[0], entrance[1])])
        visited = set()
        visited.add((entrance[0], entrance[1]))
        
        distance = 0
        while queue:
            distance += 1  
            curLength = len(queue)
            
            for _ in range(curLength):
                row, col = queue.popleft()
                
                for row_change, col_change in directions:
                    new_row = row + row_change
                    new_col = col + col_change
                    
                    if  inbound(new_row, new_col) and (new_row, new_col) not in visited:
                        if maze[new_row][new_col] == ".":
                            if inboundary(new_row,new_col):
                                return distance
                            else:
                                queue.append((new_row, new_col))
                                visited.add((new_row, new_col))
                                
                                
        return -1