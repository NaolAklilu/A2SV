class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        set1 = {}
        set2 = {}
        result = []
        
        minIndexSum = float(inf)
        
        for i in range(len(list1)):
            set1[list1[i]] = i
        
        for j in range(len(list2)):
            if list2[j] in set1:
                set2[list2[j]] = j
                
        for string in set2:
            minIndexSum = min(minIndexSum, (set1[string] + set2[string]))

        for string in set2:
            if (set2[string]+set1[string]) == minIndexSum:
                result.append(string)
                
        return result
                
                
        
            
        