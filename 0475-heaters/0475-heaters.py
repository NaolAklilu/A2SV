class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        answer = 0

        for house in houses:
            radius = float('inf')
            le = bisect.bisect_right(heaters, house)
            if le > 0:
                radius = min(radius, house - heaters[le-1])
            ge = bisect.bisect_left(heaters, house)
            if ge < len(heaters):
                radius = min(radius, heaters[ge] - house)
            answer = max(answer, radius)

        return answer