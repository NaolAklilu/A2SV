testCases = int(input())

for _ in range(testCases):
    n = int(input())
    
    leftMost = -1
    num = 0
    oneCount = 0
    for i in range(32):
        if (n >> i) & 1:
            if oneCount == 0:
                num += 2**i
                leftMost = i
            oneCount += 1

    if oneCount == 0:
        print(1)
    
    elif oneCount == 1:
        if num > 1:
            num += 2**(0)
        else:
            num += 2**(leftMost+1)
        
        print(num)
        
    else:
        print(num)
