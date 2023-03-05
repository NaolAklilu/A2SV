testCases = int(input())
 
for _ in range(testCases):
    p, m = list(map(int, input().split()))
    
    minNum = min(p, m)
    possibleTeam = (p+m)//4
    
    print(min(minNum, possibleTeam))
