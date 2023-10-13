class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        
        n = len(nums1)
        m = len(nums2)
        
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        for row in range(m-1, -1, -1):
            for col in range(n-1, -1, -1):
                dp[row][col] = max(dp[row][col+1], dp[row+1][col])
                
                if nums1[col] == nums2[row]:
                    dp[row][col] = max(dp[row][col], 1+dp[row+1][col+1])
                    
        return dp[0][0]
                