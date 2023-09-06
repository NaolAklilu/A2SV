class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ptr1 = 0
        ptr2 = 0
        result = []
        
        while ptr1<len(nums1) and ptr2<len(nums2):
            if nums1[ptr1][0] < nums2[ptr2][0]:
                result.append(nums1[ptr1])
                ptr1 += 1
            elif nums1[ptr1][0] > nums2[ptr2][0]:
                result.append(nums2[ptr2])
                ptr2 += 1
            else:
                result.append([nums1[ptr1][0], nums1[ptr1][1]+nums2[ptr2][1]])
                ptr1 += 1
                ptr2 += 1
                
        result.extend(nums1[ptr1:])
        result.extend(nums2[ptr2:])
        
        return result
                
                