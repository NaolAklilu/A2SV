class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        memo = {}
        pairs = []

        for string in strs:
            oneCount = 0
            zeroCount = 0

            for char in string:
                if char == '0':
                    zeroCount += 1
                else:
                    oneCount += 1

            pairs.append((zeroCount, oneCount))

        def dp(index, curPair):
            if index == len(strs):
                return 0

            if (index, curPair) in memo:
                return memo[(index, curPair)]

            include = 0
            if curPair[0] + pairs[index][0] <= m and curPair[1] + pairs[index][1] <= n:
                include = 1 + dp(index + 1, (curPair[0] + pairs[index][0], curPair[1] + pairs[index][1]))

            exclude = dp(index + 1, curPair)

            memo[(index, curPair)] = max(include, exclude)
            return memo[(index, curPair)]

        return dp(0, (0, 0))