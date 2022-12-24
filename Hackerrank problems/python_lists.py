if __name__ == '__main__':
    N = int(input())
    ans = []
    for command in range(N):
        input_data = list(input().split())
        if input_data[0] == 'insert':
            ans.insert(int(input_data[1]), int(input_data[2]))
        elif input_data[0] == 'print':
            print(ans)
        elif input_data[0] == 'append':
            ans.append(int(input_data[1]))
        elif input_data[0] == 'remove':
            ans.remove(int(input_data[1]))
        elif input_data[0] == 'sort':
            ans.sort()
        elif input_data[0] == 'pop':
            ans.pop()
        elif input_data[0] == 'reverse':
            ans.reverse()
