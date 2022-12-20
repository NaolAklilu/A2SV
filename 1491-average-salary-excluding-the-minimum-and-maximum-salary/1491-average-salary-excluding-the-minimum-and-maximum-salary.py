class Solution:
    def average(self, salary: List[int]) -> float:
        minNumber = salary[0]
        maxNumber = salary[0]
        
        total = 0
        for num in salary:
            total += num
            if num > maxNumber:
                maxNumber = num
            elif num < minNumber:
                minNumber = num
                
        total -= (minNumber + maxNumber)
        
        return (total/ (len(salary) - 2)) + 0.00000