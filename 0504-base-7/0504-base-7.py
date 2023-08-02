class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        
        isNegative = num<0
        num = abs(num)
        
        result = []
        while num != 0:
            result.append(str(num%7))
            num = num//7
        
        if isNegative:
            result.append("-")
        result.reverse()
        
        return "".join(result)
        
    