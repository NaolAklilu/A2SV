class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        dic = defaultdict(int)
        dic[s[right]] += 1
        
        maxWindow = 0
        while right < len(s):
            maxLength = max(dic.values())
             
            windowLen = right-left+1
            if windowLen-maxLength <= k:
                maxWindow = max(maxWindow, windowLen)
                right += 1
                if right < len(s):
                    dic[s[right]] += 1
                    
            else:
                dic[s[left]] -= 1
                left += 1
            
        return maxWindow
                
                