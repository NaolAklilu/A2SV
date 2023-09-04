class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for index in range(len(image)):
            left, right = 0, len(image[index])-1
            while left < right:
                leftValue = image[index][left]
                image[index][left] = image[index][right]
                image[index][right] = leftValue
                
                   
                left += 1
                right -= 1
                
            for i in range(len(image[index])):
                if image[index][i] == 0:
                    image[index][i] = 1
                else:
                    image[index][i] = 0
                
                
        return image
            