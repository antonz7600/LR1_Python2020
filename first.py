import re
from collections import Counter

wordList = list()
with open("input.txt") as openFile:
    for line in openFile:
        wordList.append(re.sub(r'[,.!?;\"]', "", line.strip(), count=0).split(' '))
countedWords = Counter()
for wordLine in wordList:
    for word in wordLine:
        countedWords[word] += 1
print(countedWords)

