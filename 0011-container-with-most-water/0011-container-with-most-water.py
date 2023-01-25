class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        
        maxArea = 0
        while left != right:
            minHeight = min(height[left], height[right])
            if minHeight*(right-left) > maxArea:
                maxArea = minHeight*(right-left)
                
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
                
        return maxArea
                