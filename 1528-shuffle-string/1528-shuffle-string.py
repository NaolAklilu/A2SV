class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        dic = {}
        for index in range(len(indices)):
            dic[indices[index]] = s[index]
        
        ans = []
        for index in range(len(indices)):
            ans.append(dic[index])
        return "".join(ans)