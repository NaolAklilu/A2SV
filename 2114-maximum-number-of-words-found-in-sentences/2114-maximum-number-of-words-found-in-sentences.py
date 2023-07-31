class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxLength = 0
        
        for sentence in sentences:
            lst = list(sentence.split(" "))
            maxLength = max(maxLength, len(lst))
            
        return maxLength
        