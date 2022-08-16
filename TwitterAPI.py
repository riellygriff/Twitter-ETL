import pandas
import os
import tweepy
from dotenv import load_dotenv
from Creds import BEARER_TOKEN


load_dotenv()

bearer_token = os.getenv('BEARER_TOKEN')
consumer_key = os.getenv('API_KEY')
consumer_secret = os.getenv('API_KEY_SECRET')
access_key = os.getenv('ACCESS_TOKEN')
access_secret = os.getenv('ACCESS_TOKEN_SECRET')

def user_tweets(user):
    client = tweepy.Client(bearer_token=BEARER_TOKEN)

    user = client.get_user(username=user)
    userid = user.data.id
    response = client.get_users_tweets(id=userid, exclude=['retweets', 'replies'],
                                       tweet_fields=['created_at', 'author_id', 'public_metrics'],
                                       max_results=50)
    return response
    # for tweet in response.data:
    #     print(tweet.id)
    #     print(tweet.author_id)
    #     print(tweet.created_at)
    #     print(tweet.text)
    #     print(tweet.public_metrics['retweet_count'])
    #     print(tweet.public_metrics['like_count'])
