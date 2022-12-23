A = set(map(int, input().split()))
n = int(input())

sets = []
for i in range(n):
    sets.append(set(map(int, input().split())))
  
isSuperSet = True
for numSet in sets:
    if len(numSet) >= len(A):
        isSuperSet = False
        break
    else:
        for num in numSet:
            if num not in A:
                isSuperSet = False
                break
            
print(isSuperSet)
