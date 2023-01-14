testCases = int(input())

for _ in range(testCases):
    
    n, m = list(map(int, input().split()))
    
    leftBottomDiag = {}
    rightBottomDiag = {}

    boards = []
    for _ in range(n):
        row = list(map(int, input().split()))
        boards.append(row)
    
    for row in range(len(boards)):
        for col in range(len(boards[0])):
            if row+col in rightBottomDiag.keys():
                rightBottomDiag[row+col] += boards[row][col]
                
            elif row+col not in rightBottomDiag.keys():
                rightBottomDiag[row+col] = boards[row][col]
                
            if row-col in leftBottomDiag.keys():
                leftBottomDiag[row-col] += boards[row][col]
                
            elif row-col not in leftBottomDiag.keys():
                leftBottomDiag[row-col] = boards[row][col]

    maxSum = 0       
    for row in range(len(boards)):
        for col in range(len(boards[0])):
            curSum = leftBottomDiag[row-col]
            curSum += rightBottomDiag[row+col]
            curSum -= boards[row][col]
            
            if curSum > maxSum:
                maxSum = curSum
                
    print(maxSum)
            
    
    
