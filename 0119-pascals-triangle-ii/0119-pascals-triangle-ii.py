class Solution:
    
    def factorial(self, n):
        if n <= 1:
            return 1
        return n * self.factorial(n-1)
    
    
    def getRow(self, rowIndex: int) -> List[int]:
        arr = [0]*(rowIndex + 1)
        for i in range(rowIndex+1):
            arr[i] = self.factorial(rowIndex) // (self.factorial(i)*self.factorial(rowIndex-i))
            
        return arr