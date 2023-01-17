class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        length = len(names)
        for i in range(length-1):
            maxIndex = i
            for j in range(i+1, length):
                if heights[maxIndex] < heights[j]:
                    maxIndex = j
                    
            if maxIndex != i:
                heights[maxIndex], heights[i] = heights[i], heights[maxIndex]
                names[maxIndex], names[i] = names[i], names[maxIndex]
                
        return names
                