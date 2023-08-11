class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        negatives = set()
        positives = []
        largestNum = -1
        
        for num in nums:
            if num < 0:
                negatives.add(num)
            else:
                positives.append(num)
                
        positives.sort()
        for i in range(len(positives)-1, -1, -1):
            if -1*(positives[i]) in negatives:
                return positives[i]
        return largestNum