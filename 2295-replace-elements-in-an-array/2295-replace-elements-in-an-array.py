class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        num_index = {}
        for index in range(len(nums)):
            num_index[nums[index]] = index
        
        for operation in operations:
            index = num_index[operation[0]]
            nums[index] = operation[1]
            num_index.pop(operation[0])
            num_index[operation[1]] = index
        
        return nums