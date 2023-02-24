class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        decreasingQueue = deque()
        increasingQueue = deque()
        
        left= 0
        res = 0
        
        for right in range(len(nums)):
            while decreasingQueue and decreasingQueue[-1] > nums[right]:
                decreasingQueue.pop()
            
            decreasingQueue.append(nums[right])
            
            while increasingQueue and increasingQueue[-1] < nums[right]:
                increasingQueue.pop()
        
            increasingQueue.append(nums[right])
            
            
            while increasingQueue[0] - decreasingQueue[0] > limit:
                if nums[left] == decreasingQueue[0]:
                    decreasingQueue.popleft()
                    
                if nums[left] == increasingQueue[0]:
                    increasingQueue.popleft()
                
                left += 1 
            
            res = max(res, right-left+1)
        return res
                
                
            