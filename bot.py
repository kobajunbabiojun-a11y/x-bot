import os, csv, random, sys
import tweepy

API_KEY = os.environ["X_API_KEY"]
API_SECRET = os.environ["X_API_SECRET"]
ACCESS_TOKEN = os.environ["X_ACCESS_TOKEN"]
ACCESS_SECRET = os.environ["X_ACCESS_SECRET"]

# v2 クライアント（ユーザーコンテキスト）
client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_SECRET,
    wait_on_rate_limit=True,
)

# 投稿候補の読み込み
try:
    with open("content.csv", encoding="utf-8") as f:
        posts = [r[0].strip() for r in csv.reader(f) if r and r[0].strip()]
except FileNotFoundError:
    print("content.csv not found"); sys.exit(1)

if not posts:
    print("no content"); sys.exit(1)

text = random.choice(posts)[:270]

# v2: ツイート投稿
try:
    resp = client.create_tweet(text=text)
    print("posted:", text, "| id:", resp.data.get("id"))
except tweepy.Forbidden as e:
    print("Forbidden:", e); sys.exit(1)
except Exception as e:
    print("post failed:", repr(e)); sys.exit(1)
