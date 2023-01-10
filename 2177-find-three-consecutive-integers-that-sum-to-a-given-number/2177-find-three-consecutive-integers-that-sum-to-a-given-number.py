class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        baseNum = num // 3
        
        numsSum = baseNum-1 + baseNum + baseNum+1
        if numsSum == num:
            return [baseNum-1, baseNum, baseNum+1]
        else:
            return []
        
            