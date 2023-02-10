class Solution:
    def compress(self, chars: List[str]) -> int:
        modifiedChars = []
        left, right = 0, 0
        while right < len(chars):            
            if chars[left] != chars[right]:
                count = right-left
                modifiedChars.append(chars[left])
                if count > 9:
                    for digit in str(count):
                        modifiedChars.append(digit)
                elif count > 1:
                    modifiedChars.append(str(count))
                
                left = right
                
            if right+1 == len(chars):
                count = right-left+1
                modifiedChars.append(chars[left])
                if count > 9:
                    for digit in str(count):
                        modifiedChars.append(digit)
                elif count > 1:
                    modifiedChars.append(str(count))
                    
            right += 1
            
        del chars[:]
        chars.extend(modifiedChars)
            
        return len(chars)
            
            