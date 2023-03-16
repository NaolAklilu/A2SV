class Solution:
    def splitString(self, s: str) -> bool:
        self.isExist = False
        
        def helper(index, last):
            if index == len(s):
                self.isExist = True
                return
                
            for i in range(index, len(s)):
                if last == int(s[index:i+1])+1:
                    helper(i+1, int(s[index:i+1]))

            return

        for index in range(len(s)-1):
            helper(index+1, int(s[:index+1]))
            
        return self.isExist