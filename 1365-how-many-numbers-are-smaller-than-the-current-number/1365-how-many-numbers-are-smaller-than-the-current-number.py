class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        smallerCount = []
        
        for num1 in nums:
            count = 0
            for num2 in nums:
                if num1 > num2:
                    count += 1
            smallerCount.append(count)
            
        return smallerCount