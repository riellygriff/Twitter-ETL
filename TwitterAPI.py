import pandas
import os
import tweepy
from dotenv import load_dotenv
from Creds import BEARER_TOKEN


load_dotenv()


def user_tweets(user):
    client = tweepy.Client(bearer_token=BEARER_TOKEN)

    user = client.get_user(username=user)
    userid = user.data.id
    response = client.get_users_tweets(id=userid, exclude=['retweets', 'replies'],
                                       tweet_fields=['created_at', 'author_id', 'public_metrics'],
                                       max_results=50)
    return response

