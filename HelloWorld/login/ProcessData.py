# - * - coding: <utf-8> - * -

import csv
import sys
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


reload(sys)
sys.setdefaultencoding('utf-8')



def processData():
    stopWords = stopwords.words('english')
    punctuation = list(string.punctuation)
    stop = stopWords + punctuation
    prefix = ('rt', 'https')

    with open('TwitterData.csv', 'rb') as csvFile1:
        readObj = csv.reader(csvFile1)
        csvFile2 = open('Tokenization.csv', 'wb')
        writeObj = csv.writer(csvFile2)
        next(readObj)                           # start from second

        for line in readObj:
            data = line[0]
            wordsFiltered = []
            # tokenization by nltk
            tokens = word_tokenize(data)
            # convert all letters to lower case
            tokens = [w.lower() for w in tokens]
            # remove non-alphabic items
            words = [word for word in tokens if word.isalpha()]
            # remove stop words and punctuations
            words = [w for w in words if not w in stop]
            # remove ip addresses in tweets
            words = [w for w in words if not w.startswith(prefix)]

            for w in words:
                wordsFiltered.append(w)
            print wordsFiltered
            writeObj.writerow(wordsFiltered)


    csvFile2.close()



if __name__ == "__main__":
    processData()
