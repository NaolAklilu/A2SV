class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        
        for b in range(2, n-1):
            bases = []
            num = n
            
            while num > 1:
                bases.append(num%b)
                num = num//b
            
            bases.append(num)
            
            left, right = 0, len(bases)-1
            
            while left < right:
                if bases[left] != bases[right]:
                    return False
                
                left += 1
                right -= 1
            
        return True