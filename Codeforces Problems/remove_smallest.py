testCases = int(input())
for _ in range(testCases):
    n = int(input())
    nums = list(map(int, input().split()))
    
    isExist = True
    nums.sort()
    left = 0
    right = 1
    while right < len(nums):
        if nums[right] - nums[left] <= 1:
            right += 1
            left += 1
        else:
            isExist = False
            break
        
    if isExist:
        print("YES")
    else:
        print("NO")
