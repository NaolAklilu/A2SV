class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        matrix = [[0 for _ in range(n+2)] for _ in range(n+2)]
        
        for query in queries:
            row1 = query[0]+1
            col1 = query[1]+1
            row2 = query[2]+1
            col2 = query[3]+1
            
            matrix[row1][col1] += 1
            matrix[row1][col2+1] -= 1
            matrix[row2+1][col1] -= 1
            matrix[row2+1][col2+1] += 1
            
        for row in range(1,n+2):
            for col in range(1,n+2):
                matrix[row][col] = matrix[row-1][col] + matrix[row][col-1] - matrix[row-1][col-1] + matrix[row][col]
        
        ans = []
        for i in range(1,n+1):
            ans.append(matrix[i][1:n+1])
            
        return ans
    
    