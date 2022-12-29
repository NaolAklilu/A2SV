testCases = int(input())

for _ in range(testCases):
    length = int(input())
    numsList = list(input().split(" "))
    charsList = list(input())
    
    pairDic = {}
    isValid = "Yes"
    for i in range(length):
        if numsList[i] in pairDic.keys():
            if pairDic[numsList[i]] != charsList[i]:
                isValid = "No"
                break
        else:
            pairDic[numsList[i]] = charsList[i]
                
    print(isValid)
