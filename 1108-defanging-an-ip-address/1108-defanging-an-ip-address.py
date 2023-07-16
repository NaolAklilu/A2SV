class Solution:
    def defangIPaddr(self, address: str) -> str:
        dot = "[.]"
        updatedIp = []
        
        for char in address:
            if char == ".":
                updatedIp.append(dot)
            else:
                updatedIp.append(char)
        
        return "".join(updatedIp)