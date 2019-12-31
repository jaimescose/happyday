import os
import twitter

def create_api_connection() -> twitter.Api():
    api = twitter.Api(consumer_key=os.environ['TWITTER_API_KEY'],
                    consumer_secret=os.environ['TWITTER_API_SECRET'],
                    access_token_key=os.environ['TWITTER_ACCESS_TOKEN'],
                    access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])

    return api
