class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        totalSum = 0
        while k > 0 and numOnes > 0:
            k -= 1
            numOnes -= 1
            totalSum += 1
        
        while k > 0 and numZeros > 0:
            k -= 1
            numZeros -= 1
        
        while k > 0 and numNegOnes > 0:
            k -= 1
            numNegOnes -= 1
            totalSum -= 1
            
        return totalSum