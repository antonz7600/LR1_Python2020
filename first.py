import itertools
import re
from collections import Counter


def first(filename):
    word_list = list()
    with open(filename) as openFile:
        for line in openFile:
            word_list.append(re.sub(r'[,.!?;\"]', "", line.strip(), count=0).split(' '))
    word_list = list(itertools.chain(*word_list))
    counted_words = Counter(word_list)
    print(counted_words)
