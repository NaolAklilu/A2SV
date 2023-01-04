class Solution:
    def printVertically(self, s: str) -> List[str]:
        wordsList = s.split()
        
        verticalWords = []
        maxLen = 0
        for word in wordsList:
            if len(word) > maxLen:
                maxLen = len(word)
                
        for index in range(maxLen):
            curWord = []
            countSpace = 0
            for word in wordsList:
                if index >= len(word):
                    countSpace += 1
                else:
                    if countSpace > 0:
                        curWord.append(" " * countSpace)
                        countSpace = 0
                    curWord.append(word[index])
                    
                    
            verticalWords.append("".join(curWord))                    
        
        return verticalWords