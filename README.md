# Project: Build a Dockerized Data Pipeline that analyzes the sentiment of tweets


### Goal

In this project, I built a data pippeline that collect tweets and stores them in a database. Next, the sentiment of tweets is analyzed and the annotated tweets are stored in a second database. Finally, the best or worst sentiment for a given is published on Slack every 10 minutes.

- Reads tweets from Twitter (using part of the Tweego code).
- pushes raw tweets to MongoDB
- ETL process picks a random tweet and runs vader sentiment on it.
- Stores the tweet + sentiment in Postgres DB
- Sink process prints the highest scoring tweet (could be replaced by Slack bot)

### Usage

* Install docker on your machine
* Clone the repository
* Get credentials for Twitter API and insert them in twitter_key.py
* Run docker-compose build, then docker-compose up in terminal
