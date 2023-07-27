class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        dic1 = defaultdict(int)
        dic2 = defaultdict(int)
        result = []
        
        for value, weight in items1:
            dic1[value] = weight
        
        for value, weight in items2:
            dic2[value] = weight
            
        for val in dic1:
            result.append([val, dic1[val]+dic2[val]])
        for val in dic2:
            if val not in dic1:
                result.append([val, dic2[val]])
                
        result.sort()
        return result
        
            