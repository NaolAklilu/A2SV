from collections import defaultdict

if __name__ == '__main__':
    d = defaultdict(list)
    entry = list(map(int, input().split()))
    n = entry[0]
    m = entry[1]
        
    A = []
    B = []
    
    for _ in range(0, n):
        A.append(input())
    
    for _ in range(0, m):
        B.append(input())
        
    for char in B:
        if char not in A:
            d[char].append(-1)
        elif len(d[char]) > 0:
            pass
        else:
            for i in range(0, n):
                if A[i] == char:
                    d[char].append(i+1)
             
    for element in B:
        print(*d[element])
