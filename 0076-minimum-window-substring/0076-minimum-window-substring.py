class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        s_dic = defaultdict(int)
        t_dic = defaultdict(int)
        for char in t:
            t_dic[char] += 1
            
        ansLeft, ansRight = 0, len(s)
        window_length = 0
        left = 0
        for right in range(len(s)):
            if s[right] in t_dic:
                s_dic[s[right]] += 1
                if s_dic[s[right]] == t_dic[s[right]]:
                    window_length += 1
                    
            while window_length == len(t_dic):
                if (right-left) < (ansRight-ansLeft):
                    ansLeft, ansRight = left, right
                
                if s[left] in s_dic:
                    if s_dic[s[left]] == t_dic[s[left]]:
                        window_length -= 1
                    s_dic[s[left]] -= 1
                
                left += 1
            
        if ansRight == len(s):
            return ""
        return s[ansLeft: ansRight+1]
                
                
                
                
            
            
                
        
        