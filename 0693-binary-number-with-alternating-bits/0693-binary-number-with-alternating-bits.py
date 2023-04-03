class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        res = []      
        
        for i in range(n.bit_length()):          
            if not res:
                 res.append((n >> i) & 1)
            else:
                lastDigit = (n >> i) & 1
                if lastDigit == 1:
                    if res[-1] == 0:
                        res.append((n >> i) & 1)
                    else:
                        return False
                else:
                    if res[-1] == 1:
                        res.append((n >> i) & 1)
                    else:
                        return False     
       
        return True
    