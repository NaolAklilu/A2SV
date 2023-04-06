n = int(input())
k = int(input())

dic = {}
for i in range(n):
    dic[i+1] = []

vertices = []
for _ in range(k):
    operation = list(map(int, input().split()))
    if operation[0] == 1:
        dic[operation[1]].append(operation[2])
        dic[operation[2]].append(operation[1])
    
    if operation[0] == 2:
        vertices.append(operation[1])

for num in vertices:
    print(*dic[num])
