/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

int* merge(int* left_half, int left_size, int* right_half, int right_size, int* return_size);
int* merge_sort(int* nums, int left, int right, int* return_size);

int* merge_sort(int* nums, int left, int right, int* return_size) {
    if (right == left) {
        int* result = (int*)malloc(sizeof(int));
        result[0] = nums[left];
        *return_size = 1;
        return result;
    }

    int mid = left + (right - left) / 2;
    int left_size, right_size;
    int* left_half = merge_sort(nums, left, mid, &left_size);
    int* right_half = merge_sort(nums, mid + 1, right, &right_size);

    int* result = merge(left_half, left_size, right_half, right_size, return_size);

    free(left_half);
    free(right_half);

    return result;
}

int* merge(int* left_half, int left_size, int* right_half, int right_size, int* return_size) {
    int ptr1 = 0, ptr2 = 0;
    int* result = (int*)malloc((left_size + right_size) * sizeof(int));
    int idx = 0;

    while (ptr1 < left_size && ptr2 < right_size) {
        if (left_half[ptr1] <= right_half[ptr2]) {
            result[idx++] = left_half[ptr1++];
        } else {
            result[idx++] = right_half[ptr2++];
        }
    }

    while (ptr1 < left_size) {
        result[idx++] = left_half[ptr1++];
    }

    while (ptr2 < right_size) {
        result[idx++] = right_half[ptr2++];
    }

    *return_size = left_size + right_size;
    return result;
}

int* sortArray(int* nums, int numsSize, int* returnSize) {
     return merge_sort(nums, 0, numsSize - 1, returnSize);
}