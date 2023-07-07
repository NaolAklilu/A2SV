class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        def inbound(row, col):
            return (0<=row<len(board) and 0<=col<len(board[0]))
        
        directions = [(1,0), (0,1), (0,-1), (-1,0)]
        visited = set()
        
        def findShips(row, col, direction):
            count = 0
            visited.add((row,col))
            if board[row][col] == 'X':
                count += 1
                newRow = row + direction[0]
                newCol = col + direction[1]
                
                print(newRow, newCol)
                if inbound(newRow, newCol) and (newRow, newCol) not in visited:
                    if board[newRow][newCol] == "X":
                        count += findShips(newRow, newCol, direction)
                        
            return count
        
        
        shipCount = 0
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if (row, col) not in visited:
                    maxCount = 0
                    for direction in directions:
                        curCount = findShips(row, col, direction)
                    
                        maxCount = max(maxCount, curCount)
                        if maxCount > 1:
                            shipCount += 1
                            break
                        
                    else:
                        if maxCount > 0:
                            shipCount += 1
                    

        return shipCount
                        
                        