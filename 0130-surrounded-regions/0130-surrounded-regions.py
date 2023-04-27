class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = [[0 for i in range(len(board[0]))] for j in range(len(board))]
        direction = [(-1,0), (1,0), (0,-1), (0,1)]
        
        boundaryCells = []
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == 0 or i == len(board)-1:
                    boundaryCells.append((i, j))
                else:
                    if j == 0 or j == len(board[0])-1:
                        boundaryCells.append((i, j))
                        
        print(boundaryCells)
        unSurroundCells = set()
        
        def notBoundary(row, col):
            return (0 < row < len(board)-1 and 0 < col < len(board[0])-1)
            
        def traverseRegion(row, col):
            if visited[row][col] == 0:
                visited[row][col] = 1
                
                for row_change, col_change in direction:
                    new_row = row_change + row
                    new_col = col_change + col
                    
                    if notBoundary(new_row, new_col) and board[new_row][new_col] == "O" and visited[new_row][new_col] == 0:
                        unSurroundCells.add((new_row, new_col))
                        traverseRegion(new_row, new_col)
                        
            return 
        
        for row, col in boundaryCells:
            if board[row][col] == "O":
                unSurroundCells.add((row, col))
                traverseRegion(row, col)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i, j) not in unSurroundCells and board[i][j] == "O":
                    board[i][j] = "X"
        
        
                
            
            
            
       
        