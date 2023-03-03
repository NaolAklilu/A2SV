class Solution:
    
    def kthGrammar(self, n: int, k: int) -> int:
        
        def helper(n, k):
            if n == 1:
                return 0
            
            mid = 2 **(n-2)
            if k <= mid:
                result = helper(n-1, k)
                return result

            else:
                result = helper(n-1, k-mid)
                if result == 0:
                    return 1
                else:
                    return 0
          
        
        return helper(n, k)
    