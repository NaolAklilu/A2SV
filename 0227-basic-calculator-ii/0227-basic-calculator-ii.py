class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        strings = []
        left, right = 0, 0
        while right < len(s):
            if s[right] == '+' or s[right] == '-' or s[right] == '*' or s[right] == '/':
                if right-left > 0:
                    strings.append(s[left:right])
                strings.append(s[right])
                right += 1
                left = right
                
            elif s[right] == " ":
                if right-left > 0:
                    strings.append(s[left:right])
                right += 1
                left = right
            else:
                right += 1   
        
        if right - left > 0:
            strings.append(s[left:right])
            
        for char in strings:
            if char.isnumeric():
                if not stack:
                    stack.append(int(char))
                else:
                    if stack[-1] == '*' or stack[-1] == "/":
                        operator = stack.pop()
                        num = stack.pop()
                        
                        if operator =="*":
                            stack.append(num * int(char))
                        else:
                            stack.append(math.floor(num / int(char)))
                    else:
                        stack.append(int(char))
                        
                        
            elif char == "+" or char == "-" or char == "*" or char == "/":
                stack.append(char)
            
        stack.reverse()
        while len(stack) > 1:
            num2 = stack.pop()
            operator = stack.pop()
            num1 =stack.pop()
            
            if operator == "+":
                stack.append(num2 + num1)
            else:
                stack.append(num2 - num1)
            
        return stack.pop()
        
        