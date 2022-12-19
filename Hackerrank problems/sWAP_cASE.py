def swap_case(s):
    newString = []
    for char in s:
        if char.islower():
            newString.append(char.upper())
        elif char.isupper():
            newString.append(char.lower())
        else:
            newString.append(char)
            
    return "".join(newString)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
