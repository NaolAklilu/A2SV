class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }

        int left = 0;
        int total = 0;
        int minLen = INT_MAX;

        for (int right = 0; right < nums.size(); right++) {
            total += nums[right];
            while (total >= target) {
                minLen = min(minLen, right - left + 1);
                total -= nums[left];
                left++;
            }
        }

        return minLen == INT_MAX ? 0 : minLen;
    }
};