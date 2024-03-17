class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Count the frequency of each element in the array
        freq_counter = {}
        for num in nums:
            if num in freq_counter:
                freq_counter[num] += 1
            else:
                freq_counter[num] = 1

        # Create a list of elements and their frequencies
        elements = list(freq_counter.keys())
        freqs = list(freq_counter.values())

        # Create a hash table to store the frequencies of all elements
        freq_table = {}
        for i in range(len(elements)):
            freq_table[elements[i]] = freqs[i]

        # Use a heap to find the k most frequent elements
        heap = []
        for element, freq in freq_table.items():
            heapq.heappush(heap, (freq, element))
            if len(heap) > k:
                heapq.heappop(heap)

        # Return the k most frequent elements
        result = []
        while heap:
            result.append(heapq.heappop(heap)[1])
        return result