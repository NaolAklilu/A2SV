n, m = list(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

ans = []
count = 0
ptr1 = 0
for ptr2 in range(m):
    while ptr1 < n and arr1[ptr1] < arr2[ptr2]:
        count += 1
        ptr1 += 1
        
    ans.append(count)
    
print(*ans)
