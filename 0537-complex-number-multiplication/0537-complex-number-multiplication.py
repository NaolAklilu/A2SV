class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        real1, real2 = 0, 0
        imag1, imag2 = 0, 0
        
        indx = len(num1) - 1 
        while indx >= 0:
            if num1[indx] == '+':
                real1 = int(num1[:indx])
                imag1 = int(num1[indx+1: len(num1)-1])
                break
            
            indx -= 1
            
        indx = len(num2) - 1 
        while indx >= 0:
            if num2[indx] == '+':
                real2 = int(num2[:indx])
                imag2 = int(num2[indx+1:len(num2)-1])
                break
            
            indx -= 1
            
        real = real1*real2 + (-1 * (imag1*imag2)) 
        imag = real1*imag2 +  real2*imag1
        
        return str(real) + '+' + str(imag) + 'i'
            