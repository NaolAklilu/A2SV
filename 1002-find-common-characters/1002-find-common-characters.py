class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        arrayDic = []
        commonChars = []
        offset = ord('a')

        for word in words:
            curArrayDic = [0] * 26
            for char in word:
                asciiValue = ord(char)
                curArrayDic[asciiValue - offset] += 1
                
            arrayDic.append(curArrayDic)
        
       
        for i in range(26):
            minCount = arrayDic[0][i]
            for array in arrayDic:
                if array[i] < minCount:
                    minCount = array[i]
            if minCount > 0:      
                commonChars.extend([chr(i+offset)] * minCount)
                
        return commonChars