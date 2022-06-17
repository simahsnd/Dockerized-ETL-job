import tweepy
import pymongo
import time
import twitter_keys



client = tweepy.Client(bearer_token = twitter_keys.Bearer_Token)


mongo_client = pymongo.MongoClient(host='mongodb',port=27017)


db = mongo_client.twit


search_query = 'BarackObama lang:en -is:retweet -is:reply -is:quote -has:links'
cursor = client.search_recent_tweets(query=search_query,
    tweet_fields=['text', 'created_at', 'public_metrics'], max_results=10)

 
t_end = time.time() + 20  
while time.time() < t_end: 
     for tweet in cursor.data:
          js_row = {'text': tweet.text, 'created_at': tweet.created_at}
          db.twit.insert_one(js_row)
          time.sleep(3)
