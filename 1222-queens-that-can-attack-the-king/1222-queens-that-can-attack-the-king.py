class Solution:
    def movePointer(self, queens, row, col, rowDir, colDir):
        validQueens = []
        while row >= 0 and col >= 0 and row < 8 and col < 8:
            if (row, col) in queens:
                validQueens.append([row, col])
                return validQueens
            row += rowDir
            col += colDir
        
        return validQueens
    
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        queens_set = set()
        
        for queen in queens:
            queens_set.add(tuple(queen))
        
        validQueens = []
        
        kingRow = king[0]
        kingCol = king[1]
        
        # move down
        validQueens.extend(self.movePointer(queens_set, kingRow, kingCol, 1, 0))
        
        # move right
        validQueens.extend(self.movePointer(queens_set, kingRow, kingCol, 0, 1))
        
        # move right down
        validQueens.extend(self.movePointer(queens_set, kingRow, kingCol, 1, 1))
        
        # move left down
        validQueens.extend(self.movePointer(queens_set, kingRow, kingCol, 1, -1))
        
        # move right up
        validQueens.extend(self.movePointer(queens_set, kingRow, kingCol, -1, 1))
        
        # move left up
        validQueens.extend(self.movePointer(queens_set, kingRow, kingCol, -1,-1))
        
        # move up
        validQueens.extend(self.movePointer(queens_set, kingRow, kingCol, -1, 0))
        
        # move left
        validQueens.extend(self.movePointer(queens_set, kingRow, kingCol,  0, -1))
        
        return validQueens
        
        
            
            
            
                    
                
            
        
        