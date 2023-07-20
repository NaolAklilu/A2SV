class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        index = 0
        
        while index < len(s):
            stack.append(s[index])
            index += 1
            while len(stack) >= 2:
                if stack[-2:len(stack)] == ["A","B"] or stack[-2:len(stack)] == ["C","D"]:
                    stack.pop()
                    stack.pop()
                else:
                    break
       
        return len(stack)
            