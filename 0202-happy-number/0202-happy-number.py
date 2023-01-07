class Solution:
    def isHappy(self, n: int) -> bool:
        sum_set = set()
        while n != 1:
            sum = 0
            for num in str(n):
                sum += int(num) ** 2
                
            n = sum
            if n == 1:
                return True
            
            if n in sum_set:
                return False
            sum_set.add(n)
        
        else:
            return True