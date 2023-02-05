class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left = 0
        right = len(needle)
        
        indices = []
        while left < len(haystack)-len(needle)+1:
            if haystack[left:left+right] == needle:
                indices.append(left)
            left += 1
        
        if len(indices) != 0:
            return indices[0]
        return -1