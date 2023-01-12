class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # removed column count
        count = 0
        for col in range(len(strs[0])):
            prevChar = strs[0][col]
            for word in strs:
                # if its in lexicographical order
                if ord(word[col]) >= ord(prevChar):
                    prevChar = word[col]
                 
                # we increment the removed column count by one
                else:
                    count += 1
                    break
        
        return count