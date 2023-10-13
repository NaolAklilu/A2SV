class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        stack = []
         
        for char in s:
            if char == "(":
                stack.append(char)
            else:
                if not stack:
                    stack.append(char)
                else:
                    curValue = 0
                    while stack and stack[-1] != '(' and stack[-1] != ")":
                        curValue += stack.pop()
                        
                    if not stack:
                        stack.append(curValue)
                        stack.append(char)
                    else:
                        if stack[-1] == '(':
                            curValue += 2
                            stack.pop()
                            stack.append(curValue)
                            
                        else:
                            stack.append(curValue)
                            stack.append(char)
                            

        maxCount = 0   
        curValue = 0
        while stack:
            if str(stack[-1]).isnumeric():
                curValue += stack.pop()
                maxCount = max(maxCount, curValue)
            else:
                curValue = 0
                stack.pop()
                    
        return maxCount