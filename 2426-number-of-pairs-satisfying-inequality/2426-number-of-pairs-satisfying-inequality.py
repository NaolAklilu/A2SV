class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        self.count = 0
        nums = []
        for i in range(len(nums1)):
            nums.append(nums1[i] - nums2[i])
        
        def merge_sort(left, right):
            if left == right:
                return [nums[left]]
            
            mid = left + (right-left)//2
            leftHalf = merge_sort(left, mid)
            rightHalf = merge_sort(mid+1, right)
            
            return merge(leftHalf, rightHalf)
        
        def merge(leftHalf, rightHalf):
            left, right = 0, 0
            while left < len(leftHalf):
                while right < len(rightHalf) and rightHalf[right] + diff < leftHalf[left]:
                    right += 1
                    
                self.count += len(rightHalf)-right
                left += 1
                
            ptr1, ptr2 = 0, 0
            merged = []
            while ptr1 < len(leftHalf) and ptr2 < len(rightHalf):
                if leftHalf[ptr1] <= rightHalf[ptr2]:
                    merged.append(leftHalf[ptr1])
                    ptr1 += 1
                else:
                    merged.append(rightHalf[ptr2])
                    ptr2 += 1
                    
            merged.extend(leftHalf[ptr1:])
            merged.extend(rightHalf[ptr2:])
            
            return merged
        
        merge_sort(0, len(nums)-1)
        
        return self.count
        