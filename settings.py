import configparser
config = configparser.ConfigParser()

config.read('settings.ini')

twitter =  {
    'APIKey': config.get('twitter', 'APIKey'),
    'APISecretKey': config.get('twitter', 'APISecretKey'),
    'AccessToken': config.get('twitter', 'AccessToken'),
    'AccessTokenSecret': config.get('twitter', 'AccessTokenSecret'),
}
