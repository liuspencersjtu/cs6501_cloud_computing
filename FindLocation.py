# - * - coding: <utf-8> - * -

import csv
import sys
import re
import collections
import matplotlib.pyplot as plt
import pylab as pl


reload(sys)
sys.setdefaultencoding('utf-8')


def get_words(file):
    with open(file, 'rb') as csvFile1:
        readObj = csv.reader(csvFile1)
        words_box = []
        next(readObj)                           # start from second

        for line in readObj:
            data = line[1]
            # remove chaotic characters
            if re.match(r'[a-zA-Z0-9]*', data):
                words_box.extend(data.strip().split(','))
    return collections.Counter(words_box)



def show_plots(result):
    if (len(result) > 15):
        num = 14
    else:
        num = len(result)

    for i in range(1, num):
        plt.bar((result[i][0],), (result[i][1],), facecolor='#1580ee', edgecolor='white')
    plt.title("Users' Country")
    plt.xlabel('Country')
    pl.xticks(rotation=45)
    plt.ylabel('Frequency')
    plt.savefig("Country.png")
    plt.show()



if __name__ == "__main__":
    a = get_words('Twitter.csv')
    result = a.most_common()
    print(result)
    show_plots(result)
