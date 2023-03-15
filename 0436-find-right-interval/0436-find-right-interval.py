class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        result = [-1] * n
        
        for i in range(n):
            intervals[i].append(i)
            
        sorted_intervals = sorted(intervals, key=lambda interval: interval[0])
        
        for i in range(n):
            lastBoundry = intervals[i][1]
            
            left = -1
            right = n
            
            while left+1 < right:
                mid = left + (right-left)//2
                
                if sorted_intervals[mid][0] >= lastBoundry:
                    right = mid
                else:
                    left = mid
        
            if right < n:
                result[i] = sorted_intervals[right][2]
                
        return result