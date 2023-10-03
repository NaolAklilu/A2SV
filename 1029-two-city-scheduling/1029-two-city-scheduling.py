class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = []
        for i in range(len(costs)):
            diff.append([costs[i][0] - costs[i][1], i])
        
        diff.sort()
        ans = 0
        
        for index in range(len(diff)):
            if index < len(costs)//2:
                ans += costs[diff[index][1]][0]
            else:
                ans += costs[diff[index][1]][1]
        
        return ans