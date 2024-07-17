class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustedBy = defaultdict(int)
        trustOn = defaultdict(int)
        
        if len(trust) == 0:
            if n == 1:
                return 1
            return -1
        
        for person, trustedPerson in trust:
            trustedBy[trustedPerson] += 1
            trustOn[person] += 1
            
    
        for p in trustedBy:
            if trustedBy[p] == n-1 and trustOn[p] == 0:
                return p
        
        return -1