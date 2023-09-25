class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        ans = 0
        
        for i in range(len(nums)):
            bitCount = 0
            
            rep = bin(i)
            for index in range(2, len(rep)):
                if rep[index] == '1':
                    bitCount += 1
            
            if bitCount == k:
                ans += nums[i]
        
        return ans