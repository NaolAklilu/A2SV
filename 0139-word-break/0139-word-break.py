class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[-1] = True
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s) + 1):
                if dp[j] and s[i:j] in wordDict:
                    dp[i] = True
                    break
        return dp[0]