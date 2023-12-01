class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num_count = defaultdict(int)
        good_count = 0
        
        for num in nums:
            good_count += num_count[num]
            num_count[num] += 1
        
        return good_count