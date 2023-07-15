class Solution:
    def judgeCircle(self, moves: str) -> bool:
        vertical = 0
        horizontal = 0
        
        for char in moves:
            if char == "U":
                vertical += 1
            elif char == "D":
                vertical -= 1
            elif char == "R":
                horizontal += 1
            elif char == "L":
                horizontal -= 1
                
        if horizontal == 0 and vertical == 0:
            return True
        return False