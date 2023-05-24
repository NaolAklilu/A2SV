class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = []
        n = len(costs)
        
        for first, second in costs:
            diff.append([first, second, first-second])
            
        diff.sort(key=lambda x:x[2])
        
        total = 0
        for i in range(n):
            if i < n//2:
                total += diff[i][0]
            else:
                total += diff[i][1]
                
        return total