class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        def isGood(mid):
            if citations[mid] >= len(citations)-mid:
                return True
            else:
                return False
        
        left, right = -1, len(citations)
        while left+1 < right:
            mid = left+(right-left)//2
            
            if isGood(mid):
                right = mid
            else:
                left = mid
                
        return len(citations) - right
    
    