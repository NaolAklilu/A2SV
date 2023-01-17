class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        length = len(nums)
        distinctNumbers = set()
        for i in range(length):
            distinctNumbers.add(nums[i])
            num = list(str(nums[i]))
            for i in range(len(num)//2):
                num[i], num[len(num)-1-i] = num[len(num)-1-i], num[i]
            
            num = "".join(num)
            distinctNumbers.add(int(num))
            
        return len(distinctNumbers)
            