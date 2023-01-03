class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        columns = []
        
        for i in range(len(grid)):
            col = []
            for j in range(len(grid)):
                col.append(grid[j][i])
            columns.append(tuple(col))
           
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid)):
                if tuple(grid[row]) == columns[col]:
                    count += 1
                    
        return count
        