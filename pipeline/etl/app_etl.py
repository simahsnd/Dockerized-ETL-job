import pymongo 
import time
import pandas as pd
import re
from sqlalchemy import create_engine 
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer




mongo_client = pymongo.MongoClient(host='mongodb',port=27017)

db = mongo_client.twit
#mongo_client.list_database_names()

docs = db.twit.find()
tl = list()
for doc in docs:
    tl.append(doc['text'])

df_tweets = pd.DataFrame({'tweets' :tl })
#df_tweets

mentions_regex= '@[A-Za-z0-9]+'
url_regex='https?:\/\/\S+' #this will not catch all possible URLs
hashtag_regex= '#'
rt_regex= 'RT\s'
rt_enter= '\n'

def clean_tweets(tweet):
    tweet = re.sub(mentions_regex, '', tweet)  #removes @mentions
    tweet = re.sub(hashtag_regex, '', tweet) #removes hashtag symbol
    tweet = re.sub(rt_regex, '', tweet) #removes RT to announce retweet
    tweet = re.sub(url_regex, '', tweet) #removes most URLs
    tweet = re.sub(rt_enter, ' ', tweet) #remove \n
    return tweet

df_tweets.tweets = df_tweets.tweets.apply(clean_tweets)
#df_tweets
#DATABASE = 'postgres'
#PORT = '5432'
#USER = 'sima'
#PASSWORD = '1234'
#HOST = 'localhost'

pg = create_engine('', echo=True)
pg.execute('''
    CREATE TABLE IF NOT EXISTS tweets (
    text VARCHAR(500),
    sentiment NUMERIC
);
''')
analyzer = SentimentIntensityAnalyzer()
for doc in df_tweets.itertuples():
    sentiment = analyzer.polarity_scores(doc.tweets)
    text = doc.tweets
    score = sentiment['compound'] # placeholder value
    query = "INSERT INTO tweets VALUES (%s, %s);"
    pg.execute(query, (text, score))
    time.sleep(3)
