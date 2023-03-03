class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        
        while left <= right:
            mid = left + (right-left)//2
            
            if mid**2 == x:
                return mid
            
            elif mid**2 < x and right-left > 1:
                left = mid
                
            elif mid**2 > x and right-left > 1:
                right = mid
                
            else:
                if right ** 2 > x:
                    return left
                else:
                    return right
                
            