class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if '.' in queryIP:
            nums = queryIP.split('.')
            if len(nums) < 4 or len(nums) > 4:
                return 'Neither'
            
            for num in nums:
                if len(num) < 4:
                    
                    if num == '':
                        return 'Neither'
                    
                    for char in num:
                        if char.isnumeric() == False:
                            return 'Neither'
                    
                    
                    curNum = int(num)
                    
                    if curNum > 255:
                        return 'Neither'
                    
                    if len(num) != len(str(curNum)):
                        return 'Neither'
                else:
                    return 'Neither'
                
            return 'IPv4'
            
        else:
            chars = {'a', 'b', 'c', 'd', 'e', 'f',
                    'A', 'B', 'C', 'D', 'E', 'F'}
            nums = queryIP.split(':')
            if len(nums) < 8 or len(nums) > 8:
                return 'Neither'
            
            for num in nums:
                if len(num) > 4 or len(num) == 0:
                    return 'Neither'
                
                for char in num:
                    if char.isnumeric() == False and char not in chars:
                        return 'Neither'
                
                
                
            return 'IPv6'
            
            