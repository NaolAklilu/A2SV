class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        charCount = {}
        for char in s:
            if char in charCount.keys():
                charCount[char] += 1
            else:
                charCount[char] = 1
        
        cur_dic = {}
        start_index = 0
        answer = []
        
        for i in range(len(s)):
            if s[i] in cur_dic.keys():
                cur_dic[s[i]] += 1
            else:
                cur_dic[s[i]] = 1
            
            if cur_dic[s[i]] == charCount[s[i]]:
                cur_dic.pop(s[i])
                
                if len(cur_dic) == 0:
                    answer.append(i - start_index + 1)
                    start_index = i + 1
        
        return answer