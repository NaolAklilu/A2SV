class Solution:
    def isValidSquare(self, square):
        numSet = set()
        for i in range(3):
            
            for j in range(3):
                if square[i][j] in numSet:
                    return False
                else:
                    if square[i][j].isnumeric():
                        if int(square[i][j]) < 1 or int(square[i][j]) > 9:
                            return False
                        
                        numSet.add(square[i][j])
                        
        return True
            
        
        
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        newBoard = [[] for _ in range(9)]
        
        for i in range(9):
            firstRow = []
            secondRow = []
            thirdRow = []
            row = set()
            for j in range(9):
                if board[i][j] in row:
                    return False
                if board[i][j].isnumeric():
                    row.add(board[i][j])
                    
                if j < 3:
                    firstRow.append(board[i][j])
                elif j < 6:
                    secondRow.append(board[i][j])
                else:
                    thirdRow.append(board[i][j])
            if i < 3:
                    newBoard[0].append(firstRow)
                    newBoard[1].append(secondRow)
                    newBoard[2].append(thirdRow)
            elif i < 6:
                newBoard[3].append(firstRow)
                newBoard[4].append(secondRow)
                newBoard[5].append(thirdRow)
            else:
                newBoard[6].append(firstRow)
                newBoard[7].append(secondRow)
                newBoard[8].append(thirdRow) 
                
        for i in range(9):
            col = set()
            for row in board:
                if row[i] in col:
                    return False
                if row[i].isnumeric():
                    col.add(row[i])
                    
        
        for square in newBoard:
            isSquareValid = self.isValidSquare(square)
            if isSquareValid == False:
                return False
        
        return True