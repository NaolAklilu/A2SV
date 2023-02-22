class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        left, right = 0, 0
        k = len(p)
        p_dic = defaultdict(int)
        
        for char in p:
            p_dic[char] += 1
        
        cur_dic = defaultdict(int)
        for i in range(k):
            cur_dic[s[i]] += 1
            right = i  
        
        resArray = []
        if cur_dic == p_dic:
            resArray.append(left)
            
        while right < len(s)-1:
            cur_dic[s[left]] -= 1
            if cur_dic[s[left]] == 0:
                cur_dic.pop(s[left])
            
            left += 1
            right += 1
            cur_dic[s[right]] += 1
            
            if cur_dic == p_dic:
                resArray.append(left)
        
        return resArray
        
        