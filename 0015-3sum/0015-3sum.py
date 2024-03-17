class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for first in range(len(nums)):
            second, third = first + 1, len(nums)-1
            
            while second < third:
                if nums[first] + nums[second] + nums[third] == 0:
                    ans = tuple(sorted([nums[first], nums[second], nums[third]]))
                    res.add(ans)
                    second += 1
                    third -= 1
                elif nums[first] + nums[second] + nums[third] < 0:
                    second += 1
                else:
                    third -= 1
            
        return [list(t) for t in res]