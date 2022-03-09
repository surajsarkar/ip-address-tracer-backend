from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

key = os.environ.get('ALOH_AMORA')
gate = f'https://geo.ipify.org/api/v2/country?apiKey={key}&ipAddress=0.0.0.0'

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
    app.run()
