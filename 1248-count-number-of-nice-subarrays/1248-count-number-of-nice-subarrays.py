class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # Solution using prefix sum
        newArray = [0]*len(nums)
        for i in range(len(nums)):
            if nums[i]%2 != 0:
                newArray[i] += 1
            
        dic = defaultdict(int)
        count, curSum = 0, 0
        
        for i in range(len(newArray)):
            curSum += newArray[i]
        
            if curSum == k:
                count += 1
            
            if curSum - k in dic:
                count += dic[curSum - k]
                
            dic[curSum] += 1
            
        
        return count
            
        