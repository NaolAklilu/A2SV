class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        vowels = {
            'a': ['a', 'e', 'i', 'o', 'u'],
            'e': ['e', 'i', 'o', 'u'],
            'i': ['i', 'o', 'u'],
            'o': ['o', 'u'],
            'u': ['u']
        }
        
        
        def dfs(char, curCount):
            if curCount == n:
                return 1
            
            count = 0
            for letter in vowels[char]:
                count += dfs(letter, curCount + 1)
                
            return count
        
        totalCount = 0
        for char in vowels:
            totalCount += dfs(char, 1)
        
        return totalCount
            