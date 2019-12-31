from flask import Flask, redirect

# flask config
app = Flask(__name__)
PORT = 8000
DEBUG = True

# twitter profile config
twitter_url = 'https://twitter.com/'
username = 'hppydyty'
profile_url = twitter_url + username

@app.errorhandler(404)
def not_found(error):
    return 'Sorry, not found :('

@app.route('/', methods=['GET'])
def get_index():
    return redirect(profile_url)

@app.route('/webhook/twitter/', methods=['POST'])
def manage_twitter_activity():
    return None

if __name__ == '__main__':
    app.run(port=PORT, debug=DEBUG)
