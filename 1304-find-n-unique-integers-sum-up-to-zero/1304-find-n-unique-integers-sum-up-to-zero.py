class Solution:
    def sumZero(self, n: int) -> List[int]:
        half =  n//2
        isEven = False
        ans = []
        if n%2 == 0:
            isEven = True
        
        for i in range(half):
            ans.append(-1*(half-i))

        if isEven == False:
            ans.append(0)
            
        for i in range(half):
            ans.append(half-i)
            
        return ans