from flask import Flask, jsonify, abort
import requests
# Need to include more libraries!

app = Flask(__name__)

API_BASE_URL = 'https://apiv3.imocha.io/v3'
BASE_URL = 'https://apiv3.imocha.io/v3/tests/'
MOCHA_API_KEY = 'API KEY'

if __name__ == '__main__':
    app.run(debug=True, port=5002)


