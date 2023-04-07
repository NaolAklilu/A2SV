n = int(input())

matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

roadCount = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            roadCount += 1

print(roadCount//2)
