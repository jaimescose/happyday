import twitter_connection
from functools import wraps

def create_api_connection(function):
    @wraps(function)
    def wrap_function(*args, **kwargs):
        kwargs['api'] = twitter_connection.create_api_connection()
        return function(*args, **kwargs)

    return wrap_function

@create_api_connection
def make_tweet(text, **kwargs):
    api = kwargs['api']
    api.PostUpdate(text)
