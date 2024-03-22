class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []

        queue = []
        output = []

        for i in range(len(nums)):
            while queue and queue[0][0] <= i - k:
                queue.pop(0)

            while queue and queue[-1][1] < nums[i]:
                queue.pop()

            queue.append([i, nums[i]])

            if i >= k - 1:
                output.append(queue[0][1])

        return output