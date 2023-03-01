class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        char_dic = defaultdict(int)
        
        for char in s:
            char_dic[char] += 1
        
        stack = []
        visitedChar = set()
        
        for char in s:
            while stack and char_dic[stack[-1]] > 0 and char < stack[-1] and char not in visitedChar:
                removed = stack.pop()
                visitedChar.remove(removed)
                
            if char not in visitedChar:
                stack.append(char)
                visitedChar.add(char)
                
            char_dic[char] -= 1
            
        return "".join(stack)