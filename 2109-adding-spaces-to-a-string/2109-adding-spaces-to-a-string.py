class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        string = []      
        
        curIndex = 0
        for i in range(len(s)):
            if curIndex < len(spaces): 
                if i == spaces[curIndex]:
                    string.append(" ")
                    string.append(s[i])
                    curIndex += 1
                else:
                    string.append(s[i])
            else:
                string.append(s[i])

        return "".join(string)