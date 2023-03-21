class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        self.visited = set()
        self.result = []
        def backtracking(cur, i):
            if i == len(nums):
                return
            
            for i in range(i, len(nums)):
                temp = cur[:]
                if len(temp) > 0:
                    if temp[-1] <= nums[i]:
                        temp.append(nums[i])
                        if tuple(temp) not in self.visited:
                            self.result.append(temp[:])
                            self.visited.add(tuple(temp))
                        backtracking(temp, i+1)
                        temp.pop()
                        backtracking(temp, i+1)
                    else:
                        backtracking(temp, i+1)
                        
                else:
                    temp.append(nums[i])
                    backtracking(temp, i+1)
                    
                    
        backtracking([], 0)
        
        return self.result
                
                
                    