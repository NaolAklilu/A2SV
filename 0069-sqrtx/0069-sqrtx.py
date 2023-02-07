class Solution:
    def mySqrt(self, x: int) -> int:
        for num in range(x+1):  
            if num*num == x:
                return num
            elif num*num < x:
                curNum = num
            else:
                return curNum
            
        return 0