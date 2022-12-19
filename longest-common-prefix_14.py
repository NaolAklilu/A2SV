class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        str_length_pair = {}
        resultString = ""
        for string in strs:
            str_length_pair[string] = len(string)
        
        sorted_str_length_pair = sorted(str_length_pair.items(), key=lambda x:x[1])
        
        min_string = sorted_str_length_pair[0][0]
        for i in range(sorted_str_length_pair[0][1]):
            for string in strs:
                if string[i] != min_string[i]:
                    return resultString 
            resultString += min_string[i]
            
        return resultString
