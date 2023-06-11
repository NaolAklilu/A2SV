class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        
        def dfs(curArr, i):
            address = curArr[:]
            if i == len(s) or len(curArr) > 4:
                if len(curArr) == 4:
                    res.append(curArr)
                return      
            
            address.append(s[i])
            dfs(address, i+1)
            
            if int(s[i]) != 0:
                if i+1 < len(s):
                    address1 = curArr[:]
                    address1.append(s[i:i+2])
                    dfs(address1, i+2)
                    

                if i+2 < len(s):
                    if int(s[i:i+3]) < 256:
                        address2 = curArr[:]
                        address2.append(s[i:i+3])
                        dfs(address2, i+3)
                        
            return
                
        dfs([], 0)
        
        ans = []
        for address in res:
            ans.append(".".join(address))
        
        return ans