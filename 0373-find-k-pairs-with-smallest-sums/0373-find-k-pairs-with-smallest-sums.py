class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        heap =[]
        n = len(nums1)
        m = len(nums2)
        
        for i in range(m):
            heappush(heap, [nums1[0]+nums2[i], 0, i])
                
        result = []  
        
        for _ in range(min(k, n*m)):
            total,left, right = heappop(heap)
            result.append([nums1[left], nums2[right]])
            if (left+1) < n:
                heappush(heap, [nums1[left+1]+nums2[right], left+1, right])
            
        return result