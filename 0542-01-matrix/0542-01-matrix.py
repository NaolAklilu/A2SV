class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        def inbound(row, col):
            return (0<=row<len(mat) and 0<=col<len(mat[0]))
        
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        distances = [[float(inf) for i in range(len(mat[0]))] for j in range(len(mat))]
        visited = set()
        queue = deque()
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i,j))
                    visited.add((i, j))
                    distances[i][j] = 0
                    
        distance = 0
        while queue:
            distance += 1
            curLength = len(queue)

            for _ in range(curLength):
                curRow, curCol = queue.popleft()
            
                for row_change, col_change in directions:
                    new_row = row_change + curRow
                    new_col = col_change + curCol

                    if inbound(new_row, new_col) and (new_row, new_col) not in visited:
                        distances[new_row][new_col] = distance
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col))
                
        return distances
                                

            