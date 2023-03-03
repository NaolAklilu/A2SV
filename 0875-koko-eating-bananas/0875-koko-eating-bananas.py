class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def isGood(k):
            countHr = 0
            for pile in piles:
                countHr += ceil(pile/k)
                
            if countHr <= h:
                return True
            else:
                return False
        
        
        left = 0
        right = max(piles)
        
        while left+1 < right:
            mid = left + (right - left)//2
            
            if isGood(mid):
                right = mid
            else:
                left = mid
                
        return right