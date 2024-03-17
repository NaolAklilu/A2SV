class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for first in range(len(nums)-2):
            if first > 0 and nums[first] == nums[first-1]:
                continue
            second, third = first + 1, len(nums)-1
            while second < third:
                if nums[first] + nums[second] + nums[third] == 0:
                    res.append([nums[first], nums[second], nums[third]])
                    second += 1
                    third -= 1
                    while second < third and nums[second] == nums[second-1]:
                        second += 1
                    while second < third and nums[third] == nums[third+1]:
                        third -= 1
                elif nums[first] + nums[second] + nums[third] < 0:
                    second += 1
                else:
                    third -= 1
        return res