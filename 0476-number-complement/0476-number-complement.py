class Solution:
    def findComplement(self, num: int) -> int:       
        temp = num
        mask = 1
        ptr = 0
        while temp > 0:
            ptr += 1
            temp >>= 1
    
        for i in range(ptr):
            num ^= mask
            mask <<= 1
        
        return num           
        