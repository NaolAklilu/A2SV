class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'{':'}', '[':']', '(':')'}
        stack = []
        
        for char in s:
            if char in pairs:
                stack.append(char)
            
            else:
                if not stack:
                    return False
                
                elif pairs[stack[-1]] == char:
                    stack.pop()
                else:
                    return False
        
        if stack:
            return False
        
        return True
    
    
        