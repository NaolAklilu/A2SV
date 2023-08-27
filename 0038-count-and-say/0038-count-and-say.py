class Solution:
    def countAndSay(self, n: int) -> str:
        
        nums = ["1"]
        if n == 1:
            return "1"
        
        for i in range(1, n):
            left, right = 0, 0
            curCount = 0
            newNums = []
            
            while right < len(nums):
                if nums[right] == nums[left]:
                    curCount += 1
                    right += 1
                else:
                    newNums.append(str(curCount))
                    newNums.append(nums[left])
                    curCount = 0
                    left = right
            
            newNums.append(str(curCount))
            newNums.append(nums[left])

            nums = newNums
        
        return "".join(nums) 