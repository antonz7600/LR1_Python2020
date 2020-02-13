import itertools
import re
from collections import Counter

wordList = list()
with open("input.txt") as openFile:
    for line in openFile:
        wordList.append(re.sub(r'[,.!?;\"]', "", line.strip(), count=0).split(' '))
wordList = list(itertools.chain(*wordList))
countedWords = Counter(wordList)
print(countedWords)
