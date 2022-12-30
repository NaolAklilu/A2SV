class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans = []
        
        curBody = ""
        isInBlock = False
        
        for line in source:
            i = 0
            while i < len(line):
                if isInBlock == False:
                    if line[i] == "/":
                        if i+1 < len(line):
                            if line[i+1] == "/":
                                break
                            elif line[i+1] == "*":
                                isInBlock = True
                                i += 2
                                continue
                            else:
                                curBody += line[i]
                        elif i == len(line)-1:
                            curBody += line[i]
                            
                    else:
                        curBody += line[i]
                      
                    i += 1
                
                else:
                    if line[i] == "*":
                        if i+1 < len(line):
                            if line[i+1] == "/":
                                isInBlock = False
                     
                    if isInBlock:
                        i += 1
                    else:
                        i += 2
             
            if isInBlock == False:
                if len(curBody) > 0:
                    ans.append(curBody)
                curBody = ""
                    
        return ans
                                    