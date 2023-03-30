class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        num = x ^ y
           
        for i in range(32):
            if (num >> i) & 1:
                count += 1
                
        return count