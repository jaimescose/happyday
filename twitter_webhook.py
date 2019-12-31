from twitter_connection import create_api_connection

url = 'https://api.twitter.com/1.1/account_activity/all/dev/webhooks.json'
webhook_url = 'https://hppydyty.herokuapp.com/webhook/twitter/'

api = create_api_connection()

data = {
    'url': webhook_url
}

response = api._RequestUrl(url=url, verb='POST', data=data)

print(response.content)
