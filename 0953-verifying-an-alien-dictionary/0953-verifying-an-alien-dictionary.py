class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        lexi_order = {}
        for char in order:
            lexi_order[char] = order.index(char)
            
        word_in_int = []
        for word in words:
            temp = []
            for char in word:
                temp.append(lexi_order[char])
            word_in_int.append(temp)
        
        ptr = 0
        while ptr < len(word_in_int)-1:
            if word_in_int[ptr] > word_in_int[ptr+1]:
                return False
            else:
                ptr += 1
                
        return True
        