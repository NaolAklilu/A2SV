class Solution {
    public int pivotIndex(int[] nums) {
         int leftSum = 0;
    int rightSum = 0;

    int totalSum = 0;
    for (int num : nums) {
        totalSum += num;
    }

    for (int i = 0; i < nums.length; i++) {
        if (i == 0) {
            leftSum = 0;
            rightSum = totalSum - leftSum - nums[i];
        } else if (i == nums.length - 1) {
            rightSum = 0;
            leftSum += nums[i - 1];
        } else {
            leftSum += nums[i - 1];
            rightSum = totalSum - leftSum - nums[i];
        }

        if (leftSum == rightSum) {
            return i;
        }
    }

    return -1;
    }
}