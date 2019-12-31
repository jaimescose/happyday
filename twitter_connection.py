import settings
import twitter

def create_api_connection() -> twitter.Api():
    api = twitter.Api(consumer_key=settings.twitter.get('APIKey'),
                    consumer_secret=settings.twitter.get('APIKeySecret'),
                    access_token_key=settings.twitter.get('AccessToken'),
                    access_token_secret=settings.twitter.get('AccessTokenSecret'))

    return api
