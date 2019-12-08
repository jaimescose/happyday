import settings

from flask import Flask, redirect

app = Flask(__name__)
PORT = 8000
DEBUG = True

@app.errorhandler(404)
def not_found(error):
    return 'Sorry, not found :('

@app.route('/', methods=['GET'])
def get_index():
    return redirect('https://twitter.com/hppydyty')

if __name__ == '__main__':
    app.run(port=PORT, debug=DEBUG)
