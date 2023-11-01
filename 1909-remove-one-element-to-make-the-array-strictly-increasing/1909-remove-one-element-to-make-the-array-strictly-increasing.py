class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        failPosition = []
    
        for i in range(1, len(nums)):
            if nums[i]-nums[i-1] <= 0:
                if i-2 >= 0:
                    if nums[i-2] >= nums[i]:
                        failPosition.append(i)
                    else:
                        failPosition.append(i-1)
                else:
                    failPosition.append(i-1)

        if len(failPosition) > 1:
            return False

        elif len(failPosition) == 0:
            return True

        else:
            if failPosition[0]-1 < 0 or failPosition[0]+1 == len(nums):
                return True

            else:
                if nums[failPosition[0]+1]-nums[failPosition[0]-1] <= 0:
                    return False

                return True
