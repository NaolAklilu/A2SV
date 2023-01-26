class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for _ in range(k):
            nums.insert(0, nums.pop())
        
        