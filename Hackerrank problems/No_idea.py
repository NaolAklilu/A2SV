n, m  = map(int, input().split())
array = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

happiness = 0
for num in array:
    if num in A:
        happiness += 1
    elif num in B:
        happiness -= 1

print(happiness)
