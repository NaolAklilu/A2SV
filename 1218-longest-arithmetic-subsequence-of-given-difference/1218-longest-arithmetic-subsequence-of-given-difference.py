class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        memo = defaultdict(int)
        n = len(arr)
        
        memo[arr[n-1]] = 1
        
        for i in range(n-2, -1, -1):
            if arr[i]+difference in memo:
                memo[arr[i]] = memo[arr[i]+difference] + 1  
            else:
                memo[arr[i]] = 1
                
        
        return max(memo.values())
        