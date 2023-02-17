class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left , right = 0, 0
        res = []
            
        for i in range(len(s)):
            res.append(abs(ord(s[i]) - ord(t[i])))

        preSum = [0]
        total = 0
        for dif in res:
            total += dif
            preSum.append(total)
                
        left, right = 1, 1
        maxLen = 0
        while left < len(preSum) and right < len(preSum):
            if (preSum[right] - preSum[left - 1]) <= maxCost:
                if (right - left + 1) > maxLen:
                    maxLen = right - left + 1
                right += 1
            else:
                if right == left:
                    right += 1
                left += 1
                
        return maxLen