class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        start, end = 0, n-1
        
        while start <= end:
            mid = (start+end) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[start] <= nums[mid]:
                if nums[start] <= target and nums[mid] >= target:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[end] >= target and nums[mid] < target:
                    start = mid+1
                else:
                    end = mid-1
        
        return -1
                
            
        