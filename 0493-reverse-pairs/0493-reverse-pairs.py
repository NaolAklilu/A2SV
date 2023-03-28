class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.totalCount = 0
        
        def merge_sort(left, right):
            if left == right:
                return [nums[left]]
            
            mid = left + (right-left)//2
            leftHalf = merge_sort(left, mid)
            rightHalf = merge_sort(mid+1, right)
            
            return merge(leftHalf, rightHalf)
        
        def merge(leftHalf, rightHalf):
            
            count = 0
            end = 0
            for start in range(len(leftHalf)):
                while end < len(rightHalf) and leftHalf[start] > 2*rightHalf[end]:
                    count += 1
                    end += 1
                self.totalCount += count
            
            merged = []
            left, right = 0, 0
            while left < len(leftHalf) and right < len(rightHalf):
                if leftHalf[left] <= rightHalf[right]:
                    merged.append(leftHalf[left])
                    left += 1
                else:
                    merged.append(rightHalf[right])
                    right += 1
                
            merged.extend(leftHalf[left:])
            merged.extend(rightHalf[right:])
            
            return merged
        
        merge_sort(0, len(nums)-1)
        
        return self.totalCount