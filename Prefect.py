from prefect import flow, task
from TwitterAPI import user_tweets
from prefect_gcp.credentials import GcpCredentials
from prefect_gcp.cloud_storage import cloud_storage_upload_blob_from_string
import json


@task()
def get_twitter_data(user):
    response = user_tweets(user)
    return response


@task()
def transform_tweets(response):
    tweets = []
    for tweet in response.data:
        # print(tweet)
        data = {
            'tweetid': str(tweet.id),
            'authorid': str(tweet.author_id),
            'created': str(tweet.created_at),
            'text': str(tweet.text),
            'retweet': str(tweet.public_metrics['retweet_count']),
            'likes': str(tweet.public_metrics['like_count'])
        }
        tweets.append(data)
    return tweets


@flow()
def load_tweets(tweets):
    gcp_cred = GcpCredentials(service_account_file="/home/riellygriff21/Documents/PrefectGCPCred.json")
    for tweet in tweets:
        data = json.dumps(tweet)
        cloud_storage_upload_blob_from_string(data, "prefect-test-rg", tweet['tweetid'], gcp_cred)


@flow()
def twitter_ETL(user):
    response = get_twitter_data(user)
    tweets = transform_tweets(response)
    load_tweets(tweets)


