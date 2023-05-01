class Solution:
    def maxProduct(self, words: List[str]) -> int:
        dic = {'a':0, 'b':1, "c":3, "d":4, "e":5, "f":6, "g":7,
               "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14,
               "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21,
               "v":22, "w":23, "x":24, "y":25, "z":26}
        
        bitValues = []
        for word in words:
            bitValue = 0
            for char in word:
                bitValue = bitValue | (1<<dic[char])
                
            bitValues.append(bitValue)
          
        maxLength = 0
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j:
                    if bitValues[i] & bitValues[j] == 0:
                        maxLength = max(maxLength, len(words[i])*len(words[j]))
                        
            
        return maxLength
                