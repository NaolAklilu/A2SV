class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap =[]
        n = len(nums1)
        m = len(nums2)
        
        for i in range(m):
            heapq.heappush(heap, [nums1[0]+nums2[i], 0, i])
                
        result = []  
        
        for _ in range(min(k, n*m)):
            total,left, right = heapq.heappop(heap)
            result.append([nums1[left], nums2[right]])
            if (left+1) < n:
                heapq.heappush(heap, [nums1[left+1]+nums2[right], left+1, right])
            
        return result