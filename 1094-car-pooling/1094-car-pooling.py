class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        prefix = [0]*1002
        
        for trip in trips:
            prefix[trip[1]] += trip[0]
            prefix[trip[2]] -= trip[0]
        
        for i in range(1, 1002):
            prefix[i] += prefix[i-1]

        for num in prefix:
            if num > capacity:
                return False
            
        return True
        
        