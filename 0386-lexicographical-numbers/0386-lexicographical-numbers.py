class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        nums = [str(i) for i in range(1, n+1)]
        nums.sort()
        for i in range(n):
            nums[i] = int(nums[i])
            
        return nums
            