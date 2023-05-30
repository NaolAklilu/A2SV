class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = defaultdict(int)
        length = len(nums)    
            
        if len(nums) <= 3:
            return max(nums)
        
        def dp(n):
            if n == 0:
                memo[n] = nums[n]
                return memo[n]
            
            elif n == 1:
                memo[n] = max(nums[0], nums[1])
                return memo[n] 
            
            if n not in memo:
                memo[n] = max(dp(n-1), dp(n-2) + nums[n])
                       
            return memo[n]
        
        end = nums[-1]
        nums.pop()
        right = dp(len(nums)-1)
        nums.pop(0)
        nums.append(end)
        memo.clear()
        left = dp(len(nums)-1)
                           
        return max(left, right)
        
                           
        