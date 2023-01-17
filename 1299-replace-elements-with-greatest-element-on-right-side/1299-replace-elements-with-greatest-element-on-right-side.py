class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        newArray = [0] * len(arr)
        if len(arr) == 1:
            newArray[-1] = -1
            return newArray
        
        newArray[len(arr)-1] = -1
        maxNum = arr[-1]
        for i in range(len(arr)-2, -1, -1):
            newArray[i] = maxNum
            if maxNum < arr[i]:
                maxNum = arr[i]
                
        return newArray
            