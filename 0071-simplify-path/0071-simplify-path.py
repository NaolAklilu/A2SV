class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        
        stack = []
        for pth in path:
            if pth == '' or pth == '.':
                continue
            
            elif stack and pth == '..':
                stack.pop()
            
            elif pth != "..":
                stack.append(pth)
        
        
        return "/" + "/".join(stack)