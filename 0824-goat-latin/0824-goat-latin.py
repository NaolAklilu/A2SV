class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        sentence = list(sentence.split(" "))
        print(sentence)
        vowels = ['a', "A", 'e', "E", 'i', "I", 'o', "O", 'u', "U"]
        
        for index in range(len(sentence)):
            word = list(sentence[index])
            
            if word[0] in vowels:
                word.append("ma")
                word.extend(['a'] * (index+1))
                sentence[index] = "".join(word)
            else:
                popped = word.pop(0)
                word.append(popped)
                word.append("ma")
                word.extend(["a"]* (index+1))
                sentence[index] = "".join(word)
            
        return " ".join(sentence)