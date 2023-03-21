class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        self.maxLength = 0
        def backtrack(cur, i):
            if i == len(arr):
                return
            
            temp = cur.copy()
            if len(temp) == 0:
                isExist = False
                cur_arr = set()
                for char in arr[i]:
                    if char in cur_arr:
                        isExist = True
                        break
                    else:
                        cur_arr.add(char)
                
                if not isExist:
                    temp.update(cur_arr)
                    
                self.maxLength = max(self.maxLength, len(temp))
                backtrack(temp, i+1)
                
                
            else:
                isExist = False
                cur_arr = set()
                for char in arr[i]:
                    if char in temp or char in cur_arr:
                        isExist = True
                        break
                    else:
                        cur_arr.add(char)
                        
                if not isExist:
                    temp.update(cur_arr)
                    self.maxLength = max(self.maxLength, len(temp))
                    
                    backtrack(temp, i+1)
                    for char in arr[i]:
                        temp.remove(char)
                    backtrack(temp, i+1)
                
                else:
                    backtrack(temp, i+1)
            
        for i in range(len(arr)):
            backtrack(set(), i)
        
        return self. maxLength

                        