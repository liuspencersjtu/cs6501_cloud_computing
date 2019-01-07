# - * - coding: <utf-8> - * -


# This program is used to do phrase count

import re
import collections
import matplotlib.pyplot as plt
import pylab as pl


def count_words(file):
    with open(file) as f:
        words_box = []
        for line in f:
            # remove chaotic characters
            if re.match(r'[a-zA-Z0-9]*', line):
                words_box.extend(line.strip().split(','))
    return collections.Counter(words_box)


def show_plts(result):
    if(len(result) > 15):
        num = 14
    else:
        num = len(result)

    for i in range(1, num):
        plt.bar((result[i][0]), (result[i][1]), facecolor='#1580ee', edgecolor='white')
    plt.title("Word Frequency")
    plt.xlabel('Appearing words')
    pl.xticks(rotation=45)
    plt.ylabel('Frequency')
    plt.savefig("static/Word Frequency.png")
    print('save img')



def show():
    a = count_words('static/Tokenization.csv')
    result = a.most_common()
    print(result)
    show_plts(result)
