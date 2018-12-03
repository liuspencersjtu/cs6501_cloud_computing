# - * - coding: <utf-8> - * -

import tweepy
import datetime
import csv
import sys
import re
import collections


reload(sys)
sys.setdefaultencoding('utf-8')


consumer_key = "5w07RnjEIeanOx7v3C2SyVU32"
consumer_secret = "ncRcjQ6lFqCmQdpZ1tdgOekHbYbHbajBUSkx0WqJPWss4zFKn1"
access_token = "1059459728026333186-OSh3xLdkn4G5ivbxkedtLgaBG3tsvl"
access_token_secret = "DRntBt54wmdgHocReGOcTwwnDEDsTfK3bRG2elkkM31NF"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)


time = datetime.date.today() - datetime.timedelta(days=2)


def getData():

    with open('Country.csv', 'w') as file:
        csvWriter = csv.writer(file)

        for tweet in tweepy.Cursor(api.search, q="Sponge Bob", lang="en", since=time).items(2500):
            if tweet.place == None:
                continue
            csvWriter.writerow([tweet.place.country.encode('utf-8')])
            print tweet.place.country

    file.close()


    a = get_words('Country.csv')
    result = a.most_common(15)
    print(result)



def get_words(file):
    with open(file) as f:
        words_box = []
        for line in f:
            # remove chaotic characters
            if re.match(r'[a-zA-Z0-9]*', line):
                words_box.extend(line.strip().split(','))
    return collections.Counter(words_box)







if __name__ == "__main__":
   getData()
