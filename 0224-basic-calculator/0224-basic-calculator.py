class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        
        strings = []
        left, right = 0, 0
        while right < len(s):
            if s[right] == '(' or s[right] == ')' or s[right] == '+' or s[right] == '-':
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
            if char == " ":
                continue
            elif char == "(":
                stack.append(char)
            elif char == '+' or char == '-':
                stack.append(char)
            elif char.isnumeric():
                if stack and (stack[-1] == '+' or stack[-1] =='-'):
                    sign = stack.pop()
                    
                    if sign == "-":
                        if stack and (str(stack[-1]).isnumeric() or str(stack[-1])[0] == '-'):
                            num = stack.pop()
                            stack.append(num - int(char))
                        else:
                            stack.append(-1*int(char))
                    else:
                        num = stack.pop()                            
                        stack.append(num + int(char))
                        
                else:
                    stack.append(int(char))
            else:
                num1 = stack.pop()
                stack.pop()
                if stack and (stack[-1] == '+' or stack[-1] =='-'):
                    sign = stack.pop()
                    if sign == "-":
                        if stack and (str(stack[-1]).isnumeric() or str(stack[-1])[0] == '-'):
                            num = stack.pop()
                            stack.append(num - num1)
                        else:
                            stack.append(-1*num1)
                    else:
                        num = stack.pop()                            
                        stack.append(num + num1)
                else:
                    stack.append(num1)
                    
        return stack.pop()   
        
                
