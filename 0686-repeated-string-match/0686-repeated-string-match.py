class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        
        length = len(a) + len(b)-1
        mult = math.ceil(length / len(a))
        
        strings = []
        for i in range(mult):
            strings.append(a)
            
        haystack = ''.join(strings)
        
        LPS = [0 for _ in range(len(b))]
        
        i, j = 0, 1
        while j < len(b):
            if b[i] == b[j]:
                LPS[j] = i+1
                i += 1
                j += 1
            
            elif i == 0:
                j += 1

            else:
                i = LPS[i-1]
        
        
        stringIndex, patternIndex = 0, 0
        while stringIndex < len(haystack):
            if haystack[stringIndex] == b[patternIndex]:
                stringIndex += 1
                patternIndex += 1
                
            elif patternIndex == 0:
                stringIndex += 1
            else:
                patternIndex = LPS[patternIndex - 1]
            
            if patternIndex == len(b):
                index = stringIndex - patternIndex
                return math.ceil((index+len(b))/len(a))
            
        return -1