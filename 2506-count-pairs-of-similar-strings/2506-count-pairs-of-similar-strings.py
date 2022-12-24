class Solution:
    def similarPairs(self, words: List[str]) -> int:
        visited = []
        words_set = []
        count = 0
        
        for word in words:
            words_set.append(set(word))
       
        for word in words_set:
            word_count = words_set.count(word)
            if word in visited:
                continue
            if word_count >= 2:
                visited.append(word)
                count += (word_count * (word_count-1))//2
        
        return count
