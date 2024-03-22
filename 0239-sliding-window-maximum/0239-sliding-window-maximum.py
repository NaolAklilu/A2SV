class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []

        # Create a monotonic queue to store the indices of the numbers in the window
        queue = deque()

        # Initialize the result
        result = []

        # Iterate over the input array
        for i in range(len(nums)):
            # Remove any elements from the queue that are outside the current window
            while queue and queue[0] < i - k + 1:
                queue.popleft()

            # Remove any elements from the queue that are smaller than the current number
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()

            # Add the current index to the queue
            queue.append(i)

            # If the current window is of size k, add the maximum number in the window to the result
            if i >= k - 1:
                result.append(nums[queue[0]])

        return result