class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for char in t:
            if char not in s:
                return char
            else:
                if s.count(char) != t.count(char):
                    return char
            