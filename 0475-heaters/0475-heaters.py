class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        
        curRadius = 0
        
        for house in houses:
            idx = bisect.bisect_left(heaters, house)
            if idx == 0:
                curRadius = max(curRadius, heaters[0] - house)
            elif idx == len(heaters):
                curRadius = max(curRadius, house - heaters[-1])
            else:
                curRadius = max(curRadius, min(house - heaters[idx - 1], heaters[idx] - house))
        
        return curRadius