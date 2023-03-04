class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        arr = []
        for word in words:
            curDic = defaultdict(int)
            minChar = 'z'
            for char in word:
                minChar = min(minChar, char)
                curDic[char] += 1
                
            arr.append(curDic[minChar])
         
        queryArray = []
        for query in queries:
            curDic = defaultdict(int)
            minChar = 'z'
            for char in query:
                minChar = min(minChar, char)
                curDic[char] += 1
                
            queryArray.append(curDic[minChar])
            
        arr.sort()
        
        result = []
        for query in queryArray:
            left = -1
            right = len(arr)
            
            while left+1 < right:
                mid = left + (right-left)//2
                if arr[mid] > query:
                    right = mid
                else:
                    left = mid
            
            result.append(len(arr)-right)  
                
        return result