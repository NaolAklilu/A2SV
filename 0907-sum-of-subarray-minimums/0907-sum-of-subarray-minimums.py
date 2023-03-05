class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        rightMin = [len(arr)] * len(arr)
        leftMin = [-1] * len(arr)
        
        # Find the first right minimum index
        for i in range(len(arr)):
            while stack and arr[stack[-1]] >= arr[i]:
                rightMin[stack.pop()] = i
            stack.append(i)
            
        stack.clear()
        # Find the first left minimum index
        for i in range(len(arr)-1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                leftMin[stack.pop()] = i
            
            stack.append(i)
            
        minSum = 0
        modValue = (10**9)+7
        for i in range(len(arr)):
            leftLength =  i - leftMin[i]
            rightLength = rightMin[i]-i
            
            minSum += (arr[i]*leftLength*rightLength)%modValue
        
        return minSum%modValue