class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minDif = float(inf)
        res = []
        
        for i in range(1, len(arr)):
            minDif = min(minDif, arr[i]-arr[i-1])
        
        for i in range(1, len(arr)):
            if arr[i]-arr[i-1] == minDif:
                res.append([arr[i-1], arr[i]])
                
        return res