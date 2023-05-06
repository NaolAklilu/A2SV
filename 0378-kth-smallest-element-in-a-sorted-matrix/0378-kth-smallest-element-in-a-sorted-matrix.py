class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        oneDimensions = []
        for row in matrix:
            oneDimensions.extend(row)
        
        heapify(oneDimensions)
        
        for _ in range(k-1):
            heappop(oneDimensions)
        
        return heappop(oneDimensions)
        