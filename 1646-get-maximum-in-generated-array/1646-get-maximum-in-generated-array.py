class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        memo = defaultdict(int)
        
        def getMax(num):
            
            if num <= 1:
                memo[num] = num
                return memo[num]
            
            if num not in memo:
                if num%2 == 0:
                    i = num//2
                    if i not in memo:
                        memo[num] = getMax(i)
                    else:
                        memo[num] = memo[i]
                        
                else:
                    i = num // 2
                    memo[num] = getMax(i) + getMax(i+1)
                    
            
            return memo[num]
        
        
        for i in range(n, -1,-1):
            getMax(i)
            
        return max(memo.values())