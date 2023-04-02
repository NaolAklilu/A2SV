class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minNum = min(nums)
        maxNum = max(nums)
        
        def gcd(num1, num2):
            if min(num1, num2) == 0:
                return max(num1, num2)
            
            return gcd(min(num1, num2), max(num1,num2)-min(num1, num2))
        
        return gcd(minNum, maxNum)
        
        