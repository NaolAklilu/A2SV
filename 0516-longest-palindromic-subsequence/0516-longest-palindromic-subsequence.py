class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        cache = {}
        
        def dfs(left, right):
            if left == right:
                return 1
            
            if left > right:
                return 0
            
            temp = right
            while s[temp] != s[left]:
                temp -= 1
            
            if (left, right) not in cache:
                cache[(left, right)] = dfs(left+1, temp-1) + (2 if left != temp else 1)
            
            if (left+1, right) not in cache:
                cache[(left+1, right)] = dfs(left+1, right)

            return  max(cache[(left+1, right)], cache[(left, right)])
            
        
        return dfs(0, len(s)-1)
            
            
            
                