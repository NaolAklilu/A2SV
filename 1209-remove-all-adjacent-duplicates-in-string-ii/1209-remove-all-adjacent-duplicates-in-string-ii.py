class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for char in s:
            if len(stack) > 0:
                if stack[-1][0] == char and stack[-1][1] == k-1:
                    stack.pop()
                else:
                    if stack[-1][0] == char:
                        stack[-1][1] += 1
                    else:
                        stack.append([char, 1])
            else:
                stack.append([char, 1])
                
        ans= []
        for char, count in stack:
            for _ in range(count):
                ans.append(char)
        
        return "".join(ans)