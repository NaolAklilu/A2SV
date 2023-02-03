n, k = list(map(int, input().split()))

nums = list(map(int, input().split()))
nums.sort()

if k < n:
    if k == 0:
        if nums[0]-1 > 0:
            print(nums[0]-1)
        else:
            print(-1)
            
    elif nums[k-1] != nums[k]:
        if nums[k-1] > 0:
            print(nums[k-1])
        else:
            print(-1)
        
        
    else:
        print(-1)
        
else:
    if nums[k-1] > 0:
        print(nums[k-1])
    else:
        print(-1)
