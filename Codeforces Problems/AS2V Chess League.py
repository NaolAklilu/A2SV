
def merge(leftHalf, rightHalf, diff):
    
    left, right = 0, 0
    
    while left < len(leftHalf) and right < len(rightHalf):
        if leftHalf[left][1] - rightHalf[right][1] > diff:
            right += 1
        elif rightHalf[right][1] - leftHalf[left][1] > diff:
            left += 1
        else:
            break

    ptr1 = left
    ptr2 = right
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

def mergeSort(left, right, arr, diff):
    if left == right:
        return [arr[left]]
    mid = left + (right - left) // 2
    left_half = mergeSort(left, mid, arr, diff)
    right_half = mergeSort(mid + 1, right, arr, diff)
    
    return merge(left_half, right_half, diff)

k, diff = list(map(int, input().split()))
nums = list(map(int, input().split()))
for i in range(len(nums)):
    nums[i] = [i, nums[i]]

result = mergeSort(0, len(nums)-1, nums, diff)
result.sort()

ans = []
for i in range(len(result)):
    ans.append(result[i][0]+1)
    
print(*ans)
