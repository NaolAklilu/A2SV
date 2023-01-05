class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonalElements = defaultdict(list)
        
        m = len(mat)
        n = len(mat[0])
        for index1 in range(m):
            for index2 in range(n):
                diagonalElements[index1 + index2].append(mat[index1][index2])
        
        resultArray = []
        for keyNum in diagonalElements:
            if keyNum % 2 == 0:
                nums = diagonalElements[keyNum]
                nums.reverse()
                resultArray.extend(nums)
            else:
                resultArray.extend(diagonalElements[keyNum])
                
        return resultArray