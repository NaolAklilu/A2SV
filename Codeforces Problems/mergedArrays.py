n,m = list(map(int, input().split()))
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

mergedArrays = []

ptr1, ptr2 = 0, 0
while ptr1 < len(nums1) and ptr2<len(nums2):
    if nums1[ptr1] < nums2[ptr2]:
        mergedArrays.append(nums1[ptr1])
        ptr1 += 1
        
    else:
        mergedArrays.append(nums2[ptr2])
        ptr2 += 1
        
mergedArrays.extend(nums1[ptr1:])
mergedArrays.extend(nums2[ptr2:])

print(*mergedArrays)
