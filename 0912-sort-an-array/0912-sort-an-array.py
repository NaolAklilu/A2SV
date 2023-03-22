class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge_sort(left, right):
            if right == left:
                return [nums[left]]
            
            mid = left + (right-left)//2
            left_half = merge_sort(left, mid)
            right_half = merge_sort(mid+1, right)
            
            return merge(left_half, right_half)
        
        def merge(left_half, right_half):
            ptr1, ptr2 = 0, 0
            
            res = []
            while ptr1 < len(left_half) and ptr2 < len(right_half):
                if left_half[ptr1] <= right_half[ptr2]:
                    res.append(left_half[ptr1])
                    ptr1 += 1
                else:
                    res.append(right_half[ptr2])
                    ptr2 += 1
                
            res.extend(left_half[ptr1:])
            res.extend(right_half[ptr2:])
        
            return res
        
        return merge_sort(0, len(nums)-1)
            