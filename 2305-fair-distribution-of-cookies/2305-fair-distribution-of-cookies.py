class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.res = float(inf)
        self.cur = [0] * k
        
        cookies.sort(reverse=True)
        
        def backtrack(cur, index):
            if index == len(cookies):
                curDif = max(cur)
                
                if curDif <= self.res :
                    self.res = curDif
            
                return
            
            for i in range(k):
                temp = cur[:]
                if temp[i]+cookies[index] < self.res:
                    temp[i] += cookies[index]
                    backtrack(temp, index+1)
        
        backtrack(self.cur, 0)
        
        return self.res
        
        
            
            