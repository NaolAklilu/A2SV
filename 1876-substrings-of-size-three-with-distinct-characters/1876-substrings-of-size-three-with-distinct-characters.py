class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0
        
        charCount = defaultdict(int)
        left = 0
        right = 0
        goodCount = 0
        
        while right<len(s):
            charCount[s[right]] += 1
            if right-left == 2:
                if charCount[s[left]] == 1:
                    if charCount[s[left+1]] == 1:
                        if charCount[s[right]] == 1:
                            goodCount += 1
                            
                charCount[s[left]] -= 1
                left += 1
                
            right += 1
            
        return goodCount
                