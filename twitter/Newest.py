# - * - coding: <utf-8> - * -


# This program is used to scrape the newest 5 tweets.
# This 5 tweets will be used to show up on our website


import tweepy
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



def getTweets(data):
    #search_results = api.search(q='Sponge Bob', lang="en", count=5)
    search_results = api.search(q=data, lang="en", count=5)

    for tweet in search_results:
        print(tweet.user.screen_name, "Tweeted:", tweet.text, "at", tweet.created_at)
        return tweet.text


# Read csv file
def read_csv(file):
    csv_rows = []

    with open(file, 'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        title = reader.fieldnames
        for row in reader:
            csv_rows.extend([{title[i]: row[title[i]] for i in range(len(title))}])
    return csv_rows



# Write to json file
def write_json(data, json_file, format=None):
    with open(json_file, "w") as f:
        if format == "good":
            f.write(json.dumps(data, sort_keys=False, separators=(',', ': '), encoding="utf-8", ensure_ascii=False))
        else:
            f.write(json.dumps(data))




if __name__ == "__main__":
    getTweets()
