class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        counts = Counter(nums)
        maxCount = max(counts.values())
        
        maxCountNums = []
        for val in counts:
            if counts[val] == maxCount:
                maxCountNums.append(val)
                
        minSize = float(inf)
        for num in maxCountNums:
            left, right = 0, len(nums)-1
            
            while left <= right:
                if nums[left] != num:
                    left += 1
                
                if nums[right] != num:
                    right -= 1
                
                if nums[left] == num and nums[right] == num:
                    minSize = min(minSize, right-left+1)
                    break
        
        return minSize

            