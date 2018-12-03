# - * - coding: <utf-8> - * -

import re
import collections
import matplotlib.pyplot as plt
import pylab as pl
from matplotlib.figure import Figure


def get_words(file):
    with open(file) as f:
        words_box = []
        for line in f:
            # remove chaotic characters
            if re.match(r'[a-zA-Z0-9]*', line):
                words_box.extend(line.strip().split(','))
    return collections.Counter(words_box)

def phrase():
	a = get_words('Tokenization.csv')
	result = a.most_common(15)
	print(result)
	fig = Figure()
	for i in range(2, 14):
	    plt.bar((result[i][0],), (result[i][1],), facecolor='#1580ee', edgecolor='white')
	    #plt.bar((result[i],), facecolor='#1580ee', edgecolor='white')
	plt.title('Word Frequency')
	plt.xlabel('Appearing Words')
	pl.xticks(rotation=45)
	plt.ylabel('Frequency')
	plt.savefig("Word Frequency.png")
	plt.show()
	'''
	for i in range(2, 14):
	    plt.bar((result[i][0],), (result[i][1],), facecolor='#1580ee', edgecolor='white')
	    #plt.bar((result[i],), facecolor='#1580ee', edgecolor='white')
	plt.title('Word Frequency')
	plt.xlabel('Appearing Words')
	pl.xticks(rotation=45)
	plt.ylabel('Frequency')
	plt.savefig("Word Frequency.png")
	plt.show()
	'''
