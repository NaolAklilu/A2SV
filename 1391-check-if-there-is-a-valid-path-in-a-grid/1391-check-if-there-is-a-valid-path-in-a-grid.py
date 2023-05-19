class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        parent = {}
        rank = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                parent[(i, j)] = (i, j)
                rank[(i, j)] = 1
                
        def find(cell):
            if cell == parent[cell]:
                return cell
            
            parent[cell] = find(parent[cell])
            return parent[cell]
        
        def union(cell1, cell2):
            parent1 = find(cell1)
            parent2 = find(cell2)
            
            if parent1 != parent2:
                if rank[parent1] > rank[parent2]:
                    parent[parent2] = parent1
                    rank[parent1] += rank[parent2]
                    
                else:
                    parent[parent1] = parent2
                    rank[parent2]  += rank[parent1]
                    
            
        def inbound(row, col):
            return (0<=row<len(grid) and 0<=col<len(grid[0]))
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if inbound(i, j+1) and (grid[i][j+1] == 1 or grid[i][j+1] == 3 or grid[i][j+1] == 5):
                        union((i, j), (i, j+1))

                    if inbound(i, j-1) and (grid[i][j-1] == 1 or grid[i][j-1] == 4 or grid[i][j-1] == 6):
                        union((i, j), (i, j-1))

                if grid[i][j] == 2:
                    if inbound(i-1, j) and (grid[i-1][j] == 2 or grid[i-1][j] == 3 or grid[i-1][j] == 4):
                        union((i, j), (i-1, j))

                    if inbound(i+1, j) and (grid[i+1][j] == 2 or grid[i+1][j] == 5 or grid[i+1][j] == 6):
                        union((i, j), (i+1, j))

                if grid[i][j] == 3:
                    if inbound(i, j-1) and (grid[i][j-1] == 1 or grid[i][j-1] == 4 or grid[i][j-1] == 6):
                        union((i, j), (i, j-1))

                    if inbound(i+1, j) and (grid[i+1][j] == 2 or grid[i+1][j] == 5 or grid[i+1][j] == 6):
                        union((i, j), (i+1, j))

                if grid[i][j] == 4:
                    if inbound(i, j+1) and (grid[i][j+1] == 1 or grid[i][j+1] == 3 or grid[i][j+1] == 5):
                        union((i, j), (i, j+1))

                    if inbound(i+1, j) and (grid[i+1][j] == 2 or grid[i+1][j] == 5 or grid[i+1][j] == 6):
                        union((i, j), (i+1, j))

                if grid[i][j] == 5:
                    if inbound(i-1, j) and (grid[i-1][j] == 2 or grid[i-1][j] == 3 or grid[i-1][j] == 4):
                        union((i, j), (i-1, j))

                    if inbound(i, j-1) and (grid[i][j-1] == 1 or grid[i][j-1] == 4 or grid[i][j-1] == 6):
                        union((i, j), (i, j-1))

                if grid[i][j] == 6:
                    if inbound(i-1, j) and (grid[i-1][j] == 2 or grid[i-1][j] == 3 or grid[i-1][j] == 4):
                        union((i, j), (i-1, j))

                    if inbound(i, j+1) and (grid[i][j+1] == 1 or grid[i][j+1] == 3 or grid[i][j+1] == 5):
                        union((i, j), (i, j+1))

            
        return find((0, 0)) == find((len(grid)-1, len(grid[0])-1))
                                
                            
                    
                
                    
                
                        
                    
                    
                    