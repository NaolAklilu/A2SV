class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        m = n // 4
        
        charSet = {'Q', 'W', 'E', 'R'}
        
        expected_dic = {'Q':m, 'W':m, 'E':m, 'R':m}
        
        print(expected_dic)
        
        given_dic = defaultdict(int)
        for char in s:
            given_dic[char] += 1
            
        if given_dic == expected_dic:
            return 0
            
        for char in charSet:
            if char not in given_dic:
                given_dic[char] = 0

        left = 0
        minLength = float(inf)
        for right in range(len(s)):
            given_dic[s[right]] -= 1
            while max(given_dic.values()) <= m:
                minLength = min(minLength , right - left + 1) 
                given_dic[s[left]] += 1
                left += 1
                
        return minLength

        
        