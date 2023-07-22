class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        top = 0
        bottom = 0
        count = 0
        inRowCount = {}
        
        for i in range(len(bank)):
            oneCount = 0
            for num in bank[i]:
                if num == "1":
                    oneCount += 1
            
            inRowCount[i] = oneCount
        
        while bottom < len(bank):
            if top == bottom:
                if inRowCount[top] == 0:
                    top += 1
                bottom += 1
            else:
                if inRowCount[bottom] == 0:
                    bottom += 1
                else:
                    count += (inRowCount[top]*inRowCount[bottom])
                    top = bottom
                    bottom += 1
        
        return count
                