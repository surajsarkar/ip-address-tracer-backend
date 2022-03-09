from distutils.log import debug
from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

key = os.environ.get('ALOH_AMORA')

@app.route('/')
def home():
    return "<h1>Namaste</h1>"

@app.route('/api-endpoint/', methods=['GET', 'POST'])
def find_info():
    address = request.args['address']

    response = requests.get(f'https://geo.ipify.org/api/v2/country?apiKey={key}&ipAddress={address}')

    if 200 <= response.status_code < 300:
        result = response.json()
        return jsonify(ip= result['ip'], location = result['location'], isp = result['isp'])
    else:
        return jsonify(error = 'There was a error could not parse your request please check the ip address')


if __name__ == '__main__':
    app.run(debug=os.environ.get('DEBUG'))

