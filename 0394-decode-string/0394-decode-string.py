class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = ""
        for char in s:
            if char != ']':
                if char.isnumeric():
                    num = num + char
                else:
                    if len(num) > 0:
                        stack.append(num)
                    stack.append(char)
                    num = ""
                    
            elif char == ']':
                temp = []
                while stack[-1] != '[':
                    temp.append(stack.pop())
                    
                temp.reverse()
                stack.pop()
                freq = int(stack.pop())
                stack.extend(temp*freq)
            
        return "".join(stack)
                
                