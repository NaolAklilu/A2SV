class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        left, right = 0, k-1
        num = str(num)
        count = 0
        
        while left <= len(num)-k:
            if int(num[left:right+1]) != 0:
                if int(num) % int(num[left:right+1]) == 0:
                    count += 1
            left += 1
            right += 1
            
        return count
            
            
        