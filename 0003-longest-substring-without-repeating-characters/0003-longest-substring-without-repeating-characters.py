class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left, right = 0, 0
        longestLen = 0
        while right < len(s):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            
            charSet.add(s[right])
            longestLen = max(longestLen, right-left+1)
            right += 1
        
        return longestLen