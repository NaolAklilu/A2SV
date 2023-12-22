class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        binary = [0] * len(flips)
        k = 0
        count = 0
        
        for i in range(len(flips)):
            binary[flips[i]-1] = 1
            while k < len(flips) and binary[k] == 1:
                k += 1
            
            if i == k-1:
                count += 1
            
        return count
        