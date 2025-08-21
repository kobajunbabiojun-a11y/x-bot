import os, csv, random
import tweepy

api_key = os.environ["X_API_KEY"]
api_secret = os.environ["X_API_SECRET"]
access_token = os.environ["X_ACCESS_TOKEN"]
access_secret = os.environ["X_ACCESS_SECRET"]

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_secret)
api = tweepy.API(auth)

with open("content.csv", encoding="utf-8") as f:
    posts = [row[0] for row in csv.reader(f) if row]

text = random.choice(posts)
api.update_status(status=text)
print("posted:", text)
