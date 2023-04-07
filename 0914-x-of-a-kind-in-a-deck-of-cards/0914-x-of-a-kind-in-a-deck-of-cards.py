class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def gcd(a,b):
            if min(a,b) == 0:
                return max(a,b)
            return gcd(min(a,b), max(a,b)-min(a,b))
        
        
        dic = defaultdict(int)
        
        for num in deck:
            dic[num] += 1
        
        minCount = min(dic.values())
        
        if minCount <= 1:
            return False
        
        if len(dic.values()) == 1:
            return True
        
        counts = list(dic.values())
        gcd_value = gcd(counts[0], counts[1])
        
        for i in range(len(counts)-1):
            curGcd = gcd(counts[i], counts[i+1])
            gcd_value = min(gcd_value, curGcd)
            
            if gcd_value <= 1:
                return False
            
        return True
        
        
            
        
        
        return True