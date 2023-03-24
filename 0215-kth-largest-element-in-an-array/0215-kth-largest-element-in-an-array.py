class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def quick_sort(start, end):
            if end-start <= 0:
                return 
            
            pivot = nums[start]
            write = start+1
            
            for read in range(start+1, end+1):
                if nums[read] <= pivot:
                    nums[read], nums[write] = nums[write], nums[read]
                    write += 1
                    
            nums[start], nums[write-1] = nums[write-1], nums[start]
            if write-1 == len(nums)-k:
                return
            
            elif write-1 < len(nums)-k:
                quick_sort(write, end)
            else:
                quick_sort(start, write-2)
            
        quick_sort(0, len(nums)-1)
        
        return nums[-k]
            
            