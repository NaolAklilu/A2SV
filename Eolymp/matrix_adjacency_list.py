n = int(input())
matrix = []
adjacency_list = {}
for i in range(n):
    adjacency_list[i+1] = []
    matrix.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
           adjacency_list[i+1].append(j+1)


for i in range(n):
    adjacency_list[i+1].sort()
    print(len(adjacency_list[i+1]), *adjacency_list[i+1])
