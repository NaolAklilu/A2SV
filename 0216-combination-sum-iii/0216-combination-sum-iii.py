class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [1, 2, 3, 4 ,5, 6, 7, 8, 9]
        results = []
        
        def dp(index, curAmount, curNums):
            curNums = curNums[:]
            if index == len(nums):
                if curAmount == 0 and len(curNums) == k:
                    if curNums not in results:
                        results.append(curNums)
                return
            
            if len(curNums) > k:
                return
            
            dp(index+1, curAmount, curNums)
            if nums[index] <= n:
                curNums.append(nums[index])
                dp(index + 1, curAmount - nums[index], curNums)
                curNums.pop()
                
            return
        
        dp(0, n, [])
        return results