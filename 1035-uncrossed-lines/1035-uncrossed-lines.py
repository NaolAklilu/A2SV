class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        
        @cache
        def dp(index1, index2):
            if index1>=len(nums1) or index2 >= len(nums2):
                return 0
            
            path1 = dp(index1+1, index2)
            count = 0
            for i in range(index2, len(nums2)):
                if nums1[index1] == nums2[i]:
                    path1 = max(path1, dp(index1+1, i+1)+1)
            
            return path1
        
        return dp(0, 0)
                