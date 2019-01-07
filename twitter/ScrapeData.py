# - * - coding: <utf-8> - * -

# This program is used to scrape Twitter data,
# containing tweet text information, and location information

import tweepy
import datetime
import csv
import sys


#reload(sys)
#sys.setdefaultencoding('utf-8')


consumer_key = "5w07RnjEIeanOx7v3C2SyVU32"
consumer_secret = "ncRcjQ6lFqCmQdpZ1tdgOekHbYbHbajBUSkx0WqJPWss4zFKn1"
access_token = "1059459728026333186-OSh3xLdkn4G5ivbxkedtLgaBG3tsvl"
access_token_secret = "DRntBt54wmdgHocReGOcTwwnDEDsTfK3bRG2elkkM31NF"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)


time = datetime.date.today() # - datetime.timedelta(days=2)


def getData(data):
    with open('static/TwitterData.csv', 'w') as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow(['tweets', 'location'])

        # scrape 20 tweets containing query words until current time
        for tweet in tweepy.Cursor(api.search, q=data, lang="en", until=time).items(20):
            print(tweet.user.screen_name, "Tweeted:", tweet.text, "at", tweet.created_at)
            if tweet.place != None:
                location = tweet.place.full_name
            else:
                location = ""
            # store tweet text and users' location information
            csvWriter.writerow([tweet.text.encode('utf-8'), location])

    csvFile.close()

    # with open('TwitterData.json', 'a') as f:
    #     for tweet in tweepy.Cursor(api.search, q="Sponge Bob", lang="en", since=time).items(100):
    #         print tweet.user.screen_name, "Tweeted:", tweet.text, "at", tweet.created_at
    #         json.dumps(tweet, encoding='utf-8')
    #         f.write('\n')



if __name__ == "__main__":
    getData('trump')
