class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            # Count the frequency of each element in the array
        freq_counter = {}
        for num in nums:
            if num in freq_counter:
                freq_counter[num] += 1
            else:
                freq_counter[num] = 1

        # Create a list of buckets to store elements based on their frequency
        buckets = [[] for _ in range(len(nums) + 1)]

        # Add each element to its corresponding bucket
        for num, freq in freq_counter.items():
            buckets[freq].append(num)

        # Get the k most frequent elements
        result = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result

        return result