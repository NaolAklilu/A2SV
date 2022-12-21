k = int(input())
rooms = list(map(int, input().split()))

roomCount = {}
for num in rooms:
    if num in roomCount.keys():
        roomCount[num] += 1
    else:
        roomCount[num] = 1
        
for num in roomCount.keys():
    if roomCount[num] == 1:
        print(num)
