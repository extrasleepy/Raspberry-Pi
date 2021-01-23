import tweepy
import json
import random
import time

with open('twitter_auth.json') as file:
      secrets = json.load(file)
      
auth = tweepy.OAuthHandler(secrets['consumer_key'], secrets['consumer_secret'])
auth.set_access_token(secrets['access_token'], secrets['access_token_secret'])

do = [
    "eat",
    "love",
    "snuggle",
    "see",
    "run with",
    "dream about",
    "forget",
    "caress",
    "purchase",
]

to = [
    " birds",
    " cats",
    " koalas",
    " shrimp",
    " dolphins",
    " spiders",
    " hamsters",
    " toads",
]

when = [
    " forever",
    " today",
    " tomorrow",
    " when the sun sets",
    " when you have time",
    " for free",
    " if you don't mind",
]

while True:
    one = random.choice(do)
    two = random.choice(to)
    three = random.choice(when)
    twitter = tweepy.API(auth)
    twitter.update_status(status = one + two + three)
    print("Tweeted: " + one + two + three)
    time.sleep(60)
