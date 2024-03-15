class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
   
        result = []
        for i in range(numRows):
            temp = [0 for _ in range(i+1)]
            temp[0] = 1
            temp[-1] = 1
            for j in range(1, len(temp)-1):
                temp[j] = result[-1][j-1] + result[-1][j]
            result.append(temp)
        return result