class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        years = [0] * 101
        startYear = 1950
        
        for birth, death in logs:
            years[birth-startYear] += 1
            years[death-startYear] -= 1
            
        for i in range(1, len(years)):
            years[i] += years[i-1]
        
        maxPopulation = max(years)
        
        for i in range(len(years)):
            if years[i] == maxPopulation:
                return startYear + i