testCases = int(input())

for _ in range(testCases):
    sizes = list(input().split(" "))
    
    if sizes[0][-1] == sizes[1][-1]:
        if len(sizes[0]) > len(sizes[1]):
            if sizes[0][-1] == "S":
                print("<")
            else:
                print(">")
        elif len(sizes[0]) < len(sizes[1]):
            if sizes[0][-1] == "S":
                print(">")
            else:
                print("<")
        else:
            print("=")
    else:
        if sizes[0][-1] == "L" or sizes[1][-1] == "L":
            if sizes[0][-1] == "L":
                print(">")
            
            else:
                print("<")
        else:
            if sizes[0][-1] == "M":
                print(">")
            else:
                print("<")
