class Solution {
public:
    bool find132pattern(vector<int>& nums) {
         if (nums.size() < 3) {
        return false;
    }
    
    std::stack<int> stack;
    int minIndex = -1;
    
    for (int index = nums.size() - 1; index >= 0; index--) {
        if (minIndex != -1 && nums[index] < nums[minIndex]) {
            return true;
        }
        
        while (!stack.empty() && nums[stack.top()] < nums[index]) {
            minIndex = stack.top();
            stack.pop();
        }
        
        stack.push(index);
    }
    
    return false;
    }
};