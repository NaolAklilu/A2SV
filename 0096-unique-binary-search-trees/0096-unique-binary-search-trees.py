class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 1
        G = 1
        for i in range(n):
            G = G * (4 * i + 2) // (i + 2)
        return G