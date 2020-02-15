import itertools
import re
from collections import Counter


def stc_most_words(file_name):
    word_list = list()
    with open(file_name) as openFile:
        for line in openFile:
            word_list.append(re.sub(r'[,.!?;\"]', "", line.strip(), count=0).split(' '))
    word_list = list(itertools.chain(*word_list))
    counted_words = Counter(word_list)
    fin_string = ""
    for word, count in counted_words.most_common(10):
        fin_string += word + " "
    fin_string = fin_string.capitalize()
    print(fin_string)
