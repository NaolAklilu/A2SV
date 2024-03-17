class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            # Count the frequency of each element in the array
        freq_counter = collections.Counter(nums)

        # Create a min-heap
        min_heap = []

        # Add each element and its frequency to the heap
        for num, freq in freq_counter.items():
            # If the heap is full, check if the current frequency is greater than the smallest frequency in the heap
            if len(min_heap) == k:
                if freq > min_heap[0][0]:
                    # Remove the smallest frequency and add the current frequency
                    heapq.heapreplace(min_heap, (freq, num))
            else:
                # Add the frequency and element to the heap
                heapq.heappush(min_heap, (freq, num))

        # Return the k most frequent elements
        return [x[1] for x in min_heap]