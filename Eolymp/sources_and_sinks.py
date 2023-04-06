n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

sources = set()
sinks = set()

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            sources.add(i+1)
            sinks.add(j+1)

for i in range(1, n+1):
    if (i in sources) and (i in sinks):
        sources.remove(i)
        sinks.remove(i)
    
    elif (i not in sources) and (i not in sinks):
        sources.add(i)
        sinks.add(i)

sources = list(sources)
sinks = list(sinks)

sources.sort()
sinks.sort()

srs = str(len(sources))
sks = str(len(sinks))

print(srs, *sources)
print(sks, *sinks)
