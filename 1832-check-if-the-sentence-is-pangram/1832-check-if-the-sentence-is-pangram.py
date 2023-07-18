class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        chars = defaultdict(int)
        
        for char in sentence:
            chars[char] += 1
            
        if len(chars) < 26:
            return False 
        return True
        