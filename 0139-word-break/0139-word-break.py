class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dfs(s, wordDict, memo):
            if s in memo: return memo[s]
            if not s: return True
            for word in wordDict:
                if not s.startswith(word):
                    continue
                if dfs(s[len(word):], wordDict, memo):
                    return True
            memo[s] = False
            return False

        return dfs(s, wordDict, {})