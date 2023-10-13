class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        
        for log in logs:
            if log == '../':
                if stack:
                    stack.pop()
                
            elif log == './':
                continue
                
            else:
                stack.append(log)
        
        countLog = 0
        while stack:
            stack.pop()
            countLog += 1
            
        return countLog
            