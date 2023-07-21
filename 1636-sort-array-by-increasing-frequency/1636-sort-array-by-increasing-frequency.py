class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        numCount = defaultdict(int)
        numbers = []
        for num in nums:
            numCount[num] += 1
            
        for num in numCount:
            numbers.append([num, numCount[num]])
        
        numbers.sort(reverse=True)
        numbers.sort(key=lambda x:x[1])
        result = []
        
        for num, count in numbers:
            result.extend([num] * count)
            
        return result
            