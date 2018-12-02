# - * - coding: <utf-8> - * -

import tweepy
import sys


reload(sys)
sys.setdefaultencoding('utf-8')


consumer_key = "5w07RnjEIeanOx7v3C2SyVU32"
consumer_secret = "ncRcjQ6lFqCmQdpZ1tdgOekHbYbHbajBUSkx0WqJPWss4zFKn1"
access_token = "1059459728026333186-OSh3xLdkn4G5ivbxkedtLgaBG3tsvl"
access_token_secret = "DRntBt54wmdgHocReGOcTwwnDEDsTfK3bRG2elkkM31NF"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)



def getTweets():
    search_results = api.search(q='Sponge Bob', lang="en", count=5)

    for tweet in search_results:
        print tweet.user.screen_name, "Tweeted:", tweet.text, "at", tweet.created_at



if __name__ == "__main__":
    getTweets()
