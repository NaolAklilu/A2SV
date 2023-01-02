class Solution:
    def reverseWords(self, s: str) -> str:
        string_stack = []
        resultString = ""
        for char in s:
            if char == " ":
                if string_stack:
                    while len(string_stack) != 0:
                        resultString += string_stack.pop()
                    resultString += " "
                else:
                    resultString += " "
            else:
                string_stack.append(char)
        
        while len(string_stack) != 0:
            resultString += string_stack.pop()

        return resultString

