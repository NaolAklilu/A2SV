class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        
        for char in s:
            if char == "(":
                stack.append(char)
                
            else:
                if type(stack[-1]) == int:
                    curValue = stack.pop()
                    stack.pop()
                    curValue *= 2
                    if stack and type(stack[-1]) == int:
                        num = stack.pop()
                        curValue += num
                    stack.append(curValue)
                    
                else:
                    stack.pop()
                    curValue = 1
                    if stack and type(stack[-1]) == int:
                        num = stack.pop()
                        curValue += num
                    stack.append(curValue)
                    
        return stack[-1]
                
            
        
        