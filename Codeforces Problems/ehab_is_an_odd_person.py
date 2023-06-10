n = int(input())

nums = list(map(int, input().split()))

evenCount = 0
oddCount = 0

for num in nums:
    if num%2 == 0:
        evenCount += 1
    else:
        oddCount += 1
        
if (evenCount > 0 and oddCount > 0):
    nums.sort()
    ans = []
    for i in range(n):
        ans.append(str(nums[i]))
    
    print(" ".join(ans))
    
else:
    ans = []
    for i in range(n):
        ans.append(str(nums[i]))
        
    print(" ".join(ans))
    
    
    
