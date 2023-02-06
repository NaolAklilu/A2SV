testCases = int(input())

for _ in range(testCases):
    n = int(input())
    nums = list(map(int, input().split()))
    
    resultList = [nums[0]]
    
    for num in nums[1:]:
        if resultList[-1] < 0:
            if num < 0:
                if num > resultList[-1]:
                    resultList[-1] = num
            else:
                resultList.append(num)
                
        else:
            if num > 0:
                if num > resultList[-1]:
                    resultList[-1] = num
            else:
                resultList.append(num)
                
    
    print(sum(resultList))
