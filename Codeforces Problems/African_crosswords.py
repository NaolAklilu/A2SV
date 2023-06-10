n, m = list(map(int, input().split()))

grid = []
for i in range(n):
    grid.append(list(input()))


duplicated = set()
for row in range(n):
    for col in range(m):
        # row wise check
        for i in range(m):
            if (row, col) == (row, i):
                continue
            
            if grid[row][col] == grid[row][i]:
                duplicated.add((row, col))
                duplicated.add((row, i))
                
        # Column wise check
        for j in range(n):
            if (row, col) == (j, col):
                continue
            
            if grid[row][col] == grid[j][col]:
                duplicated.add((row, col))
                duplicated.add((j, col))
                

ans = []
for row in range(n):
    for col in range(m):
        if (row, col) not in duplicated:
            ans.append(grid[row][col])
            
print("".join(ans) )

        
