class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        mult_list = []
        
        # for each digit in num1
        # calculate its product with num2
        for idx1 in range(len(num1)-1, -1, -1):
            extraDigit = 0
            curNum = ""
            for idx2 in range(len(num2)-1,-1,-1):
                multValue = int(num1[idx1]) * int(num2[idx2]) + extraDigit
                
                # if the index is the last index just and the result to curNum
                if idx2 == 0:
                    curNum = str(multValue) + curNum
                else:
                    curNum = str(multValue)[-1] + curNum
                    extraDigit = multValue // 10
            
            # add zero to last to make the each digit product
            # have equal length.
            extraZeros = "0" * (len(num1) - idx1 - 1)
            mult_list.append(int(curNum + extraZeros))
                
        return str(sum(mult_list))