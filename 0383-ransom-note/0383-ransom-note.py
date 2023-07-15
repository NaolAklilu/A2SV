class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomChar = defaultdict(int)
        magazineChar = defaultdict(int)
        
        for char in ransomNote:
            ransomChar[char] += 1
            
        for char in magazine:
            magazineChar[char] += 1
            
        isExist = True
        for char in ransomChar:
            if ransomChar[char] <= magazineChar[char]:
                continue
            else:
                isExist = False
                break
                
        return isExist
                
        
        