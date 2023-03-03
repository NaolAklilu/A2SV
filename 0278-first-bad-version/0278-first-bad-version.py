# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if isBadVersion(left):
                return left
            
            if isBadVersion(mid) == True:
                right = mid
            
            else:
                left = mid
                
            if left+1 == right:
                if isBadVersion(left):
                    return left
                else:
                    return right
                
            