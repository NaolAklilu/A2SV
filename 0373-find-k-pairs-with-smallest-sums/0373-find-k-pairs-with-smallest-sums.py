class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        
        if not nums1 or not nums2:
            return []

        heap = []
        for i in range(len(nums1)):
            # we add the pair (nums1[i] + nums2[0], i, 0) into the heap
            heapq.heappush(heap, [nums1[i] + nums2[0], i, 0])

        # take the smallest (top) element from the heap
        res = []
        while len(res) < k and heap:
            _, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                # we add the pair (nums1[i] + nums2[j+1], i, j+1) into the heap
                heapq.heappush(heap, [nums1[i] + nums2[j+1], i, j+1])
        return res
        