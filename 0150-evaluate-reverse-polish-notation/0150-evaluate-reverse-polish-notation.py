class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        
        stack = []
        
        for char in tokens:
            if char in operators:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                
                if char == '+':
                    stack.append(str(num1 + num2))
                elif char == '-':
                    stack.append(str(num1 - num2))
                elif char == '*':
                    stack.append(str(num1 * num2))
                elif char == '/':
                    num = num1 / num2
                    if num < 0:
                        stack.append(str(ceil(num1 / num2)))
                    else:
                        stack.append(str(floor(num1 / num2)))
                    
            else:
                stack.append(char)
                
        return int(stack[-1])
                        
                
                