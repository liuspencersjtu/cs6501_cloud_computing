# - * - coding: <utf-8> - * -

import re
import collections
import matplotlib.pyplot as plt
import pylab as pl



def get_words(file):
    with open(file) as f:
        words_box = []
        for line in f:
            # remove chaotic characters
            if re.match(r'[a-zA-Z0-9]*', line):
                words_box.extend(line.strip().split(','))
    return collections.Counter(words_box)


a = get_words('Tokenization.csv')
result = a.most_common(15)
print(result)


for i in range(2,14):
    plt.bar((result[i][0],), (result[i][1],), facecolor='#1580ee', edgecolor='white')
plt.title('Word Frequency')
plt.xlabel('Appearing Words')
pl.xticks(rotation=45)
plt.ylabel('Frequency')
plt.show()
