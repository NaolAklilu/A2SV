engLength = int(input())
engSubscribers = set(map(int, input().split()))
frenLength = int(input())
frenchSubscribers = set(map(int, input().split()))

print(len(engSubscribers.union(frenchSubscribers)))
