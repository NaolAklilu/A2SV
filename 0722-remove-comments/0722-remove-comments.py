class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans = []
        
        # hold non comment part of line
        curBody = ""
        
        # keep track of block comment part of the line
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
             
            # check if the line in is in block comment
            # and if not add non comment part of the line or curBody to ans list 
            if isInBlock == False:
                if len(curBody) > 0:
                    ans.append(curBody)
                curBody = ""
                    
        return ans
                                    