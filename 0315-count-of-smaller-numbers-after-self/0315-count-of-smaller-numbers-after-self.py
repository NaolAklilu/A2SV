class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = [i, nums[i]]
        
        self.ans = [0] * len(nums)
        def merge_sort(left, right):
            if left == right:
                return [nums[left]]
            
            mid = left + (right-left)//2
            leftHalf = merge_sort(left, mid)
            rightHalf = merge_sort(mid+1, right)
            
            return merge(leftHalf, rightHalf)
        
        def merge(leftHalf, rightHalf):
            left, right = 0, 0
            count = 0
            while left < len(leftHalf):
                while right < len(rightHalf) and rightHalf[right][1] < leftHalf[left][1]:
                    count += 1
                    right += 1
                
                self.ans[leftHalf[left][0]] += count 
                left += 1
            
            ptr1, ptr2 = 0, 0
            merged = []
            while ptr1 < len(leftHalf) and ptr2 < len(rightHalf):
                if leftHalf[ptr1][1] <= rightHalf[ptr2][1]:
                    merged.append(leftHalf[ptr1])
                    ptr1 += 1
                    
                else:
                    merged.append(rightHalf[ptr2])
                    ptr2 += 1
                    
            merged.extend(leftHalf[ptr1:])
            merged.extend(rightHalf[ptr2:])
            
            return merged
        
        merge_sort(0 ,len(nums)-1)
        return self.ans