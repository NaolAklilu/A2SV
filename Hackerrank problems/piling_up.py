testCaseNumber = int(input())

for _ in range(testCaseNumber):
    blocksSize = int(input())
    blocks = list(map(int, input().split()))
    stack = []
    left, right = 0, blocksSize - 1
    while left <= right:
        if blocks[left] > blocks[right]:
            if len(stack) == 0:
                stack.append(blocks[left])
                left += 1
            else:
                if stack[-1] >= blocks[left]:
                    stack.append(blocks[left])
                    left += 1
                else:
                    print("No")
                    break
                
        else:
            if len(stack) == 0:
                stack.append(blocks[right])
                right -= 1
            else:
                if stack[-1] >= blocks[right]:
                    stack.append(blocks[right])
                    right -= 1
                else:
                    print("No")
                    break
    else:
        print("Yes")
                    
    
