class Solution:
    def interpret(self, command: str) -> str:
        stack = list(command)
        res = []
        while stack:
            if stack[-1] == ')':
                if stack[-2] == '(':
                    for _ in range(2):
                        stack.pop()
                    res.insert(0, 'o')
                elif stack[-2] == 'l':
                    for _ in range(4):
                        stack.pop()
                    res.insert(0, 'al')
            else:
                res.insert(0, 'G')
                stack.pop()
                
        return ''.join(res)
            