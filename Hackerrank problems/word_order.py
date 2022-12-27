wordCount = {}
inputNumbers = int(input())

for _ in range(inputNumbers):
    text = input()
    if text in wordCount.keys():
        wordCount[text] += 1
    else:
        wordCount[text] = 1

print(len(wordCount))
for count in wordCount.values():
    print(count, end=" ")
