class Solution:
    def reverse_handler(self, left, right, s):
        if left == right:
            return s[0]
        
        s[left], s[right] = s[right], s[left]
        
        if left+1 > right-1:
            return 
        else:
            return self.reverse_handler(left+1, right-1,s)
        
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s)-1
        
        self.reverse_handler(left, right, s)
        
           
        