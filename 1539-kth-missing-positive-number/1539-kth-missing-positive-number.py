class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missingCount = 0
        index = 0
        
        for num in range(1, arr[-1]+1):
            if arr[index] != num:
                missingCount += 1
                if missingCount == k:
                    return num
            else:
                index += 1
            
        return arr[-1] + (k - missingCount)
            
        