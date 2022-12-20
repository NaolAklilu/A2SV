class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_string = []
        
        ptr1 = 0
        ptr2 = 0
        
        while ptr1 < len(word1) and ptr2 < len(word2):
            if ptr1 == ptr2:
                merged_string.append(word1[ptr1])
                ptr1 += 1
            else:
                merged_string.append(word2[ptr2])
                ptr2 += 1
        
        if ptr1 < len(word1):
            merged_string.extend(list(word1[ptr1:]))
        
        elif ptr2 < len(word2):
            merged_string.extend(list(word2[ptr2:]))
                
        return "".join(merged_string)