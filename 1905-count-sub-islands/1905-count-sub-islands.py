class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[0 for i in range(len(grid1[0]))] for j in range(len(grid1))]
        
        def inbound(row, col):
            return (0 <= row < len(grid1) and 0 <= col < len(grid1[0]))
        
        def dfs(row, col, visited):
            if grid2[row][col] != grid1[row][col]:
                self.isExist = False
                
            visited[row][col] = 1
            if grid2[row][col] == 1:
                for row_change, col_change in directions:
                    new_row = row + row_change
                    new_col = col + col_change

                    if inbound(new_row, new_col) and visited[new_row][new_col] == 0 and grid2[new_row][new_col] == 1:
                        if grid2[new_row][new_col] != grid1[new_row][new_col]:
                            self.isExist = False
                        dfs(new_row, new_col,visited)

            return
           
        count = 0
        for y in range(len(grid1)):
            for x in range(len(grid1[0])):
                if visited[y][x] == 0:
                    if grid2[y][x] == 0:
                        visited[y][x] = 1
                    else:
                        self.isExist = True
                        dfs(y,x, visited)

                        if self.isExist:
                            count += 1

        return count