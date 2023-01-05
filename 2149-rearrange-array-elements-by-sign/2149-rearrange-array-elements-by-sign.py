class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        posNumbers = []
        negNumbers = []
        
        for num in nums:
            if num > 0:
                posNumbers.append(num)
            else:
                negNumbers.append(num)
                
        modifiedArray = [posNumbers[0]]
        posPtr = 1
        negPtr = 0
        
        while negPtr < len(nums)//2:
            if modifiedArray[-1] > 0:
                modifiedArray.append(negNumbers[negPtr])
                negPtr += 1
            else:
                modifiedArray.append(posNumbers[posPtr])
                posPtr += 1
        
        return modifiedArray
        
        