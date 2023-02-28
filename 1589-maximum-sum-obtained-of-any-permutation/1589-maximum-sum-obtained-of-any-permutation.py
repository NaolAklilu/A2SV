class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        nums.sort(reverse=True)
        
        requestPrefix = [0]*(n+1)
        for request in requests:
            requestPrefix[request[0]] += 1
            requestPrefix[request[1] + 1] -= 1
            
        for i in range(1,len(requestPrefix)):
            requestPrefix[i] += requestPrefix[i-1]
        
        requestPrefix.sort(reverse=True)
        
        totalSum = 0
        for i in range(n):
            totalSum += (nums[i]*requestPrefix[i])
        
        return totalSum%((10**9)+7)
            
             
        
         