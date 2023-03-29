class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]*(n+1)
        
        for i in range(n+1):
            m = i
            while m != 0:
                if m%2 == 1:
                    ans[i]+= 1
                m //= 2
        
        return ans
            
            
            