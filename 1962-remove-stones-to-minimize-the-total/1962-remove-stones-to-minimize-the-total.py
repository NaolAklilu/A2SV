class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i in range(len(piles)):
            piles[i] *= -1
        
        heapify(piles)
        for _ in range(k):
            pile = heappop(piles)
            heappush(piles, floor(pile/2))
            
        return -1 * (sum(piles))