class Solution:
    def helperFunc(self, board, character):
        # check rows
        for row in board:
            if row[0] == character:
                if row[1] == character:
                    if row[2] == character:
                        return True
        
        columns = []
        for index in range(len(board[0])):
            curColumn = []
            for row in board:
                curColumn.append(row[index])
            columns.append(curColumn)
           
        # check Columns
        for column in columns:
            if column[0] == character:
                if column[1] == character:
                    if column[2] == character:
                        return True
        
        # Check diagonals
        # diagonal one
        if board[0][0] == character:
            if board[1][1] == character:
                if board[2][2] == character:
                    return True
        
        # diagonal two
        if board[0][2] == character:
            if board[1][1] == character:
                if board[2][0] == character:
                    return True
                
        return False
        
                
            
    def validTicTacToe(self, board: List[str]) -> bool:
        tictocDic = defaultdict(list)
        
        for idx1 in range(len(board)):
            for idx2 in range(len(board[0])):
                if board[idx1][idx2] == 'X':
                    tictocDic['X'].append((idx1, idx2))
                elif board[idx1][idx2] == 'O':
                    tictocDic['O'].append((idx1, idx2))
                else:
                    tictocDic[' '].append((idx1, idx2))
        
        if 'X' in tictocDic.keys() and 'O' in tictocDic.keys():
            if len(tictocDic['O']) == len(tictocDic['X']):
                isPlayerXWinner = self.helperFunc(board, 'X')
                if isPlayerXWinner == True:
                    return False
                return True
            
            elif len(tictocDic['O']) + 1 == len(tictocDic['X']):
                isPlayerOWinner = self.helperFunc(board, 'O')
                if isPlayerOWinner == True:
                    return False
                return True
            else:
                return False
            
        elif 'X' in tictocDic.keys() and 'O' not in tictocDic.keys():
            if len(tictocDic['X']) == 1:
                return True
            else:
                return False
        elif 'X' not in tictocDic.keys() and 'O' not in tictocDic.keys():
            return True
        else:
            return False