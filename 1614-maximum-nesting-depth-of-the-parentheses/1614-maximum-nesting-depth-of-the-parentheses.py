class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        maxDepth = 0
        
        for char in s:
            if char == "(":
                stack.append("(")
                maxDepth = max(maxDepth, len(stack))
            elif char == ")":
                stack.pop()
            
        return maxDepth