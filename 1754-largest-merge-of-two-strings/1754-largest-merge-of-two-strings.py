class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        word1 = list(word1)
        word2 = list(word2)
        
        merged = []
        
        ptr1, ptr2 = 0, 0
        while word1 and word2:
            if word1[ptr1] < word2[ptr2]:
                merged.append(word2.pop(0))
            
            elif word1[ptr1] > word2[ptr2]:
                merged.append(word1.pop(0))
                
            else:
                if len(word1) < len(word2):
                    i = 0
                    while i < len(word1):
                        if word1[i] > word2[i]:
                            merged.append(word1.pop(0))
                            break
                        elif word1[i] < word2[i]:
                            merged.append(word2.pop(0))
                            break
                            
                        i += 1
                      
                    else:
                        if i == len(word1):
                            merged.append(word2.pop(0))
                        
                else:
                    i = 0
                    while i < len(word2):
                        if word1[i] > word2[i]:
                            merged.append(word1.pop(0))
                            break
                        elif word1[i] < word2[i]:
                            merged.append(word2.pop(0))
                            break
                            
                        i += 1 
                     
                    else:
                        if i == len(word2):
                            merged.append(word1.pop(0))
        
            
        merged.extend(word1)
        merged.extend(word2)
        
        return "".join(merged)
                        
                
                    