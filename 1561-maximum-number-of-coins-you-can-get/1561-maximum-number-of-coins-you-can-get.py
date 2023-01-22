class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        pileCount = len(piles)//3
        
        MaxCoins = 0
        step = 1
        while pileCount > 0:
            MaxCoins += piles[-2*step]
            step += 1
            pileCount -= 1
        
        return MaxCoins