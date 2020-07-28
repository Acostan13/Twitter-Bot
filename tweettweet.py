import tweepy
import config

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)

api = tweepy.API(auth)

user = api.me()
print(user.name)  # Alex Costan
print(user.screen_name)  # alexcostan_
print(user.followers_count)  # 9

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
