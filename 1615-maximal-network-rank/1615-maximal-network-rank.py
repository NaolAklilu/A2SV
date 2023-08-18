class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        roadPairs = defaultdict(set)
        
        for left, right in roads:
            roadPairs[left].add(right)
            roadPairs[right].add(left)
        
        maxCount = 0
        for city1 in roadPairs:
            for city2 in roadPairs:
                if city1 != city2:
                    len1 = len(roadPairs[city1])
                    len2 = len(roadPairs[city2])
                    if city1 in roadPairs[city2]:
                        maxCount = max(maxCount, len1+len2-1)
                    else:
                        maxCount = max(maxCount, len1+len2)

        return maxCount