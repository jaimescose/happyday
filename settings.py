import configparser
config = configparser.ConfigParser()

config.read('settings.ini')

twitter =  {
    'APIKey': config.get('twitter', 'APIKey'),
    'APIKeySecret': config.get('twitter', 'APIKeySecret'),
    'AccessToken': config.get('twitter', 'AccessToken'),
    'AccessTokenSecret': config.get('twitter', 'AccessTokenSecret'),
}
