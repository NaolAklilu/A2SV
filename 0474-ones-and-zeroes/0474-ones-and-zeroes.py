class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        results = set()
        pairs = []
        
        for string in strs:
            oneCount = 0
            zeroCount = 0
            
            for char in string:
                if char == '0':
                    zeroCount += 1
                else:
                    oneCount += 1
                
            pairs.append((zeroCount, oneCount))
        
        @cache
        def dp(index, count, zeroCount, oneCount):
            if index == len(strs):
                if zeroCount <= m and oneCount <= n:
                    results.add(count)
                return
            
            dp(index+1, count, zeroCount, oneCount)
            
            if zeroCount <= m and oneCount <= n:
                count += 1
                dp(index+1, count, zeroCount + pairs[index][0], oneCount + pairs[index][1])
                  
            return
        
        dp(0, 0, 0, 0)
        return max(results)
        
            