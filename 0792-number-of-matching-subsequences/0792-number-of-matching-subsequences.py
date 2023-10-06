class Solution: 
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        charMap = defaultdict(deque)
        count = 0
        
        for char in s:
            charMap[char] = deque([])
        
        for word in words:
            charMap[word[0]].append(word)
        
        for i in range(len(s)):
            char = s[i]
            for i in range(len(charMap[char])):
                word = charMap[char].popleft()
                if len(word[1:]) == 0:
                    count += 1
                
                else:
                    curWord = word[1:]
                    if curWord[0] in charMap:
                        charMap[curWord[0]].append(curWord)
                
        return count
            
        
        