class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = []
        for i in range(len(gas)):
            diff.append(gas[i] - cost[i])
        
        if sum(diff) < 0:
            return -1
        
        curSum = 0
        ptr = 0
        for i in range(len(diff)):
            curSum += diff[i]
            if curSum < 0:
                curSum = 0
                ptr = i + 1
                
        return ptr
                
            
            