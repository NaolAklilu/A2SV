class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []

        queue = deque()
        result = []
        for i in range(len(nums)):
            while queue and queue[0] < i - k + 1:
                queue.popleft()

            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()

            queue.append(i)

            if i >= k - 1:
                result.append(nums[queue[0]])

        return result